import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import tool_context as tool
import marching_cube_np as mcnp

import inspect
import os

import picture
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
        self.ui = self._load_gui(script_dir + ".\\UITest1.ui")
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
        ui_window.Painter.clicked.connect(self.use_sphere_brush)

        ui_window.Drugger.stateChanged.connect(lambda x:x)

        # create box landscape
        ui_window.CreateTerrain_A.clicked.connect(self.create_plane_mcl)
        # create spherical terrain
        ui_window.CreateTerrain_B.clicked.connect(self.create_sphere_mcl)
        # kill all terrain
        ui_window.ClearAll.clicked.connect(self.delete_mcl)

        # radius, hardness, strength of brush
        ui_window.horizontalSlider_A.valueChanged.connect(lambda x: (self.brush_tool.set_radius(x), self.ui.spinBox_5.setValue(x)))
        ui_window.horizontalSlider_B.valueChanged.connect(lambda x: (self.brush_tool.set_hardness(x), self.ui.spinBox_6.setValue(x)))
        ui_window.horizontalSlider_C.valueChanged.connect(lambda x: (self.brush_tool.set_strength(x), self.ui.spinBox_7.setValue(x)))

        # block size, x size, y size, z size of terrain
        ui_window.MapSlider_1.valueChanged.connect(lambda x: (self.set_mcl_block(x), self.ui.spinBox_1.setValue(x)))
        ui_window.MapSlider_2.valueChanged.connect(lambda x: (self.set_mcl_y(x), self.ui.spinBox_2.setValue(x)))
        ui_window.MapSlider_3.valueChanged.connect(lambda y: (self.set_mcl_x(y), self.ui.spinBox_3.setValue(y)))
        ui_window.MapSlider_4.valueChanged.connect(lambda z: (self.set_mcl_x(z), self.ui.spinBox_4.setValue(z)))

        # spin box
        ui_window.spinBox_1.valueChanged.connect(lambda: self.ui.MapSlider_1.setValue(self.ui.spinBox_1.value()))
        ui_window.spinBox_2.valueChanged.connect(lambda: self.ui.MapSlider_2.setValue(self.ui.spinBox_2.value()))
        ui_window.spinBox_3.valueChanged.connect(lambda: self.ui.MapSlider_3.setValue(self.ui.spinBox_3.value()))
        ui_window.spinBox_4.valueChanged.connect(lambda: self.ui.MapSlider_4.setValue(self.ui.spinBox_4.value()))
        ui_window.spinBox_5.valueChanged.connect(lambda: self.ui.horizontalSlider_A.setValue(self.ui.spinBox_5.value()))
        ui_window.spinBox_6.valueChanged.connect(lambda: self.ui.horizontalSlider_B.setValue(self.ui.spinBox_6.value()))
        ui_window.spinBox_7.valueChanged.connect(lambda: self.ui.horizontalSlider_C.setValue(self.ui.spinBox_7.value()))

        # set initial value
        ui_window.horizontalSlider_A.setValue(10)
        ui_window.horizontalSlider_B.setValue(50)
        ui_window.horizontalSlider_C.setValue(100)

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

    def show_ui(self):
        self.ui.show()

    def spinbox_1(self):
        print("terrainSlider1")

    #地形长spinbox
    def spinbox_2(self):
        print("terrainSlider2")

    #地形宽spinbox
    def spinbox_3(self):
        print("terrainSlider3")

    #地形高spinbox
    def spinbox_4(self):
        print("terrainSlider4")

    #画笔大小spinbox
    def spinbox_5(self):
        self.ui.horizontalSlider_A.setValue(self.ui.spinBox_5.value())

    def spinbox_6(self):
        self.ui.horizontalSlider_B.setValue(self.ui.spinBox_6.value())

    def spinbox_7(self):
        self.ui.horizontalSlider_C.setValue(self.ui.spinBox_7.value())

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
