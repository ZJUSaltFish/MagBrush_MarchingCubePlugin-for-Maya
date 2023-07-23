# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QRawFont(__Shiboken.Object):
    """
    QRawFont(self) -> None
    QRawFont(self, fileName: str, pixelSize: float, hintingPreference: PySide2.QtGui.QFont.HintingPreference = PySide2.QtGui.QFont.HintingPreference.PreferDefaultHinting) -> None
    QRawFont(self, fontData: PySide2.QtCore.QByteArray, pixelSize: float, hintingPreference: PySide2.QtGui.QFont.HintingPreference = PySide2.QtGui.QFont.HintingPreference.PreferDefaultHinting) -> None
    QRawFont(self, other: PySide2.QtGui.QRawFont) -> None
    """
    def advancesForGlyphIndexes(self, glyphIndexes, p_int=None): # real signature unknown; restored from __doc__
        """
        advancesForGlyphIndexes(self, glyphIndexes: typing.List[int]) -> typing.List[PySide2.QtCore.QPointF]
        advancesForGlyphIndexes(self, glyphIndexes: typing.List[int], layoutFlags: PySide2.QtGui.QRawFont.LayoutFlags) -> typing.List[PySide2.QtCore.QPointF]
        """
        pass

    def alphaMapForGlyph(self, glyphIndex, antialiasingType=None, transform=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ alphaMapForGlyph(self, glyphIndex: int, antialiasingType: PySide2.QtGui.QRawFont.AntialiasingType = PySide2.QtGui.QRawFont.AntialiasingType.SubPixelAntialiasing, transform: PySide2.QtGui.QTransform = Default(QTransform)) -> PySide2.QtGui.QImage """
        pass

    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def averageCharWidth(self): # real signature unknown; restored from __doc__
        """ averageCharWidth(self) -> float """
        return 0.0

    def boundingRect(self, glyphIndex): # real signature unknown; restored from __doc__
        """ boundingRect(self, glyphIndex: int) -> PySide2.QtCore.QRectF """
        pass

    def capHeight(self): # real signature unknown; restored from __doc__
        """ capHeight(self) -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def familyName(self): # real signature unknown; restored from __doc__
        """ familyName(self) -> str """
        return ""

    def fontTable(self, tagName): # real signature unknown; restored from __doc__
        """ fontTable(self, tagName: bytes) -> PySide2.QtCore.QByteArray """
        pass

    def fromFont(self, font, writingSystem=None): # real signature unknown; restored from __doc__
        """ fromFont(font: PySide2.QtGui.QFont, writingSystem: PySide2.QtGui.QFontDatabase.WritingSystem = PySide2.QtGui.QFontDatabase.WritingSystem.Any) -> PySide2.QtGui.QRawFont """
        pass

    def glyphIndexesForString(self, text): # real signature unknown; restored from __doc__
        """ glyphIndexesForString(self, text: str) -> typing.List[int] """
        pass

    def hintingPreference(self): # real signature unknown; restored from __doc__
        """ hintingPreference(self) -> PySide2.QtGui.QFont.HintingPreference """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ leading(self) -> float """
        return 0.0

    def lineThickness(self): # real signature unknown; restored from __doc__
        """ lineThickness(self) -> float """
        return 0.0

    def loadFromData(self, fontData, pixelSize, hintingPreference): # real signature unknown; restored from __doc__
        """ loadFromData(self, fontData: PySide2.QtCore.QByteArray, pixelSize: float, hintingPreference: PySide2.QtGui.QFont.HintingPreference) -> None """
        pass

    def loadFromFile(self, fileName, pixelSize, hintingPreference): # real signature unknown; restored from __doc__
        """ loadFromFile(self, fileName: str, pixelSize: float, hintingPreference: PySide2.QtGui.QFont.HintingPreference) -> None """
        pass

    def maxCharWidth(self): # real signature unknown; restored from __doc__
        """ maxCharWidth(self) -> float """
        return 0.0

    def pathForGlyph(self, glyphIndex): # real signature unknown; restored from __doc__
        """ pathForGlyph(self, glyphIndex: int) -> PySide2.QtGui.QPainterPath """
        pass

    def pixelSize(self): # real signature unknown; restored from __doc__
        """ pixelSize(self) -> float """
        return 0.0

    def setPixelSize(self, pixelSize): # real signature unknown; restored from __doc__
        """ setPixelSize(self, pixelSize: float) -> None """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> PySide2.QtGui.QFont.Style """
        pass

    def styleName(self): # real signature unknown; restored from __doc__
        """ styleName(self) -> str """
        return ""

    def supportedWritingSystems(self): # real signature unknown; restored from __doc__
        """ supportedWritingSystems(self) -> typing.List[PySide2.QtGui.QFontDatabase.WritingSystem] """
        pass

    def supportsCharacter(self, character): # real signature unknown; restored from __doc__
        """
        supportsCharacter(self, character: str) -> bool
        supportsCharacter(self, ucs4: int) -> bool
        """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QRawFont) -> None """
        pass

    def underlinePosition(self): # real signature unknown; restored from __doc__
        """ underlinePosition(self) -> float """
        return 0.0

    def unitsPerEm(self): # real signature unknown; restored from __doc__
        """ unitsPerEm(self) -> float """
        return 0.0

    def weight(self): # real signature unknown; restored from __doc__
        """ weight(self) -> int """
        return 0

    def xHeight(self): # real signature unknown; restored from __doc__
        """ xHeight(self) -> float """
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

    AntialiasingType = None # (!) real value is "<class 'PySide2.QtGui.QRawFont.AntialiasingType'>"
    KernedAdvances = PySide2.QtGui.QRawFont.LayoutFlag.KernedAdvances
    LayoutFlag = None # (!) real value is "<class 'PySide2.QtGui.QRawFont.LayoutFlag'>"
    LayoutFlags = None # (!) real value is "<class 'PySide2.QtGui.QRawFont.LayoutFlags'>"
    PixelAntialiasing = PySide2.QtGui.QRawFont.AntialiasingType.PixelAntialiasing
    SeparateAdvances = PySide2.QtGui.QRawFont.LayoutFlag.SeparateAdvances
    SubPixelAntialiasing = PySide2.QtGui.QRawFont.AntialiasingType.SubPixelAntialiasing
    UseDesignMetrics = PySide2.QtGui.QRawFont.LayoutFlag.UseDesignMetrics
    __hash__ = None


