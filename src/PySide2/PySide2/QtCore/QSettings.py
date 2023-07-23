# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QSettings(QObject):
    """
    QSettings(self, fileName: str, format: PySide2.QtCore.QSettings.Format, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSettings(self, format: PySide2.QtCore.QSettings.Format, scope: PySide2.QtCore.QSettings.Scope, organization: str, application: str = '', parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSettings(self, organization: str, application: str = '', parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSettings(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSettings(self, scope: PySide2.QtCore.QSettings.Scope, organization: str, application: str = '', parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSettings(self, scope: PySide2.QtCore.QSettings.Scope, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def allKeys(self): # real signature unknown; restored from __doc__
        """ allKeys(self) -> typing.List[str] """
        pass

    def applicationName(self): # real signature unknown; restored from __doc__
        """ applicationName(self) -> str """
        return ""

    def beginGroup(self, prefix): # real signature unknown; restored from __doc__
        """ beginGroup(self, prefix: str) -> None """
        pass

    def beginReadArray(self, prefix): # real signature unknown; restored from __doc__
        """ beginReadArray(self, prefix: str) -> int """
        return 0

    def beginWriteArray(self, prefix, size=-1): # real signature unknown; restored from __doc__
        """ beginWriteArray(self, prefix: str, size: int = -1) -> None """
        pass

    def childGroups(self): # real signature unknown; restored from __doc__
        """ childGroups(self) -> typing.List[str] """
        pass

    def childKeys(self): # real signature unknown; restored from __doc__
        """ childKeys(self) -> typing.List[str] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def contains(self, key): # real signature unknown; restored from __doc__
        """ contains(self, key: str) -> bool """
        return False

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ defaultFormat() -> PySide2.QtCore.QSettings.Format """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ endArray(self) -> None """
        pass

    def endGroup(self): # real signature unknown; restored from __doc__
        """ endGroup(self) -> None """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def fallbacksEnabled(self): # real signature unknown; restored from __doc__
        """ fallbacksEnabled(self) -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtCore.QSettings.Format """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> str """
        return ""

    def iniCodec(self): # real signature unknown; restored from __doc__
        """ iniCodec(self) -> PySide2.QtCore.QTextCodec """
        pass

    def isAtomicSyncRequired(self): # real signature unknown; restored from __doc__
        """ isAtomicSyncRequired(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def organizationName(self): # real signature unknown; restored from __doc__
        """ organizationName(self) -> str """
        return ""

    def remove(self, key): # real signature unknown; restored from __doc__
        """ remove(self, key: str) -> None """
        pass

    def scope(self): # real signature unknown; restored from __doc__
        """ scope(self) -> PySide2.QtCore.QSettings.Scope """
        pass

    def setArrayIndex(self, i): # real signature unknown; restored from __doc__
        """ setArrayIndex(self, i: int) -> None """
        pass

    def setAtomicSyncRequired(self, enable): # real signature unknown; restored from __doc__
        """ setAtomicSyncRequired(self, enable: bool) -> None """
        pass

    def setDefaultFormat(self, format): # real signature unknown; restored from __doc__
        """ setDefaultFormat(format: PySide2.QtCore.QSettings.Format) -> None """
        pass

    def setFallbacksEnabled(self, b): # real signature unknown; restored from __doc__
        """ setFallbacksEnabled(self, b: bool) -> None """
        pass

    def setIniCodec(self, codec): # real signature unknown; restored from __doc__
        """
        setIniCodec(self, codec: PySide2.QtCore.QTextCodec) -> None
        setIniCodec(self, codecName: bytes) -> None
        """
        pass

    def setPath(self, format, scope, path): # real signature unknown; restored from __doc__
        """ setPath(format: PySide2.QtCore.QSettings.Format, scope: PySide2.QtCore.QSettings.Scope, path: str) -> None """
        pass

    def setValue(self, key, value): # real signature unknown; restored from __doc__
        """ setValue(self, key: str, value: typing.Any) -> None """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtCore.QSettings.Status """
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ sync(self) -> None """
        pass

    def value(self, arg__1, defaultValue, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ value(self, arg__1: str, defaultValue: typing.Optional[typing.Any] = None, type: typing.Optional[object] = None) -> object """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, fileName, format, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AccessError = PySide2.QtCore.QSettings.Status.AccessError
    CustomFormat1 = PySide2.QtCore.QSettings.Format.CustomFormat1
    CustomFormat10 = PySide2.QtCore.QSettings.Format.CustomFormat10
    CustomFormat11 = PySide2.QtCore.QSettings.Format.CustomFormat11
    CustomFormat12 = PySide2.QtCore.QSettings.Format.CustomFormat12
    CustomFormat13 = PySide2.QtCore.QSettings.Format.CustomFormat13
    CustomFormat14 = PySide2.QtCore.QSettings.Format.CustomFormat14
    CustomFormat15 = PySide2.QtCore.QSettings.Format.CustomFormat15
    CustomFormat16 = PySide2.QtCore.QSettings.Format.CustomFormat16
    CustomFormat2 = PySide2.QtCore.QSettings.Format.CustomFormat2
    CustomFormat3 = PySide2.QtCore.QSettings.Format.CustomFormat3
    CustomFormat4 = PySide2.QtCore.QSettings.Format.CustomFormat4
    CustomFormat5 = PySide2.QtCore.QSettings.Format.CustomFormat5
    CustomFormat6 = PySide2.QtCore.QSettings.Format.CustomFormat6
    CustomFormat7 = PySide2.QtCore.QSettings.Format.CustomFormat7
    CustomFormat8 = PySide2.QtCore.QSettings.Format.CustomFormat8
    CustomFormat9 = PySide2.QtCore.QSettings.Format.CustomFormat9
    Format = None # (!) real value is "<class 'PySide2.QtCore.QSettings.Format'>"
    FormatError = PySide2.QtCore.QSettings.Status.FormatError
    IniFormat = PySide2.QtCore.QSettings.Format.IniFormat
    InvalidFormat = PySide2.QtCore.QSettings.Format.InvalidFormat
    NativeFormat = PySide2.QtCore.QSettings.Format.NativeFormat
    NoError = PySide2.QtCore.QSettings.Status.NoError
    Registry32Format = PySide2.QtCore.QSettings.Format.Registry32Format
    Registry64Format = PySide2.QtCore.QSettings.Format.Registry64Format
    Scope = None # (!) real value is "<class 'PySide2.QtCore.QSettings.Scope'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DDE940>'
    Status = None # (!) real value is "<class 'PySide2.QtCore.QSettings.Status'>"
    SystemScope = PySide2.QtCore.QSettings.Scope.SystemScope
    UserScope = PySide2.QtCore.QSettings.Scope.UserScope


