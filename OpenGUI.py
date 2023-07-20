import sys
import maya.cmds as cmd
from PyQt5.QtWidgets import QApplication, QMainWindow
from maya import cmds

qtVersion = cmds.about(qtVersion=True)

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtUiTools

uifile_path = "D:\GitHubProgram\Mayapy_FinalProject\\UITest1.ui"

class MyWindow():
    def __init__(self, parent=None):
        self.ui = loadui(uifile_path)
        self.ui.show()


if __name__ == '__main__':
    myWindow = MyWindow()


def loadui(uifile_path):
    uifile = QtCore.QFile(uifile_path)
    uifile.open(QtCore.QFile.ReadOnly)
    uiWindow = QtUiTools.QUiLoader().load(uifile)
    uifile.close()
    return uiWindow