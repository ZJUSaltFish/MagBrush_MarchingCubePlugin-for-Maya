# MagBrush - MarchingCube Plugin for Maya

A simple plugin for maya2023, enables creating landscape with marching-cube method.
<img width="800" alt="image" src="https://github.com/ZJUSaltFish/MagBrush_MarchingCubePlugin-for-Maya/assets/114348635/34c2c9d9-02fd-4826-861b-c51fd89a52d6">


## Usage

Maya - windows - plugin manager - explore - load MarchingCubeLandscape.py

Then you will find a mcl(marching cube landscape) button in shelf/Custom

This plugin can be load from any direction in computer. But you'd best place them in maya's default plugin folder, for auto loading

It works in win11. We don't know whether it work in MAC / Linux or not



**GUI:**

<img width="295" alt="image" src="https://github.com/ZJUSaltFish/MagBrush_MarchingCubePlugin-for-Maya/assets/114348635/c0b21e2c-5bad-4394-81a9-6918772906b7">


**Terrain Creating:** 

Block Size: Num of cubes in a block

Length / Width / Height: Num of block in x / z / y direction

Plane / Sphere: Create a basic terrain with plane/sphere shape

**Brush Parameters:**

Size: Radius of sphere brush

Hardness: Speed of strength attenuation

Intensity: Strength of brush

Generating: Enable brush

Clear All: delete current terrain



**Hotkey:**

Up to now, only one hotkey: SHIFT hold - switch brush to subtract mode



## File Structure:

**src:** root folder, can be an arbitrary name.(English only)
|- **mcl_plugin:** all the utilities of mcl plugin
|   |- **pic:** some pictures
|   |- **init:** empty but needed
|   |- **manager:** central control
|   |- **marching_cube_np:** marching_cube implementation using numpy
|   |- **picture:** script to load pictures for UI
|   |- **picture.qrc:** support file
|   |- **tool_context:** script to control maya draggerContext as a tool
|   |- **UITest1.ui:** ui design based on PyQt
|- **numpy:** site-package numpy
|- **PyQt5:** site-package PyQt5
|- **Pyside2:** site-package Pyside2
|- **MarchingCubeLandscape:** Entry of mcl plugin. To load mcl, use maya plugin manager to load this file.

**sample scene:**  .mb files as example

**ReadMe:** This file



## Unfinished

Maybe you will find some interfaces or functions in script but not available on GUI. Because this is not finished yet.
Currently Missing: save/load; undo/redo; more brush modes, e.g. smoothing; more brush shapes, e.g. box, masked...; terrain transfrom; etc.



## WARN

- Marching cube is an inefficient algorithm. Maya is also inefficient, and single-thread in kernel.

​		So this plugin is of very low running speed. **Don't create a large terrain** if your cpu is not good enough.

- **BUG Known**: Don't use ctrl z for undo. Currently undo is NOT SUPPORT

(We don't know how to optimize creating and rendering meshes in maya)
