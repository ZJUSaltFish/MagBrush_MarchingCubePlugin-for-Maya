# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDataStream(__Shiboken.Object):
    """
    QDataStream(self) -> None
    QDataStream(self, arg__1: PySide2.QtCore.QByteArray) -> None
    QDataStream(self, arg__1: PySide2.QtCore.QByteArray, flags: PySide2.QtCore.QIODevice.OpenMode) -> None
    QDataStream(self, arg__1: PySide2.QtCore.QIODevice) -> None
    """
    def abortTransaction(self): # real signature unknown; restored from __doc__
        """ abortTransaction(self) -> None """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def byteOrder(self): # real signature unknown; restored from __doc__
        """ byteOrder(self) -> PySide2.QtCore.QDataStream.ByteOrder """
        pass

    def commitTransaction(self): # real signature unknown; restored from __doc__
        """ commitTransaction(self) -> bool """
        return False

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def floatingPointPrecision(self): # real signature unknown; restored from __doc__
        """ floatingPointPrecision(self) -> PySide2.QtCore.QDataStream.FloatingPointPrecision """
        pass

    def readBool(self): # real signature unknown; restored from __doc__
        """ readBool(self) -> bool """
        return False

    def readDouble(self): # real signature unknown; restored from __doc__
        """ readDouble(self) -> float """
        return 0.0

    def readFloat(self): # real signature unknown; restored from __doc__
        """ readFloat(self) -> float """
        return 0.0

    def readInt16(self): # real signature unknown; restored from __doc__
        """ readInt16(self) -> int """
        return 0

    def readInt32(self): # real signature unknown; restored from __doc__
        """ readInt32(self) -> int """
        return 0

    def readInt64(self): # real signature unknown; restored from __doc__
        """ readInt64(self) -> int """
        return 0

    def readInt8(self): # real signature unknown; restored from __doc__
        """ readInt8(self) -> int """
        return 0

    def readQChar(self): # real signature unknown; restored from __doc__
        """ readQChar(self) -> str """
        return ""

    def readQString(self): # real signature unknown; restored from __doc__
        """ readQString(self) -> str """
        return ""

    def readQStringList(self): # real signature unknown; restored from __doc__
        """ readQStringList(self) -> typing.List[str] """
        pass

    def readQVariant(self): # real signature unknown; restored from __doc__
        """ readQVariant(self) -> typing.Any """
        pass

    def readRawData(self, arg__1, len): # real signature unknown; restored from __doc__
        """ readRawData(self, arg__1: bytes, len: int) -> int """
        return 0

    def readString(self): # real signature unknown; restored from __doc__
        """ readString(self) -> str """
        return ""

    def readUInt16(self): # real signature unknown; restored from __doc__
        """ readUInt16(self) -> int """
        return 0

    def readUInt32(self): # real signature unknown; restored from __doc__
        """ readUInt32(self) -> int """
        return 0

    def readUInt64(self): # real signature unknown; restored from __doc__
        """ readUInt64(self) -> int """
        return 0

    def readUInt8(self): # real signature unknown; restored from __doc__
        """ readUInt8(self) -> int """
        return 0

    def resetStatus(self): # real signature unknown; restored from __doc__
        """ resetStatus(self) -> None """
        pass

    def rollbackTransaction(self): # real signature unknown; restored from __doc__
        """ rollbackTransaction(self) -> None """
        pass

    def setByteOrder(self, arg__1): # real signature unknown; restored from __doc__
        """ setByteOrder(self, arg__1: PySide2.QtCore.QDataStream.ByteOrder) -> None """
        pass

    def setDevice(self, arg__1): # real signature unknown; restored from __doc__
        """ setDevice(self, arg__1: PySide2.QtCore.QIODevice) -> None """
        pass

    def setFloatingPointPrecision(self, precision): # real signature unknown; restored from __doc__
        """ setFloatingPointPrecision(self, precision: PySide2.QtCore.QDataStream.FloatingPointPrecision) -> None """
        pass

    def setStatus(self, status): # real signature unknown; restored from __doc__
        """ setStatus(self, status: PySide2.QtCore.QDataStream.Status) -> None """
        pass

    def setVersion(self, arg__1): # real signature unknown; restored from __doc__
        """ setVersion(self, arg__1: int) -> None """
        pass

    def skipRawData(self, len): # real signature unknown; restored from __doc__
        """ skipRawData(self, len: int) -> int """
        return 0

    def startTransaction(self): # real signature unknown; restored from __doc__
        """ startTransaction(self) -> None """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtCore.QDataStream.Status """
        pass

    def unsetDevice(self): # real signature unknown; restored from __doc__
        """ unsetDevice(self) -> None """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> int """
        return 0

    def writeBool(self, arg__1): # real signature unknown; restored from __doc__
        """ writeBool(self, arg__1: bool) -> None """
        pass

    def writeDouble(self, arg__1): # real signature unknown; restored from __doc__
        """ writeDouble(self, arg__1: float) -> None """
        pass

    def writeFloat(self, arg__1): # real signature unknown; restored from __doc__
        """ writeFloat(self, arg__1: float) -> None """
        pass

    def writeInt16(self, arg__1): # real signature unknown; restored from __doc__
        """ writeInt16(self, arg__1: int) -> None """
        pass

    def writeInt32(self, arg__1): # real signature unknown; restored from __doc__
        """ writeInt32(self, arg__1: int) -> None """
        pass

    def writeInt64(self, arg__1): # real signature unknown; restored from __doc__
        """ writeInt64(self, arg__1: int) -> None """
        pass

    def writeInt8(self, arg__1): # real signature unknown; restored from __doc__
        """ writeInt8(self, arg__1: int) -> None """
        pass

    def writeQChar(self, arg__1): # real signature unknown; restored from __doc__
        """ writeQChar(self, arg__1: str) -> None """
        pass

    def writeQString(self, arg__1): # real signature unknown; restored from __doc__
        """ writeQString(self, arg__1: str) -> None """
        pass

    def writeQStringList(self, arg__1, p_str=None): # real signature unknown; restored from __doc__
        """ writeQStringList(self, arg__1: typing.Sequence[str]) -> None """
        pass

    def writeQVariant(self, arg__1): # real signature unknown; restored from __doc__
        """ writeQVariant(self, arg__1: typing.Any) -> None """
        pass

    def writeRawData(self, arg__1, len): # real signature unknown; restored from __doc__
        """ writeRawData(self, arg__1: bytes, len: int) -> int """
        return 0

    def writeString(self, arg__1): # real signature unknown; restored from __doc__
        """ writeString(self, arg__1: str) -> None """
        pass

    def writeUInt16(self, arg__1): # real signature unknown; restored from __doc__
        """ writeUInt16(self, arg__1: int) -> None """
        pass

    def writeUInt32(self, arg__1): # real signature unknown; restored from __doc__
        """ writeUInt32(self, arg__1: int) -> None """
        pass

    def writeUInt64(self, arg__1): # real signature unknown; restored from __doc__
        """ writeUInt64(self, arg__1: int) -> None """
        pass

    def writeUInt8(self, arg__1): # real signature unknown; restored from __doc__
        """ writeUInt8(self, arg__1: int) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: str) -> None
        __lshift__(self, arg__2: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QCborArray) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QCborMap) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QCborValue) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QDate) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QDateTime) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QEasingCurve) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QJsonArray) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QJsonDocument) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QJsonValue) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QLine) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QLineF) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QLocale) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QMargins) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QPoint) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QPointF) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QRect) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QRectF) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QSize) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QSizeF) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QTime) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QUrl) -> PySide2.QtCore.QDataStream
        __lshift__(self, arg__2: PySide2.QtCore.QUuid) -> PySide2.QtCore.QDataStream
        __lshift__(self, re: PySide2.QtCore.QRegularExpression) -> PySide2.QtCore.QDataStream
        __lshift__(self, regExp: PySide2.QtCore.QRegExp) -> PySide2.QtCore.QDataStream
        __lshift__(self, tz: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDataStream
        __lshift__(self, version: PySide2.QtCore.QVersionNumber) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, arg__2): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__2: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QCborArray) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QCborMap) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QCborValue) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QDate) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QDateTime) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QEasingCurve) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QJsonArray) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QJsonDocument) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QJsonValue) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QLine) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QLineF) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QLocale) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QMargins) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QPoint) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QPointF) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QRect) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QRectF) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QSize) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QSizeF) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QTime) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QUrl) -> PySide2.QtCore.QDataStream
        __rshift__(self, arg__2: PySide2.QtCore.QUuid) -> PySide2.QtCore.QDataStream
        __rshift__(self, re: PySide2.QtCore.QRegularExpression) -> PySide2.QtCore.QDataStream
        __rshift__(self, regExp: PySide2.QtCore.QRegExp) -> PySide2.QtCore.QDataStream
        __rshift__(self, tz: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDataStream
        __rshift__(self, version: PySide2.QtCore.QVersionNumber) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    BigEndian = PySide2.QtCore.QDataStream.ByteOrder.BigEndian
    ByteOrder = None # (!) real value is "<class 'PySide2.QtCore.QDataStream.ByteOrder'>"
    DoublePrecision = PySide2.QtCore.QDataStream.FloatingPointPrecision.DoublePrecision
    FloatingPointPrecision = None # (!) real value is "<class 'PySide2.QtCore.QDataStream.FloatingPointPrecision'>"
    LittleEndian = PySide2.QtCore.QDataStream.ByteOrder.LittleEndian
    Ok = PySide2.QtCore.QDataStream.Status.Ok
    Qt_1_0 = PySide2.QtCore.QDataStream.Version.Qt_1_0
    Qt_2_0 = PySide2.QtCore.QDataStream.Version.Qt_2_0
    Qt_2_1 = PySide2.QtCore.QDataStream.Version.Qt_2_1
    Qt_3_0 = PySide2.QtCore.QDataStream.Version.Qt_3_0
    Qt_3_1 = PySide2.QtCore.QDataStream.Version.Qt_3_1
    Qt_3_3 = PySide2.QtCore.QDataStream.Version.Qt_3_3
    Qt_4_0 = PySide2.QtCore.QDataStream.Version.Qt_4_0
    Qt_4_1 = PySide2.QtCore.QDataStream.Version.Qt_4_1
    Qt_4_2 = PySide2.QtCore.QDataStream.Version.Qt_4_2
    Qt_4_3 = PySide2.QtCore.QDataStream.Version.Qt_4_3
    Qt_4_4 = PySide2.QtCore.QDataStream.Version.Qt_4_4
    Qt_4_5 = PySide2.QtCore.QDataStream.Version.Qt_4_5
    Qt_4_6 = PySide2.QtCore.QDataStream.Version.Qt_4_6
    Qt_4_7 = PySide2.QtCore.QDataStream.Version.Qt_4_7
    Qt_4_8 = PySide2.QtCore.QDataStream.Version.Qt_4_8
    Qt_4_9 = PySide2.QtCore.QDataStream.Version.Qt_4_9
    Qt_5_0 = PySide2.QtCore.QDataStream.Version.Qt_5_0
    Qt_5_1 = PySide2.QtCore.QDataStream.Version.Qt_5_1
    Qt_5_10 = PySide2.QtCore.QDataStream.Version.Qt_5_10
    Qt_5_11 = PySide2.QtCore.QDataStream.Version.Qt_5_11
    Qt_5_12 = PySide2.QtCore.QDataStream.Version.Qt_5_12
    Qt_5_13 = PySide2.QtCore.QDataStream.Version.Qt_5_13
    Qt_5_14 = PySide2.QtCore.QDataStream.Version.Qt_5_14
    Qt_5_15 = PySide2.QtCore.QDataStream.Version.Qt_5_15
    Qt_5_2 = PySide2.QtCore.QDataStream.Version.Qt_5_2
    Qt_5_3 = PySide2.QtCore.QDataStream.Version.Qt_5_3
    Qt_5_4 = PySide2.QtCore.QDataStream.Version.Qt_5_4
    Qt_5_5 = PySide2.QtCore.QDataStream.Version.Qt_5_5
    Qt_5_6 = PySide2.QtCore.QDataStream.Version.Qt_5_6
    Qt_5_7 = PySide2.QtCore.QDataStream.Version.Qt_5_7
    Qt_5_8 = PySide2.QtCore.QDataStream.Version.Qt_5_8
    Qt_5_9 = PySide2.QtCore.QDataStream.Version.Qt_5_9
    Qt_DefaultCompiledVersion = PySide2.QtCore.QDataStream.Version.Qt_DefaultCompiledVersion
    ReadCorruptData = PySide2.QtCore.QDataStream.Status.ReadCorruptData
    ReadPastEnd = PySide2.QtCore.QDataStream.Status.ReadPastEnd
    SinglePrecision = PySide2.QtCore.QDataStream.FloatingPointPrecision.SinglePrecision
    Status = None # (!) real value is "<class 'PySide2.QtCore.QDataStream.Status'>"
    Version = None # (!) real value is "<class 'PySide2.QtCore.QDataStream.Version'>"
    WriteFailed = PySide2.QtCore.QDataStream.Status.WriteFailed


