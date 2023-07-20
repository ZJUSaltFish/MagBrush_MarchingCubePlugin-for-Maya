import inspect
import os
import sys

script_file = inspect.getframeinfo(inspect.currentframe()).filename
script_dir = os.path.dirname(os.path.abspath(script_file))
script_dir += '\mcl_plugin'
sys.path.append(script_dir)

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui

import mcl_plugin.GUI_setup as gui
import mcl_plugin.manager as manager
from mcl_plugin.tool_context import LandscapeTool

def maya_useNewAPI():
    """
    This is an empty function telling maya to use api2.0
    """
    pass

def initializePlugin(plugin_Object):
    """
    This function is called when loading the plugin from maya plugin manager or command
    :param plugin_Object: Maya will provide this
    :return: none
    """
    plugin_Fn = om.MFnPlugin(plugin_Object, 'ZJU', '1.0', 'Any')
    plugin_manager = manager.MclManager(plugin_Fn)

def uninitializePlugin(plugin_Object):
    """
    This function is called when trying to unload the plugin from plugin manager or command
    :param plugin_Object:
    :return:
    """
    pass
