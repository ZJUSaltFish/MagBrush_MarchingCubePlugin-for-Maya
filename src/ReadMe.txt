File Structure:
src: root folder, can be an arbitrary name.(English only)
|- mcl_plugin: all the utilities of mcl plugin
|- numpy: site-package numpy
|   |- pic: some pictures
|   |- __init__: empty but needed
|   |- manager: central control
|   |- marching_cube_np: marching_cube implementation using numpy
|   |- picture: script to load pictures for UI
|   |- picture.qrc: support file
|   |- tool_context: script to control maya draggerContext as a tool
|   |- UITest1.ui: ui design based on PyQt
|
|- PyQt5: site-package PyQt5
|- Pyside2: site-package Pyside2
|- MarchingCubeLandscape: Entry of mcl plugin. To load mcl, use maya plugin manager to load this file.
|- ReadMe: This file