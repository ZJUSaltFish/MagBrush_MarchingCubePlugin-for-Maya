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
    def __init__(self, plugin_fn=None):
        """
        Initialize the mcl class. should receive a maya plugin function set
        :return:
        """
        if plugin_fn is None:
            # calling a singleton
            pass
        else:
            # restore plugin
            self.plugin_fn = plugin_fn
            # add to shelf
            self.shelf_button = 'Shelf|MainShelfLayout|formLayout17|ShelfLayout|Custom|' + self.TOOL_NAME
            self.add_to_shelf()
            # tools initialize
            self.brush_tool = tool.BrushTool()
            # initialize ui
            script_file = inspect.getframeinfo(inspect.currentframe()).filename
            script_dir = os.path.dirname(os.path.abspath(script_file))
            self.ui = self._load_gui(script_dir + ".\\UITest1.ui")
            # pointer to marching cube instance
            self._mcl = None
            # parameters of creating mcl
            self._mcl_x = 5
            self._mcl_y = 5
            self._mcl_z = 5
            self._mcl_block_size = 8
            self._mcl_material = self.create_mcl_material()

    def __del__(self):
        self.remove_from_shelf()

    def unload(self):
        """
        The del function is called when the plugin is unloaded
        :return: None
        """
        # unload from shelf
        if self.brush_tool is not None:
            self.brush_tool.unload()
        if self._mcl is not None:
            self._mcl.unload()
        self.ui.close()
        self.remove_from_shelf()
        print("Shelf Button Deleted")

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
        ui_window.MapSlider_2.valueChanged.connect(lambda x: (self.set_mcl_x(x), self.ui.spinBox_2.setValue(x)))
        ui_window.MapSlider_3.valueChanged.connect(lambda z: (self.set_mcl_z(z), self.ui.spinBox_3.setValue(z)))
        ui_window.MapSlider_4.valueChanged.connect(lambda y: (self.set_mcl_y(y), self.ui.spinBox_4.setValue(y)))

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
        self._mcl = mcnp.MarchingCubeNp(self._mcl_x, self._mcl_y, self._mcl_z, self._mcl_block_size, self._mcl_material)
        assert self._mcl is not None, "failed to create terrain"
        self.brush_tool.assign_target(self._mcl)

    def delete_mcl(self):
        """
        This function deletes the existing marching cube terrain and reset all that related to it
        :return: None
        """
        if self._mcl is not None:
            self._mcl.unload()
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

    def add_to_shelf(self):
        """
        This function creates a new tool on the tool shelf.
        Use the tool to start the plugin gui
        :return: None
        """
        self.remove_from_shelf()  
        cmds.shelfLayout("MagBrush", parent='ShelfLayout')
        cmds.setParent("MagBrush")
        icon_path = os.path.dirname(os.path.abspath(
            inspect.getframeinfo(inspect.currentframe()).filename
            )) + '\\pic\\icon.png'
        self.shelf_button = cmds.shelfButton(self.TOOL_NAME,annotation=self.TOOL_NAME,
                                             image1=icon_path, command=self.show_ui)

    def remove_from_shelf(self):
        """
        This function deletes the mcltool from tool shelf
        :return: None
        """
        if cmds.shelfLayout("MagBrush", exists=True):
            buttons = cmds.shelfLayout("MagBrush", query=True, childArray=True)
            if buttons:
                cmds.deleteUI(buttons)
            cmds.deleteUI("MagBrush")

    def create_mcl_material(self):
        """
        create a landscape auto material.
        material
        |- ground: the flatter, the more ground
        |   |- grass: the higher, the more grass
        |   |- dirt: the lower, the more dirt
        |- cliff: the steeper, the more cliff
        :return: a shading group
        """

        # get camera to world matrix
        camera = cmds.lookThru(q=True)
        # create shader
        shader = cmds.shadingNode('lambert', asShader=True, name="mcl_terrain_default")
        # sampler for mesh
        sampler = cmds.shadingNode('samplerInfo', asUtility=True)
        # preset colors
        color_grass = (0.388, 1.00, 0.101)
        color_dirt = (0.530, 0.499, 0.179)
        color_cliff = (0.208, 0.211, 0.222)
        # creating and connecting nodes

        # a scale factor according to land height
        scale_factor = cmds.shadingNode('multiplyDivide', asUtility=True)
        cmds.setAttr(scale_factor + '.operation', 2)  # divide mode
        cmds.setAttr(scale_factor + '.input2', 20.0, 1.0, 1.0, type='float3')  # divide by 20
        cmds.connectAttr(sampler + '.pointObjY', scale_factor + '.input1X')

        # blend according to height to determine whether it is grass or dirt
        blend_height = cmds.shadingNode('blendColors', asUtility=True)
        cmds.setAttr(blend_height + '.color1', color_grass[0], color_grass[1], color_grass[2], type='float3')
        cmds.setAttr(blend_height + '.color2', color_dirt[0], color_dirt[1], color_dirt[2], type='float3')
        cmds.connectAttr(scale_factor + '.outputX', blend_height + '.blender')  # use a scaled coefficient to blend

        # the node to transform camera space to world space
        eye_to_world = cmds.shadingNode('vectorProduct', asUtility=True)
        cmds.setAttr(eye_to_world + '.normalizeOutput', True)
        cmds.setAttr(eye_to_world + '.operation', 3)
        cmds.connectAttr(camera + '.worldMatrix[0]', eye_to_world + '.matrix')# camera matrix
        cmds.connectAttr(sampler + '.normalCamera', eye_to_world + '.input1')# the normal in camera space to be transformed


        # This node remaps normalY (-1,1) to (0,1), and determine cliff or ground.
        remap = cmds.shadingNode('remapValue', asUtility = True)
        cmds.setAttr(remap + '.inputMax', 1)
        cmds.setAttr(remap + '.inputMin', -1)
        cmds.setAttr(remap + '.value[0].vlp', 0.6)  # vlp: start point of a linear interpolate
        cmds.setAttr(remap + '.value[0].vlfv', 0.0)  # vlfv: start value of a linear interpolate
        cmds.setAttr(remap + '.value[0].vli', 1)  # using a linear interpolation
        cmds.setAttr(remap + '.value[1].vlp', 0.7)
        cmds.setAttr(remap + '.value[1].vlfv', 1.0)
        cmds.setAttr(remap + '.value[1].vli', 1)
        cmds.connectAttr(eye_to_world + '.outputY', remap + '.inputValue')

        # the node to blend between cliff and ground using normal
        cliff_ground_blend = cmds.shadingNode('blendColors', asUtility=True)
        cmds.connectAttr(blend_height + '.output', cliff_ground_blend + '.color1')
        cmds.setAttr(cliff_ground_blend + '.color2', color_cliff[0], color_cliff[1], color_cliff[2], type='float3')
        cmds.connectAttr(remap + '.outValue', cliff_ground_blend + '.blender')

        # connect to output!
        cmds.connectAttr(cliff_ground_blend + '.output', shader + '.color')

        shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
        cmds.connectAttr(shader + ".outColor", shading_group + '.surfaceShader', f=True)
        return shading_group

    def debug_func(self):
        om.MGlobal.displayError("DEBUGGING!")
