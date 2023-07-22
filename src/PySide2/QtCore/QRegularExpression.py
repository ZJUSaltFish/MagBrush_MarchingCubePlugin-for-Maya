# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QRegularExpression(__Shiboken.Object):
    """
    QRegularExpression(self) -> None
    QRegularExpression(self, pattern: str, options: PySide2.QtCore.QRegularExpression.PatternOptions = PySide2.QtCore.QRegularExpression.PatternOption.NoPatternOption) -> None
    QRegularExpression(self, re: PySide2.QtCore.QRegularExpression) -> None
    """
    def anchoredPattern(self, expression): # real signature unknown; restored from __doc__
        """ anchoredPattern(expression: str) -> str """
        return ""

    def captureCount(self): # real signature unknown; restored from __doc__
        """ captureCount(self) -> int """
        return 0

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def escape(self, p_str): # real signature unknown; restored from __doc__
        """ escape(str: str) -> str """
        return ""

    def globalMatch(self, subject, offset=0, matchType=None, matchOptions=None): # real signature unknown; restored from __doc__
        """
        globalMatch(self, subject: str, offset: int = 0, matchType: PySide2.QtCore.QRegularExpression.MatchType = PySide2.QtCore.QRegularExpression.MatchType.NormalMatch, matchOptions: PySide2.QtCore.QRegularExpression.MatchOptions = PySide2.QtCore.QRegularExpression.MatchOption.NoMatchOption) -> PySide2.QtCore.QRegularExpressionMatchIterator
        globalMatch(self, subjectRef: str, offset: int = 0, matchType: PySide2.QtCore.QRegularExpression.MatchType = PySide2.QtCore.QRegularExpression.MatchType.NormalMatch, matchOptions: PySide2.QtCore.QRegularExpression.MatchOptions = PySide2.QtCore.QRegularExpression.MatchOption.NoMatchOption) -> PySide2.QtCore.QRegularExpressionMatchIterator
        """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def match(self, subject, offset=0, matchType=None, matchOptions=None): # real signature unknown; restored from __doc__
        """
        match(self, subject: str, offset: int = 0, matchType: PySide2.QtCore.QRegularExpression.MatchType = PySide2.QtCore.QRegularExpression.MatchType.NormalMatch, matchOptions: PySide2.QtCore.QRegularExpression.MatchOptions = PySide2.QtCore.QRegularExpression.MatchOption.NoMatchOption) -> PySide2.QtCore.QRegularExpressionMatch
        match(self, subjectRef: str, offset: int = 0, matchType: PySide2.QtCore.QRegularExpression.MatchType = PySide2.QtCore.QRegularExpression.MatchType.NormalMatch, matchOptions: PySide2.QtCore.QRegularExpression.MatchOptions = PySide2.QtCore.QRegularExpression.MatchOption.NoMatchOption) -> PySide2.QtCore.QRegularExpressionMatch
        """
        pass

    def namedCaptureGroups(self): # real signature unknown; restored from __doc__
        """ namedCaptureGroups(self) -> typing.List[str] """
        pass

    def optimize(self): # real signature unknown; restored from __doc__
        """ optimize(self) -> None """
        pass

    def pattern(self): # real signature unknown; restored from __doc__
        """ pattern(self) -> str """
        return ""

    def patternErrorOffset(self): # real signature unknown; restored from __doc__
        """ patternErrorOffset(self) -> int """
        return 0

    def patternOptions(self): # real signature unknown; restored from __doc__
        """ patternOptions(self) -> PySide2.QtCore.QRegularExpression.PatternOptions """
        pass

    def setPattern(self, pattern): # real signature unknown; restored from __doc__
        """ setPattern(self, pattern: str) -> None """
        pass

    def setPatternOptions(self, options): # real signature unknown; restored from __doc__
        """ setPatternOptions(self, options: PySide2.QtCore.QRegularExpression.PatternOptions) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QRegularExpression) -> None """
        pass

    def wildcardToRegularExpression(self, p_str): # real signature unknown; restored from __doc__
        """ wildcardToRegularExpression(str: str) -> str """
        return ""

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

    AnchoredMatchOption = PySide2.QtCore.QRegularExpression.MatchOption.AnchoredMatchOption
    CaseInsensitiveOption = PySide2.QtCore.QRegularExpression.PatternOption.CaseInsensitiveOption
    DontAutomaticallyOptimizeOption = PySide2.QtCore.QRegularExpression.PatternOption.DontAutomaticallyOptimizeOption
    DontCaptureOption = PySide2.QtCore.QRegularExpression.PatternOption.DontCaptureOption
    DontCheckSubjectStringMatchOption = PySide2.QtCore.QRegularExpression.MatchOption.DontCheckSubjectStringMatchOption
    DotMatchesEverythingOption = PySide2.QtCore.QRegularExpression.PatternOption.DotMatchesEverythingOption
    ExtendedPatternSyntaxOption = PySide2.QtCore.QRegularExpression.PatternOption.ExtendedPatternSyntaxOption
    InvertedGreedinessOption = PySide2.QtCore.QRegularExpression.PatternOption.InvertedGreedinessOption
    MatchOption = None # (!) real value is "<class 'PySide2.QtCore.QRegularExpression.MatchOption'>"
    MatchOptions = None # (!) real value is "<class 'PySide2.QtCore.QRegularExpression.MatchOptions'>"
    MatchType = None # (!) real value is "<class 'PySide2.QtCore.QRegularExpression.MatchType'>"
    MultilineOption = PySide2.QtCore.QRegularExpression.PatternOption.MultilineOption
    NoMatch = PySide2.QtCore.QRegularExpression.MatchType.NoMatch
    NoMatchOption = PySide2.QtCore.QRegularExpression.MatchOption.NoMatchOption
    NoPatternOption = PySide2.QtCore.QRegularExpression.PatternOption.NoPatternOption
    NormalMatch = PySide2.QtCore.QRegularExpression.MatchType.NormalMatch
    OptimizeOnFirstUsageOption = PySide2.QtCore.QRegularExpression.PatternOption.OptimizeOnFirstUsageOption
    PartialPreferCompleteMatch = PySide2.QtCore.QRegularExpression.MatchType.PartialPreferCompleteMatch
    PartialPreferFirstMatch = PySide2.QtCore.QRegularExpression.MatchType.PartialPreferFirstMatch
    PatternOption = None # (!) real value is "<class 'PySide2.QtCore.QRegularExpression.PatternOption'>"
    PatternOptions = None # (!) real value is "<class 'PySide2.QtCore.QRegularExpression.PatternOptions'>"
    UseUnicodePropertiesOption = PySide2.QtCore.QRegularExpression.PatternOption.UseUnicodePropertiesOption
    __hash__ = None


