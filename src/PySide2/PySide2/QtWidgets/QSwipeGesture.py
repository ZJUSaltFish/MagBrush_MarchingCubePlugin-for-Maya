# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGesture import QGesture

class QSwipeGesture(QGesture):
    """ QSwipeGesture(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def horizontalDirection(self): # real signature unknown; restored from __doc__
        """ horizontalDirection(self) -> PySide2.QtWidgets.QSwipeGesture.SwipeDirection """
        pass

    def setSwipeAngle(self, value): # real signature unknown; restored from __doc__
        """ setSwipeAngle(self, value: float) -> None """
        pass

    def swipeAngle(self): # real signature unknown; restored from __doc__
        """ swipeAngle(self) -> float """
        return 0.0

    def verticalDirection(self): # real signature unknown; restored from __doc__
        """ verticalDirection(self) -> PySide2.QtWidgets.QSwipeGesture.SwipeDirection """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Down = PySide2.QtWidgets.QSwipeGesture.SwipeDirection.Down
    Left = PySide2.QtWidgets.QSwipeGesture.SwipeDirection.Left
    NoDirection = PySide2.QtWidgets.QSwipeGesture.SwipeDirection.NoDirection
    Right = PySide2.QtWidgets.QSwipeGesture.SwipeDirection.Right
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50870380>'
    SwipeDirection = None # (!) real value is "<class 'PySide2.QtWidgets.QSwipeGesture.SwipeDirection'>"
    Up = PySide2.QtWidgets.QSwipeGesture.SwipeDirection.Up


