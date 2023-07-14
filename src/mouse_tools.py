import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omUI
import maya.cmds
class BrushContext(omUI.MPxContext):

    def __init__(self):
        super(BrushContext, self).__init__()

    def toolOnSetup(self, event):
        # Method to execute when start
        print("Tool On")

    def doPress(self, event):
        # Method to execute when mouse press
        print("Mouse Press")

    def doRelease(self, event):
        # Method to execute when mouse release
        print("Mouse Release")

    def doDrag(self, event):
        # Method to execute when mouse drag

        x, y = event.position.x, event.position.y
        print("Mouse Drag at Port Coordinate:", x, y)