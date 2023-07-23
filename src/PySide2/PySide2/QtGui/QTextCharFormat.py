# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QTextFormat import QTextFormat

class QTextCharFormat(QTextFormat):
    """
    QTextCharFormat(self) -> None
    QTextCharFormat(self, QTextCharFormat: PySide2.QtGui.QTextCharFormat) -> None
    QTextCharFormat(self, fmt: PySide2.QtGui.QTextFormat) -> None
    """
    def anchorHref(self): # real signature unknown; restored from __doc__
        """ anchorHref(self) -> str """
        return ""

    def anchorName(self): # real signature unknown; restored from __doc__
        """ anchorName(self) -> str """
        return ""

    def anchorNames(self): # real signature unknown; restored from __doc__
        """ anchorNames(self) -> typing.List[str] """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def fontCapitalization(self): # real signature unknown; restored from __doc__
        """ fontCapitalization(self) -> PySide2.QtGui.QFont.Capitalization """
        pass

    def fontFamilies(self): # real signature unknown; restored from __doc__
        """ fontFamilies(self) -> typing.Any """
        pass

    def fontFamily(self): # real signature unknown; restored from __doc__
        """ fontFamily(self) -> str """
        return ""

    def fontFixedPitch(self): # real signature unknown; restored from __doc__
        """ fontFixedPitch(self) -> bool """
        return False

    def fontHintingPreference(self): # real signature unknown; restored from __doc__
        """ fontHintingPreference(self) -> PySide2.QtGui.QFont.HintingPreference """
        pass

    def fontItalic(self): # real signature unknown; restored from __doc__
        """ fontItalic(self) -> bool """
        return False

    def fontKerning(self): # real signature unknown; restored from __doc__
        """ fontKerning(self) -> bool """
        return False

    def fontLetterSpacing(self): # real signature unknown; restored from __doc__
        """ fontLetterSpacing(self) -> float """
        return 0.0

    def fontLetterSpacingType(self): # real signature unknown; restored from __doc__
        """ fontLetterSpacingType(self) -> PySide2.QtGui.QFont.SpacingType """
        pass

    def fontOverline(self): # real signature unknown; restored from __doc__
        """ fontOverline(self) -> bool """
        return False

    def fontPointSize(self): # real signature unknown; restored from __doc__
        """ fontPointSize(self) -> float """
        return 0.0

    def fontStretch(self): # real signature unknown; restored from __doc__
        """ fontStretch(self) -> int """
        return 0

    def fontStrikeOut(self): # real signature unknown; restored from __doc__
        """ fontStrikeOut(self) -> bool """
        return False

    def fontStyleHint(self): # real signature unknown; restored from __doc__
        """ fontStyleHint(self) -> PySide2.QtGui.QFont.StyleHint """
        pass

    def fontStyleName(self): # real signature unknown; restored from __doc__
        """ fontStyleName(self) -> typing.Any """
        pass

    def fontStyleStrategy(self): # real signature unknown; restored from __doc__
        """ fontStyleStrategy(self) -> PySide2.QtGui.QFont.StyleStrategy """
        pass

    def fontUnderline(self): # real signature unknown; restored from __doc__
        """ fontUnderline(self) -> bool """
        return False

    def fontWeight(self): # real signature unknown; restored from __doc__
        """ fontWeight(self) -> int """
        return 0

    def fontWordSpacing(self): # real signature unknown; restored from __doc__
        """ fontWordSpacing(self) -> float """
        return 0.0

    def isAnchor(self): # real signature unknown; restored from __doc__
        """ isAnchor(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def setAnchor(self, anchor): # real signature unknown; restored from __doc__
        """ setAnchor(self, anchor: bool) -> None """
        pass

    def setAnchorHref(self, value): # real signature unknown; restored from __doc__
        """ setAnchorHref(self, value: str) -> None """
        pass

    def setAnchorName(self, name): # real signature unknown; restored from __doc__
        """ setAnchorName(self, name: str) -> None """
        pass

    def setAnchorNames(self, names, p_str=None): # real signature unknown; restored from __doc__
        """ setAnchorNames(self, names: typing.Sequence[str]) -> None """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """
        setFont(self, font: PySide2.QtGui.QFont) -> None
        setFont(self, font: PySide2.QtGui.QFont, behavior: PySide2.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior) -> None
        """
        pass

    def setFontCapitalization(self, capitalization): # real signature unknown; restored from __doc__
        """ setFontCapitalization(self, capitalization: PySide2.QtGui.QFont.Capitalization) -> None """
        pass

    def setFontFamilies(self, families, p_str=None): # real signature unknown; restored from __doc__
        """ setFontFamilies(self, families: typing.Sequence[str]) -> None """
        pass

    def setFontFamily(self, family): # real signature unknown; restored from __doc__
        """ setFontFamily(self, family: str) -> None """
        pass

    def setFontFixedPitch(self, fixedPitch): # real signature unknown; restored from __doc__
        """ setFontFixedPitch(self, fixedPitch: bool) -> None """
        pass

    def setFontHintingPreference(self, hintingPreference): # real signature unknown; restored from __doc__
        """ setFontHintingPreference(self, hintingPreference: PySide2.QtGui.QFont.HintingPreference) -> None """
        pass

    def setFontItalic(self, italic): # real signature unknown; restored from __doc__
        """ setFontItalic(self, italic: bool) -> None """
        pass

    def setFontKerning(self, enable): # real signature unknown; restored from __doc__
        """ setFontKerning(self, enable: bool) -> None """
        pass

    def setFontLetterSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setFontLetterSpacing(self, spacing: float) -> None """
        pass

    def setFontLetterSpacingType(self, letterSpacingType): # real signature unknown; restored from __doc__
        """ setFontLetterSpacingType(self, letterSpacingType: PySide2.QtGui.QFont.SpacingType) -> None """
        pass

    def setFontOverline(self, overline): # real signature unknown; restored from __doc__
        """ setFontOverline(self, overline: bool) -> None """
        pass

    def setFontPointSize(self, size): # real signature unknown; restored from __doc__
        """ setFontPointSize(self, size: float) -> None """
        pass

    def setFontStretch(self, factor): # real signature unknown; restored from __doc__
        """ setFontStretch(self, factor: int) -> None """
        pass

    def setFontStrikeOut(self, strikeOut): # real signature unknown; restored from __doc__
        """ setFontStrikeOut(self, strikeOut: bool) -> None """
        pass

    def setFontStyleHint(self, hint, strategy=None): # real signature unknown; restored from __doc__
        """ setFontStyleHint(self, hint: PySide2.QtGui.QFont.StyleHint, strategy: PySide2.QtGui.QFont.StyleStrategy = PySide2.QtGui.QFont.StyleStrategy.PreferDefault) -> None """
        pass

    def setFontStyleName(self, styleName): # real signature unknown; restored from __doc__
        """ setFontStyleName(self, styleName: str) -> None """
        pass

    def setFontStyleStrategy(self, strategy): # real signature unknown; restored from __doc__
        """ setFontStyleStrategy(self, strategy: PySide2.QtGui.QFont.StyleStrategy) -> None """
        pass

    def setFontUnderline(self, underline): # real signature unknown; restored from __doc__
        """ setFontUnderline(self, underline: bool) -> None """
        pass

    def setFontWeight(self, weight): # real signature unknown; restored from __doc__
        """ setFontWeight(self, weight: int) -> None """
        pass

    def setFontWordSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setFontWordSpacing(self, spacing: float) -> None """
        pass

    def setTableCellColumnSpan(self, tableCellColumnSpan): # real signature unknown; restored from __doc__
        """ setTableCellColumnSpan(self, tableCellColumnSpan: int) -> None """
        pass

    def setTableCellRowSpan(self, tableCellRowSpan): # real signature unknown; restored from __doc__
        """ setTableCellRowSpan(self, tableCellRowSpan: int) -> None """
        pass

    def setTextOutline(self, pen): # real signature unknown; restored from __doc__
        """ setTextOutline(self, pen: PySide2.QtGui.QPen) -> None """
        pass

    def setToolTip(self, tip): # real signature unknown; restored from __doc__
        """ setToolTip(self, tip: str) -> None """
        pass

    def setUnderlineColor(self, color): # real signature unknown; restored from __doc__
        """ setUnderlineColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setUnderlineStyle(self, style): # real signature unknown; restored from __doc__
        """ setUnderlineStyle(self, style: PySide2.QtGui.QTextCharFormat.UnderlineStyle) -> None """
        pass

    def setVerticalAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setVerticalAlignment(self, alignment: PySide2.QtGui.QTextCharFormat.VerticalAlignment) -> None """
        pass

    def tableCellColumnSpan(self): # real signature unknown; restored from __doc__
        """ tableCellColumnSpan(self) -> int """
        return 0

    def tableCellRowSpan(self): # real signature unknown; restored from __doc__
        """ tableCellRowSpan(self) -> int """
        return 0

    def textOutline(self): # real signature unknown; restored from __doc__
        """ textOutline(self) -> PySide2.QtGui.QPen """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def underlineColor(self): # real signature unknown; restored from __doc__
        """ underlineColor(self) -> PySide2.QtGui.QColor """
        pass

    def underlineStyle(self): # real signature unknown; restored from __doc__
        """ underlineStyle(self) -> PySide2.QtGui.QTextCharFormat.UnderlineStyle """
        pass

    def verticalAlignment(self): # real signature unknown; restored from __doc__
        """ verticalAlignment(self) -> PySide2.QtGui.QTextCharFormat.VerticalAlignment """
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

    AlignBaseline = PySide2.QtGui.QTextCharFormat.VerticalAlignment.AlignBaseline
    AlignBottom = PySide2.QtGui.QTextCharFormat.VerticalAlignment.AlignBottom
    AlignMiddle = PySide2.QtGui.QTextCharFormat.VerticalAlignment.AlignMiddle
    AlignNormal = PySide2.QtGui.QTextCharFormat.VerticalAlignment.AlignNormal
    AlignSubScript = PySide2.QtGui.QTextCharFormat.VerticalAlignment.AlignSubScript
    AlignSuperScript = PySide2.QtGui.QTextCharFormat.VerticalAlignment.AlignSuperScript
    AlignTop = PySide2.QtGui.QTextCharFormat.VerticalAlignment.AlignTop
    DashDotDotLine = PySide2.QtGui.QTextCharFormat.UnderlineStyle.DashDotDotLine
    DashDotLine = PySide2.QtGui.QTextCharFormat.UnderlineStyle.DashDotLine
    DashUnderline = PySide2.QtGui.QTextCharFormat.UnderlineStyle.DashUnderline
    DotLine = PySide2.QtGui.QTextCharFormat.UnderlineStyle.DotLine
    FontPropertiesAll = PySide2.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior.FontPropertiesAll
    FontPropertiesInheritanceBehavior = None # (!) real value is "<class 'PySide2.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior'>"
    FontPropertiesSpecifiedOnly = PySide2.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior.FontPropertiesSpecifiedOnly
    NoUnderline = PySide2.QtGui.QTextCharFormat.UnderlineStyle.NoUnderline
    SingleUnderline = PySide2.QtGui.QTextCharFormat.UnderlineStyle.SingleUnderline
    SpellCheckUnderline = PySide2.QtGui.QTextCharFormat.UnderlineStyle.SpellCheckUnderline
    UnderlineStyle = None # (!) real value is "<class 'PySide2.QtGui.QTextCharFormat.UnderlineStyle'>"
    VerticalAlignment = None # (!) real value is "<class 'PySide2.QtGui.QTextCharFormat.VerticalAlignment'>"
    WaveUnderline = PySide2.QtGui.QTextCharFormat.UnderlineStyle.WaveUnderline


