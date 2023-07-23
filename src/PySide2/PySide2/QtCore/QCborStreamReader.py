# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCborStreamReader(__Shiboken.Object):
    """
    QCborStreamReader(self) -> None
    QCborStreamReader(self, data: PySide2.QtCore.QByteArray) -> None
    QCborStreamReader(self, data: bytes, len: int) -> None
    QCborStreamReader(self, data: bytearray, len: int) -> None
    QCborStreamReader(self, device: PySide2.QtCore.QIODevice) -> None
    """
    def addData(self, data): # real signature unknown; restored from __doc__
        """
        addData(self, data: PySide2.QtCore.QByteArray) -> None
        addData(self, data: bytes, len: int) -> None
        addData(self, data: bytearray, len: int) -> None
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def containerDepth(self): # real signature unknown; restored from __doc__
        """ containerDepth(self) -> int """
        return 0

    def currentOffset(self): # real signature unknown; restored from __doc__
        """ currentOffset(self) -> int """
        return 0

    def currentStringChunkSize(self): # real signature unknown; restored from __doc__
        """ currentStringChunkSize(self) -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def enterContainer(self): # real signature unknown; restored from __doc__
        """ enterContainer(self) -> bool """
        return False

    def hasNext(self): # real signature unknown; restored from __doc__
        """ hasNext(self) -> bool """
        return False

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isBool(self): # real signature unknown; restored from __doc__
        """ isBool(self) -> bool """
        return False

    def isByteArray(self): # real signature unknown; restored from __doc__
        """ isByteArray(self) -> bool """
        return False

    def isContainer(self): # real signature unknown; restored from __doc__
        """ isContainer(self) -> bool """
        return False

    def isDouble(self): # real signature unknown; restored from __doc__
        """ isDouble(self) -> bool """
        return False

    def isFalse(self): # real signature unknown; restored from __doc__
        """ isFalse(self) -> bool """
        return False

    def isFloat(self): # real signature unknown; restored from __doc__
        """ isFloat(self) -> bool """
        return False

    def isFloat16(self): # real signature unknown; restored from __doc__
        """ isFloat16(self) -> bool """
        return False

    def isInteger(self): # real signature unknown; restored from __doc__
        """ isInteger(self) -> bool """
        return False

    def isInvalid(self): # real signature unknown; restored from __doc__
        """ isInvalid(self) -> bool """
        return False

    def isLengthKnown(self): # real signature unknown; restored from __doc__
        """ isLengthKnown(self) -> bool """
        return False

    def isMap(self): # real signature unknown; restored from __doc__
        """ isMap(self) -> bool """
        return False

    def isNegativeInteger(self): # real signature unknown; restored from __doc__
        """ isNegativeInteger(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isSimpleType(self): # real signature unknown; restored from __doc__
        """
        isSimpleType(self) -> bool
        isSimpleType(self, st: PySide2.QtCore.QCborSimpleType) -> bool
        """
        return False

    def isString(self): # real signature unknown; restored from __doc__
        """ isString(self) -> bool """
        return False

    def isTag(self): # real signature unknown; restored from __doc__
        """ isTag(self) -> bool """
        return False

    def isTrue(self): # real signature unknown; restored from __doc__
        """ isTrue(self) -> bool """
        return False

    def isUndefined(self): # real signature unknown; restored from __doc__
        """ isUndefined(self) -> bool """
        return False

    def isUnsignedInteger(self): # real signature unknown; restored from __doc__
        """ isUnsignedInteger(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> PySide2.QtCore.QCborError """
        pass

    def leaveContainer(self): # real signature unknown; restored from __doc__
        """ leaveContainer(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def next(self, maxRecursion=10000): # real signature unknown; restored from __doc__
        """ next(self, maxRecursion: int = 10000) -> bool """
        return False

    def parentContainerType(self): # real signature unknown; restored from __doc__
        """ parentContainerType(self) -> PySide2.QtCore.QCborStreamReader.Type """
        pass

    def readByteArray(self): # real signature unknown; restored from __doc__
        """ readByteArray(self) -> PySide2.QtCore.QCborStringResultByteArray """
        pass

    def readString(self): # real signature unknown; restored from __doc__
        """ readString(self) -> PySide2.QtCore.QCborStringResultString """
        pass

    def reparse(self): # real signature unknown; restored from __doc__
        """ reparse(self) -> None """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def setDevice(self, device): # real signature unknown; restored from __doc__
        """ setDevice(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def toBool(self): # real signature unknown; restored from __doc__
        """ toBool(self) -> bool """
        return False

    def toDouble(self): # real signature unknown; restored from __doc__
        """ toDouble(self) -> float """
        return 0.0

    def toFloat(self): # real signature unknown; restored from __doc__
        """ toFloat(self) -> float """
        return 0.0

    def toInteger(self): # real signature unknown; restored from __doc__
        """ toInteger(self) -> int """
        return 0

    def toSimpleType(self): # real signature unknown; restored from __doc__
        """ toSimpleType(self) -> PySide2.QtCore.QCborSimpleType """
        pass

    def toUnsignedInteger(self): # real signature unknown; restored from __doc__
        """ toUnsignedInteger(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.QCborStreamReader.Type """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Array = PySide2.QtCore.QCborStreamReader.Type.Array
    ByteArray = PySide2.QtCore.QCborStreamReader.Type.ByteArray
    ByteString = PySide2.QtCore.QCborStreamReader.Type.ByteString
    Double = PySide2.QtCore.QCborStreamReader.Type.Double
    EndOfString = PySide2.QtCore.QCborStreamReader.StringResultCode.EndOfString
    Error = PySide2.QtCore.QCborStreamReader.StringResultCode.Error
    Float = PySide2.QtCore.QCborStreamReader.Type.Float
    Float16 = PySide2.QtCore.QCborStreamReader.Type.Float16
    HalfFloat = PySide2.QtCore.QCborStreamReader.Type.HalfFloat
    Invalid = PySide2.QtCore.QCborStreamReader.Type.Invalid
    Map = PySide2.QtCore.QCborStreamReader.Type.Map
    NegativeInteger = PySide2.QtCore.QCborStreamReader.Type.NegativeInteger
    Ok = PySide2.QtCore.QCborStreamReader.StringResultCode.Ok
    SimpleType = PySide2.QtCore.QCborStreamReader.Type.SimpleType
    String = PySide2.QtCore.QCborStreamReader.Type.String
    StringResultCode = None # (!) real value is "<class 'PySide2.QtCore.QCborStreamReader.StringResultCode'>"
    Tag = PySide2.QtCore.QCborStreamReader.Type.Tag
    TextString = PySide2.QtCore.QCborStreamReader.Type.TextString
    Type = None # (!) real value is "<class 'PySide2.QtCore.QCborStreamReader.Type'>"
    UnsignedInteger = PySide2.QtCore.QCborStreamReader.Type.UnsignedInteger


