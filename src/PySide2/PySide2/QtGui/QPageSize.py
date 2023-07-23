# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPageSize(__Shiboken.Object):
    """
    QPageSize(self) -> None
    QPageSize(self, other: PySide2.QtGui.QPageSize) -> None
    QPageSize(self, pageSizeId: PySide2.QtGui.QPageSize.PageSizeId) -> None
    QPageSize(self, pointSize: PySide2.QtCore.QSize, name: str = '', matchPolicy: PySide2.QtGui.QPageSize.SizeMatchPolicy = PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch) -> None
    QPageSize(self, size: PySide2.QtCore.QSizeF, units: PySide2.QtGui.QPageSize.Unit, name: str = '', matchPolicy: PySide2.QtGui.QPageSize.SizeMatchPolicy = PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch) -> None
    """
    def definitionSize(self, pageSizeId): # real signature unknown; restored from __doc__
        """
        definitionSize(pageSizeId: PySide2.QtGui.QPageSize.PageSizeId) -> PySide2.QtCore.QSizeF
        definitionSize(self) -> PySide2.QtCore.QSizeF
        """
        pass

    def definitionUnits(self, pageSizeId): # real signature unknown; restored from __doc__
        """
        definitionUnits(pageSizeId: PySide2.QtGui.QPageSize.PageSizeId) -> PySide2.QtGui.QPageSize.Unit
        definitionUnits(self) -> PySide2.QtGui.QPageSize.Unit
        """
        pass

    def id(self, pointSize, matchPolicy=None): # real signature unknown; restored from __doc__
        """
        id(pointSize: PySide2.QtCore.QSize, matchPolicy: PySide2.QtGui.QPageSize.SizeMatchPolicy = PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch) -> PySide2.QtGui.QPageSize.PageSizeId
        id(self) -> PySide2.QtGui.QPageSize.PageSizeId
        id(size: PySide2.QtCore.QSizeF, units: PySide2.QtGui.QPageSize.Unit, matchPolicy: PySide2.QtGui.QPageSize.SizeMatchPolicy = PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch) -> PySide2.QtGui.QPageSize.PageSizeId
        id(windowsId: int) -> PySide2.QtGui.QPageSize.PageSizeId
        """
        pass

    def isEquivalentTo(self, other): # real signature unknown; restored from __doc__
        """ isEquivalentTo(self, other: PySide2.QtGui.QPageSize) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def key(self, pageSizeId): # real signature unknown; restored from __doc__
        """
        key(pageSizeId: PySide2.QtGui.QPageSize.PageSizeId) -> str
        key(self) -> str
        """
        return ""

    def name(self, pageSizeId): # real signature unknown; restored from __doc__
        """
        name(pageSizeId: PySide2.QtGui.QPageSize.PageSizeId) -> str
        name(self) -> str
        """
        return ""

    def rect(self, units): # real signature unknown; restored from __doc__
        """ rect(self, units: PySide2.QtGui.QPageSize.Unit) -> PySide2.QtCore.QRectF """
        pass

    def rectPixels(self, resolution): # real signature unknown; restored from __doc__
        """ rectPixels(self, resolution: int) -> PySide2.QtCore.QRect """
        pass

    def rectPoints(self): # real signature unknown; restored from __doc__
        """ rectPoints(self) -> PySide2.QtCore.QRect """
        pass

    def size(self, pageSizeId, units): # real signature unknown; restored from __doc__
        """
        size(pageSizeId: PySide2.QtGui.QPageSize.PageSizeId, units: PySide2.QtGui.QPageSize.Unit) -> PySide2.QtCore.QSizeF
        size(self, units: PySide2.QtGui.QPageSize.Unit) -> PySide2.QtCore.QSizeF
        """
        pass

    def sizePixels(self, pageSizeId, resolution): # real signature unknown; restored from __doc__
        """
        sizePixels(pageSizeId: PySide2.QtGui.QPageSize.PageSizeId, resolution: int) -> PySide2.QtCore.QSize
        sizePixels(self, resolution: int) -> PySide2.QtCore.QSize
        """
        pass

    def sizePoints(self, pageSizeId): # real signature unknown; restored from __doc__
        """
        sizePoints(pageSizeId: PySide2.QtGui.QPageSize.PageSizeId) -> PySide2.QtCore.QSize
        sizePoints(self) -> PySide2.QtCore.QSize
        """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QPageSize) -> None """
        pass

    def windowsId(self, pageSizeId): # real signature unknown; restored from __doc__
        """
        windowsId(pageSizeId: PySide2.QtGui.QPageSize.PageSizeId) -> int
        windowsId(self) -> int
        """
        return 0

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    A0 = PySide2.QtGui.QPageSize.PageSizeId.A0
    A1 = PySide2.QtGui.QPageSize.PageSizeId.A1
    A10 = PySide2.QtGui.QPageSize.PageSizeId.A10
    A2 = PySide2.QtGui.QPageSize.PageSizeId.A2
    A3 = PySide2.QtGui.QPageSize.PageSizeId.A3
    A3Extra = PySide2.QtGui.QPageSize.PageSizeId.A3Extra
    A4 = PySide2.QtGui.QPageSize.PageSizeId.A4
    A4Extra = PySide2.QtGui.QPageSize.PageSizeId.A4Extra
    A4Plus = PySide2.QtGui.QPageSize.PageSizeId.A4Plus
    A4Small = PySide2.QtGui.QPageSize.PageSizeId.A4Small
    A5 = PySide2.QtGui.QPageSize.PageSizeId.A5
    A5Extra = PySide2.QtGui.QPageSize.PageSizeId.A5Extra
    A6 = PySide2.QtGui.QPageSize.PageSizeId.A6
    A7 = PySide2.QtGui.QPageSize.PageSizeId.A7
    A8 = PySide2.QtGui.QPageSize.PageSizeId.A8
    A9 = PySide2.QtGui.QPageSize.PageSizeId.A9
    AnsiA = PySide2.QtGui.QPageSize.PageSizeId.AnsiA
    AnsiB = PySide2.QtGui.QPageSize.PageSizeId.AnsiB
    AnsiC = PySide2.QtGui.QPageSize.PageSizeId.AnsiC
    AnsiD = PySide2.QtGui.QPageSize.PageSizeId.AnsiD
    AnsiE = PySide2.QtGui.QPageSize.PageSizeId.AnsiE
    ArchA = PySide2.QtGui.QPageSize.PageSizeId.ArchA
    ArchB = PySide2.QtGui.QPageSize.PageSizeId.ArchB
    ArchC = PySide2.QtGui.QPageSize.PageSizeId.ArchC
    ArchD = PySide2.QtGui.QPageSize.PageSizeId.ArchD
    ArchE = PySide2.QtGui.QPageSize.PageSizeId.ArchE
    B0 = PySide2.QtGui.QPageSize.PageSizeId.B0
    B1 = PySide2.QtGui.QPageSize.PageSizeId.B1
    B10 = PySide2.QtGui.QPageSize.PageSizeId.B10
    B2 = PySide2.QtGui.QPageSize.PageSizeId.B2
    B3 = PySide2.QtGui.QPageSize.PageSizeId.B3
    B4 = PySide2.QtGui.QPageSize.PageSizeId.B4
    B5 = PySide2.QtGui.QPageSize.PageSizeId.B5
    B5Extra = PySide2.QtGui.QPageSize.PageSizeId.B5Extra
    B6 = PySide2.QtGui.QPageSize.PageSizeId.B6
    B7 = PySide2.QtGui.QPageSize.PageSizeId.B7
    B8 = PySide2.QtGui.QPageSize.PageSizeId.B8
    B9 = PySide2.QtGui.QPageSize.PageSizeId.B9
    C5E = PySide2.QtGui.QPageSize.PageSizeId.C5E
    Cicero = PySide2.QtGui.QPageSize.Unit.Cicero
    Comm10E = PySide2.QtGui.QPageSize.PageSizeId.Comm10E
    Custom = PySide2.QtGui.QPageSize.PageSizeId.Custom
    Didot = PySide2.QtGui.QPageSize.Unit.Didot
    DLE = PySide2.QtGui.QPageSize.PageSizeId.DLE
    DoublePostcard = PySide2.QtGui.QPageSize.PageSizeId.DoublePostcard
    Envelope10 = PySide2.QtGui.QPageSize.PageSizeId.Envelope10
    Envelope11 = PySide2.QtGui.QPageSize.PageSizeId.Envelope11
    Envelope12 = PySide2.QtGui.QPageSize.PageSizeId.Envelope12
    Envelope14 = PySide2.QtGui.QPageSize.PageSizeId.Envelope14
    Envelope9 = PySide2.QtGui.QPageSize.PageSizeId.Envelope9
    EnvelopeB4 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeB4
    EnvelopeB5 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeB5
    EnvelopeB6 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeB6
    EnvelopeC0 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC0
    EnvelopeC1 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC1
    EnvelopeC2 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC2
    EnvelopeC3 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC3
    EnvelopeC4 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC4
    EnvelopeC5 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC5
    EnvelopeC6 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC6
    EnvelopeC65 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC65
    EnvelopeC7 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeC7
    EnvelopeChou3 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeChou3
    EnvelopeChou4 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeChou4
    EnvelopeDL = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeDL
    EnvelopeInvite = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeInvite
    EnvelopeItalian = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeItalian
    EnvelopeKaku2 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeKaku2
    EnvelopeKaku3 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeKaku3
    EnvelopeMonarch = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeMonarch
    EnvelopePersonal = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePersonal
    EnvelopePrc1 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc1
    EnvelopePrc10 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc10
    EnvelopePrc2 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc2
    EnvelopePrc3 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc3
    EnvelopePrc4 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc4
    EnvelopePrc5 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc5
    EnvelopePrc6 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc6
    EnvelopePrc7 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc7
    EnvelopePrc8 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc8
    EnvelopePrc9 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopePrc9
    EnvelopeYou4 = PySide2.QtGui.QPageSize.PageSizeId.EnvelopeYou4
    ExactMatch = PySide2.QtGui.QPageSize.SizeMatchPolicy.ExactMatch
    Executive = PySide2.QtGui.QPageSize.PageSizeId.Executive
    ExecutiveStandard = PySide2.QtGui.QPageSize.PageSizeId.ExecutiveStandard
    FanFoldGerman = PySide2.QtGui.QPageSize.PageSizeId.FanFoldGerman
    FanFoldGermanLegal = PySide2.QtGui.QPageSize.PageSizeId.FanFoldGermanLegal
    FanFoldUS = PySide2.QtGui.QPageSize.PageSizeId.FanFoldUS
    Folio = PySide2.QtGui.QPageSize.PageSizeId.Folio
    FuzzyMatch = PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch
    FuzzyOrientationMatch = PySide2.QtGui.QPageSize.SizeMatchPolicy.FuzzyOrientationMatch
    Imperial10x11 = PySide2.QtGui.QPageSize.PageSizeId.Imperial10x11
    Imperial10x13 = PySide2.QtGui.QPageSize.PageSizeId.Imperial10x13
    Imperial10x14 = PySide2.QtGui.QPageSize.PageSizeId.Imperial10x14
    Imperial12x11 = PySide2.QtGui.QPageSize.PageSizeId.Imperial12x11
    Imperial15x11 = PySide2.QtGui.QPageSize.PageSizeId.Imperial15x11
    Imperial7x9 = PySide2.QtGui.QPageSize.PageSizeId.Imperial7x9
    Imperial8x10 = PySide2.QtGui.QPageSize.PageSizeId.Imperial8x10
    Imperial9x11 = PySide2.QtGui.QPageSize.PageSizeId.Imperial9x11
    Imperial9x12 = PySide2.QtGui.QPageSize.PageSizeId.Imperial9x12
    Inch = PySide2.QtGui.QPageSize.Unit.Inch
    JisB0 = PySide2.QtGui.QPageSize.PageSizeId.JisB0
    JisB1 = PySide2.QtGui.QPageSize.PageSizeId.JisB1
    JisB10 = PySide2.QtGui.QPageSize.PageSizeId.JisB10
    JisB2 = PySide2.QtGui.QPageSize.PageSizeId.JisB2
    JisB3 = PySide2.QtGui.QPageSize.PageSizeId.JisB3
    JisB4 = PySide2.QtGui.QPageSize.PageSizeId.JisB4
    JisB5 = PySide2.QtGui.QPageSize.PageSizeId.JisB5
    JisB6 = PySide2.QtGui.QPageSize.PageSizeId.JisB6
    JisB7 = PySide2.QtGui.QPageSize.PageSizeId.JisB7
    JisB8 = PySide2.QtGui.QPageSize.PageSizeId.JisB8
    JisB9 = PySide2.QtGui.QPageSize.PageSizeId.JisB9
    LastPageSize = PySide2.QtGui.QPageSize.PageSizeId.LastPageSize
    Ledger = PySide2.QtGui.QPageSize.PageSizeId.Ledger
    Legal = PySide2.QtGui.QPageSize.PageSizeId.Legal
    LegalExtra = PySide2.QtGui.QPageSize.PageSizeId.LegalExtra
    Letter = PySide2.QtGui.QPageSize.PageSizeId.Letter
    LetterExtra = PySide2.QtGui.QPageSize.PageSizeId.LetterExtra
    LetterPlus = PySide2.QtGui.QPageSize.PageSizeId.LetterPlus
    LetterSmall = PySide2.QtGui.QPageSize.PageSizeId.LetterSmall
    Millimeter = PySide2.QtGui.QPageSize.Unit.Millimeter
    Note = PySide2.QtGui.QPageSize.PageSizeId.Note
    NPageSize = PySide2.QtGui.QPageSize.PageSizeId.NPageSize
    NPaperSize = PySide2.QtGui.QPageSize.PageSizeId.NPaperSize
    PageSizeId = None # (!) real value is "<class 'PySide2.QtGui.QPageSize.PageSizeId'>"
    Pica = PySide2.QtGui.QPageSize.Unit.Pica
    Point = PySide2.QtGui.QPageSize.Unit.Point
    Postcard = PySide2.QtGui.QPageSize.PageSizeId.Postcard
    Prc16K = PySide2.QtGui.QPageSize.PageSizeId.Prc16K
    Prc32K = PySide2.QtGui.QPageSize.PageSizeId.Prc32K
    Prc32KBig = PySide2.QtGui.QPageSize.PageSizeId.Prc32KBig
    Quarto = PySide2.QtGui.QPageSize.PageSizeId.Quarto
    SizeMatchPolicy = None # (!) real value is "<class 'PySide2.QtGui.QPageSize.SizeMatchPolicy'>"
    Statement = PySide2.QtGui.QPageSize.PageSizeId.Statement
    SuperA = PySide2.QtGui.QPageSize.PageSizeId.SuperA
    SuperB = PySide2.QtGui.QPageSize.PageSizeId.SuperB
    Tabloid = PySide2.QtGui.QPageSize.PageSizeId.Tabloid
    TabloidExtra = PySide2.QtGui.QPageSize.PageSizeId.TabloidExtra
    Unit = None # (!) real value is "<class 'PySide2.QtGui.QPageSize.Unit'>"
    __hash__ = None


