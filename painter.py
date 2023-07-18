import maya.cmds as cmds

# 创建默认的球体
sphereRadius = 10
sphereStrenth = 0.5
sphere = cmds.polySphere(radius=sphereRadius/10)[0]
cmds.addAttr(sphere,attributeType = 'float',longName = "radius",defaultValue = sphereRadius)
cmds.addAttr(sphere,attributeType = 'float',longName = "strength",defaultValue = sphereStrenth)

# 创建一个lambert 材质
mat = cmds.shadingNode('lambert', asShader=True, name="mat")
cmds.sets(name='%sSG' % mat, renderable=True, noSurfaceShader=True, empty=True)
cmds.connectAttr('%s.outColor' % mat, '%sSG.surfaceShader' % mat)
# 将材质赋给球体,并使其不可选中
cmds.select(sphere)
cmds.sets(forceElement='%sSG' % mat)
# 设置球体的默认透明度值
cmds.setAttr('%s.transparency' % mat, sphereHardness, sphereHardness, sphereHardness, type="double3")
# 将该物体设置为不可选中
cmds.setAttr(sphere+".overrideEnabled", 1)
cmds.setAttr(sphere+".overrideDisplayType", 2)
cmds.select(clear=True)
# 更新球体的半径
def updateSphereRadius(radius):
    cmds.setAttr(sphere + '.radius', radius)
    scalenow = radius/sphereRadius
    cmds.setAttr(sphere+ '.scale',scalenow ,scalenow,scalenow)
    
# 更新球体的硬度/透明度
def updateSphereStrength(strength):
    cmds.setAttr(sphere + '.strength', strength)
    cmds.setAttr('%s.transparency' % mat, 1-strength, 1-strength, 1-strength, type="double3")
# 在新窗口中创建 GUI 界面
window = cmds.window(title='Adjust Sphere Radius', widthHeight=(300, 200))
cmds.columnLayout(adjustableColumn=True)

# Radius Slider
cmds.separator(height=10, style='none')
cmds.text(label='Radius')
cmds.floatSliderGrp(min=1, max=50, value=sphereRadius, field=True, dragCommand=lambda x: updateSphereRadius(x))
cmds.separator(height=10, style='none')
cmds.text(label='Strength')
cmds.floatSliderGrp(min=0.0, max=1.0, value=sphereStrenth, field=True, dragCommand=lambda x: updateSphereStrength(x))

cmds.showWindow(window)