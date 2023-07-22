# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QIODevice import QIODevice

class QFileDevice(QIODevice):
    """
    QFileDevice(self) -> None
    QFileDevice(self, parent: PySide2.QtCore.QObject) -> None
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtCore.QFileDevice.FileError """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def fileTime(self, time): # real signature unknown; restored from __doc__
        """ fileTime(self, time: PySide2.QtCore.QFileDevice.FileTime) -> PySide2.QtCore.QDateTime """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def map(self, offset, size, flags=None): # real signature unknown; restored from __doc__
        """ map(self, offset: int, size: int, flags: PySide2.QtCore.QFileDevice.MemoryMapFlags = PySide2.QtCore.QFileDevice.MemoryMapFlags.NoOptions) -> bytes """
        return b""

    def permissions(self): # real signature unknown; restored from __doc__
        """ permissions(self) -> PySide2.QtCore.QFileDevice.Permissions """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def readData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, data: bytes, maxlen: int) -> int """
        return 0

    def readLineData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readLineData(self, data: bytes, maxlen: int) -> int """
        return 0

    def resize(self, sz): # real signature unknown; restored from __doc__
        """ resize(self, sz: int) -> bool """
        return False

    def seek(self, offset): # real signature unknown; restored from __doc__
        """ seek(self, offset: int) -> bool """
        return False

    def setFileTime(self, newDate, fileTime): # real signature unknown; restored from __doc__
        """ setFileTime(self, newDate: PySide2.QtCore.QDateTime, fileTime: PySide2.QtCore.QFileDevice.FileTime) -> bool """
        return False

    def setPermissions(self, permissionSpec): # real signature unknown; restored from __doc__
        """ setPermissions(self, permissionSpec: PySide2.QtCore.QFileDevice.Permissions) -> bool """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def unmap(self, address): # real signature unknown; restored from __doc__
        """ unmap(self, address: bytes) -> bool """
        return False

    def unsetError(self): # real signature unknown; restored from __doc__
        """ unsetError(self) -> None """
        pass

    def writeData(self, data, len): # real signature unknown; restored from __doc__
        """ writeData(self, data: bytes, len: int) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AbortError = PySide2.QtCore.QFileDevice.FileError.AbortError
    AutoCloseHandle = PySide2.QtCore.QFileDevice.FileHandleFlag.AutoCloseHandle
    CopyError = PySide2.QtCore.QFileDevice.FileError.CopyError
    DontCloseHandle = PySide2.QtCore.QFileDevice.FileHandleFlag.DontCloseHandle
    ExeGroup = PySide2.QtCore.QFileDevice.Permission.ExeGroup
    ExeOther = PySide2.QtCore.QFileDevice.Permission.ExeOther
    ExeOwner = PySide2.QtCore.QFileDevice.Permission.ExeOwner
    ExeUser = PySide2.QtCore.QFileDevice.Permission.ExeUser
    FatalError = PySide2.QtCore.QFileDevice.FileError.FatalError
    FileAccessTime = PySide2.QtCore.QFileDevice.FileTime.FileAccessTime
    FileBirthTime = PySide2.QtCore.QFileDevice.FileTime.FileBirthTime
    FileError = None # (!) real value is "<class 'PySide2.QtCore.QFileDevice.FileError'>"
    FileHandleFlag = None # (!) real value is "<class 'PySide2.QtCore.QFileDevice.FileHandleFlag'>"
    FileHandleFlags = None # (!) real value is "<class 'PySide2.QtCore.QFileDevice.FileHandleFlags'>"
    FileMetadataChangeTime = PySide2.QtCore.QFileDevice.FileTime.FileMetadataChangeTime
    FileModificationTime = PySide2.QtCore.QFileDevice.FileTime.FileModificationTime
    FileTime = None # (!) real value is "<class 'PySide2.QtCore.QFileDevice.FileTime'>"
    MapPrivateOption = PySide2.QtCore.QFileDevice.MemoryMapFlags.MapPrivateOption
    MemoryMapFlags = None # (!) real value is "<class 'PySide2.QtCore.QFileDevice.MemoryMapFlags'>"
    NoError = PySide2.QtCore.QFileDevice.FileError.NoError
    NoOptions = PySide2.QtCore.QFileDevice.MemoryMapFlags.NoOptions
    OpenError = PySide2.QtCore.QFileDevice.FileError.OpenError
    Permission = None # (!) real value is "<class 'PySide2.QtCore.QFileDevice.Permission'>"
    Permissions = None # (!) real value is "<class 'PySide2.QtCore.QFileDevice.Permissions'>"
    PermissionsError = PySide2.QtCore.QFileDevice.FileError.PermissionsError
    PositionError = PySide2.QtCore.QFileDevice.FileError.PositionError
    ReadError = PySide2.QtCore.QFileDevice.FileError.ReadError
    ReadGroup = PySide2.QtCore.QFileDevice.Permission.ReadGroup
    ReadOther = PySide2.QtCore.QFileDevice.Permission.ReadOther
    ReadOwner = PySide2.QtCore.QFileDevice.Permission.ReadOwner
    ReadUser = PySide2.QtCore.QFileDevice.Permission.ReadUser
    RemoveError = PySide2.QtCore.QFileDevice.FileError.RemoveError
    RenameError = PySide2.QtCore.QFileDevice.FileError.RenameError
    ResizeError = PySide2.QtCore.QFileDevice.FileError.ResizeError
    ResourceError = PySide2.QtCore.QFileDevice.FileError.ResourceError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DEFA80>'
    TimeOutError = PySide2.QtCore.QFileDevice.FileError.TimeOutError
    UnspecifiedError = PySide2.QtCore.QFileDevice.FileError.UnspecifiedError
    WriteError = PySide2.QtCore.QFileDevice.FileError.WriteError
    WriteGroup = PySide2.QtCore.QFileDevice.Permission.WriteGroup
    WriteOther = PySide2.QtCore.QFileDevice.Permission.WriteOther
    WriteOwner = PySide2.QtCore.QFileDevice.Permission.WriteOwner
    WriteUser = PySide2.QtCore.QFileDevice.Permission.WriteUser


