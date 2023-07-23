# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QItemSelection(__Shiboken.Object):
    """
    QItemSelection(self) -> None
    QItemSelection(self, QItemSelection: PySide2.QtCore.QItemSelection) -> None
    QItemSelection(self, topLeft: PySide2.QtCore.QModelIndex, bottomRight: PySide2.QtCore.QModelIndex) -> None
    """
    def append(self, t): # real signature unknown; restored from __doc__
        """
        append(self, t: PySide2.QtCore.QItemSelectionRange) -> None
        append(self, t: typing.Sequence[PySide2.QtCore.QItemSelectionRange]) -> None
        """
        pass

    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def back(self): # real signature unknown; restored from __doc__
        """ back(self) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def constFirst(self): # real signature unknown; restored from __doc__
        """ constFirst(self) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def constLast(self): # real signature unknown; restored from __doc__
        """ constLast(self) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def contains(self, index): # real signature unknown; restored from __doc__
        """ contains(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """
        count(self) -> int
        count(self, t: PySide2.QtCore.QItemSelectionRange) -> int
        """
        return 0

    def detachShared(self): # real signature unknown; restored from __doc__
        """ detachShared(self) -> None """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """ empty(self) -> bool """
        return False

    def endsWith(self, t): # real signature unknown; restored from __doc__
        """ endsWith(self, t: PySide2.QtCore.QItemSelectionRange) -> bool """
        return False

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def fromSet(self, set, PySide2_QtCore_QItemSelectionRange=None): # real signature unknown; restored from __doc__
        """ fromSet(set: typing.Set[PySide2.QtCore.QItemSelectionRange]) -> typing.List[PySide2.QtCore.QItemSelectionRange] """
        pass

    def fromVector(self, vector, PySide2_QtCore_QItemSelectionRange=None): # real signature unknown; restored from __doc__
        """ fromVector(vector: typing.List[PySide2.QtCore.QItemSelectionRange]) -> typing.List[PySide2.QtCore.QItemSelectionRange] """
        pass

    def front(self): # real signature unknown; restored from __doc__
        """ front(self) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def indexes(self): # real signature unknown; restored from __doc__
        """ indexes(self) -> typing.List[int] """
        pass

    def indexOf(self, t, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, t: PySide2.QtCore.QItemSelectionRange, from_: int = 0) -> int """
        return 0

    def insert(self, i, t): # real signature unknown; restored from __doc__
        """ insert(self, i: int, t: PySide2.QtCore.QItemSelectionRange) -> None """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSharedWith(self, other, PySide2_QtCore_QItemSelectionRange=None): # real signature unknown; restored from __doc__
        """ isSharedWith(self, other: typing.Sequence[PySide2.QtCore.QItemSelectionRange]) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def lastIndexOf(self, t, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, t: PySide2.QtCore.QItemSelectionRange, from_: int = -1) -> int """
        return 0

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def merge(self, other, command): # real signature unknown; restored from __doc__
        """ merge(self, other: PySide2.QtCore.QItemSelection, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None """
        pass

    def mid(self, pos, length=-1): # real signature unknown; restored from __doc__
        """ mid(self, pos: int, length: int = -1) -> typing.List[PySide2.QtCore.QItemSelectionRange] """
        pass

    def move(self, from_, to): # real signature unknown; restored from __doc__
        """ move(self, from_: int, to: int) -> None """
        pass

    def pop_back(self): # real signature unknown; restored from __doc__
        """ pop_back(self) -> None """
        pass

    def pop_front(self): # real signature unknown; restored from __doc__
        """ pop_front(self) -> None """
        pass

    def prepend(self, t): # real signature unknown; restored from __doc__
        """ prepend(self, t: PySide2.QtCore.QItemSelectionRange) -> None """
        pass

    def push_back(self, t): # real signature unknown; restored from __doc__
        """ push_back(self, t: PySide2.QtCore.QItemSelectionRange) -> None """
        pass

    def push_front(self, t): # real signature unknown; restored from __doc__
        """ push_front(self, t: PySide2.QtCore.QItemSelectionRange) -> None """
        pass

    def removeAll(self, t): # real signature unknown; restored from __doc__
        """ removeAll(self, t: PySide2.QtCore.QItemSelectionRange) -> int """
        return 0

    def removeAt(self, i): # real signature unknown; restored from __doc__
        """ removeAt(self, i: int) -> None """
        pass

    def removeFirst(self): # real signature unknown; restored from __doc__
        """ removeFirst(self) -> None """
        pass

    def removeLast(self): # real signature unknown; restored from __doc__
        """ removeLast(self) -> None """
        pass

    def removeOne(self, t): # real signature unknown; restored from __doc__
        """ removeOne(self, t: PySide2.QtCore.QItemSelectionRange) -> bool """
        return False

    def replace(self, i, t): # real signature unknown; restored from __doc__
        """ replace(self, i: int, t: PySide2.QtCore.QItemSelectionRange) -> None """
        pass

    def reserve(self, size): # real signature unknown; restored from __doc__
        """ reserve(self, size: int) -> None """
        pass

    def select(self, topLeft, bottomRight): # real signature unknown; restored from __doc__
        """ select(self, topLeft: PySide2.QtCore.QModelIndex, bottomRight: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setSharable(self, sharable): # real signature unknown; restored from __doc__
        """ setSharable(self, sharable: bool) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def split(self, range, other, result): # real signature unknown; restored from __doc__
        """ split(range: PySide2.QtCore.QItemSelectionRange, other: PySide2.QtCore.QItemSelectionRange, result: PySide2.QtCore.QItemSelection) -> None """
        pass

    def startsWith(self, t): # real signature unknown; restored from __doc__
        """ startsWith(self, t: PySide2.QtCore.QItemSelectionRange) -> bool """
        return False

    def swap(self, i, j): # real signature unknown; restored from __doc__
        """
        swap(self, i: int, j: int) -> None
        swap(self, other: typing.Sequence[PySide2.QtCore.QItemSelectionRange]) -> None
        """
        pass

    def swapItemsAt(self, i, j): # real signature unknown; restored from __doc__
        """ swapItemsAt(self, i: int, j: int) -> None """
        pass

    def takeAt(self, i): # real signature unknown; restored from __doc__
        """ takeAt(self, i: int) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def takeFirst(self): # real signature unknown; restored from __doc__
        """ takeFirst(self) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def takeLast(self): # real signature unknown; restored from __doc__
        """ takeLast(self) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def toSet(self): # real signature unknown; restored from __doc__
        """ toSet(self) -> typing.Set[PySide2.QtCore.QItemSelectionRange] """
        pass

    def toVector(self): # real signature unknown; restored from __doc__
        """ toVector(self) -> typing.List[PySide2.QtCore.QItemSelectionRange] """
        pass

    def value(self, i): # real signature unknown; restored from __doc__
        """
        value(self, i: int) -> PySide2.QtCore.QItemSelectionRange
        value(self, i: int, defaultValue: PySide2.QtCore.QItemSelectionRange) -> PySide2.QtCore.QItemSelectionRange
        """
        pass

    def __add__(self, l, PySide2_QtCore_QItemSelectionRange=None): # real signature unknown; restored from __doc__
        """
        __add__(self, l: typing.Sequence[PySide2.QtCore.QItemSelectionRange]) -> typing.List[PySide2.QtCore.QItemSelectionRange]
        
        Return self+value.
        """
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

    def __iadd__(self, l, PySide2_QtCore_QItemSelectionRange=None): # real signature unknown; restored from __doc__
        """
        __iadd__(self, l: typing.Sequence[PySide2.QtCore.QItemSelectionRange]) -> typing.List[PySide2.QtCore.QItemSelectionRange]
        __iadd__(self, t: PySide2.QtCore.QItemSelectionRange) -> typing.List[PySide2.QtCore.QItemSelectionRange]
        
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

    def __lshift__(self, l, PySide2_QtCore_QItemSelectionRange=None): # real signature unknown; restored from __doc__
        """
        __lshift__(self, l: typing.Sequence[PySide2.QtCore.QItemSelectionRange]) -> typing.List[PySide2.QtCore.QItemSelectionRange]
        __lshift__(self, t: PySide2.QtCore.QItemSelectionRange) -> typing.List[PySide2.QtCore.QItemSelectionRange]
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


