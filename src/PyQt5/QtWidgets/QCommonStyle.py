# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QStyle import QStyle

class QCommonStyle(QStyle):
    """ QCommonStyle() """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawComplexControl(self, cc, opt, p, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawComplexControl(self, cc: QStyle.ComplexControl, opt: QStyleOptionComplex, p: QPainter, widget: typing.Optional[QWidget] = None) """
        pass

    def drawControl(self, element, opt, p, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawControl(self, element: QStyle.ControlElement, opt: QStyleOption, p: QPainter, widget: typing.Optional[QWidget] = None) """
        pass

    def drawPrimitive(self, pe, opt, p, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPrimitive(self, pe: QStyle.PrimitiveElement, opt: QStyleOption, p: QPainter, widget: typing.Optional[QWidget] = None) """
        pass

    def generatedIconPixmap(self, iconMode, pixmap, opt): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, iconMode: QIcon.Mode, pixmap: QPixmap, opt: QStyleOption) -> QPixmap """
        pass

    def hitTestComplexControl(self, cc, opt, pt, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTestComplexControl(self, cc: QStyle.ComplexControl, opt: QStyleOptionComplex, pt: QPoint, widget: typing.Optional[QWidget] = None) -> QStyle.SubControl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def layoutSpacing(self, control1, control2, orientation, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ layoutSpacing(self, control1: QSizePolicy.ControlType, control2: QSizePolicy.ControlType, orientation: Qt.Orientation, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None) -> int """
        pass

    def pixelMetric(self, m, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ pixelMetric(self, m: QStyle.PixelMetric, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None) -> int """
        pass

    def polish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        polish(self, widget: QWidget)
        polish(self, app: QApplication)
        polish(self, a0: QPalette) -> QPalette
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sizeFromContents(self, ct, opt, contentsSize, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeFromContents(self, ct: QStyle.ContentsType, opt: QStyleOption, contentsSize: QSize, widget: typing.Optional[QWidget] = None) -> QSize """
        pass

    def standardIcon(self, standardIcon, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardIcon(self, standardIcon: QStyle.StandardPixmap, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None) -> QIcon """
        pass

    def standardPixmap(self, sp, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardPixmap(self, sp: QStyle.StandardPixmap, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None) -> QPixmap """
        pass

    def styleHint(self, sh, option, QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ styleHint(self, sh: QStyle.StyleHint, option: typing.Optional[QStyleOption] = None, widget: typing.Optional[QWidget] = None, returnData: typing.Optional[QStyleHintReturn] = None) -> int """
        pass

    def subControlRect(self, cc, opt, sc, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ subControlRect(self, cc: QStyle.ComplexControl, opt: QStyleOptionComplex, sc: QStyle.SubControl, widget: typing.Optional[QWidget] = None) -> QRect """
        pass

    def subElementRect(self, r, opt, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ subElementRect(self, r: QStyle.SubElement, opt: QStyleOption, widget: typing.Optional[QWidget] = None) -> QRect """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unpolish(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        unpolish(self, widget: QWidget)
        unpolish(self, application: QApplication)
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


