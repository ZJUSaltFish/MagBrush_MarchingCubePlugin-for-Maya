# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QUuid(__Shiboken.Object):
    """
    QUuid(self) -> None
    QUuid(self, arg__1: PySide2.QtCore.QByteArray) -> None
    QUuid(self, arg__1: str) -> None
    QUuid(self, arg__1: bytes) -> None
    QUuid(self, l: int, w1: int, w2: int, b1: int, b2: int, b3: int, b4: int, b5: int, b6: int, b7: int, b8: int) -> None
    """
    def createUuid(self): # real signature unknown; restored from __doc__
        """ createUuid() -> PySide2.QtCore.QUuid """
        pass

    def createUuidV3(self, ns, baseData): # real signature unknown; restored from __doc__
        """
        createUuidV3(ns: PySide2.QtCore.QUuid, baseData: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QUuid
        createUuidV3(ns: PySide2.QtCore.QUuid, baseData: str) -> PySide2.QtCore.QUuid
        """
        pass

    def createUuidV5(self, ns, baseData): # real signature unknown; restored from __doc__
        """
        createUuidV5(ns: PySide2.QtCore.QUuid, baseData: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QUuid
        createUuidV5(ns: PySide2.QtCore.QUuid, baseData: str) -> PySide2.QtCore.QUuid
        """
        pass

    def fromRfc4122(self, arg__1): # real signature unknown; restored from __doc__
        """ fromRfc4122(arg__1: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QUuid """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toByteArray(self): # real signature unknown; restored from __doc__
        """
        toByteArray(self) -> PySide2.QtCore.QByteArray
        toByteArray(self, mode: PySide2.QtCore.QUuid.StringFormat) -> PySide2.QtCore.QByteArray
        """
        pass

    def toRfc4122(self): # real signature unknown; restored from __doc__
        """ toRfc4122(self) -> PySide2.QtCore.QByteArray """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """
        toString(self) -> str
        toString(self, mode: PySide2.QtCore.QUuid.StringFormat) -> str
        """
        return ""

    def variant(self): # real signature unknown; restored from __doc__
        """ variant(self) -> PySide2.QtCore.QUuid.Variant """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> PySide2.QtCore.QUuid.Version """
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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__(self) -> object """
        return object()

    def __repr__(self): # real signature unknown; restored from __doc__
        """
        __repr__(self) -> object
        
        Return repr(self).
        """
        return object()

    DCE = PySide2.QtCore.QUuid.Variant.DCE
    EmbeddedPOSIX = PySide2.QtCore.QUuid.Version.EmbeddedPOSIX
    Id128 = PySide2.QtCore.QUuid.StringFormat.Id128
    Md5 = PySide2.QtCore.QUuid.Version.Md5
    Microsoft = PySide2.QtCore.QUuid.Variant.Microsoft
    Name = PySide2.QtCore.QUuid.Version.Name
    NCS = PySide2.QtCore.QUuid.Variant.NCS
    Random = PySide2.QtCore.QUuid.Version.Random
    Reserved = PySide2.QtCore.QUuid.Variant.Reserved
    Sha1 = PySide2.QtCore.QUuid.Version.Sha1
    StringFormat = None # (!) real value is "<class 'PySide2.QtCore.QUuid.StringFormat'>"
    Time = PySide2.QtCore.QUuid.Version.Time
    Variant = None # (!) real value is "<class 'PySide2.QtCore.QUuid.Variant'>"
    VarUnknown = PySide2.QtCore.QUuid.Variant.VarUnknown
    Version = None # (!) real value is "<class 'PySide2.QtCore.QUuid.Version'>"
    VerUnknown = PySide2.QtCore.QUuid.Version.VerUnknown
    WithBraces = PySide2.QtCore.QUuid.StringFormat.WithBraces
    WithoutBraces = PySide2.QtCore.QUuid.StringFormat.WithoutBraces
    __hash__ = None


