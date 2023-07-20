import maya.cmds as cmds

cmds.polyCreateFacet(p=[(-20,0,-20),(-20,0,20),(20,0,20),(20,0,-20)])

cmds.ls(type='mesh')
cmds.rename(cmds.ls(type='mesh'),"genshin")

cmds.delete(cmds.ls('genshin'))