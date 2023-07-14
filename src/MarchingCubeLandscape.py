import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import GUI_setup as gui

def maya_useNewAPI():
    """
    This is an empty function telling maya to use api2.0
    """
    pass


class ToolBuildCommand(omui.MPxContextCommand):
    def __int__(self):
        om.MPxContextCommand.__init__(self)
    def makeObj(self):
        return  gui.LandscapeTool()

    @classmethod
    def tool_creator(cls):
        return ToolBuildCommand()

def initializePlugin(plugin_object):
    plugin_Fn = om.MFnPlugin(plugin_object)

    try:
        plugin_Fn.registerContextCommand("MCL_Tool", ToolBuildCommand.tool_creator())
    except:
        om.MGlobal.displayError("Failed to register Editor")

def uninitializePlugin(plugin_object):
    plugin_Fn = om.MFnPlugin(plugin_object)

    try:
        plugin_Fn.deregisterContextCommand("MCL_Tool")
    except:
        om.MGlobal.displayError(("Failed to unregister Editor"))
