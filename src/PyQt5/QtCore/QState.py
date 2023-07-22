# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractState import QAbstractState

class QState(QAbstractState):
    """
    QState(parent: typing.Optional[QState] = None)
    QState(childMode: QState.ChildMode, parent: typing.Optional[QState] = None)
    """
    def addTransition(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addTransition(self, transition: QAbstractTransition)
        addTransition(self, signal: pyqtBoundSignal, target: QAbstractState) -> QSignalTransition
        addTransition(self, target: QAbstractState) -> QAbstractTransition
        """
        return QSignalTransition or QAbstractTransition

    def assignProperty(self, p_object, name, value): # real signature unknown; restored from __doc__
        """ assignProperty(self, object: QObject, name: str, value: Any) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childMode(self): # real signature unknown; restored from __doc__
        """ childMode(self) -> QState.ChildMode """
        pass

    def childModeChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def errorState(self): # real signature unknown; restored from __doc__
        """ errorState(self) -> QAbstractState """
        return QAbstractState

    def errorStateChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: QEvent) -> bool """
        return False

    def finished(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def initialState(self): # real signature unknown; restored from __doc__
        """ initialState(self) -> QAbstractState """
        return QAbstractState

    def initialStateChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def onEntry(self, event): # real signature unknown; restored from __doc__
        """ onEntry(self, event: QEvent) """
        pass

    def onExit(self, event): # real signature unknown; restored from __doc__
        """ onExit(self, event: QEvent) """
        pass

    def propertiesAssigned(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeTransition(self, transition): # real signature unknown; restored from __doc__
        """ removeTransition(self, transition: QAbstractTransition) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setChildMode(self, mode): # real signature unknown; restored from __doc__
        """ setChildMode(self, mode: QState.ChildMode) """
        pass

    def setErrorState(self, state): # real signature unknown; restored from __doc__
        """ setErrorState(self, state: QAbstractState) """
        pass

    def setInitialState(self, state): # real signature unknown; restored from __doc__
        """ setInitialState(self, state: QAbstractState) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transitions(self): # real signature unknown; restored from __doc__
        """ transitions(self) -> List[QAbstractTransition] """
        return []

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DontRestoreProperties = 0
    ExclusiveStates = 0
    ParallelStates = 1
    RestoreProperties = 1


