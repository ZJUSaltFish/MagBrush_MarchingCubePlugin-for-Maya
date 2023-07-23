import inspect
import os
import sys
import maya.cmds as cmd
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from maya import cmds
#import marching_cube_np

import pic

qtVersion = cmds.about(qtVersion=True)

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtUiTools



uifile_path = "D:\GitHubProgram\Mayapy_FinalProject\\UITest1.ui"

def loadui(uifile_path):
    uifile = QtCore.QFile(uifile_path)
    uifile.open(QtCore.QFile.ReadOnly)
    uiWindow = QtUiTools.QUiLoader().load(uifile)
    uifile.close()
    return uiWindow

class MclGui():
    def __init__(self, parent=None):
        self.ui = loadui(uifile_path)
        self.ui.show()

    #下面是将UI里控件和代码里的函数连接起来，基础格式是 UI控件.Signal.Function，其中Function就是具体功能
        #button
        self.ui.Painter.clicked.connect(self.A)

        #checkbox
        self.ui.Drugger.stateChanged.connect(self.B)


        self.ui.CreateTerrain_A.clicked.connect(self.E)
        self.ui.CreateTerrain_B.clicked.connect(self.F)
        self.ui.ClearAll.clicked.connect(self.G)

        #slider
        self.ui.horizontalSlider_A.valueChanged.connect(self.sliderA)
        self.ui.horizontalSlider_B.valueChanged.connect(self.sliderB)
        self.ui.horizontalSlider_C.valueChanged.connect(self.sliderC)

        self.ui.MapSlider_1.valueChanged.connect(self.terrainSliderA)
        self.ui.MapSlider_2.valueChanged.connect(self.terrainSliderB)
        self.ui.MapSlider_3.valueChanged.connect(self.terrainSliderC)
        self.ui.MapSlider_4.valueChanged.connect(self.terrainSliderD)

        #spinbox
        self.ui.spinBox_1.valueChanged.connect(self.spinbox_1)
        self.ui.spinBox_2.valueChanged.connect(self.spinbox_2)
        self.ui.spinBox_3.valueChanged.connect(self.spinbox_3)
        self.ui.spinBox_4.valueChanged.connect(self.spinbox_4)
        self.ui.spinBox_5.valueChanged.connect(self.spinbox_5)
        self.ui.spinBox_6.valueChanged.connect(self.spinbox_6)
        self.ui.spinBox_7.valueChanged.connect(self.spinbox_7)


        #checkbox

    #创建画笔
    def A(self):
        # 创建默认的球体
        self.sphereRadius = 10
        self.sphereStrength = 0.5
        sphereHardness = 1.0
        self.ui.horizontalSlider_A.setValue(10)
        self.ui.horizontalSlider_B.setValue(50)
        self.ui.horizontalSlider_C.setValue(100)
        self.add_green = (0.343, 0.684, 0.306)
        self.erase_red = (0.951, 0.311, 0.215)
        self.sphere = cmds.polySphere(radius=self.sphereRadius / 10)[0]
        cmds.addAttr(self.sphere, attributeType='float', longName="radius", defaultValue=self.sphereRadius)
        cmds.addAttr(self.sphere, attributeType='float', longName="strength", defaultValue=self.sphereStrength)
        cmds.addAttr(self.sphere, attributeType='float', longName="hardness", defaultValue=sphereHardness)
        cmds.addAttr(self.sphere, attributeType='bool', longName="isErase", defaultValue=False)
        # 创建一个rampshader 材质
        self.mat = cmds.shadingNode('rampShader', asShader=True, name="mat")
        cmds.sets(name='%sSG' % self.mat, renderable=True, noSurfaceShader=True, empty=True)
        cmds.connectAttr('%s.outColor' % self.mat, '%sSG.surfaceShader' % self.mat)
        # 去除光照
        cmds.setAttr('%s.specularity' % self.mat, 0)
        # 将材质赋给球体,并使其不可选中
        cmds.select(self.sphere)
        cmds.sets(forceElement='%sSG' % self.mat)
        # 设置球体的默认ambient颜色值
        if (cmds.getAttr(self.sphere + '.isErase')):
            cmds.setAttr('%s.ambientColor' % self.mat, self.sphereStrength * self.erase_red[0], self.sphereStrength * self.erase_red[1],
                         self.sphereStrength * self.erase_red[2], type="double3")
        else:
            cmds.setAttr('%s.ambientColor' % self.mat, self.sphereStrength * self.add_green[0], self.sphereStrength * self.add_green[1],
                         self.sphereStrength * self.add_green[2], type="double3")
        # 设置球体的默认渐变值
        cmds.setAttr('%s.transparency[0].transparency_Color' % self.mat, 1.0, 1.0, 1.0, type="double3")
        cmds.setAttr('%s.transparency[1].transparency_Color' % self.mat, 0.6, 0.6, 0.6, type="double3")
        cmds.setAttr('%s.transparency[1].transparency_Position' % self.mat, 0.001)
        cmds.setAttr('%s.transparency[1].transparency_Interp' % self.mat, 1)
        # 将该物体设置为不可选中
        cmds.setAttr(self.sphere + ".overrideEnabled", 1)
        cmds.setAttr(self.sphere + ".overrideDisplayType", 2)
        cmds.select(clear=True)

    #画笔的增减模式
    def B(self):
        self.A
        self.sliderC
        print ("B")

        if (cmds.getAttr(self.sphere + '.isErase') == False):
            cmds.setAttr(self.sphere + '.isErase', True)
        else:
            cmds.setAttr(self.sphere + '.isErase', False)
        #加减画笔有不同颜色
        if (cmds.getAttr(self.sphere + '.isErase')):
            cmds.setAttr('%s.ambientColor' % self.mat, self.strength * self.erase_red[0], self.strength * self.erase_red[1],
                         self.strength * self.erase_red[2], type="double3")
        else:
            cmds.setAttr('%s.ambientColor' % self.mat, self.strength * self.add_green[0], self.strength * self.add_green[1],
                         self.strength * self.add_green[2], type="double3")


    #创建地形1
    def E(self):
        print("E")
        #marching_cube_np.init_face()

    #创建地形2
    def F(self):
        print("F")
        #marching_cube_np.init_sphere()

    #清除地形
    def G(self):
        print("G")

    #画笔大小
    def sliderA(self):
        print ("sliderA")
        self.A
        #这个是获取进度条的数值
        self.Radius = self.ui.horizontalSlider_A.value()
        self.ui.spinBox_5.setValue(self.ui.horizontalSlider_A.value())
        # 更新球体的半径
        cmds.setAttr(self.sphere + '.radius', self.Radius)
        scalenow = self.Radius / self.sphereRadius
        cmds.setAttr(self.sphere + '.scale', scalenow, scalenow, scalenow)

    #画笔硬度
    def sliderB(self):
        print ("sliderB")
        self.A
        self.Hardness = self.ui.horizontalSlider_B.value()/100
        self.ui.spinBox_6.setValue(self.ui.horizontalSlider_B.value())
        # 更新球体的硬度
        cmds.setAttr(self.sphere + '.hardness', self.Hardness)
        if (self.Hardness < 1):
            cmds.setAttr('%s.transparency[1].transparency_Position' % self.mat, 1 - self.Hardness)
        #else:
            #cmds.setAttr('%s.transparency[1].transparency_Position' % self.mat, 0.001)

    #画笔强度
    def sliderC(self):
        print ("sliderC")
        self.A
        self.strength = self.ui.horizontalSlider_C.value()/100
        self.ui.spinBox_3.setValue(self.ui.horizontalSlider_C.value())
        # 更新球体的强度/ambient颜色
        cmds.setAttr(self.sphere + '.strength', self.strength)
        if (cmds.getAttr(self.sphere + '.isErase')):
            cmds.setAttr('%s.ambientColor' % self.mat, self.strength * self.erase_red[0], self.strength * self.erase_red[1],
                         self.strength * self.erase_red[2], type="double3")
        else:
            cmds.setAttr('%s.ambientColor' % self.mat, self.strength * self.add_green[0], self.strength * self.add_green[1],
                         self.strength * self.add_green[2], type="double3")

    #地形区块大小
    def terrainSliderA(self):
        print("terrainSliderA")

    #地形长
    def terrainSliderB(self):
        print("terrainSliderB")

    #地形宽
    def terrainSliderC(self):
        print("terrainSliderC")

    #地形高
    def terrainSliderD(self):
        print("terrainSliderD")

    #地形区块大小spinbox
    def spinbox_1(self):
        print("terrainSlider1")

    #地形长spinbox
    def spinbox_2(self):
        print("terrainSlider2")

    #地形宽spinbox
    def spinbox_3(self):
        print("terrainSlider3")

    #地形高spinbox
    def spinbox_4(self):
        print("terrainSlider4")

    #画笔大小spinbox
    def spinbox_5(self):
        self.sliderA
        self.ui.horizontalSlider_A.setValue(self.ui.spinBox_5.value())

    def spinbox_6(self):
        self.sliderB
        self.ui.horizontalSlider_B.setValue(self.ui.spinBox_6.value())

    def spinbox_7(self):
        self.sliderC
        self.ui.horizontalSlider_C.setValue(self.ui.spinBox_7.value())


if __name__ == '__main__':
    myWindow = MclGui()
