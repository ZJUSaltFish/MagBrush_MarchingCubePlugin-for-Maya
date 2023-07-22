# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QStyleOption import QStyleOption

class QStyleOptionGraphicsItem(QStyleOption):
    """
    QStyleOptionGraphicsItem(self) -> None
    QStyleOptionGraphicsItem(self, other: PySide2.QtWidgets.QStyleOptionGraphicsItem) -> None
    QStyleOptionGraphicsItem(self, version: int) -> None
    """
    def levelOfDetailFromTransform(self, worldTransform): # real signature unknown; restored from __doc__
        """ levelOfDetailFromTransform(worldTransform: PySide2.QtGui.QTransform) -> float """
        return 0.0

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    exposedRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    levelOfDetail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    StyleOptionType = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionGraphicsItem.StyleOptionType'>"
    StyleOptionVersion = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionGraphicsItem.StyleOptionVersion'>"
    Type = PySide2.QtWidgets.QStyleOptionGraphicsItem.StyleOptionType.Type
    Version = PySide2.QtWidgets.QStyleOptionGraphicsItem.StyleOptionVersion.Version


