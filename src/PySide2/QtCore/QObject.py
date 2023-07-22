# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QObject(__Shiboken.Object):
    """ QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def blockSignals(self, b): # real signature unknown; restored from __doc__
        """ blockSignals(self, b: bool) -> bool """
        return False

    def childEvent(self, event): # real signature unknown; restored from __doc__
        """ childEvent(self, event: PySide2.QtCore.QChildEvent) -> None """
        pass

    def children(self): # real signature unknown; restored from __doc__
        """ children(self) -> typing.List[PySide2.QtCore.QObject] """
        pass

    def connect(self, arg__1, arg__2, arg__3, type=None): # real signature unknown; restored from __doc__
        """
        connect(arg__1: PySide2.QtCore.QObject, arg__2: bytes, arg__3: typing.Callable, type: PySide2.QtCore.Qt.ConnectionType = PySide2.QtCore.Qt.ConnectionType.AutoConnection) -> bool
        connect(self, arg__1: bytes, arg__2: typing.Callable, type: PySide2.QtCore.Qt.ConnectionType = PySide2.QtCore.Qt.ConnectionType.AutoConnection) -> bool
        connect(self, arg__1: bytes, arg__2: PySide2.QtCore.QObject, arg__3: bytes, type: PySide2.QtCore.Qt.ConnectionType = PySide2.QtCore.Qt.ConnectionType.AutoConnection) -> bool
        connect(self, sender: PySide2.QtCore.QObject, signal: bytes, member: bytes, type: PySide2.QtCore.Qt.ConnectionType = PySide2.QtCore.Qt.ConnectionType.AutoConnection) -> PySide2.QtCore.QMetaObject.Connection
        connect(sender: PySide2.QtCore.QObject, signal: PySide2.QtCore.QMetaMethod, receiver: PySide2.QtCore.QObject, method: PySide2.QtCore.QMetaMethod, type: PySide2.QtCore.Qt.ConnectionType = PySide2.QtCore.Qt.ConnectionType.AutoConnection) -> PySide2.QtCore.QMetaObject.Connection
        connect(sender: PySide2.QtCore.QObject, signal: bytes, receiver: PySide2.QtCore.QObject, member: bytes, type: PySide2.QtCore.Qt.ConnectionType = PySide2.QtCore.Qt.ConnectionType.AutoConnection) -> PySide2.QtCore.QMetaObject.Connection
        """
        return False

    def connectNotify(self, signal): # real signature unknown; restored from __doc__
        """ connectNotify(self, signal: PySide2.QtCore.QMetaMethod) -> None """
        pass

    def customEvent(self, event): # real signature unknown; restored from __doc__
        """ customEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def deleteLater(self): # real signature unknown; restored from __doc__
        """ deleteLater(self) -> None """
        pass

    def destroyed(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(self, arg__1): # real signature unknown; restored from __doc__
        """
        disconnect(arg__1: PySide2.QtCore.QMetaObject.Connection) -> bool
        disconnect(arg__1: PySide2.QtCore.QObject, arg__2: bytes, arg__3: typing.Callable) -> bool
        disconnect(self, arg__1: bytes, arg__2: typing.Callable) -> bool
        disconnect(self, receiver: PySide2.QtCore.QObject, member: typing.Optional[bytes] = None) -> bool
        disconnect(self, signal: bytes, receiver: PySide2.QtCore.QObject, member: bytes) -> bool
        disconnect(sender: PySide2.QtCore.QObject, signal: PySide2.QtCore.QMetaMethod, receiver: PySide2.QtCore.QObject, member: PySide2.QtCore.QMetaMethod) -> bool
        disconnect(sender: PySide2.QtCore.QObject, signal: bytes, receiver: PySide2.QtCore.QObject, member: bytes) -> bool
        """
        return False

    def disconnectNotify(self, signal): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, signal: PySide2.QtCore.QMetaMethod) -> None """
        pass

    def dumpObjectInfo(self): # real signature unknown; restored from __doc__
        """ dumpObjectInfo(self) -> None """
        pass

    def dumpObjectTree(self): # real signature unknown; restored from __doc__
        """ dumpObjectTree(self) -> None """
        pass

    def dynamicPropertyNames(self): # real signature unknown; restored from __doc__
        """ dynamicPropertyNames(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def emit(self, arg__1, *args): # real signature unknown; restored from __doc__
        """ emit(self, arg__1: bytes, *args: None) -> bool """
        return False

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, watched, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def findChild(self, arg__1, arg__2=''): # real signature unknown; restored from __doc__
        """ findChild(self, arg__1: type, arg__2: str = '') -> object """
        return object()

    def findChildren(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        findChildren(self, arg__1: type, arg__2: PySide2.QtCore.QRegExp) -> typing.Iterable
        findChildren(self, arg__1: type, arg__2: PySide2.QtCore.QRegularExpression) -> typing.Iterable
        findChildren(self, arg__1: type, arg__2: str = '') -> typing.Iterable
        """
        pass

    def inherits(self, classname): # real signature unknown; restored from __doc__
        """ inherits(self, classname: bytes) -> bool """
        return False

    def installEventFilter(self, filterObj): # real signature unknown; restored from __doc__
        """ installEventFilter(self, filterObj: PySide2.QtCore.QObject) -> None """
        pass

    def isSignalConnected(self, signal): # real signature unknown; restored from __doc__
        """ isSignalConnected(self, signal: PySide2.QtCore.QMetaMethod) -> bool """
        return False

    def isWidgetType(self): # real signature unknown; restored from __doc__
        """ isWidgetType(self) -> bool """
        return False

    def isWindowType(self): # real signature unknown; restored from __doc__
        """ isWindowType(self) -> bool """
        return False

    def killTimer(self, id): # real signature unknown; restored from __doc__
        """ killTimer(self, id: int) -> None """
        pass

    def metaObject(self): # real signature unknown; restored from __doc__
        """ metaObject(self) -> PySide2.QtCore.QMetaObject """
        pass

    def moveToThread(self, thread): # real signature unknown; restored from __doc__
        """ moveToThread(self, thread: PySide2.QtCore.QThread) -> None """
        pass

    def objectName(self): # real signature unknown; restored from __doc__
        """ objectName(self) -> str """
        return ""

    def objectNameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> PySide2.QtCore.QObject """
        pass

    def property(self, name): # real signature unknown; restored from __doc__
        """ property(self, name: bytes) -> typing.Any """
        pass

    def receivers(self, signal): # real signature unknown; restored from __doc__
        """ receivers(self, signal: bytes) -> int """
        return 0

    def registerUserData(self): # real signature unknown; restored from __doc__
        """ registerUserData() -> int """
        return 0

    def removeEventFilter(self, obj): # real signature unknown; restored from __doc__
        """ removeEventFilter(self, obj: PySide2.QtCore.QObject) -> None """
        pass

    def sender(self): # real signature unknown; restored from __doc__
        """ sender(self) -> PySide2.QtCore.QObject """
        pass

    def senderSignalIndex(self): # real signature unknown; restored from __doc__
        """ senderSignalIndex(self) -> int """
        return 0

    def setObjectName(self, name): # real signature unknown; restored from __doc__
        """ setObjectName(self, name: str) -> None """
        pass

    def setParent(self, parent): # real signature unknown; restored from __doc__
        """ setParent(self, parent: PySide2.QtCore.QObject) -> None """
        pass

    def setProperty(self, name, value): # real signature unknown; restored from __doc__
        """ setProperty(self, name: bytes, value: typing.Any) -> bool """
        return False

    def signalsBlocked(self): # real signature unknown; restored from __doc__
        """ signalsBlocked(self) -> bool """
        return False

    def startTimer(self, interval, timerType=None): # real signature unknown; restored from __doc__
        """ startTimer(self, interval: int, timerType: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> int """
        return 0

    def thread(self): # real signature unknown; restored from __doc__
        """ thread(self) -> PySide2.QtCore.QThread """
        pass

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def tr(self, arg__1, arg__2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ tr(self, arg__1: bytes, arg__2: bytes = b'', arg__3: int = -1) -> str """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DCDD40>'


