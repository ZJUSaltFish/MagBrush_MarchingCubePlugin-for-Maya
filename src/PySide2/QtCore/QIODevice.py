# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QIODevice(QObject):
    """
    QIODevice(self) -> None
    QIODevice(self, parent: PySide2.QtCore.QObject) -> None
    """
    def aboutToClose(self, *args, **kwargs): # real signature unknown
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def bytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def channelBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def channelReadyRead(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def commitTransaction(self): # real signature unknown; restored from __doc__
        """ commitTransaction(self) -> None """
        pass

    def currentReadChannel(self): # real signature unknown; restored from __doc__
        """ currentReadChannel(self) -> int """
        return 0

    def currentWriteChannel(self): # real signature unknown; restored from __doc__
        """ currentWriteChannel(self) -> int """
        return 0

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def getChar(self, c): # real signature unknown; restored from __doc__
        """ getChar(self, c: bytes) -> bool """
        return False

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isTextModeEnabled(self): # real signature unknown; restored from __doc__
        """ isTextModeEnabled(self) -> bool """
        return False

    def isTransactionStarted(self): # real signature unknown; restored from __doc__
        """ isTransactionStarted(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def open(self, mode): # real signature unknown; restored from __doc__
        """ open(self, mode: PySide2.QtCore.QIODevice.OpenMode) -> bool """
        return False

    def openMode(self): # real signature unknown; restored from __doc__
        """ openMode(self) -> PySide2.QtCore.QIODevice.OpenMode """
        pass

    def peek(self, maxlen): # real signature unknown; restored from __doc__
        """ peek(self, maxlen: int) -> PySide2.QtCore.QByteArray """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def putChar(self, c): # real signature unknown; restored from __doc__
        """ putChar(self, c: int) -> bool """
        return False

    def read(self, maxlen): # real signature unknown; restored from __doc__
        """ read(self, maxlen: int) -> PySide2.QtCore.QByteArray """
        pass

    def readAll(self): # real signature unknown; restored from __doc__
        """ readAll(self) -> PySide2.QtCore.QByteArray """
        pass

    def readChannelCount(self): # real signature unknown; restored from __doc__
        """ readChannelCount(self) -> int """
        return 0

    def readChannelFinished(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, data: bytes, maxlen: int) -> int """
        return 0

    def readLine(self, maxlen=0): # real signature unknown; restored from __doc__
        """ readLine(self, maxlen: int = 0) -> PySide2.QtCore.QByteArray """
        pass

    def readLineData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readLineData(self, data: bytes, maxlen: int) -> int """
        return 0

    def readyRead(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> bool """
        return False

    def rollbackTransaction(self): # real signature unknown; restored from __doc__
        """ rollbackTransaction(self) -> None """
        pass

    def seek(self, pos): # real signature unknown; restored from __doc__
        """ seek(self, pos: int) -> bool """
        return False

    def setCurrentReadChannel(self, channel): # real signature unknown; restored from __doc__
        """ setCurrentReadChannel(self, channel: int) -> None """
        pass

    def setCurrentWriteChannel(self, channel): # real signature unknown; restored from __doc__
        """ setCurrentWriteChannel(self, channel: int) -> None """
        pass

    def setErrorString(self, errorString): # real signature unknown; restored from __doc__
        """ setErrorString(self, errorString: str) -> None """
        pass

    def setOpenMode(self, openMode): # real signature unknown; restored from __doc__
        """ setOpenMode(self, openMode: PySide2.QtCore.QIODevice.OpenMode) -> None """
        pass

    def setTextModeEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setTextModeEnabled(self, enabled: bool) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def skip(self, maxSize): # real signature unknown; restored from __doc__
        """ skip(self, maxSize: int) -> int """
        return 0

    def startTransaction(self): # real signature unknown; restored from __doc__
        """ startTransaction(self) -> None """
        pass

    def ungetChar(self, c): # real signature unknown; restored from __doc__
        """ ungetChar(self, c: int) -> None """
        pass

    def waitForBytesWritten(self, msecs): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int) -> bool """
        return False

    def waitForReadyRead(self, msecs): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int) -> bool """
        return False

    def write(self, data): # real signature unknown; restored from __doc__
        """ write(self, data: PySide2.QtCore.QByteArray) -> int """
        return 0

    def writeChannelCount(self): # real signature unknown; restored from __doc__
        """ writeChannelCount(self) -> int """
        return 0

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

    Append = PySide2.QtCore.QIODevice.OpenModeFlag.Append
    ExistingOnly = PySide2.QtCore.QIODevice.OpenModeFlag.ExistingOnly
    NewOnly = PySide2.QtCore.QIODevice.OpenModeFlag.NewOnly
    NotOpen = PySide2.QtCore.QIODevice.OpenModeFlag.NotOpen
    OpenMode = None # (!) real value is "<class 'PySide2.QtCore.QIODevice.OpenMode'>"
    OpenModeFlag = None # (!) real value is "<class 'PySide2.QtCore.QIODevice.OpenModeFlag'>"
    ReadOnly = PySide2.QtCore.QIODevice.OpenModeFlag.ReadOnly
    ReadWrite = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DCF180>'
    Text = PySide2.QtCore.QIODevice.OpenModeFlag.Text
    Truncate = PySide2.QtCore.QIODevice.OpenModeFlag.Truncate
    Unbuffered = PySide2.QtCore.QIODevice.OpenModeFlag.Unbuffered
    WriteOnly = PySide2.QtCore.QIODevice.OpenModeFlag.WriteOnly


