# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QStylePainter(__PyQt5_QtGui.QPainter):
    """
    QStylePainter()
    QStylePainter(w: QWidget)
    QStylePainter(pd: QPaintDevice, w: QWidget)
    """
    def begin(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        begin(self, w: QWidget) -> bool
        begin(self, pd: QPaintDevice, w: QWidget) -> bool
        """
        return False

    def drawComplexControl(self, cc, opt): # real signature unknown; restored from __doc__
        """ drawComplexControl(self, cc: QStyle.ComplexControl, opt: QStyleOptionComplex) """
        pass

    def drawControl(self, ce, opt): # real signature unknown; restored from __doc__
        """ drawControl(self, ce: QStyle.ControlElement, opt: QStyleOption) """
        pass

    def drawItemPixmap(self, r, flags, pixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, r: QRect, flags: int, pixmap: QPixmap) """
        pass

    def drawItemText(self, rect, flags, pal, enabled, text, textRole=None): # real signature unknown; restored from __doc__
        """ drawItemText(self, rect: QRect, flags: int, pal: QPalette, enabled: bool, text: str, textRole: QPalette.ColorRole = QPalette.NoRole) """
        pass

    def drawPrimitive(self, pe, opt): # real signature unknown; restored from __doc__
        """ drawPrimitive(self, pe: QStyle.PrimitiveElement, opt: QStyleOption) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QStyle """
        return QStyle

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


