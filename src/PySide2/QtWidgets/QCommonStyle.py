# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QStyle import QStyle

class QCommonStyle(QStyle):
    """ QCommonStyle(self) -> None """
    def drawComplexControl(self, cc, opt, p, w, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawComplexControl(self, cc: PySide2.QtWidgets.QStyle.ComplexControl, opt: PySide2.QtWidgets.QStyleOptionComplex, p: PySide2.QtGui.QPainter, w: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def drawControl(self, element, opt, p, w, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawControl(self, element: PySide2.QtWidgets.QStyle.ControlElement, opt: PySide2.QtWidgets.QStyleOption, p: PySide2.QtGui.QPainter, w: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def drawPrimitive(self, pe, opt, p, w, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPrimitive(self, pe: PySide2.QtWidgets.QStyle.PrimitiveElement, opt: PySide2.QtWidgets.QStyleOption, p: PySide2.QtGui.QPainter, w: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def generatedIconPixmap(self, iconMode, pixmap, opt): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, iconMode: PySide2.QtGui.QIcon.Mode, pixmap: PySide2.QtGui.QPixmap, opt: PySide2.QtWidgets.QStyleOption) -> PySide2.QtGui.QPixmap """
        pass

    def hitTestComplexControl(self, cc, opt, pt, w, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTestComplexControl(self, cc: PySide2.QtWidgets.QStyle.ComplexControl, opt: PySide2.QtWidgets.QStyleOptionComplex, pt: PySide2.QtCore.QPoint, w: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtWidgets.QStyle.SubControl """
        pass

    def layoutSpacing(self, control1, control2, orientation, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ layoutSpacing(self, control1: PySide2.QtWidgets.QSizePolicy.ControlType, control2: PySide2.QtWidgets.QSizePolicy.ControlType, orientation: PySide2.QtCore.Qt.Orientation, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> int """
        pass

    def pixelMetric(self, m, opt, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ pixelMetric(self, m: PySide2.QtWidgets.QStyle.PixelMetric, opt: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> int """
        pass

    def polish(self, app): # real signature unknown; restored from __doc__
        """
        polish(self, app: PySide2.QtWidgets.QApplication) -> None
        polish(self, application: PySide2.QtWidgets.QApplication) -> None
        polish(self, arg__1: PySide2.QtGui.QPalette) -> None
        polish(self, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def sizeFromContents(self, ct, opt, contentsSize, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeFromContents(self, ct: PySide2.QtWidgets.QStyle.ContentsType, opt: PySide2.QtWidgets.QStyleOption, contentsSize: PySide2.QtCore.QSize, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtCore.QSize """
        pass

    def standardIcon(self, standardIcon, opt, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardIcon(self, standardIcon: PySide2.QtWidgets.QStyle.StandardPixmap, opt: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtGui.QIcon """
        pass

    def standardPixmap(self, sp, opt, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardPixmap(self, sp: PySide2.QtWidgets.QStyle.StandardPixmap, opt: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtGui.QPixmap """
        pass

    def styleHint(self, sh, opt, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ styleHint(self, sh: PySide2.QtWidgets.QStyle.StyleHint, opt: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, w: typing.Optional[PySide2.QtWidgets.QWidget] = None, shret: typing.Optional[PySide2.QtWidgets.QStyleHintReturn] = None) -> int """
        pass

    def subControlRect(self, cc, opt, sc, w, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ subControlRect(self, cc: PySide2.QtWidgets.QStyle.ComplexControl, opt: PySide2.QtWidgets.QStyleOptionComplex, sc: PySide2.QtWidgets.QStyle.SubControl, w: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtCore.QRect """
        pass

    def subElementRect(self, r, opt, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ subElementRect(self, r: PySide2.QtWidgets.QStyle.SubElement, opt: PySide2.QtWidgets.QStyleOption, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtCore.QRect """
        pass

    def unpolish(self, application): # real signature unknown; restored from __doc__
        """
        unpolish(self, application: PySide2.QtWidgets.QApplication) -> None
        unpolish(self, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507829C0>'


