# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QVersionNumber(__Shiboken.Object):
    """
    QVersionNumber(self) -> None
    QVersionNumber(self, maj: int) -> None
    QVersionNumber(self, maj: int, min: int) -> None
    QVersionNumber(self, maj: int, min: int, mic: int) -> None
    QVersionNumber(self, seg: typing.List[int]) -> None
    """
    def commonPrefix(self, v1, v2): # real signature unknown; restored from __doc__
        """ commonPrefix(v1: PySide2.QtCore.QVersionNumber, v2: PySide2.QtCore.QVersionNumber) -> PySide2.QtCore.QVersionNumber """
        pass

    def compare(self, v1, v2): # real signature unknown; restored from __doc__
        """ compare(v1: PySide2.QtCore.QVersionNumber, v2: PySide2.QtCore.QVersionNumber) -> int """
        return 0

    def fromString(self, string): # real signature unknown; restored from __doc__
        """ fromString(string: str) -> typing.Tuple[PySide2.QtCore.QVersionNumber, int] """
        pass

    def isNormalized(self): # real signature unknown; restored from __doc__
        """ isNormalized(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isPrefixOf(self, other): # real signature unknown; restored from __doc__
        """ isPrefixOf(self, other: PySide2.QtCore.QVersionNumber) -> bool """
        return False

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ majorVersion(self) -> int """
        return 0

    def microVersion(self): # real signature unknown; restored from __doc__
        """ microVersion(self) -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ minorVersion(self) -> int """
        return 0

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> PySide2.QtCore.QVersionNumber """
        pass

    def segmentAt(self, index): # real signature unknown; restored from __doc__
        """ segmentAt(self, index: int) -> int """
        return 0

    def segmentCount(self): # real signature unknown; restored from __doc__
        """ segmentCount(self) -> int """
        return 0

    def segments(self): # real signature unknown; restored from __doc__
        """ segments(self) -> typing.List[int] """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

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

    __hash__ = None


