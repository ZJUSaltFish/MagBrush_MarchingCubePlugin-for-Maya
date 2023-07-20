import maya.cmds as cmds
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui

class LandscapeTool(omui.MPxContext):
    """
    This is a class defining Marching Cubes Landscape Editor
    It dont works. I dont understand
    """
    TOOL_NAME = 'mcltool'

    def __init__(self):
        super(LandscapeTool, self).__init__()


    def __del__(self):
        pass

    def stringClassName(self):
        """
        This function is called by mels to determine the unique name of the tool
        :return: MString
        """
        return self.TOOL_NAME

    def toolOnSetup(self):
        om.MGlobal.displayInfo(self.TOOL_NAME + " is activated.")

    def toolOffCleanup(self):
        om.MGlobal.displayInfo(self.TOOL_NAME + " is stopped.")

    def doPress(self, event, view, _):
        print("Pressed")

class BrushTool():
    CONTEXT_NAME = "BrushContext"

    def __init__(self):
        cmds.draggerContext(self.CONTEXT_NAME , dragCommand = self._ray_check, edit = False, image1 = 'commandButton.png')
        self.brush_name = self.BRUSH_NAME0


    def enable(self):
        cmds.setToolTo(self.CONTEXT_NAME)

    def _ray_check(self):
        mouse_pos = cmds.draggerContext(self.CONTEXT_NAME, query=True, dragPoint=True)

        viewport_pos = om.MPoint(mouse_pos[0], mouse_pos[1], 0)

        #projection_matrix = om.MMatrix(omui.M3dView().active3dView().projectionMatrix())

        ray_source = om.MPoint()
        ray_direction = om.MVector()
        omui.M3dView().active3dView().viewToWorld(int(viewport_pos[0]), int(viewport_pos[1]), ray_source, ray_direction)

        selection_list = om.MGlobal.getActiveSelectionList()

        intersect_point = om.MFloatPoint()

        hit = False
        selec_iter = om.MItSelectionList(selection_list)

        while not selec_iter.isDone():
            dag_path = selec_iter.getDagPath()
            fn_mesh = om.MFnMesh(dag_path)

            hit_return = fn_mesh.closestIntersection(om.MFloatPoint(ray_source), om.MFloatVector(ray_direction),
                                                     om.MSpace.kWorld, 1000, False)
            if hit_return:
                hit = True
                intersect_point = hit_return[0]
                break

            selec_iter.next()

        if hit:
            print("Intersection Point: ", intersect_point)
            #do something else
            self._render_brush(location = intersect_point)
        else:
            self._hide_brush()

    BRUSH_NAME0 = "MCLBrush"
    def _render_brush(self, *, location):
        """
        If no brush created: create a brush at location
        If brush exists: show it, then move to location
        :param location: (floatX, floatY, floatZ)
        :return: None
        """
        if cmds.objExists(self.brush_name) :
            cmds.showHidden(self.brush_name)
        else:
            cmds.sphere(name = self.brush_name, radius = 0.1)
        cmds.move(location[0], location[1], location[2], self.brush_name, absolute=True, worldSpace=True)

    def _hide_brush(self):
        if cmds.objExists(self.brush_name):
            cmds.hide(self.brush_name)
