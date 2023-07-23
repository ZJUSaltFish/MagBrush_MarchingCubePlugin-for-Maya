# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QState import QState

class QStateMachine(QState):
    """
    QStateMachine(self, childMode: PySide2.QtCore.QState.ChildMode, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QStateMachine(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def addDefaultAnimation(self, animation): # real signature unknown; restored from __doc__
        """ addDefaultAnimation(self, animation: PySide2.QtCore.QAbstractAnimation) -> None """
        pass

    def addState(self, state): # real signature unknown; restored from __doc__
        """ addState(self, state: PySide2.QtCore.QAbstractState) -> None """
        pass

    def beginMicrostep(self, event): # real signature unknown; restored from __doc__
        """ beginMicrostep(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def beginSelectTransitions(self, event): # real signature unknown; restored from __doc__
        """ beginSelectTransitions(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def cancelDelayedEvent(self, id): # real signature unknown; restored from __doc__
        """ cancelDelayedEvent(self, id: int) -> bool """
        return False

    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) -> None """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """
        configuration(self) -> typing.Set[PySide2.QtCore.QAbstractState]
        configuration(self) -> typing.List[PySide2.QtCore.QAbstractState]
        """
        pass

    def defaultAnimations(self): # real signature unknown; restored from __doc__
        """ defaultAnimations(self) -> typing.List[PySide2.QtCore.QAbstractAnimation] """
        pass

    def endMicrostep(self, event): # real signature unknown; restored from __doc__
        """ endMicrostep(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def endSelectTransitions(self, event): # real signature unknown; restored from __doc__
        """ endSelectTransitions(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtCore.QStateMachine.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, watched, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def globalRestorePolicy(self): # real signature unknown; restored from __doc__
        """ globalRestorePolicy(self) -> PySide2.QtCore.QState.RestorePolicy """
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def onEntry(self, event): # real signature unknown; restored from __doc__
        """ onEntry(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def onExit(self, event): # real signature unknown; restored from __doc__
        """ onExit(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def postDelayedEvent(self, event, delay): # real signature unknown; restored from __doc__
        """ postDelayedEvent(self, event: PySide2.QtCore.QEvent, delay: int) -> int """
        return 0

    def postEvent(self, event, priority=None): # real signature unknown; restored from __doc__
        """ postEvent(self, event: PySide2.QtCore.QEvent, priority: PySide2.QtCore.QStateMachine.EventPriority = PySide2.QtCore.QStateMachine.EventPriority.NormalPriority) -> None """
        pass

    def removeDefaultAnimation(self, animation): # real signature unknown; restored from __doc__
        """ removeDefaultAnimation(self, animation: PySide2.QtCore.QAbstractAnimation) -> None """
        pass

    def removeState(self, state): # real signature unknown; restored from __doc__
        """ removeState(self, state: PySide2.QtCore.QAbstractState) -> None """
        pass

    def runningChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setAnimated(self, enabled): # real signature unknown; restored from __doc__
        """ setAnimated(self, enabled: bool) -> None """
        pass

    def setGlobalRestorePolicy(self, restorePolicy): # real signature unknown; restored from __doc__
        """ setGlobalRestorePolicy(self, restorePolicy: PySide2.QtCore.QState.RestorePolicy) -> None """
        pass

    def setRunning(self, running): # real signature unknown; restored from __doc__
        """ setRunning(self, running: bool) -> None """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def started(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def stopped(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, childMode, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Error = None # (!) real value is "<class 'PySide2.QtCore.QStateMachine.Error'>"
    EventPriority = None # (!) real value is "<class 'PySide2.QtCore.QStateMachine.EventPriority'>"
    HighPriority = PySide2.QtCore.QStateMachine.EventPriority.HighPriority
    NoCommonAncestorForTransitionError = PySide2.QtCore.QStateMachine.Error.NoCommonAncestorForTransitionError
    NoDefaultStateInHistoryStateError = PySide2.QtCore.QStateMachine.Error.NoDefaultStateInHistoryStateError
    NoError = PySide2.QtCore.QStateMachine.Error.NoError
    NoInitialStateError = PySide2.QtCore.QStateMachine.Error.NoInitialStateError
    NormalPriority = PySide2.QtCore.QStateMachine.EventPriority.NormalPriority
    SignalEvent = None # (!) real value is "<class 'PySide2.QtCore.QStateMachine.SignalEvent'>"
    StateMachineChildModeSetToParallelError = PySide2.QtCore.QStateMachine.Error.StateMachineChildModeSetToParallelError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4D2C0>'
    WrappedEvent = None # (!) real value is "<class 'PySide2.QtCore.QStateMachine.WrappedEvent'>"


