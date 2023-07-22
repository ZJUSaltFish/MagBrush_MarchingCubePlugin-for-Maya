# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QTimeLine(QObject):
    """ QTimeLine(self, duration: int = 1000, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> int """
        return 0

    def currentTime(self): # real signature unknown; restored from __doc__
        """ currentTime(self) -> int """
        return 0

    def currentValue(self): # real signature unknown; restored from __doc__
        """ currentValue(self) -> float """
        return 0.0

    def curveShape(self): # real signature unknown; restored from __doc__
        """ curveShape(self) -> PySide2.QtCore.QTimeLine.CurveShape """
        pass

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> PySide2.QtCore.QTimeLine.Direction """
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ easingCurve(self) -> PySide2.QtCore.QEasingCurve """
        pass

    def endFrame(self): # real signature unknown; restored from __doc__
        """ endFrame(self) -> int """
        return 0

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def frameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def frameForTime(self, msec): # real signature unknown; restored from __doc__
        """ frameForTime(self, msec: int) -> int """
        return 0

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def setCurrentTime(self, msec): # real signature unknown; restored from __doc__
        """ setCurrentTime(self, msec: int) -> None """
        pass

    def setCurveShape(self, shape): # real signature unknown; restored from __doc__
        """ setCurveShape(self, shape: PySide2.QtCore.QTimeLine.CurveShape) -> None """
        pass

    def setDirection(self, direction): # real signature unknown; restored from __doc__
        """ setDirection(self, direction: PySide2.QtCore.QTimeLine.Direction) -> None """
        pass

    def setDuration(self, duration): # real signature unknown; restored from __doc__
        """ setDuration(self, duration: int) -> None """
        pass

    def setEasingCurve(self, curve): # real signature unknown; restored from __doc__
        """ setEasingCurve(self, curve: PySide2.QtCore.QEasingCurve) -> None """
        pass

    def setEndFrame(self, frame): # real signature unknown; restored from __doc__
        """ setEndFrame(self, frame: int) -> None """
        pass

    def setFrameRange(self, startFrame, endFrame): # real signature unknown; restored from __doc__
        """ setFrameRange(self, startFrame: int, endFrame: int) -> None """
        pass

    def setLoopCount(self, count): # real signature unknown; restored from __doc__
        """ setLoopCount(self, count: int) -> None """
        pass

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) -> None """
        pass

    def setStartFrame(self, frame): # real signature unknown; restored from __doc__
        """ setStartFrame(self, frame: int) -> None """
        pass

    def setUpdateInterval(self, interval): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, interval: int) -> None """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def startFrame(self): # real signature unknown; restored from __doc__
        """ startFrame(self) -> int """
        return 0

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtCore.QTimeLine.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def toggleDirection(self): # real signature unknown; restored from __doc__
        """ toggleDirection(self) -> None """
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def valueForTime(self, msec): # real signature unknown; restored from __doc__
        """ valueForTime(self, msec: int) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, duration=1000, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Backward = PySide2.QtCore.QTimeLine.Direction.Backward
    CosineCurve = PySide2.QtCore.QTimeLine.CurveShape.CosineCurve
    CurveShape = None # (!) real value is "<class 'PySide2.QtCore.QTimeLine.CurveShape'>"
    Direction = None # (!) real value is "<class 'PySide2.QtCore.QTimeLine.Direction'>"
    EaseInCurve = PySide2.QtCore.QTimeLine.CurveShape.EaseInCurve
    EaseInOutCurve = PySide2.QtCore.QTimeLine.CurveShape.EaseInOutCurve
    EaseOutCurve = PySide2.QtCore.QTimeLine.CurveShape.EaseOutCurve
    Forward = PySide2.QtCore.QTimeLine.Direction.Forward
    LinearCurve = PySide2.QtCore.QTimeLine.CurveShape.LinearCurve
    NotRunning = PySide2.QtCore.QTimeLine.State.NotRunning
    Paused = PySide2.QtCore.QTimeLine.State.Paused
    Running = PySide2.QtCore.QTimeLine.State.Running
    SineCurve = PySide2.QtCore.QTimeLine.CurveShape.SineCurve
    State = None # (!) real value is "<class 'PySide2.QtCore.QTimeLine.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DDFF00>'


