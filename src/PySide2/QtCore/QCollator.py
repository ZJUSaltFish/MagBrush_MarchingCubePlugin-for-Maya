# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCollator(__Shiboken.Object):
    """
    QCollator(self) -> None
    QCollator(self, arg__1: PySide2.QtCore.QCollator) -> None
    QCollator(self, locale: PySide2.QtCore.QLocale) -> None
    """
    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ caseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity """
        pass

    def compare(self, s1, len1, s2, len2): # real signature unknown; restored from __doc__
        """
        compare(self, s1: bytes, len1: int, s2: bytes, len2: int) -> int
        compare(self, s1: str, s2: str) -> int
        compare(self, s1: str, s2: str) -> int
        """
        return 0

    def ignorePunctuation(self): # real signature unknown; restored from __doc__
        """ ignorePunctuation(self) -> bool """
        return False

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> PySide2.QtCore.QLocale """
        pass

    def numericMode(self): # real signature unknown; restored from __doc__
        """ numericMode(self) -> bool """
        return False

    def setCaseSensitivity(self, cs): # real signature unknown; restored from __doc__
        """ setCaseSensitivity(self, cs: PySide2.QtCore.Qt.CaseSensitivity) -> None """
        pass

    def setIgnorePunctuation(self, on): # real signature unknown; restored from __doc__
        """ setIgnorePunctuation(self, on: bool) -> None """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: PySide2.QtCore.QLocale) -> None """
        pass

    def setNumericMode(self, on): # real signature unknown; restored from __doc__
        """ setNumericMode(self, on: bool) -> None """
        pass

    def sortKey(self, string): # real signature unknown; restored from __doc__
        """ sortKey(self, string: str) -> PySide2.QtCore.QCollatorSortKey """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QCollator) -> None """
        pass

    def __call__(self, s1, s2): # real signature unknown; restored from __doc__
        """
        __call__(self, s1: str, s2: str) -> bool
        
        Call self as a function.
        """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


