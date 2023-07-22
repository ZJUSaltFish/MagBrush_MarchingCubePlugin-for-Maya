# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCborValue(__Shiboken.Object):
    """
    QCborValue(self) -> None
    QCborValue(self, a: PySide2.QtCore.QCborArray) -> None
    QCborValue(self, b_: bool) -> None
    QCborValue(self, ba: PySide2.QtCore.QByteArray) -> None
    QCborValue(self, dt: PySide2.QtCore.QDateTime) -> None
    QCborValue(self, i: int) -> None
    QCborValue(self, i: int) -> None
    QCborValue(self, m: PySide2.QtCore.QCborMap) -> None
    QCborValue(self, other: PySide2.QtCore.QCborValue) -> None
    QCborValue(self, rx: PySide2.QtCore.QRegularExpression) -> None
    QCborValue(self, s: str) -> None
    QCborValue(self, s: bytes) -> None
    QCborValue(self, st: PySide2.QtCore.QCborSimpleType) -> None
    QCborValue(self, t_: PySide2.QtCore.QCborKnownTags, tv: PySide2.QtCore.QCborValue = Default(QCborValue)) -> None
    QCborValue(self, t_: PySide2.QtCore.QCborValue.Type) -> None
    QCborValue(self, u: int) -> None
    QCborValue(self, url: PySide2.QtCore.QUrl) -> None
    QCborValue(self, uuid: PySide2.QtCore.QUuid) -> None
    QCborValue(self, v: float) -> None
    """
    def compare(self, other): # real signature unknown; restored from __doc__
        """ compare(self, other: PySide2.QtCore.QCborValue) -> int """
        return 0

    def fromCbor(self, ba, error, PySide2_QtCore_QCborParserError=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        fromCbor(ba: PySide2.QtCore.QByteArray, error: typing.Optional[PySide2.QtCore.QCborParserError] = None) -> PySide2.QtCore.QCborValue
        fromCbor(data: bytes, len: int, error: typing.Optional[PySide2.QtCore.QCborParserError] = None) -> PySide2.QtCore.QCborValue
        fromCbor(data: bytearray, len: int, error: typing.Optional[PySide2.QtCore.QCborParserError] = None) -> PySide2.QtCore.QCborValue
        fromCbor(reader: PySide2.QtCore.QCborStreamReader) -> PySide2.QtCore.QCborValue
        """
        pass

    def fromJsonValue(self, v): # real signature unknown; restored from __doc__
        """ fromJsonValue(v: PySide2.QtCore.QJsonValue) -> PySide2.QtCore.QCborValue """
        pass

    def fromVariant(self, variant): # real signature unknown; restored from __doc__
        """ fromVariant(variant: typing.Any) -> PySide2.QtCore.QCborValue """
        pass

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

    def isDateTime(self): # real signature unknown; restored from __doc__
        """ isDateTime(self) -> bool """
        return False

    def isDouble(self): # real signature unknown; restored from __doc__
        """ isDouble(self) -> bool """
        return False

    def isFalse(self): # real signature unknown; restored from __doc__
        """ isFalse(self) -> bool """
        return False

    def isInteger(self): # real signature unknown; restored from __doc__
        """ isInteger(self) -> bool """
        return False

    def isInvalid(self): # real signature unknown; restored from __doc__
        """ isInvalid(self) -> bool """
        return False

    def isMap(self): # real signature unknown; restored from __doc__
        """ isMap(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isRegularExpression(self): # real signature unknown; restored from __doc__
        """ isRegularExpression(self) -> bool """
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

    def isUrl(self): # real signature unknown; restored from __doc__
        """ isUrl(self) -> bool """
        return False

    def isUuid(self): # real signature unknown; restored from __doc__
        """ isUuid(self) -> bool """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QCborValue) -> None """
        pass

    def taggedValue(self, defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ taggedValue(self, defaultValue: PySide2.QtCore.QCborValue = Default(QCborValue)) -> PySide2.QtCore.QCborValue """
        pass

    def toArray(self): # real signature unknown; restored from __doc__
        """
        toArray(self) -> PySide2.QtCore.QCborArray
        toArray(self, defaultValue: PySide2.QtCore.QCborArray) -> PySide2.QtCore.QCborArray
        """
        pass

    def toBool(self, defaultValue=False): # real signature unknown; restored from __doc__
        """ toBool(self, defaultValue: bool = False) -> bool """
        return False

    def toByteArray(self, defaultValue={}): # real signature unknown; restored from __doc__
        """ toByteArray(self, defaultValue: PySide2.QtCore.QByteArray = {}) -> PySide2.QtCore.QByteArray """
        pass

    def toCbor(self, opt=None): # real signature unknown; restored from __doc__
        """
        toCbor(self, opt: PySide2.QtCore.QCborValue.EncodingOptions = PySide2.QtCore.QCborValue.EncodingOption.NoTransformation) -> PySide2.QtCore.QByteArray
        toCbor(self, writer: PySide2.QtCore.QCborStreamWriter, opt: PySide2.QtCore.QCborValue.EncodingOptions = PySide2.QtCore.QCborValue.EncodingOption.NoTransformation) -> None
        """
        pass

    def toDateTime(self, defaultValue={}): # real signature unknown; restored from __doc__
        """ toDateTime(self, defaultValue: PySide2.QtCore.QDateTime = {}) -> PySide2.QtCore.QDateTime """
        pass

    def toDiagnosticNotation(self, opts=None): # real signature unknown; restored from __doc__
        """ toDiagnosticNotation(self, opts: PySide2.QtCore.QCborValue.DiagnosticNotationOptions = PySide2.QtCore.QCborValue.DiagnosticNotationOption.Compact) -> str """
        return ""

    def toDouble(self, defaultValue=0): # real signature unknown; restored from __doc__
        """ toDouble(self, defaultValue: float = 0) -> float """
        return 0.0

    def toInteger(self, defaultValue=0): # real signature unknown; restored from __doc__
        """ toInteger(self, defaultValue: int = 0) -> int """
        return 0

    def toJsonValue(self): # real signature unknown; restored from __doc__
        """ toJsonValue(self) -> PySide2.QtCore.QJsonValue """
        pass

    def toMap(self): # real signature unknown; restored from __doc__
        """
        toMap(self) -> PySide2.QtCore.QCborMap
        toMap(self, defaultValue: PySide2.QtCore.QCborMap) -> PySide2.QtCore.QCborMap
        """
        pass

    def toRegularExpression(self, defaultValue={}): # real signature unknown; restored from __doc__
        """ toRegularExpression(self, defaultValue: PySide2.QtCore.QRegularExpression = {}) -> PySide2.QtCore.QRegularExpression """
        pass

    def toSimpleType(self, defaultValue=None): # real signature unknown; restored from __doc__
        """ toSimpleType(self, defaultValue: PySide2.QtCore.QCborSimpleType = PySide2.QtCore.QCborSimpleType.Undefined) -> PySide2.QtCore.QCborSimpleType """
        pass

    def toString(self, defaultValue={}): # real signature unknown; restored from __doc__
        """ toString(self, defaultValue: str = {}) -> str """
        return ""

    def toUrl(self, defaultValue={}): # real signature unknown; restored from __doc__
        """ toUrl(self, defaultValue: PySide2.QtCore.QUrl = {}) -> PySide2.QtCore.QUrl """
        pass

    def toUuid(self, defaultValue={}): # real signature unknown; restored from __doc__
        """ toUuid(self, defaultValue: PySide2.QtCore.QUuid = {}) -> PySide2.QtCore.QUuid """
        pass

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> typing.Any """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.QCborValue.Type """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Array = PySide2.QtCore.QCborValue.Type.Array
    ByteArray = PySide2.QtCore.QCborValue.Type.ByteArray
    Compact = PySide2.QtCore.QCborValue.DiagnosticNotationOption.Compact
    DateTime = PySide2.QtCore.QCborValue.Type.DateTime
    DiagnosticNotationOption = None # (!) real value is "<class 'PySide2.QtCore.QCborValue.DiagnosticNotationOption'>"
    DiagnosticNotationOptions = None # (!) real value is "<class 'PySide2.QtCore.QCborValue.DiagnosticNotationOptions'>"
    Double = PySide2.QtCore.QCborValue.Type.Double
    EncodingOption = None # (!) real value is "<class 'PySide2.QtCore.QCborValue.EncodingOption'>"
    EncodingOptions = None # (!) real value is "<class 'PySide2.QtCore.QCborValue.EncodingOptions'>"
    ExtendedFormat = PySide2.QtCore.QCborValue.DiagnosticNotationOption.ExtendedFormat
    False_ = PySide2.QtCore.QCborValue.Type.False_
    Integer = PySide2.QtCore.QCborValue.Type.Integer
    Invalid = PySide2.QtCore.QCborValue.Type.Invalid
    LineWrapped = PySide2.QtCore.QCborValue.DiagnosticNotationOption.LineWrapped
    Map = PySide2.QtCore.QCborValue.Type.Map
    NoTransformation = PySide2.QtCore.QCborValue.EncodingOption.NoTransformation
    Null = PySide2.QtCore.QCborValue.Type.Null
    RegularExpression = PySide2.QtCore.QCborValue.Type.RegularExpression
    SimpleType = PySide2.QtCore.QCborValue.Type.SimpleType
    SortKeysInMaps = PySide2.QtCore.QCborValue.EncodingOption.SortKeysInMaps
    String = PySide2.QtCore.QCborValue.Type.String
    Tag = PySide2.QtCore.QCborValue.Type.Tag
    True_ = PySide2.QtCore.QCborValue.Type.True_
    Type = None # (!) real value is "<class 'PySide2.QtCore.QCborValue.Type'>"
    Undefined = PySide2.QtCore.QCborValue.Type.Undefined
    Url = PySide2.QtCore.QCborValue.Type.Url
    UseFloat = PySide2.QtCore.QCborValue.EncodingOption.UseFloat
    UseFloat16 = PySide2.QtCore.QCborValue.EncodingOption.UseFloat16
    UseIntegers = PySide2.QtCore.QCborValue.EncodingOption.UseIntegers
    Uuid = PySide2.QtCore.QCborValue.Type.Uuid
    __hash__ = None


