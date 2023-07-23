# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QCommonStyle import QCommonStyle

class QProxyStyle(QCommonStyle):
    """
    QProxyStyle(self, key: str) -> None
    QProxyStyle(self, style: typing.Optional[PySide2.QtWidgets.QStyle] = None) -> None
    """
    def baseStyle(self): # real signature unknown; restored from __doc__
        """ baseStyle(self) -> PySide2.QtWidgets.QStyle """
        pass

    def drawComplexControl(self, control, option, painter, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawComplexControl(self, control: PySide2.QtWidgets.QStyle.ComplexControl, option: PySide2.QtWidgets.QStyleOptionComplex, painter: PySide2.QtGui.QPainter, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def drawControl(self, element, option, painter, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawControl(self, element: PySide2.QtWidgets.QStyle.ControlElement, option: PySide2.QtWidgets.QStyleOption, painter: PySide2.QtGui.QPainter, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def drawItemPixmap(self, painter, rect, alignment, pixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, alignment: int, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def drawItemText(self, painter, rect, flags, pal, enabled, text, textRole=None): # real signature unknown; restored from __doc__
        """ drawItemText(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, flags: int, pal: PySide2.QtGui.QPalette, enabled: bool, text: str, textRole: PySide2.QtGui.QPalette.ColorRole = PySide2.QtGui.QPalette.ColorRole.NoRole) -> None """
        pass

    def drawPrimitive(self, element, option, painter, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPrimitive(self, element: PySide2.QtWidgets.QStyle.PrimitiveElement, option: PySide2.QtWidgets.QStyleOption, painter: PySide2.QtGui.QPainter, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def generatedIconPixmap(self, iconMode, pixmap, opt): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, iconMode: PySide2.QtGui.QIcon.Mode, pixmap: PySide2.QtGui.QPixmap, opt: PySide2.QtWidgets.QStyleOption) -> PySide2.QtGui.QPixmap """
        pass

    def hitTestComplexControl(self, control, option, pos, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTestComplexControl(self, control: PySide2.QtWidgets.QStyle.ComplexControl, option: PySide2.QtWidgets.QStyleOptionComplex, pos: PySide2.QtCore.QPoint, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtWidgets.QStyle.SubControl """
        pass

    def itemPixmapRect(self, r, flags, pixmap): # real signature unknown; restored from __doc__
        """ itemPixmapRect(self, r: PySide2.QtCore.QRect, flags: int, pixmap: PySide2.QtGui.QPixmap) -> PySide2.QtCore.QRect """
        pass

    def itemTextRect(self, fm, r, flags, enabled, text): # real signature unknown; restored from __doc__
        """ itemTextRect(self, fm: PySide2.QtGui.QFontMetrics, r: PySide2.QtCore.QRect, flags: int, enabled: bool, text: str) -> PySide2.QtCore.QRect """
        pass

    def layoutSpacing(self, control1, control2, orientation, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ layoutSpacing(self, control1: PySide2.QtWidgets.QSizePolicy.ControlType, control2: PySide2.QtWidgets.QSizePolicy.ControlType, orientation: PySide2.QtCore.Qt.Orientation, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> int """
        pass

    def pixelMetric(self, metric, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ pixelMetric(self, metric: PySide2.QtWidgets.QStyle.PixelMetric, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> int """
        pass

    def polish(self, app): # real signature unknown; restored from __doc__
        """
        polish(self, app: PySide2.QtWidgets.QApplication) -> None
        polish(self, pal: PySide2.QtGui.QPalette) -> None
        polish(self, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def setBaseStyle(self, style): # real signature unknown; restored from __doc__
        """ setBaseStyle(self, style: PySide2.QtWidgets.QStyle) -> None """
        pass

    def sizeFromContents(self, type, option, size, widget): # real signature unknown; restored from __doc__
        """ sizeFromContents(self, type: PySide2.QtWidgets.QStyle.ContentsType, option: PySide2.QtWidgets.QStyleOption, size: PySide2.QtCore.QSize, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtCore.QSize """
        pass

    def standardIcon(self, standardIcon, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardIcon(self, standardIcon: PySide2.QtWidgets.QStyle.StandardPixmap, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtGui.QIcon """
        pass

    def standardPalette(self): # real signature unknown; restored from __doc__
        """ standardPalette(self) -> PySide2.QtGui.QPalette """
        pass

    def standardPixmap(self, standardPixmap, opt, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardPixmap(self, standardPixmap: PySide2.QtWidgets.QStyle.StandardPixmap, opt: PySide2.QtWidgets.QStyleOption, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtGui.QPixmap """
        pass

    def styleHint(self, hint, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ styleHint(self, hint: PySide2.QtWidgets.QStyle.StyleHint, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None, returnData: typing.Optional[PySide2.QtWidgets.QStyleHintReturn] = None) -> int """
        pass

    def subControlRect(self, cc, opt, sc, widget): # real signature unknown; restored from __doc__
        """ subControlRect(self, cc: PySide2.QtWidgets.QStyle.ComplexControl, opt: PySide2.QtWidgets.QStyleOptionComplex, sc: PySide2.QtWidgets.QStyle.SubControl, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtCore.QRect """
        pass

    def subElementRect(self, element, option, widget): # real signature unknown; restored from __doc__
        """ subElementRect(self, element: PySide2.QtWidgets.QStyle.SubElement, option: PySide2.QtWidgets.QStyleOption, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtCore.QRect """
        pass

    def unpolish(self, app): # real signature unknown; restored from __doc__
        """
        unpolish(self, app: PySide2.QtWidgets.QApplication) -> None
        unpolish(self, application: PySide2.QtWidgets.QApplication) -> None
        unpolish(self, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, key): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50782C00>'


