# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QFont(__Shiboken.Object):
    """
    QFont(self) -> None
    QFont(self, family: str, pointSize: int = -1, weight: int = -1, italic: bool = False) -> None
    QFont(self, font: PySide2.QtGui.QFont) -> None
    QFont(self, font: PySide2.QtGui.QFont, pd: PySide2.QtGui.QPaintDevice) -> None
    """
    def bold(self): # real signature unknown; restored from __doc__
        """ bold(self) -> bool """
        return False

    def cacheStatistics(self): # real signature unknown; restored from __doc__
        """ cacheStatistics() -> None """
        pass

    def capitalization(self): # real signature unknown; restored from __doc__
        """ capitalization(self) -> PySide2.QtGui.QFont.Capitalization """
        pass

    def cleanup(self): # real signature unknown; restored from __doc__
        """ cleanup() -> None """
        pass

    def defaultFamily(self): # real signature unknown; restored from __doc__
        """ defaultFamily(self) -> str """
        return ""

    def exactMatch(self): # real signature unknown; restored from __doc__
        """ exactMatch(self) -> bool """
        return False

    def families(self): # real signature unknown; restored from __doc__
        """ families(self) -> typing.List[str] """
        pass

    def family(self): # real signature unknown; restored from __doc__
        """ family(self) -> str """
        return ""

    def fixedPitch(self): # real signature unknown; restored from __doc__
        """ fixedPitch(self) -> bool """
        return False

    def fromString(self, arg__1): # real signature unknown; restored from __doc__
        """ fromString(self, arg__1: str) -> bool """
        return False

    def hintingPreference(self): # real signature unknown; restored from __doc__
        """ hintingPreference(self) -> PySide2.QtGui.QFont.HintingPreference """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize() -> None """
        pass

    def insertSubstitution(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ insertSubstitution(arg__1: str, arg__2: str) -> None """
        pass

    def insertSubstitutions(self, arg__1, arg__2, p_str=None): # real signature unknown; restored from __doc__
        """ insertSubstitutions(arg__1: str, arg__2: typing.Sequence[str]) -> None """
        pass

    def isCopyOf(self, arg__1): # real signature unknown; restored from __doc__
        """ isCopyOf(self, arg__1: PySide2.QtGui.QFont) -> bool """
        return False

    def italic(self): # real signature unknown; restored from __doc__
        """ italic(self) -> bool """
        return False

    def kerning(self): # real signature unknown; restored from __doc__
        """ kerning(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def lastResortFamily(self): # real signature unknown; restored from __doc__
        """ lastResortFamily(self) -> str """
        return ""

    def lastResortFont(self): # real signature unknown; restored from __doc__
        """ lastResortFont(self) -> str """
        return ""

    def letterSpacing(self): # real signature unknown; restored from __doc__
        """ letterSpacing(self) -> float """
        return 0.0

    def letterSpacingType(self): # real signature unknown; restored from __doc__
        """ letterSpacingType(self) -> PySide2.QtGui.QFont.SpacingType """
        pass

    def overline(self): # real signature unknown; restored from __doc__
        """ overline(self) -> bool """
        return False

    def pixelSize(self): # real signature unknown; restored from __doc__
        """ pixelSize(self) -> int """
        return 0

    def pointSize(self): # real signature unknown; restored from __doc__
        """ pointSize(self) -> int """
        return 0

    def pointSizeF(self): # real signature unknown; restored from __doc__
        """ pointSizeF(self) -> float """
        return 0.0

    def rawMode(self): # real signature unknown; restored from __doc__
        """ rawMode(self) -> bool """
        return False

    def rawName(self): # real signature unknown; restored from __doc__
        """ rawName(self) -> str """
        return ""

    def removeSubstitutions(self, arg__1): # real signature unknown; restored from __doc__
        """ removeSubstitutions(arg__1: str) -> None """
        pass

    def resolve(self): # real signature unknown; restored from __doc__
        """
        resolve(self) -> int
        resolve(self, arg__1: PySide2.QtGui.QFont) -> PySide2.QtGui.QFont
        resolve(self, mask: int) -> None
        """
        return 0

    def setBold(self, arg__1): # real signature unknown; restored from __doc__
        """ setBold(self, arg__1: bool) -> None """
        pass

    def setCapitalization(self, arg__1): # real signature unknown; restored from __doc__
        """ setCapitalization(self, arg__1: PySide2.QtGui.QFont.Capitalization) -> None """
        pass

    def setFamilies(self, arg__1, p_str=None): # real signature unknown; restored from __doc__
        """ setFamilies(self, arg__1: typing.Sequence[str]) -> None """
        pass

    def setFamily(self, arg__1): # real signature unknown; restored from __doc__
        """ setFamily(self, arg__1: str) -> None """
        pass

    def setFixedPitch(self, arg__1): # real signature unknown; restored from __doc__
        """ setFixedPitch(self, arg__1: bool) -> None """
        pass

    def setHintingPreference(self, hintingPreference): # real signature unknown; restored from __doc__
        """ setHintingPreference(self, hintingPreference: PySide2.QtGui.QFont.HintingPreference) -> None """
        pass

    def setItalic(self, b): # real signature unknown; restored from __doc__
        """ setItalic(self, b: bool) -> None """
        pass

    def setKerning(self, arg__1): # real signature unknown; restored from __doc__
        """ setKerning(self, arg__1: bool) -> None """
        pass

    def setLetterSpacing(self, type, spacing): # real signature unknown; restored from __doc__
        """ setLetterSpacing(self, type: PySide2.QtGui.QFont.SpacingType, spacing: float) -> None """
        pass

    def setOverline(self, arg__1): # real signature unknown; restored from __doc__
        """ setOverline(self, arg__1: bool) -> None """
        pass

    def setPixelSize(self, arg__1): # real signature unknown; restored from __doc__
        """ setPixelSize(self, arg__1: int) -> None """
        pass

    def setPointSize(self, arg__1): # real signature unknown; restored from __doc__
        """ setPointSize(self, arg__1: int) -> None """
        pass

    def setPointSizeF(self, arg__1): # real signature unknown; restored from __doc__
        """ setPointSizeF(self, arg__1: float) -> None """
        pass

    def setRawMode(self, arg__1): # real signature unknown; restored from __doc__
        """ setRawMode(self, arg__1: bool) -> None """
        pass

    def setRawName(self, arg__1): # real signature unknown; restored from __doc__
        """ setRawName(self, arg__1: str) -> None """
        pass

    def setStretch(self, arg__1): # real signature unknown; restored from __doc__
        """ setStretch(self, arg__1: int) -> None """
        pass

    def setStrikeOut(self, arg__1): # real signature unknown; restored from __doc__
        """ setStrikeOut(self, arg__1: bool) -> None """
        pass

    def setStyle(self, style): # real signature unknown; restored from __doc__
        """ setStyle(self, style: PySide2.QtGui.QFont.Style) -> None """
        pass

    def setStyleHint(self, arg__1, strategy=None): # real signature unknown; restored from __doc__
        """ setStyleHint(self, arg__1: PySide2.QtGui.QFont.StyleHint, strategy: PySide2.QtGui.QFont.StyleStrategy = PySide2.QtGui.QFont.StyleStrategy.PreferDefault) -> None """
        pass

    def setStyleName(self, arg__1): # real signature unknown; restored from __doc__
        """ setStyleName(self, arg__1: str) -> None """
        pass

    def setStyleStrategy(self, s): # real signature unknown; restored from __doc__
        """ setStyleStrategy(self, s: PySide2.QtGui.QFont.StyleStrategy) -> None """
        pass

    def setUnderline(self, arg__1): # real signature unknown; restored from __doc__
        """ setUnderline(self, arg__1: bool) -> None """
        pass

    def setWeight(self, arg__1): # real signature unknown; restored from __doc__
        """ setWeight(self, arg__1: int) -> None """
        pass

    def setWordSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setWordSpacing(self, spacing: float) -> None """
        pass

    def stretch(self): # real signature unknown; restored from __doc__
        """ stretch(self) -> int """
        return 0

    def strikeOut(self): # real signature unknown; restored from __doc__
        """ strikeOut(self) -> bool """
        return False

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> PySide2.QtGui.QFont.Style """
        pass

    def styleHint(self): # real signature unknown; restored from __doc__
        """ styleHint(self) -> PySide2.QtGui.QFont.StyleHint """
        pass

    def styleName(self): # real signature unknown; restored from __doc__
        """ styleName(self) -> str """
        return ""

    def styleStrategy(self): # real signature unknown; restored from __doc__
        """ styleStrategy(self) -> PySide2.QtGui.QFont.StyleStrategy """
        pass

    def substitute(self, arg__1): # real signature unknown; restored from __doc__
        """ substitute(arg__1: str) -> str """
        return ""

    def substitutes(self, arg__1): # real signature unknown; restored from __doc__
        """ substitutes(arg__1: str) -> typing.List[str] """
        pass

    def substitutions(self): # real signature unknown; restored from __doc__
        """ substitutions() -> typing.List[str] """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QFont) -> None """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def underline(self): # real signature unknown; restored from __doc__
        """ underline(self) -> bool """
        return False

    def weight(self): # real signature unknown; restored from __doc__
        """ weight(self) -> int """
        return 0

    def wordSpacing(self): # real signature unknown; restored from __doc__
        """ wordSpacing(self) -> float """
        return 0.0

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

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    AbsoluteSpacing = PySide2.QtGui.QFont.SpacingType.AbsoluteSpacing
    AllLowercase = PySide2.QtGui.QFont.Capitalization.AllLowercase
    AllUppercase = PySide2.QtGui.QFont.Capitalization.AllUppercase
    AnyStretch = PySide2.QtGui.QFont.Stretch.AnyStretch
    AnyStyle = PySide2.QtGui.QFont.StyleHint.AnyStyle
    Black = PySide2.QtGui.QFont.Weight.Black
    Bold = PySide2.QtGui.QFont.Weight.Bold
    Capitalization = None # (!) real value is "<class 'PySide2.QtGui.QFont.Capitalization'>"
    Capitalize = PySide2.QtGui.QFont.Capitalization.Capitalize
    Condensed = PySide2.QtGui.QFont.Stretch.Condensed
    Courier = PySide2.QtGui.QFont.StyleHint.Courier
    Cursive = PySide2.QtGui.QFont.StyleHint.Cursive
    Decorative = PySide2.QtGui.QFont.StyleHint.Decorative
    DemiBold = PySide2.QtGui.QFont.Weight.DemiBold
    Expanded = PySide2.QtGui.QFont.Stretch.Expanded
    ExtraBold = PySide2.QtGui.QFont.Weight.ExtraBold
    ExtraCondensed = PySide2.QtGui.QFont.Stretch.ExtraCondensed
    ExtraExpanded = PySide2.QtGui.QFont.Stretch.ExtraExpanded
    ExtraLight = PySide2.QtGui.QFont.Weight.ExtraLight
    Fantasy = PySide2.QtGui.QFont.StyleHint.Fantasy
    ForceIntegerMetrics = PySide2.QtGui.QFont.StyleStrategy.ForceIntegerMetrics
    ForceOutline = PySide2.QtGui.QFont.StyleStrategy.ForceOutline
    Helvetica = PySide2.QtGui.QFont.StyleHint.Helvetica
    HintingPreference = None # (!) real value is "<class 'PySide2.QtGui.QFont.HintingPreference'>"
    Light = PySide2.QtGui.QFont.Weight.Light
    Medium = PySide2.QtGui.QFont.Weight.Medium
    MixedCase = PySide2.QtGui.QFont.Capitalization.MixedCase
    Monospace = PySide2.QtGui.QFont.StyleHint.Monospace
    NoAntialias = PySide2.QtGui.QFont.StyleStrategy.NoAntialias
    NoFontMerging = PySide2.QtGui.QFont.StyleStrategy.NoFontMerging
    Normal = PySide2.QtGui.QFont.Weight.Normal
    NoSubpixelAntialias = PySide2.QtGui.QFont.StyleStrategy.NoSubpixelAntialias
    OldEnglish = PySide2.QtGui.QFont.StyleHint.OldEnglish
    OpenGLCompatible = PySide2.QtGui.QFont.StyleStrategy.OpenGLCompatible
    PercentageSpacing = PySide2.QtGui.QFont.SpacingType.PercentageSpacing
    PreferAntialias = PySide2.QtGui.QFont.StyleStrategy.PreferAntialias
    PreferBitmap = PySide2.QtGui.QFont.StyleStrategy.PreferBitmap
    PreferDefault = PySide2.QtGui.QFont.StyleStrategy.PreferDefault
    PreferDefaultHinting = PySide2.QtGui.QFont.HintingPreference.PreferDefaultHinting
    PreferDevice = PySide2.QtGui.QFont.StyleStrategy.PreferDevice
    PreferFullHinting = PySide2.QtGui.QFont.HintingPreference.PreferFullHinting
    PreferMatch = PySide2.QtGui.QFont.StyleStrategy.PreferMatch
    PreferNoHinting = PySide2.QtGui.QFont.HintingPreference.PreferNoHinting
    PreferNoShaping = PySide2.QtGui.QFont.StyleStrategy.PreferNoShaping
    PreferOutline = PySide2.QtGui.QFont.StyleStrategy.PreferOutline
    PreferQuality = PySide2.QtGui.QFont.StyleStrategy.PreferQuality
    PreferVerticalHinting = PySide2.QtGui.QFont.HintingPreference.PreferVerticalHinting
    SansSerif = PySide2.QtGui.QFont.StyleHint.SansSerif
    SemiCondensed = PySide2.QtGui.QFont.Stretch.SemiCondensed
    SemiExpanded = PySide2.QtGui.QFont.Stretch.SemiExpanded
    Serif = PySide2.QtGui.QFont.StyleHint.Serif
    SmallCaps = PySide2.QtGui.QFont.Capitalization.SmallCaps
    SpacingType = None # (!) real value is "<class 'PySide2.QtGui.QFont.SpacingType'>"
    Stretch = None # (!) real value is "<class 'PySide2.QtGui.QFont.Stretch'>"
    Style = None # (!) real value is "<class 'PySide2.QtGui.QFont.Style'>"
    StyleHint = None # (!) real value is "<class 'PySide2.QtGui.QFont.StyleHint'>"
    StyleItalic = PySide2.QtGui.QFont.Style.StyleItalic
    StyleNormal = PySide2.QtGui.QFont.Style.StyleNormal
    StyleOblique = PySide2.QtGui.QFont.Style.StyleOblique
    StyleStrategy = None # (!) real value is "<class 'PySide2.QtGui.QFont.StyleStrategy'>"
    System = PySide2.QtGui.QFont.StyleHint.System
    Thin = PySide2.QtGui.QFont.Weight.Thin
    Times = PySide2.QtGui.QFont.StyleHint.Times
    TypeWriter = PySide2.QtGui.QFont.StyleHint.TypeWriter
    UltraCondensed = PySide2.QtGui.QFont.Stretch.UltraCondensed
    UltraExpanded = PySide2.QtGui.QFont.Stretch.UltraExpanded
    Unstretched = PySide2.QtGui.QFont.Stretch.Unstretched
    Weight = None # (!) real value is "<class 'PySide2.QtGui.QFont.Weight'>"
    __hash__ = None


