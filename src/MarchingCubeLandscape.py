import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omUI

def maya_useNewAPI():
    """
    This is an empty function telling maya to use api2.0
    """
    pass

def initializePlugin(plugin_object):
    plugin_Fn = om.MFnPlugin(plugin_object)

    try:
        pass
    except:
        om.MGlobal.displayError("Failed to register Editor")

def uninitializePlugin(plugin_object):
    plugin_object = om.MFnPlugin(plugin_object)

    try:
        pass
    except:
        om.MGlobal.displayError(("Failed to unregister Editor"))
