# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QFontDatabase(__Shiboken.Object):
    """
    QFontDatabase(self) -> None
    QFontDatabase(self, QFontDatabase: PySide2.QtGui.QFontDatabase) -> None
    """
    def addApplicationFont(self, fileName): # real signature unknown; restored from __doc__
        """ addApplicationFont(fileName: str) -> int """
        return 0

    def addApplicationFontFromData(self, fontData): # real signature unknown; restored from __doc__
        """ addApplicationFontFromData(fontData: PySide2.QtCore.QByteArray) -> int """
        return 0

    def applicationFontFamilies(self, id): # real signature unknown; restored from __doc__
        """ applicationFontFamilies(id: int) -> typing.List[str] """
        pass

    def bold(self, family, style): # real signature unknown; restored from __doc__
        """ bold(self, family: str, style: str) -> bool """
        return False

    def families(self, writingSystem=None): # real signature unknown; restored from __doc__
        """ families(self, writingSystem: PySide2.QtGui.QFontDatabase.WritingSystem = PySide2.QtGui.QFontDatabase.WritingSystem.Any) -> typing.List[str] """
        pass

    def font(self, family, style, pointSize): # real signature unknown; restored from __doc__
        """ font(self, family: str, style: str, pointSize: int) -> PySide2.QtGui.QFont """
        pass

    def hasFamily(self, family): # real signature unknown; restored from __doc__
        """ hasFamily(self, family: str) -> bool """
        return False

    def isBitmapScalable(self, family, style=''): # real signature unknown; restored from __doc__
        """ isBitmapScalable(self, family: str, style: str = '') -> bool """
        return False

    def isFixedPitch(self, family, style=''): # real signature unknown; restored from __doc__
        """ isFixedPitch(self, family: str, style: str = '') -> bool """
        return False

    def isPrivateFamily(self, family): # real signature unknown; restored from __doc__
        """ isPrivateFamily(self, family: str) -> bool """
        return False

    def isScalable(self, family, style=''): # real signature unknown; restored from __doc__
        """ isScalable(self, family: str, style: str = '') -> bool """
        return False

    def isSmoothlyScalable(self, family, style=''): # real signature unknown; restored from __doc__
        """ isSmoothlyScalable(self, family: str, style: str = '') -> bool """
        return False

    def italic(self, family, style): # real signature unknown; restored from __doc__
        """ italic(self, family: str, style: str) -> bool """
        return False

    def pointSizes(self, family, style=''): # real signature unknown; restored from __doc__
        """ pointSizes(self, family: str, style: str = '') -> typing.List[int] """
        pass

    def removeAllApplicationFonts(self): # real signature unknown; restored from __doc__
        """ removeAllApplicationFonts() -> bool """
        return False

    def removeApplicationFont(self, id): # real signature unknown; restored from __doc__
        """ removeApplicationFont(id: int) -> bool """
        return False

    def smoothSizes(self, family, style): # real signature unknown; restored from __doc__
        """ smoothSizes(self, family: str, style: str) -> typing.List[int] """
        pass

    def standardSizes(self): # real signature unknown; restored from __doc__
        """ standardSizes() -> typing.List[int] """
        pass

    def styles(self, family): # real signature unknown; restored from __doc__
        """ styles(self, family: str) -> typing.List[str] """
        pass

    def styleString(self, font): # real signature unknown; restored from __doc__
        """
        styleString(self, font: PySide2.QtGui.QFont) -> str
        styleString(self, fontInfo: PySide2.QtGui.QFontInfo) -> str
        """
        return ""

    def supportsThreadedFontRendering(self): # real signature unknown; restored from __doc__
        """ supportsThreadedFontRendering() -> bool """
        return False

    def systemFont(self, type): # real signature unknown; restored from __doc__
        """ systemFont(type: PySide2.QtGui.QFontDatabase.SystemFont) -> PySide2.QtGui.QFont """
        pass

    def weight(self, family, style): # real signature unknown; restored from __doc__
        """ weight(self, family: str, style: str) -> int """
        return 0

    def writingSystemName(self, writingSystem): # real signature unknown; restored from __doc__
        """ writingSystemName(writingSystem: PySide2.QtGui.QFontDatabase.WritingSystem) -> str """
        return ""

    def writingSystems(self): # real signature unknown; restored from __doc__
        """
        writingSystems(self) -> typing.List[PySide2.QtGui.QFontDatabase.WritingSystem]
        writingSystems(self, family: str) -> typing.List[PySide2.QtGui.QFontDatabase.WritingSystem]
        """
        pass

    def writingSystemSample(self, writingSystem): # real signature unknown; restored from __doc__
        """ writingSystemSample(writingSystem: PySide2.QtGui.QFontDatabase.WritingSystem) -> str """
        return ""

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Any = PySide2.QtGui.QFontDatabase.WritingSystem.Any
    Arabic = PySide2.QtGui.QFontDatabase.WritingSystem.Arabic
    Armenian = PySide2.QtGui.QFontDatabase.WritingSystem.Armenian
    Bengali = PySide2.QtGui.QFontDatabase.WritingSystem.Bengali
    Cyrillic = PySide2.QtGui.QFontDatabase.WritingSystem.Cyrillic
    Devanagari = PySide2.QtGui.QFontDatabase.WritingSystem.Devanagari
    FixedFont = PySide2.QtGui.QFontDatabase.SystemFont.FixedFont
    GeneralFont = PySide2.QtGui.QFontDatabase.SystemFont.GeneralFont
    Georgian = PySide2.QtGui.QFontDatabase.WritingSystem.Georgian
    Greek = PySide2.QtGui.QFontDatabase.WritingSystem.Greek
    Gujarati = PySide2.QtGui.QFontDatabase.WritingSystem.Gujarati
    Gurmukhi = PySide2.QtGui.QFontDatabase.WritingSystem.Gurmukhi
    Hebrew = PySide2.QtGui.QFontDatabase.WritingSystem.Hebrew
    Japanese = PySide2.QtGui.QFontDatabase.WritingSystem.Japanese
    Kannada = PySide2.QtGui.QFontDatabase.WritingSystem.Kannada
    Khmer = PySide2.QtGui.QFontDatabase.WritingSystem.Khmer
    Korean = PySide2.QtGui.QFontDatabase.WritingSystem.Korean
    Lao = PySide2.QtGui.QFontDatabase.WritingSystem.Lao
    Latin = PySide2.QtGui.QFontDatabase.WritingSystem.Latin
    Malayalam = PySide2.QtGui.QFontDatabase.WritingSystem.Malayalam
    Myanmar = PySide2.QtGui.QFontDatabase.WritingSystem.Myanmar
    Nko = PySide2.QtGui.QFontDatabase.WritingSystem.Nko
    Ogham = PySide2.QtGui.QFontDatabase.WritingSystem.Ogham
    Oriya = PySide2.QtGui.QFontDatabase.WritingSystem.Oriya
    Other = PySide2.QtGui.QFontDatabase.WritingSystem.Other
    Runic = PySide2.QtGui.QFontDatabase.WritingSystem.Runic
    SimplifiedChinese = PySide2.QtGui.QFontDatabase.WritingSystem.SimplifiedChinese
    Sinhala = PySide2.QtGui.QFontDatabase.WritingSystem.Sinhala
    SmallestReadableFont = PySide2.QtGui.QFontDatabase.SystemFont.SmallestReadableFont
    Symbol = PySide2.QtGui.QFontDatabase.WritingSystem.Symbol
    Syriac = PySide2.QtGui.QFontDatabase.WritingSystem.Syriac
    SystemFont = None # (!) real value is "<class 'PySide2.QtGui.QFontDatabase.SystemFont'>"
    Tamil = PySide2.QtGui.QFontDatabase.WritingSystem.Tamil
    Telugu = PySide2.QtGui.QFontDatabase.WritingSystem.Telugu
    Thaana = PySide2.QtGui.QFontDatabase.WritingSystem.Thaana
    Thai = PySide2.QtGui.QFontDatabase.WritingSystem.Thai
    Tibetan = PySide2.QtGui.QFontDatabase.WritingSystem.Tibetan
    TitleFont = PySide2.QtGui.QFontDatabase.SystemFont.TitleFont
    TraditionalChinese = PySide2.QtGui.QFontDatabase.WritingSystem.TraditionalChinese
    Vietnamese = PySide2.QtGui.QFontDatabase.WritingSystem.Vietnamese
    WritingSystem = None # (!) real value is "<class 'PySide2.QtGui.QFontDatabase.WritingSystem'>"
    WritingSystemsCount = PySide2.QtGui.QFontDatabase.WritingSystem.WritingSystemsCount


