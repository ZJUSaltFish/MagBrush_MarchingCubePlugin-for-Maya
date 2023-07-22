# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QTextBoundaryFinder(__Shiboken.Object):
    """
    QTextBoundaryFinder(self) -> None
    QTextBoundaryFinder(self, other: PySide2.QtCore.QTextBoundaryFinder) -> None
    QTextBoundaryFinder(self, type: PySide2.QtCore.QTextBoundaryFinder.BoundaryType, string: str) -> None
    """
    def boundaryReasons(self): # real signature unknown; restored from __doc__
        """ boundaryReasons(self) -> PySide2.QtCore.QTextBoundaryFinder.BoundaryReasons """
        pass

    def isAtBoundary(self): # real signature unknown; restored from __doc__
        """ isAtBoundary(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def setPosition(self, position): # real signature unknown; restored from __doc__
        """ setPosition(self, position: int) -> None """
        pass

    def string(self): # real signature unknown; restored from __doc__
        """ string(self) -> str """
        return ""

    def toEnd(self): # real signature unknown; restored from __doc__
        """ toEnd(self) -> None """
        pass

    def toNextBoundary(self): # real signature unknown; restored from __doc__
        """ toNextBoundary(self) -> int """
        return 0

    def toPreviousBoundary(self): # real signature unknown; restored from __doc__
        """ toPreviousBoundary(self) -> int """
        return 0

    def toStart(self): # real signature unknown; restored from __doc__
        """ toStart(self) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.QTextBoundaryFinder.BoundaryType """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BoundaryReason = None # (!) real value is "<class 'PySide2.QtCore.QTextBoundaryFinder.BoundaryReason'>"
    BoundaryReasons = None # (!) real value is "<class 'PySide2.QtCore.QTextBoundaryFinder.BoundaryReasons'>"
    BoundaryType = None # (!) real value is "<class 'PySide2.QtCore.QTextBoundaryFinder.BoundaryType'>"
    BreakOpportunity = PySide2.QtCore.QTextBoundaryFinder.BoundaryReason.BreakOpportunity
    EndOfItem = PySide2.QtCore.QTextBoundaryFinder.BoundaryReason.EndOfItem
    Grapheme = PySide2.QtCore.QTextBoundaryFinder.BoundaryType.Grapheme
    Line = PySide2.QtCore.QTextBoundaryFinder.BoundaryType.Line
    MandatoryBreak = PySide2.QtCore.QTextBoundaryFinder.BoundaryReason.MandatoryBreak
    NotAtBoundary = PySide2.QtCore.QTextBoundaryFinder.BoundaryReason.NotAtBoundary
    Sentence = PySide2.QtCore.QTextBoundaryFinder.BoundaryType.Sentence
    SoftHyphen = PySide2.QtCore.QTextBoundaryFinder.BoundaryReason.SoftHyphen
    StartOfItem = PySide2.QtCore.QTextBoundaryFinder.BoundaryReason.StartOfItem
    Word = PySide2.QtCore.QTextBoundaryFinder.BoundaryType.Word


