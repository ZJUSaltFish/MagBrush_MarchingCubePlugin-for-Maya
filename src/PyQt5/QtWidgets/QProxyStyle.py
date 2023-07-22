# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QCommonStyle import QCommonStyle

class QProxyStyle(QCommonStyle):
    """
    QProxyStyle(style: typing.Optional[QStyle] = None)
    QProxyStyle(key: str)
    """
    def baseStyle(self): # real signature unknown; restored from __doc__
        """ baseStyle(self) -> QStyle """
        return QStyle

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawComplexControl(self, control, option, painter, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawComplexControl(self, control: QStyle.ComplexControl, option: QStyleOptionComplex, painter: QPainter, widget: typing.Optional[QWidget] = None) """
        pass

    def drawControl(self, element, option, painter, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawControl(self, element: QStyle.ControlElement, option: QStyleOption, painter: QPainter, widget: typing.Optional[QWidget] = None) """
        pass

    def drawItemPixmap(self, painter, rect, alignment, pixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, painter: QPainter, rect: QRect, alignment: int, pixmap: QPixmap) """
        pass

    def drawItemText(self, painter, rect, flags, pal, enabled, text, textRole=None): # real signature unknown; restored from __doc__
        """ drawItemText(self, painter: QPainter, rect: QRect, flags: int, pal: QPalette, enabled: bool, text: str, textRole: QPalette.ColorRole = QPalette.NoRole) """
        pass

    def drawPrimitive(self, element, option, painter, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPrimitive(self, element: QStyle.PrimitiveElement, option: QStyleOption, painter: QPainter, widget: typing.Optional[QWidget] = None) """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: QEvent) -> bool """
        return False

    def generatedIconPixmap(self, iconMode, pixmap, opt): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, iconMode: QIcon.Mode, pixmap: QPixmap, opt: QStyleOption) -> QPixmap """
        pass

    def hitTestComplexControl(self, control, option, pos, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTestComplexControl(self, control: QStyle.ComplexControl, option: QStyleOptionComplex, pos: QPoint, widget: typing.Optional[QWidget] = None) -> QStyle.SubControl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemPixmapRect(self, r, flags, pixmap): # real signature unknown; restored from __doc__
        """ itemPixmapRect(self, r: QRect, flags: int, pixmap: QPixmap) -> QRect """
        pass

    def itemTextRect(self, fm, r, flags, enabled, text): # real signature unknown; restored from __doc__
        """ itemTextRect(self, fm: QFontMetrics, r: QRect, flags: int, enabled: bool, text: str) -> QRect """
        pass

    def layoutSpacing(self, control1, control2, orientation, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ layoutSpacing(self, control1: QSizePolicy.ControlType, control2: QSizePolicy.ControlType, orientation: Qt.Orientation, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None) -> int """
        pass

    def pixelMetric(self, metric, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ pixelMetric(self, metric: QStyle.PixelMetric, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None) -> int """
        pass

    def polish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        polish(self, widget: QWidget)
        polish(self, pal: QPalette) -> QPalette
        polish(self, app: QApplication)
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseStyle(self, style): # real signature unknown; restored from __doc__
        """ setBaseStyle(self, style: QStyle) """
        pass

    def sizeFromContents(self, type, option, size, widget): # real signature unknown; restored from __doc__
        """ sizeFromContents(self, type: QStyle.ContentsType, option: QStyleOption, size: QSize, widget: QWidget) -> QSize """
        pass

    def standardIcon(self, standardIcon, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardIcon(self, standardIcon: QStyle.StandardPixmap, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None) -> QIcon """
        pass

    def standardPalette(self): # real signature unknown; restored from __doc__
        """ standardPalette(self) -> QPalette """
        pass

    def standardPixmap(self, standardPixmap, opt, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardPixmap(self, standardPixmap: QStyle.StandardPixmap, opt: QStyleOption, widget: typing.Optional[QWidget] = None) -> QPixmap """
        pass

    def styleHint(self, hint, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ styleHint(self, hint: QStyle.StyleHint, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None, returnData: typing.Optional[QStyleHintReturn] = None) -> int """
        pass

    def subControlRect(self, cc, opt, sc, widget): # real signature unknown; restored from __doc__
        """ subControlRect(self, cc: QStyle.ComplexControl, opt: QStyleOptionComplex, sc: QStyle.SubControl, widget: QWidget) -> QRect """
        pass

    def subElementRect(self, element, option, widget): # real signature unknown; restored from __doc__
        """ subElementRect(self, element: QStyle.SubElement, option: QStyleOption, widget: QWidget) -> QRect """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unpolish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        unpolish(self, widget: QWidget)
        unpolish(self, app: QApplication)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


