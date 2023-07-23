# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QObject(__sip.wrapper):
    """ QObject(parent: typing.Optional[QObject] = None) """
    def blockSignals(self, b): # real signature unknown; restored from __doc__
        """ blockSignals(self, b: bool) -> bool """
        return False

    def childEvent(self, a0): # real signature unknown; restored from __doc__
        """ childEvent(self, a0: QChildEvent) """
        pass

    def children(self): # real signature unknown; restored from __doc__
        """ children(self) -> List[QObject] """
        return []

    def connectNotify(self, signal): # real signature unknown; restored from __doc__
        """ connectNotify(self, signal: QMetaMethod) """
        pass

    def customEvent(self, a0): # real signature unknown; restored from __doc__
        """ customEvent(self, a0: QEvent) """
        pass

    def deleteLater(self): # real signature unknown; restored from __doc__
        """ deleteLater(self) """
        pass

    def destroyed(self, *args, **kwargs): # real signature unknown
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

    def disconnect(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        disconnect(a0: QMetaObject.Connection) -> bool
        disconnect(self)
        """
        return False

    def disconnectNotify(self, signal): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, signal: QMetaMethod) """
        pass

    def dumpObjectInfo(self): # real signature unknown; restored from __doc__
        """ dumpObjectInfo(self) """
        pass

    def dumpObjectTree(self): # real signature unknown; restored from __doc__
        """ dumpObjectTree(self) """
        pass

    def dynamicPropertyNames(self): # real signature unknown; restored from __doc__
        """ dynamicPropertyNames(self) -> List[QByteArray] """
        return []

    def event(self, a0): # real signature unknown; restored from __doc__
        """ event(self, a0: QEvent) -> bool """
        return False

    def eventFilter(self, a0, a1): # real signature unknown; restored from __doc__
        """ eventFilter(self, a0: QObject, a1: QEvent) -> bool """
        return False

    def findChild(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        findChild(self, type: type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject
        findChild(self, types: Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject
        """
        pass

    def findChildren(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        findChildren(self, type: type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, types: Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, type: type, regExp: QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, types: Tuple, regExp: QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, type: type, re: QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        findChildren(self, types: Tuple, re: QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
        """
        pass

    def inherits(self, classname): # real signature unknown; restored from __doc__
        """ inherits(self, classname: str) -> bool """
        return False

    def installEventFilter(self, a0): # real signature unknown; restored from __doc__
        """ installEventFilter(self, a0: QObject) """
        pass

    def isSignalConnected(self, signal): # real signature unknown; restored from __doc__
        """ isSignalConnected(self, signal: QMetaMethod) -> bool """
        return False

    def isWidgetType(self): # real signature unknown; restored from __doc__
        """ isWidgetType(self) -> bool """
        return False

    def isWindowType(self): # real signature unknown; restored from __doc__
        """ isWindowType(self) -> bool """
        return False

    def killTimer(self, id): # real signature unknown; restored from __doc__
        """ killTimer(self, id: int) """
        pass

    def metaObject(self): # real signature unknown; restored from __doc__
        """ metaObject(self) -> QMetaObject """
        return QMetaObject

    def moveToThread(self, thread): # real signature unknown; restored from __doc__
        """ moveToThread(self, thread: QThread) """
        pass

    def objectName(self): # real signature unknown; restored from __doc__
        """ objectName(self) -> str """
        return ""

    def objectNameChanged(self, *args, **kwargs): # real signature unknown
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

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QObject """
        return QObject

    def property(self, name): # real signature unknown; restored from __doc__
        """ property(self, name: str) -> Any """
        pass

    def pyqtConfigure(self, *more): # real signature unknown; restored from __doc__
        """
        QObject.pyqtConfigure(...)
        
        Each keyword argument is either the name of a Qt property or a Qt signal.
        For properties the property is set to the given value which should be of an
        appropriate type.
        For signals the signal is connected to the given value which should be a
        callable.
        """
        pass

    def receivers(self, signal): # real signature unknown; restored from __doc__
        """ receivers(self, signal: PYQT_SIGNAL) -> int """
        return 0

    def removeEventFilter(self, a0): # real signature unknown; restored from __doc__
        """ removeEventFilter(self, a0: QObject) """
        pass

    def sender(self): # real signature unknown; restored from __doc__
        """ sender(self) -> QObject """
        return QObject

    def senderSignalIndex(self): # real signature unknown; restored from __doc__
        """ senderSignalIndex(self) -> int """
        return 0

    def setObjectName(self, name): # real signature unknown; restored from __doc__
        """ setObjectName(self, name: str) """
        pass

    def setParent(self, a0): # real signature unknown; restored from __doc__
        """ setParent(self, a0: QObject) """
        pass

    def setProperty(self, name, value): # real signature unknown; restored from __doc__
        """ setProperty(self, name: str, value: Any) -> bool """
        return False

    def signalsBlocked(self): # real signature unknown; restored from __doc__
        """ signalsBlocked(self) -> bool """
        return False

    def startTimer(self, interval, timerType=None): # real signature unknown; restored from __doc__
        """ startTimer(self, interval: int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int """
        return 0

    def thread(self): # real signature unknown; restored from __doc__
        """ thread(self) -> QThread """
        return QThread

    def timerEvent(self, a0): # real signature unknown; restored from __doc__
        """ timerEvent(self, a0: QTimerEvent) """
        pass

    def tr(self, sourceText, disambiguation, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ tr(self, sourceText: str, disambiguation: typing.Optional[str] = None, n: int = -1) -> str """
        pass

    def __getattr__(self, name): # real signature unknown; restored from __doc__
        """ __getattr__(self, name: str) -> object """
        return object()

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




