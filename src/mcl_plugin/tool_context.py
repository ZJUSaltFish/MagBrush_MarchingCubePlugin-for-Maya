import threading
import time

import maya.cmds as cmds
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import math

from marching_cube_np import MarchingCubeNp as mcnp

from enum import Enum


class BrushTypes(Enum):
    sphere = 'mcl_sphere_brush'
    cube = 'mcl_cube_brush'


class BrushModes(Enum):
    add = 0
    subtract = 1
    smooth = 2

class BrushStrokes(Enum):
    by_surface = 0
    by_view = 1

class BrushModeColors():
    add = (0.343, 0.684, 0.306)
    subtract = (0.951, 0.311, 0.215)

class BrushTool():
    CONTEXT_NAME = "BrushContext"

    def __init__(self):
        """
        The tool is a state machine
        Switching its radius, strength, hardness, shape, mode according to GUI
        """
        # initialize variables
        # the pointer to marching cube instance
        self._mcl = None
        # name of brush object
        self._BRUSH_NAME = 'mcl_brush'
        # the material that brush will use
        self._brush_mat = self._create_brush_mat()
        # the shape or type of brush
        self._brush_type = BrushTypes.sphere
        # basic properties of the brush
        self._brush_radius = 1.0
        self._brush_strength = 0.5
        self._brush_hardness = 1.0
        # brush mode, add, subtract, smooth, etc
        self._brush_mode = BrushModes.add

        # registering
        cmds.draggerContext(self.CONTEXT_NAME, initialize=self._switch_on, finalize=self._switch_off, edit=False,
                                                    image1='commandButton.png',
                                                    dragCommand=self._draw, pressCommand=self._draw, releaseCommand = self._release)
        # self._KEY_EVENT = om.MEventMessage.addEventCallback("KeyDown", self._hotkey_callback)

        # variables of a stroke
        self._brush_stroke_mode = BrushStrokes.by_surface
        self._start_source = None
        self._start_dir = None
        self._stroke_start = None
        self._brush_dragging = False

    def unload(self):
        self._mcl = None
        cmds.setToolTo("moveSuperContext")
        if cmds.draggerContext(self.CONTEXT_NAME, exists=True):
            cmds.deleteUI(self.CONTEXT_NAME, toolContext=True)
        print("Tool Context Deleted")

    def assign_target(self, mcl_instance):
        """
        This function sets the target of the tool. If no target set, tool will not work
        :param mcl_instance: instance of MarchingCubeNp. See marching_cube_np.py
        :return: None
        """
        self._mcl = mcl_instance

    def enable(self, *brush_type):
        """
        This function is used when clicking "Tool" button on GUI
        It will create a new tool instance
        :param BrushTypes.brush_type:
        :return:
        """
        # update brush type
        self._brush_type = brush_type
        # activate the tool
        cmds.setToolTo(self.CONTEXT_NAME)

    def update_mode(self):
        """
        This function updates the hotkey states and returns the current brush mode
        :return: BrushModes.some_mode
        """
        if cmds.getModifiers() & 1:
            self._brush_mode = BrushModes.subtract
        elif cmds.getModifiers() & 3:
            self._brush_mode = BrushModes.smooth
        else:
            self._brush_mode = BrushModes.add
        return self._brush_mode

    def set_radius(self, radius):
        self._brush_radius = radius / 10.0
        if self._brush_type == BrushTypes.sphere:
            # Find the node that builds the sphere brush
            build_node = None
            if cmds.ls(self._BRUSH_NAME) != []:
                history = cmds.listHistory(self._BRUSH_NAME)
                for node in history:
                    if cmds.nodeType(node) == 'makeNurbSphere':
                        build_node = node
                        break

                cmds.setAttr(build_node + '.radius', self._brush_radius)

    def set_hardness(self, hardness):
        self._brush_hardness = hardness / 100.0
        cmds.setAttr('%s.transparency[1].transparency_Position' % self._brush_mat, 1 - self._brush_hardness * 0.9)

    def set_strength(self, strength):
        self._brush_strength = strength / 100.0
        if self._brush_mode == BrushModes.add:
            cmds.setAttr('%s.ambientColor' % self._brush_mat,
                         self._brush_strength * BrushModeColors.add[0],
                         self._brush_strength * BrushModeColors.add[1],
                         self._brush_strength * BrushModeColors.add[2],
                         type="double3")
        else:
            cmds.setAttr('%s.ambientColor' % self._brush_mat,
                         self._brush_strength * BrushModeColors.subtract[0],
                         self._brush_strength * BrushModeColors.subtract[1],
                         self._brush_strength * BrushModeColors.subtract[2],
                         type="double3")

    def _switch_on(self):
        """
        This function is used to create a new tool instance
        automatically called when switching to mcltool
        :return:
        """
        self._new_brush(self._brush_type)

    def _switch_off(self):
        """
        This function is used to delete current tool instance
        automatically called when switching off
        :return:
        """
        if cmds.objExists(self._BRUSH_NAME):
            cmds.delete(self._BRUSH_NAME)

    def _draw(self):
        """
        This function combine _press and _draw to prevent bug caused by maya dragCommand and pressCommand
        Called when user is drawing a stroke.
        It works differently according to brush mode:
        mode0 - draw on surface.
        mode1 - draw on view plane. This enables drawing on void
        By default, mode0
        :return: None
        """
        if self._brush_stroke_mode is BrushStrokes.by_surface:
            # draw on surface: just keep drawing
            if self._mcl is None:
                return
            self.update_mode()
            location = self._ray_march()
            if location is None:
                self._hide_brush()
            else:
                self._render_brush(location=location)
                if self._brush_mode == BrushModes.subtract:
                    self._mcl.add_point(location, self._brush_radius, self._brush_strength, self._brush_hardness)
                else:
                    self._mcl.add_point(location, self._brush_radius, -self._brush_strength, self._brush_hardness)

        elif self._brush_stroke_mode is BrushStrokes.by_view:
            # draw by wive: the press determines the stroke start, then the drag moves brush on view plane
            if self._brush_dragging:
                self._drag()
            else:
                self._brush_dragging = True
                self._press()
        else:
            pass

    def _release(self):
        """
        This function is called when user release mouse
        :return:
        """
        self._brush_dragging = False
        self._start_source = None
        self._start_dir = None
        self._stroke_start = None

    def switch_stroke(self, new_stroke_mode):
        """
        This function switches the stroke mode.
        :param new_stroke_mode: BrushStrokes(Enum)
        :return: None
        """
        self._brush_stroke_mode = new_stroke_mode
        self._release()  # reset the brush

    def _press(self):
        """
        This function called when mouse pressed. it stores the start point of stroke
        :return: None
        """
        # Only draw when there is a landscape instance
        if self._mcl is None:
            return
        # first update brush mode
        self.update_mode()
        # then get brush location
        mouse_pos = cmds.draggerContext(self.CONTEXT_NAME, query=True, anchorPoint=True)
        tmp = self._ray_check(mouse_pos)
        # location = self._ray_march()
        if tmp is None:
            # failed to start a stroke on void
            self._hide_brush()

            self._stroke_start = None
            self._start_source = None
            self._start_dir = None

            self._brush_dragging = False
        else:
            (x,y,z,t) = tmp[0]
            self._stroke_start = om.MPoint(x,y,z)
            self._start_source = tmp[1]
            self._start_dir = tmp[2]
            # place brush at location
            self._render_brush(location=self._stroke_start)
            # edit marching cubes at location
            (x, y, z, t) = self._stroke_start
            if self._brush_mode == BrushModes.subtract:
                # press shift to subtract
                self._mcl.add_point(om.MPoint(x, y, z),
                                 self._brush_radius, self._brush_strength, self._brush_hardness)
            else:
                self._mcl.add_point(om.MPoint(x, y, z),
                                 self._brush_radius, -self._brush_strength, self._brush_hardness)

    def _drag(self):
        """
        This function called when user is dragging cursor to draw
        :return: None
        """
        # Only draw when there is a landscape instance
        if self._mcl is None:
            return
        # first update brush mode
        self.update_mode()
        # then get brush location
        mouse_pos = cmds.draggerContext(self.CONTEXT_NAME, query=True, dragPoint=True)
        location = self._ray_to_view(mouse_pos)
        # location = self._ray_march()
        if location is None:
            self._hide_brush()
        else:
            # place brush at location
            self._render_brush(location=location)
            # edit marching cubes at location
            (x, y, z) = (location.x, location.y, location.z)
            if self._brush_mode == BrushModes.subtract:
                # press shift to subtract
                self._mcl.add_point(om.MPoint(x, y, z),
                                 self._brush_radius, self._brush_strength, self._brush_hardness)
            else:
                self._mcl.add_point(om.MPoint(x, y, z),
                                 self._brush_radius, -self._brush_strength, self._brush_hardness)
            # self._mcl.render()

    def _ray_to_view(self, mouse_pos):
        """
        This function calculates the intersection point of the ray from mouse and view plane passing brush
        """

        viewport_pos = om.MPoint(mouse_pos[0], mouse_pos[1], 0)
        ray_source = om.MPoint()
        ray_direction = om.MVector()
        omui.M3dView().active3dView().viewToWorld(
            int(viewport_pos[0]), int(viewport_pos[1]), ray_source, ray_direction)

        normal = self._start_source - self._stroke_start

        angle_btn = om.MVector.angle(-normal, ray_direction)

        view_to_point = ray_direction * om.MVector.length(normal) / math.cos(angle_btn)

        target = self._stroke_start + normal + om.MVector(ray_source) - om.MVector(self._start_source) + view_to_point

        return om.MVector(target)

    def _ray_check(self, mouse_pos):
        """
        This function use the ray check method to get the intersection point of the ray from mouse and the terrain mesh
        The intersection point can be used for brush position.
        :param mouse_pos:
        :return:
        """

        viewport_pos = om.MPoint(mouse_pos[0], mouse_pos[1], 0)

        # projection_matrix = om.MMatrix(omui.M3dView().active3dView().projectionMatrix())

        ray_source = om.MPoint()
        ray_direction = om.MVector()
        omui.M3dView().active3dView().viewToWorld(
            int(viewport_pos[0]), int(viewport_pos[1]), ray_source, ray_direction)

        #selection_list = om.MGlobal.getActiveSelectionList()
        selection_list = om.MSelectionList()
        tmp_list = cmds.ls("block*")
        for selected in tmp_list:
            selection_list.add(selected)

        hit = False
        selec_iter = om.MItSelectionList(selection_list)

        final_hit_return = []

        while not selec_iter.isDone():
            dag_path = selec_iter.getDagPath()
            fn_mesh = om.MFnMesh(dag_path)

            hit_return = fn_mesh.closestIntersection(om.MFloatPoint(ray_source), om.MFloatVector(ray_direction),
                                                     om.MSpace.kWorld, 1000, False)
            if hit_return:
                if final_hit_return == [] or hit_return[1] < final_hit_return[1]:
                    final_hit_return = hit_return
                # hit = True
                # intersect_point = hit_return[0]
                # break

            selec_iter.next()

        if final_hit_return != []:
            intersect_point = final_hit_return[0]
            return (intersect_point, ray_source, ray_direction)
        else:
            return None

    def _ray_march(self):
        """
        Ray marching is another way to get the brush position
        This method enabled because Marching Cubes have sample points of SDF
        :return: the location of brush
        """
        # get mouse position in pixel coordinate
        mouse_pos = cmds.draggerContext(
            self.CONTEXT_NAME, query=True, dragPoint=True)
        # convert to MPoint
        viewport_pos = om.MPoint(mouse_pos[0], mouse_pos[1], 0)
        # get the source and direction of ray
        ray_source = om.MPoint()
        ray_direction = om.MVector()
        omui.M3dView().active3dView().viewToWorld(
            int(viewport_pos[0]), int(viewport_pos[1]), ray_source, ray_direction)
        # marching until touch the surface of SDF
        step = 1.0
        find = False
        for i in range(64):
            ray_source += ray_direction * step
            dist = self._mcl.get_distance(ray_source)
            if -0.15 < dist < 0.15:
                find = True
                break
            elif dist < 0:
                step = -0.1
            elif dist < 0.5:
                step = 0.1
            else:
                pass
        if find is True:
            return ray_source
        else:
            return None

    def _render_brush(self, *, location):
        """
        If no brush created: create a brush at location
        If brush exists: show it, then move to location
        :param location: (floatX, floatY, floatZ)
        :return: None
        """
        if cmds.objExists(self._BRUSH_NAME):
            cmds.showHidden(self._BRUSH_NAME)
            cmds.move(location[0], location[1], location[2],
                      self._BRUSH_NAME, absolute=True, worldSpace=True)
            cmds.refresh()

    def _hide_brush(self):
        if cmds.objExists(self._BRUSH_NAME):
            cmds.hide(self._BRUSH_NAME)

    def _new_brush(self, *brush_type):
        # delete old brush object
        if cmds.objExists(self._BRUSH_NAME):
            cmds.delete(self._BRUSH_NAME)
        # create new brush object
        if brush_type == BrushTypes.cube:
            self._brush_type = BrushTypes.cube
            pass
        else:
            # 创建默认的球体
            cmds.sphere(name=self._BRUSH_NAME, radius=self._brush_radius)
            # 将材质赋给球体,并使其不可选中
            cmds.select(self._BRUSH_NAME)
            cmds.sets(forceElement='%sSG' % self._brush_mat)
            # 设置球体的默认ambient颜色值
            if self._brush_mode == BrushModes.subtract:
                cmds.setAttr('%s.ambientColor' % self._brush_mat,
                             self._brush_strength * BrushModeColors.subtract[0],
                             self._brush_strength * BrushModeColors.subtract[1],
                             self._brush_strength * BrushModeColors.subtract[2],
                             type="double3")
            else:
                cmds.setAttr('%s.ambientColor' % self._brush_mat,
                             self._brush_strength * BrushModeColors.add[0],
                             self._brush_strength * BrushModeColors.add[1],
                             self._brush_strength * BrushModeColors.add[2],
                             type="double3")
            # 设置球体的默认渐变值
            cmds.setAttr('%s.transparency[0].transparency_Color' %
                         self._brush_mat, 1.0, 1.0, 1.0, type="double3")
            cmds.setAttr('%s.transparency[1].transparency_Color' %
                         self._brush_mat, 0.54, 0.54, 0.54, type="double3")
            cmds.setAttr(
                '%s.transparency[1].transparency_Position' % self._brush_mat, 0.001)
            cmds.setAttr(
                '%s.transparency[1].transparency_Interp' % self._brush_mat, 1)
            # 将该物体设置为不可选中
            cmds.setAttr(self._BRUSH_NAME + ".overrideEnabled", 1)
            cmds.setAttr(self._BRUSH_NAME + ".overrideDisplayType", 2)
            cmds.select(clear=True)
            # make sure self._brush_type is not None
            self._brush_type = BrushTypes.sphere

    def _create_brush_mat(self):
        """
        Create a rampshader material
        return: material shading node (cmds.shadingNode)
        """
        mat = cmds.shadingNode('rampShader', asShader=True, name="mat")
        cmds.sets(name='%sSG' % mat, renderable=True,
                  noSurfaceShader=True, empty=True)
        cmds.connectAttr('%s.outColor' % mat, '%sSG.surfaceShader' % mat)
        # set no lighting
        cmds.setAttr('%s.specularity' % mat, 0)
        return mat
