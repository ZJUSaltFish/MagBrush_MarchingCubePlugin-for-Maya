import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import mcl_plugin.GUI_setup as gui

def maya_useNewAPI():
    """
    This is an empty function telling maya to use api2.0
    """
    pass


class ToolBuildCommand(omui.MPxContextCommand):
    def __init__(self):
        omui.MPxContextCommand.__init__(self)
        self.makeObj()

    def __del__(self):
        self.tool.remove_from_shelf()

    def makeObj(self):
        """
        This is an overlay function of MPxContetCommand.makeObj
        It Creates a proxy context. Maya dont call it(why?) so I call it in __init__
        :return: MPxContext
        """
        self.tool = gui.LandscapeTool()

    @staticmethod
    def toolCreator():
        return ToolBuildCommand()

def initializePlugin(plugin_Object):
    """
    This function is called when loading the plugin from maya plugin manager or command
    :param plugin_Object: Maya will provide this
    :return: none
    """
    plugin_Fn = om.MFnPlugin(plugin_Object, 'ZJU', '1.0', 'Any')
    try:
        plugin_Fn.registerContextCommand("mcltool", ToolBuildCommand.toolCreator)
        print("Successfully Initialized")
    except:
        om.MGlobal.displayError("Failed to register Editor")

def uninitializePlugin(plugin_Object):
    """
    This function is called when trying to unload the plugin from plugin manager or command
    :param plugin_Object:
    :return:
    """
    plugin_Fn = om.MFnPlugin(plugin_Object, 'ZJU', '1.0', 'Any')

    try:
        plugin_Fn.deregisterContextCommand("mcltool")
    except:
        om.MGlobal.displayError(("Failed to unregister Editor"))
