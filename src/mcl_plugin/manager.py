import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import tool_context as tool
import marching_cube_np as mcnp

import inspect
import os

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtUiTools


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

    # This class should be a single instance. Only 1 manager in a maya instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    # functions
    def __init__(self, *plugin_fn):
        """
        Initialize the mcl class. should receive a maya plugin function set
        :return:
        """
        assert plugin_fn is not None, "Failed to load the mcl plugin!"
        # restore plugin
        self.plugin_fn = plugin_fn
        # add to shelf
        self.add_to_shelf()
        # tools initialize
        self.brush_tool = tool.BrushTool()
        # initialize ui
        script_file = inspect.getframeinfo(inspect.currentframe()).filename
        script_dir = os.path.dirname(os.path.abspath(script_file))
        print(script_dir + "\\UITest.ui")
        self._ui = self._load_gui(script_dir + ".\\UITest1.ui")
        # pointer to marching cube instance
        self._mcl = None
        # parameters of creating mcl
        self._mcl_x = 5
        self._mcl_y = 5
        self._mcl_z = 5
        self._mcl_block_size = 8

    def __del__(self):
        pass

    def start_tool(self, _):
        """
        This function starts a custom landscape editing tool
        :return: None
        """
        self.brush_tool.enable()

    def stop_tool(self, _):
        """
        This function deregisters a custom tool and remove it from Maya Kernel
        :return: None
        """

    def _load_gui(self, uipath):
        # load ui from file
        uifile = QtCore.QFile(uipath)
        uifile.open(QtCore.QFile.ReadOnly)
        ui_window = QtUiTools.QUiLoader().load(uifile)
        uifile.close()
        # initialize ui with functions
        # create brush
        #ui_window.Painter.clicked.connect(self.A)
        #
        #ui_window.Drugger.clicked.connect(self.B)
        #ui_window.CreateCube.clicked.connect(self.C)
        ui_window.CreateSphere.clicked.connect(self.use_sphere_brush)

        # create box landscape
        ui_window.CreateTerrain_A.clicked.connect(self.create_plane_mcl)
        # create spherical terrain
        ui_window.CreateTerrain_B.clicked.connect(self.create_sphere_mcl)
        # kill all terrain
        ui_window.ClearAll.clicked.connect(self.delete_mcl)

        # radius, hardness, strength of brush
        ui_window.horizontalSlider_A.valueChanged.connect(self.brush_tool.set_radius)
        ui_window.horizontalSlider_B.valueChanged.connect(self.brush_tool.set_hardness)
        ui_window.horizontalSlider_C.valueChanged.connect(self.brush_tool.set_strength)

        # block size, x size, y size, z size of terrain
        ui_window.MapSlider_1.valueChanged.connect(self.set_mcl_x)
        ui_window.MapSlider_2.valueChanged.connect(self.set_mcl_y)
        ui_window.MapSlider_3.valueChanged.connect(self.set_mcl_z)
        ui_window.MapSlider_4.valueChanged.connect(self.set_mcl_block)

        return ui_window

    def create_sphere_mcl(self):
        """
        Create a marching cube terrain with a spherical initialization
        :return: None
        """
        self._create_mcl()
        self._mcl.init_sphere()

    def create_plane_mcl(self):
        """
        Create a marching cube terrain with a planer initialization
        :return: None
        """
        self._create_mcl()
        self._mcl.init_face()

    def _create_mcl(self):
        """
        This function creates a new marching cube instance
        :return: marching cubes instance. See marching_cube_np.py
        """
        self.delete_mcl()
        self._mcl = mcnp.MarchingCubeNp(self._mcl_x, self._mcl_y, self._mcl_z, self._mcl_block_size)
        assert self._mcl is not None, "failed to create terrain"
        self.brush_tool.assign_target(self._mcl)

    def delete_mcl(self):
        """
        This function deletes the existing marching cube terrain and reset all that related to it
        :return: None
        """
        if self._mcl is not None:
            del self._mcl
        self._mcl = None
        self.brush_tool.assign_target(None)

    def use_sphere_brush(self):
        """
        Set brush to sphere
        :return: None
        """
        self.brush_tool.enable(tool.BrushTypes.sphere)

    def use_cube_brush(self):
        """
        set brush type to cube
        :return: None
        """
        self.brush_tool.enable(tool.BrushTypes.cube)

    def set_mcl_x(self,x):
        """
        This tool set the mcl_x for creating
        Note it can not be used for editing
        :return: None
        """
        self._mcl_x = x
    def set_mcl_y(self,y):
        """
        This tool set the mcl_y for creating
        Note it can not be used for editing
        :return: None
        """
        self._mcl_y = y
    def set_mcl_z(self,z):
        """
        This tool set the mcl_z for creating
        Note it can not be used for editing
        :return: None
        """
        self._mcl_z = z
    def set_mcl_block(self,b):
        """
        This tool set the mcl_block_sie for creating
        Note it can not be used for editing
        :return: None
        """
        self._mcl_block_size = b

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
        cmds.floatSliderGrp(min=1, max=10, value=1, field=True,
                            dragCommand=lambda x: self.brush_tool.set_radius(x))
        # Strength Slider
        cmds.separator(height=10, style='none')
        cmds.text(label='Strength')
        cmds.floatSliderGrp(min=0.0, max=1.0, value=1, field=True,
                            dragCommand=lambda x: self.brush_tool.set_strength(x))
        # Hardness Slider
        cmds.separator(height=10, style='none')
        cmds.text(label='Hardness')
        cmds.floatSliderGrp(min=0.0, max=1.0, value=1, field=True,
                            dragCommand=lambda x: self.brush_tool.set_hardness(x))

        explain_Tool = "Start landscape editing tool"
        cmds.button(l='Tool', ann=explain_Tool, h=60, w=20, c=self.start_tool)

        cmds.showWindow(WINDOW_NAME)

    def show_ui(self):
        self._ui.show()
    def add_to_shelf(self):
        """
        This function creates a new tool on the tool shelf.
        Use the tool to start the plugin gui
        :return: None
        """
        print("Adding " + self.TOOL_NAME + " to Shelf/Custom")
        shelf_top_level = mel.eval(
            "global string $gShelfTopLevel;$temp = $gShelfTopLevel")
        cmds.setParent("%s|Custom" % shelf_top_level)
        cmds.shelfButton(annotation=self.TOOL_NAME,
                         image1='commandButton.png', command=self.show_ui)

    def remove_from_shelf(self):
        """
        This function deletes the mcltool from tool shelf
        :return: None
        """
        print("Removing " + self.TOOL_NAME + " to Shelf/Custom")

    def debug_func(self):
        om.MGlobal.displayError("DEBUGGING!")
