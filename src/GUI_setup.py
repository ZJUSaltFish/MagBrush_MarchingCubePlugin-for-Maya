'''
Automatically load the tool to shelf after plugin setup
Adjusted based on yunanask's verson
inspired by https://zhuanlan.zhihu.com/p/82989116
'''

import maya.cmds as cmd
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance


class LandscapeTool(omui.MPxContext):
    """
    This is a class defining Marching Cubes Landscape Editor
    as a tool
    It will be placed on maya's tool shelf / custom
    """
    def __init__(self):
        omui.MPxContext.__init__(self)
        print("land")
        self.mainGUI()

    def doPress(self, event, view):
        self.mainGUI()
    def open_gui(self):
        self.mainGUI()
    def mainGUI(self):
        print("HI")
        WINDOW_NAME = 'CC_Tool'
        WINDOW_TITLE = 'CC_Tool1.0'

        try:
            cmd.deleteUI(WINDOW_NAME)
        except:
            pass

        cmd.window(WINDOW_NAME, title=WINDOW_TITLE)
        cmd.columnLayout(adj=True)

        explain_ZeroPivot = '坐标移动至原点'
        explain_Clean = '物体和坐标移动到原点'

        cmd.button(l='ZeroPivot', ann=explain_ZeroPivot, h=60, w=20, c='pivotMoveToWorldPositon000()')
        cmd.button(l='ZeroMeshClean', ann=explain_Clean, h=60, w=20, c='meshMoveToWorldPosition000AndClean()')

        cmd.showWindow(WINDOW_NAME)

    def add_tool_to_shelf(self, tool_name, tool_icon, tool_command):
        shelf_layout = omui.MayaWindow().findChild(QtWidgets.QLayout, "__mainLayout")
        shelf_widget = shelf_layout.itemAt(0).widget()

        button = QtWidgets.QPushButton()
        button.setText(tool_name)
        button.setIcon(QtGui.QIcon(tool_icon))
        button.setToolTip(tool_name)
        button.clicked.connect(tool_command)

        shelf_widget.layout().addWidget(button)
