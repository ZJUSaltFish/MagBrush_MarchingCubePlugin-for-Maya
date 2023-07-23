# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QGestureEvent(__PySide2_QtCore.QEvent):
    """ QGestureEvent(self, gestures: typing.Sequence[PySide2.QtWidgets.QGesture]) -> None """
    def accept(self): # real signature unknown; restored from __doc__
        """
        accept(self) -> None
        accept(self, arg__1: PySide2.QtCore.Qt.GestureType) -> None
        accept(self, arg__1: PySide2.QtWidgets.QGesture) -> None
        """
        pass

    def activeGestures(self): # real signature unknown; restored from __doc__
        """ activeGestures(self) -> typing.List[PySide2.QtWidgets.QGesture] """
        pass

    def canceledGestures(self): # real signature unknown; restored from __doc__
        """ canceledGestures(self) -> typing.List[PySide2.QtWidgets.QGesture] """
        pass

    def gesture(self, type): # real signature unknown; restored from __doc__
        """ gesture(self, type: PySide2.QtCore.Qt.GestureType) -> PySide2.QtWidgets.QGesture """
        pass

    def gestures(self): # real signature unknown; restored from __doc__
        """ gestures(self) -> typing.List[PySide2.QtWidgets.QGesture] """
        pass

    def ignore(self): # real signature unknown; restored from __doc__
        """
        ignore(self) -> None
        ignore(self, arg__1: PySide2.QtCore.Qt.GestureType) -> None
        ignore(self, arg__1: PySide2.QtWidgets.QGesture) -> None
        """
        pass

    def isAccepted(self): # real signature unknown; restored from __doc__
        """
        isAccepted(self) -> bool
        isAccepted(self, arg__1: PySide2.QtCore.Qt.GestureType) -> bool
        isAccepted(self, arg__1: PySide2.QtWidgets.QGesture) -> bool
        """
        return False

    def mapToGraphicsScene(self, gesturePoint): # real signature unknown; restored from __doc__
        """ mapToGraphicsScene(self, gesturePoint: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF """
        pass

    def setAccepted(self, accepted): # real signature unknown; restored from __doc__
        """
        setAccepted(self, accepted: bool) -> None
        setAccepted(self, arg__1: PySide2.QtCore.Qt.GestureType, arg__2: bool) -> None
        setAccepted(self, arg__1: PySide2.QtWidgets.QGesture, arg__2: bool) -> None
        """
        pass

    def setWidget(self, widget): # real signature unknown; restored from __doc__
        """ setWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, gestures, PySide2_QtWidgets_QGesture=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


