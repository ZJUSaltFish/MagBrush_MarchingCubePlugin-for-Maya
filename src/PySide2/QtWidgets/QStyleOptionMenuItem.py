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

class QStyleOptionMenuItem(QStyleOption):
    """
    QStyleOptionMenuItem(self) -> None
    QStyleOptionMenuItem(self, other: PySide2.QtWidgets.QStyleOptionMenuItem) -> None
    QStyleOptionMenuItem(self, version: int) -> None
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    checked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    checkType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxIconWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    menuHasCheckableItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    menuItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    menuRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tabWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CheckType = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionMenuItem.CheckType'>"
    DefaultItem = PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType.DefaultItem
    EmptyArea = PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType.EmptyArea
    Exclusive = PySide2.QtWidgets.QStyleOptionMenuItem.CheckType.Exclusive
    Margin = PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType.Margin
    MenuItemType = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType'>"
    NonExclusive = PySide2.QtWidgets.QStyleOptionMenuItem.CheckType.NonExclusive
    Normal = PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType.Normal
    NotCheckable = PySide2.QtWidgets.QStyleOptionMenuItem.CheckType.NotCheckable
    Scroller = PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType.Scroller
    Separator = PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType.Separator
    StyleOptionType = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionMenuItem.StyleOptionType'>"
    StyleOptionVersion = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionMenuItem.StyleOptionVersion'>"
    SubMenu = PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType.SubMenu
    TearOff = PySide2.QtWidgets.QStyleOptionMenuItem.MenuItemType.TearOff
    Type = PySide2.QtWidgets.QStyleOptionMenuItem.StyleOptionType.Type
    Version = PySide2.QtWidgets.QStyleOptionMenuItem.StyleOptionVersion.Version


