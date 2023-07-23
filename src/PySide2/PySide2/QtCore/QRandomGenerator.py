# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QRandomGenerator(__Shiboken.Object):
    """
    QRandomGenerator(self, begin: int, end: int) -> None
    QRandomGenerator(self, other: PySide2.QtCore.QRandomGenerator) -> None
    QRandomGenerator(self, seedBuffer: int, len: int) -> None
    QRandomGenerator(self, seedValue: int = 1) -> None
    """
    def bounded(self, highest): # real signature unknown; restored from __doc__
        """
        bounded(self, highest: float) -> float
        bounded(self, highest: int) -> int
        bounded(self, highest: int) -> int
        bounded(self, lowest: int, highest: int) -> int
        bounded(self, lowest: int, highest: int) -> int
        """
        return 0.0

    def discard(self, z): # real signature unknown; restored from __doc__
        """ discard(self, z: int) -> None """
        pass

    def generate(self): # real signature unknown; restored from __doc__
        """ generate(self) -> int """
        return 0

    def generate64(self): # real signature unknown; restored from __doc__
        """ generate64(self) -> int """
        return 0

    def generateDouble(self): # real signature unknown; restored from __doc__
        """ generateDouble(self) -> float """
        return 0.0

    def global_(self): # real signature unknown; restored from __doc__
        """ global_() -> PySide2.QtCore.QRandomGenerator """
        pass

    def max(self): # real signature unknown; restored from __doc__
        """ max() -> int """
        return 0

    def min(self): # real signature unknown; restored from __doc__
        """ min() -> int """
        return 0

    def securelySeeded(self): # real signature unknown; restored from __doc__
        """ securelySeeded() -> PySide2.QtCore.QRandomGenerator """
        pass

    def seed(self, s=1): # real signature unknown; restored from __doc__
        """ seed(self, s: int = 1) -> None """
        pass

    def system(self): # real signature unknown; restored from __doc__
        """ system() -> PySide2.QtCore.QRandomGenerator """
        pass

    def __init__(self, begin, end): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


