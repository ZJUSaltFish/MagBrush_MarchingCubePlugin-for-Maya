# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QJsonDocument(__Shiboken.Object):
    """
    QJsonDocument(self) -> None
    QJsonDocument(self, array: PySide2.QtCore.QJsonArray) -> None
    QJsonDocument(self, object: typing.Dict[str, PySide2.QtCore.QJsonValue]) -> None
    QJsonDocument(self, other: PySide2.QtCore.QJsonDocument) -> None
    """
    def array(self): # real signature unknown; restored from __doc__
        """ array(self) -> PySide2.QtCore.QJsonArray """
        pass

    def fromBinaryData(self, data, validation=None): # real signature unknown; restored from __doc__
        """ fromBinaryData(data: PySide2.QtCore.QByteArray, validation: PySide2.QtCore.QJsonDocument.DataValidation = PySide2.QtCore.QJsonDocument.DataValidation.Validate) -> PySide2.QtCore.QJsonDocument """
        pass

    def fromJson(self, json, error, PySide2_QtCore_QJsonParseError=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromJson(json: PySide2.QtCore.QByteArray, error: typing.Optional[PySide2.QtCore.QJsonParseError] = None) -> PySide2.QtCore.QJsonDocument """
        pass

    def fromRawData(self, data, size, validation=None): # real signature unknown; restored from __doc__
        """ fromRawData(data: bytes, size: int, validation: PySide2.QtCore.QJsonDocument.DataValidation = PySide2.QtCore.QJsonDocument.DataValidation.Validate) -> PySide2.QtCore.QJsonDocument """
        pass

    def fromVariant(self, variant): # real signature unknown; restored from __doc__
        """ fromVariant(variant: typing.Any) -> PySide2.QtCore.QJsonDocument """
        pass

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isObject(self): # real signature unknown; restored from __doc__
        """ isObject(self) -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> typing.Dict[str, PySide2.QtCore.QJsonValue] """
        pass

    def rawData(self): # real signature unknown; restored from __doc__
        """ rawData(self) -> typing.Tuple[bytes, int] """
        pass

    def setArray(self, array): # real signature unknown; restored from __doc__
        """ setArray(self, array: PySide2.QtCore.QJsonArray) -> None """
        pass

    def setObject(self, p_object, p_str=None, PySide2_QtCore_QJsonValue=None): # real signature unknown; restored from __doc__
        """ setObject(self, object: typing.Dict[str, PySide2.QtCore.QJsonValue]) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QJsonDocument) -> None """
        pass

    def toBinaryData(self): # real signature unknown; restored from __doc__
        """ toBinaryData(self) -> PySide2.QtCore.QByteArray """
        pass

    def toJson(self): # real signature unknown; restored from __doc__
        """
        toJson(self) -> PySide2.QtCore.QByteArray
        toJson(self, format: PySide2.QtCore.QJsonDocument.JsonFormat) -> PySide2.QtCore.QByteArray
        """
        pass

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> typing.Any """
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

    BypassValidation = PySide2.QtCore.QJsonDocument.DataValidation.BypassValidation
    Compact = PySide2.QtCore.QJsonDocument.JsonFormat.Compact
    DataValidation = None # (!) real value is "<class 'PySide2.QtCore.QJsonDocument.DataValidation'>"
    Indented = PySide2.QtCore.QJsonDocument.JsonFormat.Indented
    JsonFormat = None # (!) real value is "<class 'PySide2.QtCore.QJsonDocument.JsonFormat'>"
    Validate = PySide2.QtCore.QJsonDocument.DataValidation.Validate
    __hash__ = None


