# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QAbstractAnimation(QObject):
    """ QAbstractAnimation(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def currentLoop(self): # real signature unknown; restored from __doc__
        """ currentLoop(self) -> int """
        return 0

    def currentLoopChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentLoopTime(self): # real signature unknown; restored from __doc__
        """ currentLoopTime(self) -> int """
        return 0

    def currentTime(self): # real signature unknown; restored from __doc__
        """ currentTime(self) -> int """
        return 0

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> PySide2.QtCore.QAbstractAnimation.Direction """
        pass

    def directionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> PySide2.QtCore.QAnimationGroup """
        pass

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) -> None """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def setCurrentTime(self, msecs): # real signature unknown; restored from __doc__
        """ setCurrentTime(self, msecs: int) -> None """
        pass

    def setDirection(self, direction): # real signature unknown; restored from __doc__
        """ setDirection(self, direction: PySide2.QtCore.QAbstractAnimation.Direction) -> None """
        pass

    def setLoopCount(self, loopCount): # real signature unknown; restored from __doc__
        """ setLoopCount(self, loopCount: int) -> None """
        pass

    def setPaused(self, arg__1): # real signature unknown; restored from __doc__
        """ setPaused(self, arg__1: bool) -> None """
        pass

    def start(self, policy=None): # real signature unknown; restored from __doc__
        """ start(self, policy: PySide2.QtCore.QAbstractAnimation.DeletionPolicy = PySide2.QtCore.QAbstractAnimation.DeletionPolicy.KeepWhenStopped) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtCore.QAbstractAnimation.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def totalDuration(self): # real signature unknown; restored from __doc__
        """ totalDuration(self) -> int """
        return 0

    def updateCurrentTime(self, currentTime): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, currentTime: int) -> None """
        pass

    def updateDirection(self, direction): # real signature unknown; restored from __doc__
        """ updateDirection(self, direction: PySide2.QtCore.QAbstractAnimation.Direction) -> None """
        pass

    def updateState(self, newState, oldState): # real signature unknown; restored from __doc__
        """ updateState(self, newState: PySide2.QtCore.QAbstractAnimation.State, oldState: PySide2.QtCore.QAbstractAnimation.State) -> None """
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

    Backward = PySide2.QtCore.QAbstractAnimation.Direction.Backward
    DeleteWhenStopped = PySide2.QtCore.QAbstractAnimation.DeletionPolicy.DeleteWhenStopped
    DeletionPolicy = None # (!) real value is "<class 'PySide2.QtCore.QAbstractAnimation.DeletionPolicy'>"
    Direction = None # (!) real value is "<class 'PySide2.QtCore.QAbstractAnimation.Direction'>"
    Forward = PySide2.QtCore.QAbstractAnimation.Direction.Forward
    KeepWhenStopped = PySide2.QtCore.QAbstractAnimation.DeletionPolicy.KeepWhenStopped
    Paused = PySide2.QtCore.QAbstractAnimation.State.Paused
    Running = PySide2.QtCore.QAbstractAnimation.State.Running
    State = None # (!) real value is "<class 'PySide2.QtCore.QAbstractAnimation.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E64B00>'
    Stopped = PySide2.QtCore.QAbstractAnimation.State.Stopped


