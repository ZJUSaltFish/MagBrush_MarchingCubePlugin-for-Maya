# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QJsonValue(__Shiboken.Object):
    """
    QJsonValue(self, a: PySide2.QtCore.QJsonArray) -> None
    QJsonValue(self, arg__1: PySide2.QtCore.QJsonValue.Type = PySide2.QtCore.QJsonValue.Type.Null) -> None
    QJsonValue(self, b: bool) -> None
    QJsonValue(self, n: float) -> None
    QJsonValue(self, n: int) -> None
    QJsonValue(self, o: typing.Dict[str, PySide2.QtCore.QJsonValue]) -> None
    QJsonValue(self, other: PySide2.QtCore.QJsonValue) -> None
    QJsonValue(self, s: str) -> None
    QJsonValue(self, s: bytes) -> None
    QJsonValue(self, v: int) -> None
    """
    def fromVariant(self, variant): # real signature unknown; restored from __doc__
        """ fromVariant(variant: typing.Any) -> PySide2.QtCore.QJsonValue """
        pass

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isBool(self): # real signature unknown; restored from __doc__
        """ isBool(self) -> bool """
        return False

    def isDouble(self): # real signature unknown; restored from __doc__
        """ isDouble(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isObject(self): # real signature unknown; restored from __doc__
        """ isObject(self) -> bool """
        return False

    def isString(self): # real signature unknown; restored from __doc__
        """ isString(self) -> bool """
        return False

    def isUndefined(self): # real signature unknown; restored from __doc__
        """ isUndefined(self) -> bool """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QJsonValue) -> None """
        pass

    def toArray(self): # real signature unknown; restored from __doc__
        """
        toArray(self) -> PySide2.QtCore.QJsonArray
        toArray(self, defaultValue: PySide2.QtCore.QJsonArray) -> PySide2.QtCore.QJsonArray
        """
        pass

    def toBool(self, defaultValue=False): # real signature unknown; restored from __doc__
        """ toBool(self, defaultValue: bool = False) -> bool """
        return False

    def toDouble(self, defaultValue=0): # real signature unknown; restored from __doc__
        """ toDouble(self, defaultValue: float = 0) -> float """
        return 0.0

    def toInt(self, defaultValue=0): # real signature unknown; restored from __doc__
        """ toInt(self, defaultValue: int = 0) -> int """
        return 0

    def toObject(self): # real signature unknown; restored from __doc__
        """
        toObject(self) -> typing.Dict[str, PySide2.QtCore.QJsonValue]
        toObject(self, defaultValue: typing.Dict[str, PySide2.QtCore.QJsonValue]) -> typing.Dict[str, PySide2.QtCore.QJsonValue]
        """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """
        toString(self) -> str
        toString(self, defaultValue: str) -> str
        """
        return ""

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> typing.Any """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.QJsonValue.Type """
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

    def __init__(self, a): # real signature unknown; restored from __doc__
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

    Array = PySide2.QtCore.QJsonValue.Type.Array
    Bool = PySide2.QtCore.QJsonValue.Type.Bool
    Double = PySide2.QtCore.QJsonValue.Type.Double
    Null = PySide2.QtCore.QJsonValue.Type.Null
    Object = PySide2.QtCore.QJsonValue.Type.Object
    String = PySide2.QtCore.QJsonValue.Type.String
    Type = None # (!) real value is "<class 'PySide2.QtCore.QJsonValue.Type'>"
    Undefined = PySide2.QtCore.QJsonValue.Type.Undefined
    __hash__ = None


