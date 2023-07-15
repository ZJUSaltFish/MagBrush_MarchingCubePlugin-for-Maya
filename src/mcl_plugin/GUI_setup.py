'''
Automatically load the tool to shelf after plugin setup
Adjusted based on yunanask's verson
inspired by https://zhuanlan.zhihu.com/p/82989116
'''
import maya.cmds
import maya.cmds as cmd
import maya.mel as mel
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance


class LandscapeTool(omui.MPxContext):
    TOOL_NAME = 'mcltool'
    """
    This is a class defining Marching Cubes Landscape Editor
    as a tool
    It will be placed on maya's tool shelf / custom
    """
    def __init__(self):
        omui.MPxContext.__init__(self)
        self.add_to_shelf()

    def stringClassName(self):
        """
        This function is called by mels to determine the unique name of the tool
        :return: MString
        """
        return 'mcltool'
    def doPress(self, event, view):
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

    def add_to_shelf(self):
        """
        This function creates a new tool on the tool shelf.
        Use the tool to start the plugin gui
        :return: None
        """
        print("Adding "+ self.TOOL_NAME + " to Shelf/Custom")
        shelf_top_level = mel.eval("global string $gShelfTopLevel;$temp = $gShelfTopLevel")
        maya.cmds.setParent("%s|Custom" % shelf_top_level)
        maya.cmds.shelfButton( annotation=self.TOOL_NAME, image1 = 'commandButton.png', command=self.mainGUI )

    def remove_from_shelf(self):
        """
        This function deletes the mcltool
        :return: None
        """
        print("Removing " + self.TOOL_NAME+" to Shelf/Custom")
