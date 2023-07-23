import inspect
import os
import sys
# Add this plugin to maya python dir
script_file = inspect.getframeinfo(inspect.currentframe()).filename
script_dir = os.path.dirname(os.path.abspath(script_file))
sys.path.append(script_dir + '\\mcl_plugin')
# Add numpy to maya python dir
sys.path.append(script_dir + '\\numpy')
# Add pyqt5 to maya python dir
sys.path.append(script_dir + '\\PyQt5')
# Add PySide2 to maya python dir
sys.path.append(script_dir + '\\PySide2')
# Add
sys.path.append(script_dir + '\\PyQt5\\PyQt5')

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui

import mcl_plugin.manager as manager



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
