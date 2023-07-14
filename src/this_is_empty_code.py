import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omUI
import maya.cmds as cmds

def ray_check():
    mouse_pos = cmds.draggerContext('DraggerContext', query=True, anchorPoint=True)

    viewport_pos = om.MPoint(mouse_pos[0], mouse_pos[1], 0)
    #viewport_vec = om.MVector(viewport_pos)
    #viewport_vec.normalize()
    #viewport_pos = om.MPoint(viewport_vec)

    #camera = omUI.M3dView().active3dView().camera()
    projection_matrix = om.MMatrix(omUI.M3dView().active3dView().projectionMatrix())
    inverse_matrix = projection_matrix.inverse()
    
    ray_source = om.MPoint()
    ray_direction = om.MVector()
    omUI.M3dView().active3dView().viewToWorld(int(viewport_pos[0]), int(viewport_pos[1]), ray_source, ray_direction)

    selection_list = om.MGlobal.getActiveSelectionList()

    intersect_point = om.MFloatPoint()
    intersect_normal = om.MFloatVector()

    hit = False
    selec_iter = om.MItSelectionList(selection_list)

    while not selec_iter.isDone():
        dag_path = selec_iter.getDagPath()
        fn_mesh = om.MFnMesh(dag_path)

        hit_return = fn_mesh.closestIntersection(om.MFloatPoint(ray_source), om.MFloatVector(ray_direction), om.MSpace.kWorld, 1000, False)
        if hit_return:
            hit = True
            intersect_point = hit_return[0]
            break

        selec_iter.next()

    if hit:
        #intersect_point = intersect_point * camera.inclusiveMatrix()

        print("Intersection Point: ", intersect_point)



cmds.draggerContext("DraggerContext", pressCommand = ray_check, edit = True)

cmds.setToolTo("DraggerContext")

print("Updated")
