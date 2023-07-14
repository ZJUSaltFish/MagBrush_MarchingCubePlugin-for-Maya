''''
https://zhuanlan.zhihu.com/p/82989116
目前要添加到maya的工具架中,需要手动操作.工具架-工具架编辑器-工具架内容,点击添加按钮添加自定义脚本-命令,选择python,内容改成exec(open("F:/WordasPic/Mayapy_FinalProject/main.py",encoding='utf-8').read())
注意!!要把路径改成自己的main.py所存放的路径
正在尝试怎么自动化这个步骤
'''
#/usr/bin/env python
# -*- coding: UTF-8 -*-
import maya.cmds as cmd
# from importlib import reload
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
# #解决中文问题
# def utf_8String(StringT):
#   utf_8String = StringT
#   #utf_8String.encode('utf-8')
#   utf_8String = str(utf_8String, "utf-8")
#   return utf_8String

def checkSelect():
  list_select = []
  if cmd.ls(sl = True) != []:
    list_select = cmd.ls(sl=True)
    return list_select
  else:
    return []

def centerPivot():
  for i in checkSelect():
    cmd.xform(i, centerPivots=True)

def pivotMoveToWorldPositon000():
  for i in checkSelect():
    Name = i
    cmd.move(0, 0, 0, Name+'.rotatePivot', Name+'.scalePivot', rpr=True)
    cmd.makeIdentity(Name, a=True)

def meshMoveToWorldPosition000AndClean():
  centerPivot()
  for i in checkSelect():
    cmd.move(0, 0, 0, i, rpr=True)
    cmd.makeIdentity(i, a=True)

def mainGui():
  windowName = 'CC_Tool'
  windowTitle = 'CC_Tool1.0'

  try:
    cmd.deleteUI(windowName)
  except:
    pass
  cmd.window(windowName,title = windowTitle)
  cmd.columnLayout(adj = True)

  explain_ZeroPivot = '坐标移动至原点'
  explain_Clean = '物体和坐标移动到原点'

  cmd.button(l='ZeroPivot', ann=explain_ZeroPivot, h=60, w=20, c='pivotMoveToWorldPositon000()')
  cmd.button(l='ZeroMeshClean', ann=explain_Clean, h=60, w=20, c='meshMoveToWorldPosition000AndClean()')

  cmd.showWindow(windowName)

mainGui()