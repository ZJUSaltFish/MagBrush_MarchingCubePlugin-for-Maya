# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QItemSelectionRange(__Shiboken.Object):
    """
    QItemSelectionRange(self) -> None
    QItemSelectionRange(self, index: PySide2.QtCore.QModelIndex) -> None
    QItemSelectionRange(self, other: PySide2.QtCore.QItemSelectionRange) -> None
    QItemSelectionRange(self, topL: PySide2.QtCore.QModelIndex, bottomR: PySide2.QtCore.QModelIndex) -> None
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> PySide2.QtCore.QPersistentModelIndex """
        pass

    def contains(self, index): # real signature unknown; restored from __doc__
        """
        contains(self, index: PySide2.QtCore.QModelIndex) -> bool
        contains(self, row: int, column: int, parentIndex: PySide2.QtCore.QModelIndex) -> bool
        """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def indexes(self): # real signature unknown; restored from __doc__
        """ indexes(self) -> typing.List[int] """
        pass

    def intersected(self, other): # real signature unknown; restored from __doc__
        """ intersected(self, other: PySide2.QtCore.QItemSelectionRange) -> PySide2.QtCore.QItemSelectionRange """
        pass

    def intersects(self, other): # real signature unknown; restored from __doc__
        """ intersects(self, other: PySide2.QtCore.QItemSelectionRange) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def left(self): # real signature unknown; restored from __doc__
        """ left(self) -> int """
        return 0

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> PySide2.QtCore.QAbstractItemModel """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> PySide2.QtCore.QModelIndex """
        pass

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QItemSelectionRange) -> None """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> PySide2.QtCore.QPersistentModelIndex """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

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


