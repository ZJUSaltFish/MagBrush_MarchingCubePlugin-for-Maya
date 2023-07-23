# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QStylePainter(__PySide2_QtGui.QPainter):
    """
    QStylePainter(self) -> None
    QStylePainter(self, pd: PySide2.QtGui.QPaintDevice, w: PySide2.QtWidgets.QWidget) -> None
    QStylePainter(self, w: PySide2.QtWidgets.QWidget) -> None
    """
    def begin(self, arg__1): # real signature unknown; restored from __doc__
        """
        begin(self, arg__1: PySide2.QtGui.QPaintDevice) -> bool
        begin(self, pd: PySide2.QtGui.QPaintDevice, w: PySide2.QtWidgets.QWidget) -> bool
        begin(self, w: PySide2.QtWidgets.QWidget) -> bool
        """
        return False

    def drawComplexControl(self, cc, opt): # real signature unknown; restored from __doc__
        """ drawComplexControl(self, cc: PySide2.QtWidgets.QStyle.ComplexControl, opt: PySide2.QtWidgets.QStyleOptionComplex) -> None """
        pass

    def drawControl(self, ce, opt): # real signature unknown; restored from __doc__
        """ drawControl(self, ce: PySide2.QtWidgets.QStyle.ControlElement, opt: PySide2.QtWidgets.QStyleOption) -> None """
        pass

    def drawItemPixmap(self, r, flags, pixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, r: PySide2.QtCore.QRect, flags: int, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def drawItemText(self, r, flags, pal, enabled, text, textRole=None): # real signature unknown; restored from __doc__
        """ drawItemText(self, r: PySide2.QtCore.QRect, flags: int, pal: PySide2.QtGui.QPalette, enabled: bool, text: str, textRole: PySide2.QtGui.QPalette.ColorRole = PySide2.QtGui.QPalette.ColorRole.NoRole) -> None """
        pass

    def drawPrimitive(self, pe, opt): # real signature unknown; restored from __doc__
        """ drawPrimitive(self, pe: PySide2.QtWidgets.QStyle.PrimitiveElement, opt: PySide2.QtWidgets.QStyleOption) -> None """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> PySide2.QtWidgets.QStyle """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


