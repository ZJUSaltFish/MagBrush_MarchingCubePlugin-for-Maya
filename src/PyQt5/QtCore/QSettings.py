# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QSettings(QObject):
    """
    QSettings(organization: str, application: str = '', parent: typing.Optional[QObject] = None)
    QSettings(scope: QSettings.Scope, organization: str, application: str = '', parent: typing.Optional[QObject] = None)
    QSettings(format: QSettings.Format, scope: QSettings.Scope, organization: str, application: str = '', parent: typing.Optional[QObject] = None)
    QSettings(fileName: str, format: QSettings.Format, parent: typing.Optional[QObject] = None)
    QSettings(scope: QSettings.Scope, parent: typing.Optional[QObject] = None)
    QSettings(parent: typing.Optional[QObject] = None)
    """
    def allKeys(self): # real signature unknown; restored from __doc__
        """ allKeys(self) -> List[str] """
        return []

    def applicationName(self): # real signature unknown; restored from __doc__
        """ applicationName(self) -> str """
        return ""

    def beginGroup(self, prefix): # real signature unknown; restored from __doc__
        """ beginGroup(self, prefix: str) """
        pass

    def beginReadArray(self, prefix): # real signature unknown; restored from __doc__
        """ beginReadArray(self, prefix: str) -> int """
        return 0

    def beginWriteArray(self, prefix, size=-1): # real signature unknown; restored from __doc__
        """ beginWriteArray(self, prefix: str, size: int = -1) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childGroups(self): # real signature unknown; restored from __doc__
        """ childGroups(self) -> List[str] """
        return []

    def childKeys(self): # real signature unknown; restored from __doc__
        """ childKeys(self) -> List[str] """
        return []

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, key): # real signature unknown; restored from __doc__
        """ contains(self, key: str) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ defaultFormat() -> QSettings.Format """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ endArray(self) """
        pass

    def endGroup(self): # real signature unknown; restored from __doc__
        """ endGroup(self) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
        return False

    def fallbacksEnabled(self): # real signature unknown; restored from __doc__
        """ fallbacksEnabled(self) -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSettings.Format """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> str """
        return ""

    def iniCodec(self): # real signature unknown; restored from __doc__
        """ iniCodec(self) -> QTextCodec """
        return QTextCodec

    def isAtomicSyncRequired(self): # real signature unknown; restored from __doc__
        """ isAtomicSyncRequired(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def organizationName(self): # real signature unknown; restored from __doc__
        """ organizationName(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, key): # real signature unknown; restored from __doc__
        """ remove(self, key: str) """
        pass

    def scope(self): # real signature unknown; restored from __doc__
        """ scope(self) -> QSettings.Scope """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setArrayIndex(self, i): # real signature unknown; restored from __doc__
        """ setArrayIndex(self, i: int) """
        pass

    def setAtomicSyncRequired(self, enable): # real signature unknown; restored from __doc__
        """ setAtomicSyncRequired(self, enable: bool) """
        pass

    def setDefaultFormat(self, format): # real signature unknown; restored from __doc__
        """ setDefaultFormat(format: QSettings.Format) """
        pass

    def setFallbacksEnabled(self, b): # real signature unknown; restored from __doc__
        """ setFallbacksEnabled(self, b: bool) """
        pass

    def setIniCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setIniCodec(self, codec: QTextCodec)
        setIniCodec(self, codecName: str)
        """
        pass

    def setPath(self, format, scope, path): # real signature unknown; restored from __doc__
        """ setPath(format: QSettings.Format, scope: QSettings.Scope, path: str) """
        pass

    def setValue(self, key, value): # real signature unknown; restored from __doc__
        """ setValue(self, key: str, value: Any) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QSettings.Status """
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ sync(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, key, defaultValue=None, type=None): # real signature unknown; restored from __doc__
        """ value(self, key: str, defaultValue: Any = None, type: type = None) -> object """
        return object()

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AccessError = 1
    FormatError = 2
    IniFormat = 1
    InvalidFormat = 16
    NativeFormat = 0
    NoError = 0
    SystemScope = 1
    UserScope = 0


