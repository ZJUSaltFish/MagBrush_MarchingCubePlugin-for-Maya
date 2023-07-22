import sys
import maya.cmds as cmd
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from maya import cmds
import marching_cube_np

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

class MyWindow():
    def __init__(self, parent=None):
        self.ui = loadui(uifile_path)
        self.ui.show()

        #button
        self.ui.Painter.clicked.connect(self.A)
        self.ui.Drugger.clicked.connect(self.B)
        self.ui.CreateCube.clicked.connect(self.C)
        self.ui.CreateSphere.clicked.connect(self.D)

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

        #checkbox


    def A(self):
        # 创建默认的球体
        self.sphereRadius = 10
        sphereStrength = 0.5
        sphereHardness = 1.0
        self.sphere = cmds.polySphere(radius=self.sphereRadius / 10)[0]
        cmds.addAttr(self.sphere, attributeType='float', longName="radius", defaultValue=self.sphereRadius)
        cmds.addAttr(self.sphere, attributeType='float', longName="strength", defaultValue=sphereStrength)
        cmds.addAttr(self.sphere, attributeType='float', longName="hardness", defaultValue=sphereHardness)
        # 创建一个rampshader 材质
        self.mat = cmds.shadingNode('rampShader', asShader=True, name="mat")
        cmds.sets(name='%sSG' % self.mat, renderable=True, noSurfaceShader=True, empty=True)
        cmds.connectAttr('%s.outColor' % self.mat, '%sSG.surfaceShader' % self.mat)
        # 将材质赋给球体,并使其不可选中
        cmds.select(self.sphere)
        cmds.sets(forceElement='%sSG' % self.mat)
        # 设置球体的默认ambient颜色值
        cmds.setAttr('%s.ambientColor' % self.mat, sphereStrength, sphereStrength, sphereStrength, type="double3")
        # 设置球体的默认渐变值
        cmds.setAttr('%s.transparency[0].transparency_Color' % self.mat, 1.0, 1.0, 1.0, type="double3")
        cmds.setAttr('%s.transparency[1].transparency_Color' % self.mat, 0, 0, 0, type="double3")
        cmds.setAttr('%s.transparency[1].transparency_Position' % self.mat, 0.001)
        cmds.setAttr('%s.transparency[1].transparency_Interp' % self.mat, 1)
        # 将该物体设置为不可选中
        cmds.setAttr(self.sphere + ".overrideEnabled", 1)
        cmds.setAttr(self.sphere + ".overrideDisplayType", 2)
        cmds.select(clear=True)
    def B(self):
        print ("B")
    def C(self):
        print ("C")
    def D(self):
        print ("D")
        self.A
        self.sliderA
        self.sliderB
        self.sliderC

    def E(self):
        marching_cube_np.init_face()
    def F(self):
        marching_cube_np.init_sphere()

    def sliderA(self):
        print ("sliderA")
        self.A
        self.Radius = self.ui.horizontalSlider_A.value()
        # 更新球体的半径
        cmds.setAttr(self.sphere + '.radius', self.Radius)
        scalenow = self.Radius / self.sphereRadius
        cmds.setAttr(self.sphere + '.scale', scalenow, scalenow, scalenow)


    def sliderB(self):
        print ("sliderB")
        self.A
        self.Hardness = self.ui.horizontalSlider_B.value()
        # 更新球体的硬度
        cmds.setAttr(self.sphere + '.hardness', self.Hardness)
        if (self.Hardness < 1):
            cmds.setAttr('%s.transparency[1].transparency_Position' % self.mat, 1 - self.Hardness)
        else:
            cmds.setAttr('%s.transparency[1].transparency_Position' % self.mat, 0.001)


    def sliderC(self):
        print ("sliderC")
        self.A
        self.Strength = self.ui.horizontalSlider_C.value()
        # 更新球体的强度/ambient颜色
        cmds.setAttr(self.sphere + '.strength', self.Strength)
        cmds.setAttr('%s.ambientColor' % self.mat, self.Strength, self.Strength, self.Strength, type="double3")


if __name__ == '__main__':
    myWindow = MyWindow()
