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

class QStyleOptionToolBox(QStyleOption):
    """
    QStyleOptionToolBox(self) -> None
    QStyleOptionToolBox(self, other: PySide2.QtWidgets.QStyleOptionToolBox) -> None
    QStyleOptionToolBox(self, version: int) -> None
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selectedPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Beginning = PySide2.QtWidgets.QStyleOptionToolBox.TabPosition.Beginning
    End = PySide2.QtWidgets.QStyleOptionToolBox.TabPosition.End
    Middle = PySide2.QtWidgets.QStyleOptionToolBox.TabPosition.Middle
    NextIsSelected = PySide2.QtWidgets.QStyleOptionToolBox.SelectedPosition.NextIsSelected
    NotAdjacent = PySide2.QtWidgets.QStyleOptionToolBox.SelectedPosition.NotAdjacent
    OnlyOneTab = PySide2.QtWidgets.QStyleOptionToolBox.TabPosition.OnlyOneTab
    PreviousIsSelected = PySide2.QtWidgets.QStyleOptionToolBox.SelectedPosition.PreviousIsSelected
    SelectedPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionToolBox.SelectedPosition'>"
    StyleOptionType = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionToolBox.StyleOptionType'>"
    StyleOptionVersion = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionToolBox.StyleOptionVersion'>"
    TabPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionToolBox.TabPosition'>"
    Type = PySide2.QtWidgets.QStyleOptionToolBox.StyleOptionType.Type
    Version = PySide2.QtWidgets.QStyleOptionToolBox.StyleOptionVersion.Version


