# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QByteArray(__Shiboken.Object):
    """
    QByteArray(self) -> None
    QByteArray(self, arg__1: bytearray) -> None
    QByteArray(self, arg__1: bytes) -> None
    QByteArray(self, arg__1: PySide2.QtCore.QByteArray) -> None
    QByteArray(self, size: int, c: int) -> None
    """
    def append(self, a): # real signature unknown; restored from __doc__
        """
        append(self, a: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        append(self, c: int) -> PySide2.QtCore.QByteArray
        append(self, count: int, c: int) -> PySide2.QtCore.QByteArray
        """
        pass

    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> int """
        return 0

    def back(self): # real signature unknown; restored from __doc__
        """ back(self) -> int """
        return 0

    def capacity(self): # real signature unknown; restored from __doc__
        """ capacity(self) -> int """
        return 0

    def cbegin(self): # real signature unknown; restored from __doc__
        """ cbegin(self) -> bytes """
        return b""

    def cend(self): # real signature unknown; restored from __doc__
        """ cend(self) -> bytes """
        return b""

    def chop(self, n): # real signature unknown; restored from __doc__
        """ chop(self, n: int) -> None """
        pass

    def chopped(self, len): # real signature unknown; restored from __doc__
        """ chopped(self, len: int) -> PySide2.QtCore.QByteArray """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def compare(self, a, cs=None): # real signature unknown; restored from __doc__
        """
        compare(self, a: PySide2.QtCore.QByteArray, cs: PySide2.QtCore.Qt.CaseSensitivity = PySide2.QtCore.Qt.CaseSensitivity.CaseSensitive) -> int
        compare(self, c: bytes, cs: PySide2.QtCore.Qt.CaseSensitivity = PySide2.QtCore.Qt.CaseSensitivity.CaseSensitive) -> int
        """
        return 0

    def contains(self, a): # real signature unknown; restored from __doc__
        """
        contains(self, a: PySide2.QtCore.QByteArray) -> bool
        contains(self, c: int) -> bool
        """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """
        count(self) -> int
        count(self, a: PySide2.QtCore.QByteArray) -> int
        count(self, c: int) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> bytes """
        return b""

    def endsWith(self, a): # real signature unknown; restored from __doc__
        """
        endsWith(self, a: PySide2.QtCore.QByteArray) -> bool
        endsWith(self, c: int) -> bool
        """
        return False

    def fill(self, c, size=-1): # real signature unknown; restored from __doc__
        """ fill(self, c: int, size: int = -1) -> PySide2.QtCore.QByteArray """
        pass

    def fromBase64(self, base64): # real signature unknown; restored from __doc__
        """
        fromBase64(base64: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        fromBase64(base64: PySide2.QtCore.QByteArray, options: PySide2.QtCore.QByteArray.Base64Options) -> PySide2.QtCore.QByteArray
        """
        pass

    def fromBase64Encoding(self, base64, options=None): # real signature unknown; restored from __doc__
        """ fromBase64Encoding(base64: PySide2.QtCore.QByteArray, options: PySide2.QtCore.QByteArray.Base64Options = PySide2.QtCore.QByteArray.Base64Option.Base64Encoding) -> PySide2.QtCore.QByteArray.FromBase64Result """
        pass

    def fromHex(self, hexEncoded): # real signature unknown; restored from __doc__
        """ fromHex(hexEncoded: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray """
        pass

    def fromPercentEncoding(self, pctEncoded, percent='%'): # real signature unknown; restored from __doc__
        """ fromPercentEncoding(pctEncoded: PySide2.QtCore.QByteArray, percent: int = '%') -> PySide2.QtCore.QByteArray """
        pass

    def fromRawData(self, arg__1, size): # real signature unknown; restored from __doc__
        """ fromRawData(arg__1: bytes, size: int) -> PySide2.QtCore.QByteArray """
        pass

    def front(self): # real signature unknown; restored from __doc__
        """ front(self) -> int """
        return 0

    def indexOf(self, a, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, a: PySide2.QtCore.QByteArray, from_: int = 0) -> int """
        return 0

    def insert(self, i, a): # real signature unknown; restored from __doc__
        """
        insert(self, i: int, a: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        insert(self, i: int, count: int, c: int) -> PySide2.QtCore.QByteArray
        """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isLower(self): # real signature unknown; restored from __doc__
        """ isLower(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isSharedWith(self, other): # real signature unknown; restored from __doc__
        """ isSharedWith(self, other: PySide2.QtCore.QByteArray) -> bool """
        return False

    def isUpper(self): # real signature unknown; restored from __doc__
        """ isUpper(self) -> bool """
        return False

    def lastIndexOf(self, a, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, a: PySide2.QtCore.QByteArray, from_: int = -1) -> int """
        return 0

    def left(self, len): # real signature unknown; restored from __doc__
        """ left(self, len: int) -> PySide2.QtCore.QByteArray """
        pass

    def leftJustified(self, width, fill=' ', truncate=False): # real signature unknown; restored from __doc__
        """ leftJustified(self, width: int, fill: int = ' ', truncate: bool = False) -> PySide2.QtCore.QByteArray """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def mid(self, index, len=-1): # real signature unknown; restored from __doc__
        """ mid(self, index: int, len: int = -1) -> PySide2.QtCore.QByteArray """
        pass

    def number(self, arg__1, f='g', prec=6): # real signature unknown; restored from __doc__
        """
        number(arg__1: float, f: int = 'g', prec: int = 6) -> PySide2.QtCore.QByteArray
        number(arg__1: int, base: int = 10) -> PySide2.QtCore.QByteArray
        number(arg__1: int, base: int = 10) -> PySide2.QtCore.QByteArray
        """
        pass

    def prepend(self, a): # real signature unknown; restored from __doc__
        """
        prepend(self, a: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        prepend(self, c: int) -> PySide2.QtCore.QByteArray
        prepend(self, count: int, c: int) -> PySide2.QtCore.QByteArray
        """
        pass

    def remove(self, index, len): # real signature unknown; restored from __doc__
        """ remove(self, index: int, len: int) -> PySide2.QtCore.QByteArray """
        pass

    def repeated(self, times): # real signature unknown; restored from __doc__
        """ repeated(self, times: int) -> PySide2.QtCore.QByteArray """
        pass

    def replace(self, before, after): # real signature unknown; restored from __doc__
        """
        replace(self, before: PySide2.QtCore.QByteArray, after: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        replace(self, before: str, after: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        replace(self, before: int, after: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        replace(self, before: int, after: int) -> PySide2.QtCore.QByteArray
        replace(self, index: int, len: int, s: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        """
        pass

    def reserve(self, size): # real signature unknown; restored from __doc__
        """ reserve(self, size: int) -> None """
        pass

    def resize(self, size): # real signature unknown; restored from __doc__
        """ resize(self, size: int) -> None """
        pass

    def right(self, len): # real signature unknown; restored from __doc__
        """ right(self, len: int) -> PySide2.QtCore.QByteArray """
        pass

    def rightJustified(self, width, fill=' ', truncate=False): # real signature unknown; restored from __doc__
        """ rightJustified(self, width: int, fill: int = ' ', truncate: bool = False) -> PySide2.QtCore.QByteArray """
        pass

    def setNum(self, arg__1, f='g', prec=6): # real signature unknown; restored from __doc__
        """
        setNum(self, arg__1: float, f: int = 'g', prec: int = 6) -> PySide2.QtCore.QByteArray
        setNum(self, arg__1: int, base: int = 10) -> PySide2.QtCore.QByteArray
        setNum(self, arg__1: int, base: int = 10) -> PySide2.QtCore.QByteArray
        """
        pass

    def setRawData(self, a, n): # real signature unknown; restored from __doc__
        """ setRawData(self, a: bytes, n: int) -> PySide2.QtCore.QByteArray """
        pass

    def shrink_to_fit(self): # real signature unknown; restored from __doc__
        """ shrink_to_fit(self) -> None """
        pass

    def simplified(self): # real signature unknown; restored from __doc__
        """ simplified(self) -> PySide2.QtCore.QByteArray """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def split(self, sep): # real signature unknown; restored from __doc__
        """ split(self, sep: int) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def squeeze(self): # real signature unknown; restored from __doc__
        """ squeeze(self) -> None """
        pass

    def startsWith(self, a): # real signature unknown; restored from __doc__
        """
        startsWith(self, a: PySide2.QtCore.QByteArray) -> bool
        startsWith(self, c: int) -> bool
        """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QByteArray) -> None """
        pass

    def toBase64(self): # real signature unknown; restored from __doc__
        """
        toBase64(self) -> PySide2.QtCore.QByteArray
        toBase64(self, options: PySide2.QtCore.QByteArray.Base64Options) -> PySide2.QtCore.QByteArray
        """
        pass

    def toDouble(self): # real signature unknown; restored from __doc__
        """ toDouble(self) -> typing.Tuple[float, bool] """
        pass

    def toFloat(self): # real signature unknown; restored from __doc__
        """ toFloat(self) -> typing.Tuple[float, bool] """
        pass

    def toHex(self): # real signature unknown; restored from __doc__
        """
        toHex(self) -> PySide2.QtCore.QByteArray
        toHex(self, separator: int) -> PySide2.QtCore.QByteArray
        """
        pass

    def toInt(self, base=10): # real signature unknown; restored from __doc__
        """ toInt(self, base: int = 10) -> typing.Tuple[int, bool] """
        pass

    def toLong(self, base=10): # real signature unknown; restored from __doc__
        """ toLong(self, base: int = 10) -> typing.Tuple[int, bool] """
        pass

    def toLongLong(self, base=10): # real signature unknown; restored from __doc__
        """ toLongLong(self, base: int = 10) -> typing.Tuple[int, bool] """
        pass

    def toLower(self): # real signature unknown; restored from __doc__
        """ toLower(self) -> PySide2.QtCore.QByteArray """
        pass

    def toPercentEncoding(self, exclude=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toPercentEncoding(self, exclude: PySide2.QtCore.QByteArray = Default(QByteArray), include: PySide2.QtCore.QByteArray = Default(QByteArray), percent: int = '%') -> PySide2.QtCore.QByteArray """
        pass

    def toShort(self, base=10): # real signature unknown; restored from __doc__
        """ toShort(self, base: int = 10) -> typing.Tuple[int, bool] """
        pass

    def toUInt(self, base=10): # real signature unknown; restored from __doc__
        """ toUInt(self, base: int = 10) -> typing.Tuple[int, bool] """
        pass

    def toULong(self, base=10): # real signature unknown; restored from __doc__
        """ toULong(self, base: int = 10) -> typing.Tuple[int, bool] """
        pass

    def toULongLong(self, base=10): # real signature unknown; restored from __doc__
        """ toULongLong(self, base: int = 10) -> typing.Tuple[int, bool] """
        pass

    def toUpper(self): # real signature unknown; restored from __doc__
        """ toUpper(self) -> PySide2.QtCore.QByteArray """
        pass

    def toUShort(self, base=10): # real signature unknown; restored from __doc__
        """ toUShort(self, base: int = 10) -> typing.Tuple[int, bool] """
        pass

    def trimmed(self): # real signature unknown; restored from __doc__
        """ trimmed(self) -> PySide2.QtCore.QByteArray """
        pass

    def truncate(self, pos): # real signature unknown; restored from __doc__
        """ truncate(self, pos: int) -> None """
        pass

    def __add__(self, a2): # real signature unknown; restored from __doc__
        """
        __add__(self, a2: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        __add__(self, a2: int) -> PySide2.QtCore.QByteArray
        __add__(self, arg__1: bytearray) -> PySide2.QtCore.QByteArray
        __add__(self, arg__1: bytes) -> None
        
        Return self+value.
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, a): # real signature unknown; restored from __doc__
        """
        __iadd__(self, a: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        __iadd__(self, arg__1: bytearray) -> PySide2.QtCore.QByteArray
        __iadd__(self, c: int) -> PySide2.QtCore.QByteArray
        
        Return self+=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__(self) -> object """
        return object()

    def __repr__(self): # real signature unknown; restored from __doc__
        """
        __repr__(self) -> object
        
        Return repr(self).
        """
        return object()

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """
        __str__(self) -> object
        
        Return str(self).
        """
        return object()

    AbortOnBase64DecodingErrors = PySide2.QtCore.QByteArray.Base64Option.AbortOnBase64DecodingErrors
    Base64DecodingStatus = None # (!) real value is "<class 'PySide2.QtCore.QByteArray.Base64DecodingStatus'>"
    Base64Encoding = PySide2.QtCore.QByteArray.Base64Option.Base64Encoding
    Base64Option = None # (!) real value is "<class 'PySide2.QtCore.QByteArray.Base64Option'>"
    Base64Options = None # (!) real value is "<class 'PySide2.QtCore.QByteArray.Base64Options'>"
    Base64UrlEncoding = PySide2.QtCore.QByteArray.Base64Option.Base64UrlEncoding
    FromBase64Result = None # (!) real value is "<class 'PySide2.QtCore.QByteArray.FromBase64Result'>"
    IgnoreBase64DecodingErrors = PySide2.QtCore.QByteArray.Base64Option.IgnoreBase64DecodingErrors
    KeepTrailingEquals = PySide2.QtCore.QByteArray.Base64Option.KeepTrailingEquals
    OmitTrailingEquals = PySide2.QtCore.QByteArray.Base64Option.OmitTrailingEquals


