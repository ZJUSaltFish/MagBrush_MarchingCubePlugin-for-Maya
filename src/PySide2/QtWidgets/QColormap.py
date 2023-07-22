# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QColormap(__Shiboken.Object):
    """ QColormap(self, colormap: PySide2.QtWidgets.QColormap) -> None """
    def cleanup(self): # real signature unknown; restored from __doc__
        """ cleanup() -> None """
        pass

    def colorAt(self, pixel): # real signature unknown; restored from __doc__
        """ colorAt(self, pixel: int) -> PySide2.QtGui.QColor """
        pass

    def colormap(self): # real signature unknown; restored from __doc__
        """ colormap(self) -> typing.List[PySide2.QtGui.QColor] """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize() -> None """
        pass

    def instance(self, screen=-1): # real signature unknown; restored from __doc__
        """ instance(screen: int = -1) -> PySide2.QtWidgets.QColormap """
        pass

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> PySide2.QtWidgets.QColormap.Mode """
        pass

    def pixel(self, color): # real signature unknown; restored from __doc__
        """ pixel(self, color: PySide2.QtGui.QColor) -> int """
        return 0

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self, colormap): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Direct = PySide2.QtWidgets.QColormap.Mode.Direct
    Gray = PySide2.QtWidgets.QColormap.Mode.Gray
    Indexed = PySide2.QtWidgets.QColormap.Mode.Indexed
    Mode = None # (!) real value is "<class 'PySide2.QtWidgets.QColormap.Mode'>"


