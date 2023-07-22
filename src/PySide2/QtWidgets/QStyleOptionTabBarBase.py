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

class QStyleOptionTabBarBase(QStyleOption):
    """
    QStyleOptionTabBarBase(self) -> None
    QStyleOptionTabBarBase(self, other: PySide2.QtWidgets.QStyleOptionTabBarBase) -> None
    QStyleOptionTabBarBase(self, version: int) -> None
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    documentMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selectedTabRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tabBarRect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    StyleOptionType = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionTabBarBase.StyleOptionType'>"
    StyleOptionVersion = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionTabBarBase.StyleOptionVersion'>"
    Type = PySide2.QtWidgets.QStyleOptionTabBarBase.StyleOptionType.Type
    Version = PySide2.QtWidgets.QStyleOptionTabBarBase.StyleOptionVersion.Version


