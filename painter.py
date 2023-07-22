import maya.cmds as cmds
import math
# 创建默认的球体
sphereRadius = 10
sphereStrength = 0.5
sphereHardness = 1.0
add_green = (0.343,0.684,0.306)
erase_red = (0.951,0.311,0.215)
sphere = cmds.polySphere(radius=sphereRadius/10)[0]
cmds.addAttr(sphere,attributeType = 'float',longName = "radius",defaultValue = sphereRadius)
cmds.addAttr(sphere,attributeType = 'float',longName = "strength",defaultValue = sphereStrength)
cmds.addAttr(sphere,attributeType = 'float',longName = "hardness",defaultValue = sphereHardness)
cmds.addAttr(sphere,attributeType = 'bool',longName = "isErase",defaultValue = False)
# 创建一个rampshader 材质
mat = cmds.shadingNode('rampShader', asShader=True, name="mat")
cmds.sets(name='%sSG' % mat, renderable=True, noSurfaceShader=True, empty=True)
cmds.connectAttr('%s.outColor' % mat, '%sSG.surfaceShader' % mat)
#去除光照
cmds.setAttr('%s.specularity' % mat,0)
#cmds.setAttr('%s.diffuse' % mat,0)
# 将材质赋给球体,并使其不可选中
cmds.select(sphere)
cmds.sets(forceElement='%sSG' % mat)
# 设置球体的默认ambient颜色值
if(cmds.getAttr(sphere+'.isErase')):
    cmds.setAttr('%s.ambientColor' % mat, sphereStrength*erase_red[0], sphereStrength*erase_red[1], sphereStrength*erase_red[2], type="double3")
else:
    cmds.setAttr('%s.ambientColor' % mat, sphereStrength*add_green[0], sphereStrength*add_green[1], sphereStrength*add_green[2], type="double3")
# 设置球体的默认渐变值
cmds.setAttr('%s.transparency[0].transparency_Color' % mat, 1.0, 1.0, 1.0, type="double3")
cmds.setAttr('%s.transparency[1].transparency_Color' % mat, 0.6, 0.6, 0.6, type="double3")
cmds.setAttr('%s.transparency[1].transparency_Position' % mat, 0.001)
cmds.setAttr('%s.transparency[1].transparency_Interp' % mat, 1)
# 将该物体设置为不可选中
cmds.setAttr(sphere+".overrideEnabled", 1)
cmds.setAttr(sphere+".overrideDisplayType", 2)
cmds.select(clear=True)

# 更新球体的半径
def updateSphereRadius(radius):
    cmds.setAttr(sphere + '.radius', radius)
    scalenow = radius/sphereRadius
    cmds.setAttr(sphere+ '.scale',scalenow ,scalenow,scalenow)

# 更新球体的硬度
def updateSphereHardness(hardness):
    cmds.setAttr(sphere + '.hardness', hardness)
    if(hardness<1):
        cmds.setAttr('%s.transparency[1].transparency_Position' % mat, 1-hardness)
    #else:
        #cmds.setAttr('%s.transparency[1].transparency_Position' % mat, 0.001)
        
# 更新球体的强度/ambient颜色
def updateSphereStrength(strength):
    cmds.setAttr(sphere + '.strength', strength)
    if(cmds.getAttr(sphere+'.isErase')):
        cmds.setAttr('%s.ambientColor' % mat, strength*erase_red[0], strength*erase_red[1], strength*erase_red[2], type="double3")
    else:
        cmds.setAttr('%s.ambientColor' % mat, strength*add_green[0], strength*add_green[1], strength*add_green[2], type="double3")
    
# 在新窗口中创建 GUI 界面
window = cmds.window(title='Adjust Sphere Radius', widthHeight=(300, 200))
cmds.columnLayout(adjustableColumn=True)

# Radius Slider
cmds.separator(height=10, style='none')
cmds.text(label='Radius')
cmds.floatSliderGrp(min=1, max=50, value=sphereRadius, field=True, dragCommand=lambda x: updateSphereRadius(x))
# Strength Slider
cmds.separator(height=10, style='none')
cmds.text(label='Strength')
cmds.floatSliderGrp(min=0.1, max=1.0, value=sphereStrength, field=True, dragCommand=lambda x: updateSphereStrength(x))
# Hardness Slider
cmds.separator(height=10, style='none')
cmds.text(label='Hardness')
cmds.floatSliderGrp(min=0.0, max=1.0, value=sphereHardness, field=True, dragCommand=lambda x: updateSphereHardness(x))
cmds.showWindow(window)
