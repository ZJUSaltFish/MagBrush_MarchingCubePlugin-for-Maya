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

class QSlider(QAbstractSlider):
    """
    QSlider(self, orientation: PySide2.QtCore.Qt.Orientation, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QSlider(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionSlider) -> None """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def mouseMoveEvent(self, ev): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, ev: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, ev): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, ev: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, ev): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, ev: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def paintEvent(self, ev): # real signature unknown; restored from __doc__
        """ paintEvent(self, ev: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def setTickInterval(self, ti): # real signature unknown; restored from __doc__
        """ setTickInterval(self, ti: int) -> None """
        pass

    def setTickPosition(self, position): # real signature unknown; restored from __doc__
        """ setTickPosition(self, position: PySide2.QtWidgets.QSlider.TickPosition) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def tickInterval(self): # real signature unknown; restored from __doc__
        """ tickInterval(self) -> int """
        return 0

    def tickPosition(self): # real signature unknown; restored from __doc__
        """ tickPosition(self) -> PySide2.QtWidgets.QSlider.TickPosition """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, orientation, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    NoTicks = PySide2.QtWidgets.QSlider.TickPosition.NoTicks
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507D7480>'
    TickPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QSlider.TickPosition'>"
    TicksAbove = PySide2.QtWidgets.QSlider.TickPosition.TicksAbove
    TicksBelow = PySide2.QtWidgets.QSlider.TickPosition.TicksBelow
    TicksBothSides = PySide2.QtWidgets.QSlider.TickPosition.TicksBothSides
    TicksLeft = PySide2.QtWidgets.QSlider.TickPosition.TicksLeft
    TicksRight = PySide2.QtWidgets.QSlider.TickPosition.TicksRight


