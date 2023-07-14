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

    @staticmethod
    def toolCreator():
        return ToolBuildCommand()

def initializePlugin(plugin_Object):
    plugin_Fn = om.MFnPlugin(plugin_Object, 'ZJU', '1.0', 'Any')

    try:
        print("TRYIT")
        plugin_Fn.registerContextCommand("mcltool", ToolBuildCommand.toolCreator)
    except:
        om.MGlobal.displayError("Failed to register Editor")

def uninitializePlugin(plugin_Object):
    plugin_Fn = om.MFnPlugin(plugin_Object, 'ZJU', '1.0', 'Any')

    try:
        plugin_Fn.deregisterContextCommand("mcltool")
    except:
        om.MGlobal.displayError(("Failed to unregister Editor"))
