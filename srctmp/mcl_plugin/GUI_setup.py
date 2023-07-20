import maya.cmds as cmd
import maya.mel as mel
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui

class MclGui():
    TOOL_NAME = 'mcltool'
    """
    This is a class defining Marching Cubes Landscape Editor
    as a tool
    It will be placed on maya's tool shelf / custom
    """
    def __init__(self):
        pass
    def custom_gui_settings(self):
        """
        Some functions like this defines custom gui settings
        :return: a custom gui setting
        """
        pass
