# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractState import QAbstractState

class QState(QAbstractState):
    """
    QState(self, childMode: PySide2.QtCore.QState.ChildMode, parent: typing.Optional[PySide2.QtCore.QState] = None) -> None
    QState(self, parent: typing.Optional[PySide2.QtCore.QState] = None) -> None
    """
    def addTransition(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        addTransition(self, arg__1: object, arg__2: PySide2.QtCore.QAbstractState) -> PySide2.QtCore.QSignalTransition
        addTransition(self, sender: PySide2.QtCore.QObject, signal: bytes, target: PySide2.QtCore.QAbstractState) -> PySide2.QtCore.QSignalTransition
        addTransition(self, target: PySide2.QtCore.QAbstractState) -> PySide2.QtCore.QAbstractTransition
        addTransition(self, transition: PySide2.QtCore.QAbstractTransition) -> None
        """
        pass

    def assignProperty(self, p_object, name, value): # real signature unknown; restored from __doc__
        """ assignProperty(self, object: PySide2.QtCore.QObject, name: bytes, value: typing.Any) -> None """
        pass

    def childMode(self): # real signature unknown; restored from __doc__
        """ childMode(self) -> PySide2.QtCore.QState.ChildMode """
        pass

    def childModeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def errorState(self): # real signature unknown; restored from __doc__
        """ errorState(self) -> PySide2.QtCore.QAbstractState """
        pass

    def errorStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def initialState(self): # real signature unknown; restored from __doc__
        """ initialState(self) -> PySide2.QtCore.QAbstractState """
        pass

    def initialStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def onEntry(self, event): # real signature unknown; restored from __doc__
        """ onEntry(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def onExit(self, event): # real signature unknown; restored from __doc__
        """ onExit(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def propertiesAssigned(self, *args, **kwargs): # real signature unknown
        pass

    def removeTransition(self, transition): # real signature unknown; restored from __doc__
        """ removeTransition(self, transition: PySide2.QtCore.QAbstractTransition) -> None """
        pass

    def setChildMode(self, mode): # real signature unknown; restored from __doc__
        """ setChildMode(self, mode: PySide2.QtCore.QState.ChildMode) -> None """
        pass

    def setErrorState(self, state): # real signature unknown; restored from __doc__
        """ setErrorState(self, state: PySide2.QtCore.QAbstractState) -> None """
        pass

    def setInitialState(self, state): # real signature unknown; restored from __doc__
        """ setInitialState(self, state: PySide2.QtCore.QAbstractState) -> None """
        pass

    def transitions(self): # real signature unknown; restored from __doc__
        """ transitions(self) -> typing.List[PySide2.QtCore.QAbstractTransition] """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, childMode, parent, PySide2_QtCore_QState=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ChildMode = None # (!) real value is "<class 'PySide2.QtCore.QState.ChildMode'>"
    DontRestoreProperties = PySide2.QtCore.QState.RestorePolicy.DontRestoreProperties
    ExclusiveStates = PySide2.QtCore.QState.ChildMode.ExclusiveStates
    ParallelStates = PySide2.QtCore.QState.ChildMode.ParallelStates
    RestorePolicy = None # (!) real value is "<class 'PySide2.QtCore.QState.RestorePolicy'>"
    RestoreProperties = PySide2.QtCore.QState.RestorePolicy.RestoreProperties
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4CAC0>'


