'''
Automatically load the tool to shelf after plugin setup
Adjusted based on yunanask's verson
inspired by https://zhuanlan.zhihu.com/p/82989116
'''

import maya.cmds as cmd
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui



class LandscapeTool(omui.MPxContext):
    """
    This is a class defining Marching Cubes Landscape Editor
    as a tool
    It will be placed on maya's tool shelf / custom
    """
    def __int__(self):
        omui.MPxContext.__init__(self)

    def doPress(self, event, view):
        self.mainGUI()
    def open_gui(self):
        self.mainGUI()
    def mainGUI(self):
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

