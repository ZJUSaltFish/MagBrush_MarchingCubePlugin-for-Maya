# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractSlider import QAbstractSlider

class QDial(QAbstractSlider):
    """ QDial(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionSlider) -> None """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def mouseMoveEvent(self, me): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, me: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, me): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, me: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, me): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, me: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def notchesVisible(self): # real signature unknown; restored from __doc__
        """ notchesVisible(self) -> bool """
        return False

    def notchSize(self): # real signature unknown; restored from __doc__
        """ notchSize(self) -> int """
        return 0

    def notchTarget(self): # real signature unknown; restored from __doc__
        """ notchTarget(self) -> float """
        return 0.0

    def paintEvent(self, pe): # real signature unknown; restored from __doc__
        """ paintEvent(self, pe: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def resizeEvent(self, re): # real signature unknown; restored from __doc__
        """ resizeEvent(self, re: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def setNotchesVisible(self, visible): # real signature unknown; restored from __doc__
        """ setNotchesVisible(self, visible: bool) -> None """
        pass

    def setNotchTarget(self, target): # real signature unknown; restored from __doc__
        """ setNotchTarget(self, target: float) -> None """
        pass

    def setWrapping(self, on): # real signature unknown; restored from __doc__
        """ setWrapping(self, on: bool) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def sliderChange(self, change): # real signature unknown; restored from __doc__
        """ sliderChange(self, change: PySide2.QtWidgets.QAbstractSlider.SliderChange) -> None """
        pass

    def wrapping(self): # real signature unknown; restored from __doc__
        """ wrapping(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507D7840>'


