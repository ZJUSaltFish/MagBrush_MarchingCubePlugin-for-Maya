# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QBitArray(__Shiboken.Object):
    """
    QBitArray(self) -> None
    QBitArray(self, other: PySide2.QtCore.QBitArray) -> None
    QBitArray(self, size: int, val: bool = False) -> None
    """
    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> bool """
        return False

    def bits(self): # real signature unknown; restored from __doc__
        """ bits(self) -> bytes """
        return b""

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearBit(self, i): # real signature unknown; restored from __doc__
        """ clearBit(self, i: int) -> None """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """
        count(self) -> int
        count(self, on: bool) -> int
        """
        return 0

    def fill(self, val, first, last): # real signature unknown; restored from __doc__
        """
        fill(self, val: bool, first: int, last: int) -> None
        fill(self, val: bool, size: int = -1) -> bool
        """
        pass

    def fromBits(self, data, len): # real signature unknown; restored from __doc__
        """ fromBits(data: bytes, len: int) -> PySide2.QtCore.QBitArray """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def resize(self, size): # real signature unknown; restored from __doc__
        """ resize(self, size: int) -> None """
        pass

    def setBit(self, i): # real signature unknown; restored from __doc__
        """
        setBit(self, i: int) -> None
        setBit(self, i: int, val: bool) -> None
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QBitArray) -> None """
        pass

    def testBit(self, i): # real signature unknown; restored from __doc__
        """ testBit(self, i: int) -> bool """
        return False

    def toggleBit(self, i): # real signature unknown; restored from __doc__
        """ toggleBit(self, i: int) -> bool """
        return False

    def truncate(self, pos): # real signature unknown; restored from __doc__
        """ truncate(self, pos: int) -> None """
        pass

    def __and__(self, arg__2): # real signature unknown; restored from __doc__
        """
        __and__(self, arg__2: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray
        
        Return self&value.
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

    def __iand__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __iand__(self, arg__1: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray
        
        Return self&=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __invert__(self): # real signature unknown; restored from __doc__
        """
        __invert__(self) -> PySide2.QtCore.QBitArray
        
        ~self
        """
        pass

    def __ior__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __ior__(self, arg__1: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray
        
        Return self|=value.
        """
        pass

    def __ixor__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __ixor__(self, arg__1: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray
        
        Return self^=value.
        """
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

    def __or__(self, arg__2): # real signature unknown; restored from __doc__
        """
        __or__(self, arg__2: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray
        
        Return self|value.
        """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __xor__(self, arg__2): # real signature unknown; restored from __doc__
        """
        __xor__(self, arg__2: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray
        
        Return self^value.
        """
        pass


