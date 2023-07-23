# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QRegExp(__Shiboken.Object):
    """
    QRegExp(self) -> None
    QRegExp(self, pattern: str, cs: PySide2.QtCore.Qt.CaseSensitivity = PySide2.QtCore.Qt.CaseSensitivity.CaseSensitive, syntax: PySide2.QtCore.QRegExp.PatternSyntax = PySide2.QtCore.QRegExp.PatternSyntax.RegExp) -> None
    QRegExp(self, rx: PySide2.QtCore.QRegExp) -> None
    """
    def cap(self, nth=0): # real signature unknown; restored from __doc__
        """ cap(self, nth: int = 0) -> str """
        return ""

    def captureCount(self): # real signature unknown; restored from __doc__
        """ captureCount(self) -> int """
        return 0

    def capturedTexts(self): # real signature unknown; restored from __doc__
        """ capturedTexts(self) -> typing.List[str] """
        pass

    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ caseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def escape(self, p_str): # real signature unknown; restored from __doc__
        """ escape(str: str) -> str """
        return ""

    def exactMatch(self, p_str): # real signature unknown; restored from __doc__
        """ exactMatch(self, str: str) -> bool """
        return False

    def indexIn(self, p_str, offset=0, caretMode=None): # real signature unknown; restored from __doc__
        """ indexIn(self, str: str, offset: int = 0, caretMode: PySide2.QtCore.QRegExp.CaretMode = PySide2.QtCore.QRegExp.CaretMode.CaretAtZero) -> int """
        return 0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isMinimal(self): # real signature unknown; restored from __doc__
        """ isMinimal(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastIndexIn(self, p_str, offset=-1, caretMode=None): # real signature unknown; restored from __doc__
        """ lastIndexIn(self, str: str, offset: int = -1, caretMode: PySide2.QtCore.QRegExp.CaretMode = PySide2.QtCore.QRegExp.CaretMode.CaretAtZero) -> int """
        return 0

    def matchedLength(self): # real signature unknown; restored from __doc__
        """ matchedLength(self) -> int """
        return 0

    def pattern(self): # real signature unknown; restored from __doc__
        """ pattern(self) -> str """
        return ""

    def patternSyntax(self): # real signature unknown; restored from __doc__
        """ patternSyntax(self) -> PySide2.QtCore.QRegExp.PatternSyntax """
        pass

    def pos(self, nth=0): # real signature unknown; restored from __doc__
        """ pos(self, nth: int = 0) -> int """
        return 0

    def replace(self, sourceString, after): # real signature unknown; restored from __doc__
        """ replace(self, sourceString: str, after: str) -> str """
        return ""

    def setCaseSensitivity(self, cs): # real signature unknown; restored from __doc__
        """ setCaseSensitivity(self, cs: PySide2.QtCore.Qt.CaseSensitivity) -> None """
        pass

    def setMinimal(self, minimal): # real signature unknown; restored from __doc__
        """ setMinimal(self, minimal: bool) -> None """
        pass

    def setPattern(self, pattern): # real signature unknown; restored from __doc__
        """ setPattern(self, pattern: str) -> None """
        pass

    def setPatternSyntax(self, syntax): # real signature unknown; restored from __doc__
        """ setPatternSyntax(self, syntax: PySide2.QtCore.QRegExp.PatternSyntax) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QRegExp) -> None """
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

    CaretAtOffset = PySide2.QtCore.QRegExp.CaretMode.CaretAtOffset
    CaretAtZero = PySide2.QtCore.QRegExp.CaretMode.CaretAtZero
    CaretMode = None # (!) real value is "<class 'PySide2.QtCore.QRegExp.CaretMode'>"
    CaretWontMatch = PySide2.QtCore.QRegExp.CaretMode.CaretWontMatch
    FixedString = PySide2.QtCore.QRegExp.PatternSyntax.FixedString
    PatternSyntax = None # (!) real value is "<class 'PySide2.QtCore.QRegExp.PatternSyntax'>"
    RegExp = PySide2.QtCore.QRegExp.PatternSyntax.RegExp
    RegExp2 = PySide2.QtCore.QRegExp.PatternSyntax.RegExp2
    W3CXmlSchema11 = PySide2.QtCore.QRegExp.PatternSyntax.W3CXmlSchema11
    Wildcard = PySide2.QtCore.QRegExp.PatternSyntax.Wildcard
    WildcardUnix = PySide2.QtCore.QRegExp.PatternSyntax.WildcardUnix
    __hash__ = None


