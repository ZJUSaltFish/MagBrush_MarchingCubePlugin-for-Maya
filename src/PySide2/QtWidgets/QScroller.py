# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QScroller(__PySide2_QtCore.QObject):
    # no doc
    def activeScrollers(self): # real signature unknown; restored from __doc__
        """ activeScrollers() -> typing.List[PySide2.QtWidgets.QScroller] """
        pass

    def ensureVisible(self, rect, xmargin, ymargin): # real signature unknown; restored from __doc__
        """
        ensureVisible(self, rect: PySide2.QtCore.QRectF, xmargin: float, ymargin: float) -> None
        ensureVisible(self, rect: PySide2.QtCore.QRectF, xmargin: float, ymargin: float, scrollTime: int) -> None
        """
        pass

    def finalPosition(self): # real signature unknown; restored from __doc__
        """ finalPosition(self) -> PySide2.QtCore.QPointF """
        pass

    def grabbedGesture(self, target): # real signature unknown; restored from __doc__
        """ grabbedGesture(target: PySide2.QtCore.QObject) -> PySide2.QtCore.Qt.GestureType """
        pass

    def grabGesture(self, target, gestureType=None): # real signature unknown; restored from __doc__
        """ grabGesture(target: PySide2.QtCore.QObject, gestureType: PySide2.QtWidgets.QScroller.ScrollerGestureType = PySide2.QtWidgets.QScroller.ScrollerGestureType.TouchGesture) -> PySide2.QtCore.Qt.GestureType """
        pass

    def handleInput(self, input, position, timestamp=0): # real signature unknown; restored from __doc__
        """ handleInput(self, input: PySide2.QtWidgets.QScroller.Input, position: PySide2.QtCore.QPointF, timestamp: int = 0) -> bool """
        return False

    def hasScroller(self, target): # real signature unknown; restored from __doc__
        """ hasScroller(target: PySide2.QtCore.QObject) -> bool """
        return False

    def pixelPerMeter(self): # real signature unknown; restored from __doc__
        """ pixelPerMeter(self) -> PySide2.QtCore.QPointF """
        pass

    def resendPrepareEvent(self): # real signature unknown; restored from __doc__
        """ resendPrepareEvent(self) -> None """
        pass

    def scroller(self, target): # real signature unknown; restored from __doc__
        """ scroller(target: PySide2.QtCore.QObject) -> PySide2.QtWidgets.QScroller """
        pass

    def scrollerProperties(self): # real signature unknown; restored from __doc__
        """ scrollerProperties(self) -> PySide2.QtWidgets.QScrollerProperties """
        pass

    def scrollerPropertiesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def scrollTo(self, pos): # real signature unknown; restored from __doc__
        """
        scrollTo(self, pos: PySide2.QtCore.QPointF) -> None
        scrollTo(self, pos: PySide2.QtCore.QPointF, scrollTime: int) -> None
        """
        pass

    def setScrollerProperties(self, prop): # real signature unknown; restored from __doc__
        """ setScrollerProperties(self, prop: PySide2.QtWidgets.QScrollerProperties) -> None """
        pass

    def setSnapPositionsX(self, first, interval): # real signature unknown; restored from __doc__
        """
        setSnapPositionsX(self, first: float, interval: float) -> None
        setSnapPositionsX(self, positions: typing.Sequence[float]) -> None
        """
        pass

    def setSnapPositionsY(self, first, interval): # real signature unknown; restored from __doc__
        """
        setSnapPositionsY(self, first: float, interval: float) -> None
        setSnapPositionsY(self, positions: typing.Sequence[float]) -> None
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtWidgets.QScroller.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> PySide2.QtCore.QObject """
        pass

    def ungrabGesture(self, target): # real signature unknown; restored from __doc__
        """ ungrabGesture(target: PySide2.QtCore.QObject) -> None """
        pass

    def velocity(self): # real signature unknown; restored from __doc__
        """ velocity(self) -> PySide2.QtCore.QPointF """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Dragging = PySide2.QtWidgets.QScroller.State.Dragging
    Inactive = PySide2.QtWidgets.QScroller.State.Inactive
    Input = None # (!) real value is "<class 'PySide2.QtWidgets.QScroller.Input'>"
    InputMove = PySide2.QtWidgets.QScroller.Input.InputMove
    InputPress = PySide2.QtWidgets.QScroller.Input.InputPress
    InputRelease = PySide2.QtWidgets.QScroller.Input.InputRelease
    LeftMouseButtonGesture = PySide2.QtWidgets.QScroller.ScrollerGestureType.LeftMouseButtonGesture
    MiddleMouseButtonGesture = PySide2.QtWidgets.QScroller.ScrollerGestureType.MiddleMouseButtonGesture
    Pressed = PySide2.QtWidgets.QScroller.State.Pressed
    RightMouseButtonGesture = PySide2.QtWidgets.QScroller.ScrollerGestureType.RightMouseButtonGesture
    ScrollerGestureType = None # (!) real value is "<class 'PySide2.QtWidgets.QScroller.ScrollerGestureType'>"
    Scrolling = PySide2.QtWidgets.QScroller.State.Scrolling
    State = None # (!) real value is "<class 'PySide2.QtWidgets.QScroller.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50794400>'
    TouchGesture = PySide2.QtWidgets.QScroller.ScrollerGestureType.TouchGesture


