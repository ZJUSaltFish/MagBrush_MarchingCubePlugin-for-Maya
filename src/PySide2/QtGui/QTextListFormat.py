# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QTextFormat import QTextFormat

class QTextListFormat(QTextFormat):
    """
    QTextListFormat(self) -> None
    QTextListFormat(self, QTextListFormat: PySide2.QtGui.QTextListFormat) -> None
    QTextListFormat(self, fmt: PySide2.QtGui.QTextFormat) -> None
    """
    def indent(self): # real signature unknown; restored from __doc__
        """ indent(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def numberPrefix(self): # real signature unknown; restored from __doc__
        """ numberPrefix(self) -> str """
        return ""

    def numberSuffix(self): # real signature unknown; restored from __doc__
        """ numberSuffix(self) -> str """
        return ""

    def setIndent(self, indent): # real signature unknown; restored from __doc__
        """ setIndent(self, indent: int) -> None """
        pass

    def setNumberPrefix(self, numberPrefix): # real signature unknown; restored from __doc__
        """ setNumberPrefix(self, numberPrefix: str) -> None """
        pass

    def setNumberSuffix(self, numberSuffix): # real signature unknown; restored from __doc__
        """ setNumberSuffix(self, numberSuffix: str) -> None """
        pass

    def setStyle(self, style): # real signature unknown; restored from __doc__
        """ setStyle(self, style: PySide2.QtGui.QTextListFormat.Style) -> None """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> PySide2.QtGui.QTextListFormat.Style """
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

    ListCircle = PySide2.QtGui.QTextListFormat.Style.ListCircle
    ListDecimal = PySide2.QtGui.QTextListFormat.Style.ListDecimal
    ListDisc = PySide2.QtGui.QTextListFormat.Style.ListDisc
    ListLowerAlpha = PySide2.QtGui.QTextListFormat.Style.ListLowerAlpha
    ListLowerRoman = PySide2.QtGui.QTextListFormat.Style.ListLowerRoman
    ListSquare = PySide2.QtGui.QTextListFormat.Style.ListSquare
    ListStyleUndefined = PySide2.QtGui.QTextListFormat.Style.ListStyleUndefined
    ListUpperAlpha = PySide2.QtGui.QTextListFormat.Style.ListUpperAlpha
    ListUpperRoman = PySide2.QtGui.QTextListFormat.Style.ListUpperRoman
    Style = None # (!) real value is "<class 'PySide2.QtGui.QTextListFormat.Style'>"


