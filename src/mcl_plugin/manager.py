import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
from GUI_setup import MclGui
from tool_context import BrushTool

class MclManager(object):
    """
    This is a class to manager all the mcltool functions
    mcl = Marching Cube Landscape
    """
    # Constants
    VENDOR = 'zju group 11'
    VERSION = '1.0'
    API_VERSION = 'Any'
    TOOL_NAME = 'mcltool'

    #This class should be a single instance. Only 1 manager in a maya instance
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    #functions
    def __init__(self, *plugin_fn):
        """
        Initialize the mcl class. should receive a maya plugin function set
        :return:
        """
        if( plugin_fn != None):
            self.plugin_fn = plugin_fn
            self.gui = MclGui()
            self.add_to_shelf()
            self.brush_tool = BrushTool()

    def __del__(self):
        pass

    def start_tool(self, _):
        """
        This function starts a custom landscape editing tool
        :return: None
        """
        self.brush_tool.enable()
        """
        try:
            #self.plugin_fn.registerContextCommand(self.TOOL_NAME, self.create_context)
            print("Successfully Initialized")
        except:
            om.MGlobal.displayError("Failed to register Editor")
        """

    def stop_tool(self, _):
        """
        This function deregisters a custom tool and remove it from Maya Kernel
        :return: None
        """

        """
        try:
            self.plugin_fn.deregisterContextCommand(self.TOOL_NAME)
        except:
            om.MGlobal.displayError(("Failed to unregister Editor"))
        """

    def show_gui(self):
        """
        This function shows a gui as interface between user and this manager
        The GUI can be closed and reopened
        :return: None
        """
        WINDOW_NAME = 'CC_Tool'
        WINDOW_TITLE = 'CC_Tool1.0'

        try:
            cmds.deleteUI(WINDOW_NAME)
        except:
            pass

        cmds.window(WINDOW_NAME, title=WINDOW_TITLE)
        cmds.columnLayout(adj=True)

        # Radius Slider
        cmds.separator(height=10, style='none')
        cmds.text(label='Radius')
        cmds.floatSliderGrp(min=1, max=50, value=10, field=True,
                            dragCommand=lambda x: self.brush_tool.set_radius(x))
        # Strength Slider
        cmds.separator(height=10, style='none')
        cmds.text(label='Strength')
        cmds.floatSliderGrp(min=0.0, max=1.0, value=10, field=True,
                            dragCommand=lambda x: self.brush_tool.set_strength(x))


        explain_Tool = "Start landscape editing tool"
        cmds.button(l = 'Tool', ann = explain_Tool, h = 60, w = 20, c = self.start_tool)

        cmds.showWindow(WINDOW_NAME)

    def add_to_shelf(self):
        """
        This function creates a new tool on the tool shelf.
        Use the tool to start the plugin gui
        :return: None
        """
        print("Adding " + self.TOOL_NAME + " to Shelf/Custom")
        shelf_top_level = mel.eval("global string $gShelfTopLevel;$temp = $gShelfTopLevel")
        cmds.setParent("%s|Custom" % shelf_top_level)
        cmds.shelfButton(annotation=self.TOOL_NAME, image1='commandButton.png', command=self.show_gui)

    def remove_from_shelf(self):
        """
        This function deletes the mcltool from tool shelf
        :return: None
        """
        print("Removing " + self.TOOL_NAME + " to Shelf/Custom")

    def debug_func(self):
        om.MGlobal.displayError("DEBUGGING!")