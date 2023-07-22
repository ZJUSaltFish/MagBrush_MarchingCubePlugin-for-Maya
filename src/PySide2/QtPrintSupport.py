# encoding: utf-8
# module PySide2.QtPrintSupport
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtPrintSupport.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtGui as __PySide2_QtGui
import PySide2.QtWidgets as __PySide2_QtWidgets
import Shiboken as __Shiboken


# no functions
# classes

class QAbstractPrintDialog(__PySide2_QtWidgets.QDialog):
    """ QAbstractPrintDialog(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def addEnabledOption(self, option): # real signature unknown; restored from __doc__
        """ addEnabledOption(self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption) -> None """
        pass

    def enabledOptions(self): # real signature unknown; restored from __doc__
        """ enabledOptions(self) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions """
        pass

    def fromPage(self): # real signature unknown; restored from __doc__
        """ fromPage(self) -> int """
        return 0

    def isOptionEnabled(self, option): # real signature unknown; restored from __doc__
        """ isOptionEnabled(self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption) -> bool """
        return False

    def maxPage(self): # real signature unknown; restored from __doc__
        """ maxPage(self) -> int """
        return 0

    def minPage(self): # real signature unknown; restored from __doc__
        """ minPage(self) -> int """
        return 0

    def printer(self): # real signature unknown; restored from __doc__
        """ printer(self) -> PySide2.QtPrintSupport.QPrinter """
        pass

    def printRange(self): # real signature unknown; restored from __doc__
        """ printRange(self) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange """
        pass

    def setEnabledOptions(self, options): # real signature unknown; restored from __doc__
        """ setEnabledOptions(self, options: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions) -> None """
        pass

    def setFromTo(self, fromPage, toPage): # real signature unknown; restored from __doc__
        """ setFromTo(self, fromPage: int, toPage: int) -> None """
        pass

    def setMinMax(self, min, max): # real signature unknown; restored from __doc__
        """ setMinMax(self, min: int, max: int) -> None """
        pass

    def setOptionTabs(self, tabs, PySide2_QtWidgets_QWidget=None): # real signature unknown; restored from __doc__
        """ setOptionTabs(self, tabs: typing.Sequence[PySide2.QtWidgets.QWidget]) -> None """
        pass

    def setPrintRange(self, range): # real signature unknown; restored from __doc__
        """ setPrintRange(self, range: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange) -> None """
        pass

    def toPage(self): # real signature unknown; restored from __doc__
        """ toPage(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, printer, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AllPages = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange.AllPages
    CurrentPage = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange.CurrentPage
    DontUseSheet = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.DontUseSheet
    None_ = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.None_
    PageRange = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange.PageRange
    PrintCollateCopies = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintCollateCopies
    PrintCurrentPage = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintCurrentPage
    PrintDialogOption = None # (!) real value is "<class 'PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption'>"
    PrintDialogOptions = None # (!) real value is "<class 'PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions'>"
    PrintPageRange = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintPageRange
    PrintRange = None # (!) real value is "<class 'PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange'>"
    PrintSelection = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintSelection
    PrintShowPageSize = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintShowPageSize
    PrintToFile = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption.PrintToFile
    Selection = PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange.Selection
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025A0187D400>'


class QPageSetupDialog(__PySide2_QtWidgets.QDialog):
    """
    QPageSetupDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QPageSetupDialog(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) -> None """
        pass

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def printer(self): # real signature unknown; restored from __doc__
        """ printer(self) -> PySide2.QtPrintSupport.QPrinter """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025A0187CD80>'


class QPrintDialog(QAbstractPrintDialog):
    """
    QPrintDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QPrintDialog(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def accepted(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) -> None """
        pass

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption, on: bool = True) -> None """
        pass

    def setOptions(self, options): # real signature unknown; restored from __doc__
        """ setOptions(self, options: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025A0187D5C0>'


class QPrintEngine(__Shiboken.Object):
    """ QPrintEngine(self) -> None """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> bool """
        return False

    def metric(self, arg__1): # real signature unknown; restored from __doc__
        """ metric(self, arg__1: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ newPage(self) -> bool """
        return False

    def printerState(self): # real signature unknown; restored from __doc__
        """ printerState(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState """
        pass

    def property(self, key): # real signature unknown; restored from __doc__
        """ property(self, key: PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey) -> typing.Any """
        pass

    def setProperty(self, key, value): # real signature unknown; restored from __doc__
        """ setProperty(self, key: PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey, value: typing.Any) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    PPK_CollateCopies = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_CollateCopies
    PPK_ColorMode = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_ColorMode
    PPK_CopyCount = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_CopyCount
    PPK_Creator = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_Creator
    PPK_CustomBase = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_CustomBase
    PPK_CustomPaperSize = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_CustomPaperSize
    PPK_DocumentName = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_DocumentName
    PPK_Duplex = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_Duplex
    PPK_FontEmbedding = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_FontEmbedding
    PPK_FullPage = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_FullPage
    PPK_NumberOfCopies = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_NumberOfCopies
    PPK_Orientation = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_Orientation
    PPK_OutputFileName = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_OutputFileName
    PPK_PageMargins = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PageMargins
    PPK_PageOrder = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PageOrder
    PPK_PageRect = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PageRect
    PPK_PageSize = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PageSize
    PPK_PaperName = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PaperName
    PPK_PaperRect = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PaperRect
    PPK_PaperSize = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PaperSize
    PPK_PaperSource = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PaperSource
    PPK_PaperSources = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PaperSources
    PPK_PrinterName = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PrinterName
    PPK_PrinterProgram = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_PrinterProgram
    PPK_QPageLayout = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_QPageLayout
    PPK_QPageMargins = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_QPageMargins
    PPK_QPageSize = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_QPageSize
    PPK_Resolution = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_Resolution
    PPK_SelectionOption = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_SelectionOption
    PPK_SupportedResolutions = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_SupportedResolutions
    PPK_SupportsMultipleCopies = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_SupportsMultipleCopies
    PPK_WindowsPageSize = PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey.PPK_WindowsPageSize
    PrintEnginePropertyKey = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey'>"


class QPrinter(__PySide2_QtGui.QPagedPaintDevice):
    """
    QPrinter(self, mode: PySide2.QtPrintSupport.QPrinter.PrinterMode = PySide2.QtPrintSupport.QPrinter.PrinterMode.ScreenResolution) -> None
    QPrinter(self, printer: PySide2.QtPrintSupport.QPrinterInfo, mode: PySide2.QtPrintSupport.QPrinter.PrinterMode = PySide2.QtPrintSupport.QPrinter.PrinterMode.ScreenResolution) -> None
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> bool """
        return False

    def actualNumCopies(self): # real signature unknown; restored from __doc__
        """ actualNumCopies(self) -> int """
        return 0

    def collateCopies(self): # real signature unknown; restored from __doc__
        """ collateCopies(self) -> bool """
        return False

    def colorMode(self): # real signature unknown; restored from __doc__
        """ colorMode(self) -> PySide2.QtPrintSupport.QPrinter.ColorMode """
        pass

    def copyCount(self): # real signature unknown; restored from __doc__
        """ copyCount(self) -> int """
        return 0

    def creator(self): # real signature unknown; restored from __doc__
        """ creator(self) -> str """
        return ""

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def docName(self): # real signature unknown; restored from __doc__
        """ docName(self) -> str """
        return ""

    def doubleSidedPrinting(self): # real signature unknown; restored from __doc__
        """ doubleSidedPrinting(self) -> bool """
        return False

    def duplex(self): # real signature unknown; restored from __doc__
        """ duplex(self) -> PySide2.QtPrintSupport.QPrinter.DuplexMode """
        pass

    def fontEmbeddingEnabled(self): # real signature unknown; restored from __doc__
        """ fontEmbeddingEnabled(self) -> bool """
        return False

    def fromPage(self): # real signature unknown; restored from __doc__
        """ fromPage(self) -> int """
        return 0

    def fullPage(self): # real signature unknown; restored from __doc__
        """ fullPage(self) -> bool """
        return False

    def getPageMargins(self, unit): # real signature unknown; restored from __doc__
        """ getPageMargins(self, unit: PySide2.QtPrintSupport.QPrinter.Unit) -> typing.Tuple[float, float, float, float] """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def metric(self, arg__1): # real signature unknown; restored from __doc__
        """ metric(self, arg__1: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ newPage(self) -> bool """
        return False

    def numCopies(self): # real signature unknown; restored from __doc__
        """ numCopies(self) -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtPrintSupport.QPrinter.Orientation """
        pass

    def outputFileName(self): # real signature unknown; restored from __doc__
        """ outputFileName(self) -> str """
        return ""

    def outputFormat(self): # real signature unknown; restored from __doc__
        """ outputFormat(self) -> PySide2.QtPrintSupport.QPrinter.OutputFormat """
        pass

    def pageOrder(self): # real signature unknown; restored from __doc__
        """ pageOrder(self) -> PySide2.QtPrintSupport.QPrinter.PageOrder """
        pass

    def pageRect(self): # real signature unknown; restored from __doc__
        """
        pageRect(self) -> PySide2.QtCore.QRect
        pageRect(self, arg__1: PySide2.QtPrintSupport.QPrinter.Unit) -> PySide2.QtCore.QRectF
        """
        pass

    def pageSize(self): # real signature unknown; restored from __doc__
        """ pageSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def paperName(self): # real signature unknown; restored from __doc__
        """ paperName(self) -> str """
        return ""

    def paperRect(self): # real signature unknown; restored from __doc__
        """
        paperRect(self) -> PySide2.QtCore.QRect
        paperRect(self, arg__1: PySide2.QtPrintSupport.QPrinter.Unit) -> PySide2.QtCore.QRectF
        """
        pass

    def paperSize(self): # real signature unknown; restored from __doc__
        """
        paperSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize
        paperSize(self, unit: PySide2.QtPrintSupport.QPrinter.Unit) -> PySide2.QtCore.QSizeF
        """
        pass

    def paperSource(self): # real signature unknown; restored from __doc__
        """ paperSource(self) -> PySide2.QtPrintSupport.QPrinter.PaperSource """
        pass

    def pdfVersion(self): # real signature unknown; restored from __doc__
        """ pdfVersion(self) -> PySide2.QtGui.QPagedPaintDevice.PdfVersion """
        pass

    def printEngine(self): # real signature unknown; restored from __doc__
        """ printEngine(self) -> PySide2.QtPrintSupport.QPrintEngine """
        pass

    def printerName(self): # real signature unknown; restored from __doc__
        """ printerName(self) -> str """
        return ""

    def printerState(self): # real signature unknown; restored from __doc__
        """ printerState(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState """
        pass

    def printProgram(self): # real signature unknown; restored from __doc__
        """ printProgram(self) -> str """
        return ""

    def printRange(self): # real signature unknown; restored from __doc__
        """ printRange(self) -> PySide2.QtPrintSupport.QPrinter.PrintRange """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def setCollateCopies(self, collate): # real signature unknown; restored from __doc__
        """ setCollateCopies(self, collate: bool) -> None """
        pass

    def setColorMode(self, arg__1): # real signature unknown; restored from __doc__
        """ setColorMode(self, arg__1: PySide2.QtPrintSupport.QPrinter.ColorMode) -> None """
        pass

    def setCopyCount(self, arg__1): # real signature unknown; restored from __doc__
        """ setCopyCount(self, arg__1: int) -> None """
        pass

    def setCreator(self, arg__1): # real signature unknown; restored from __doc__
        """ setCreator(self, arg__1: str) -> None """
        pass

    def setDocName(self, arg__1): # real signature unknown; restored from __doc__
        """ setDocName(self, arg__1: str) -> None """
        pass

    def setDoubleSidedPrinting(self, enable): # real signature unknown; restored from __doc__
        """ setDoubleSidedPrinting(self, enable: bool) -> None """
        pass

    def setDuplex(self, duplex): # real signature unknown; restored from __doc__
        """ setDuplex(self, duplex: PySide2.QtPrintSupport.QPrinter.DuplexMode) -> None """
        pass

    def setEngines(self, printEngine, paintEngine): # real signature unknown; restored from __doc__
        """ setEngines(self, printEngine: PySide2.QtPrintSupport.QPrintEngine, paintEngine: PySide2.QtGui.QPaintEngine) -> None """
        pass

    def setFontEmbeddingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setFontEmbeddingEnabled(self, enable: bool) -> None """
        pass

    def setFromTo(self, fromPage, toPage): # real signature unknown; restored from __doc__
        """ setFromTo(self, fromPage: int, toPage: int) -> None """
        pass

    def setFullPage(self, arg__1): # real signature unknown; restored from __doc__
        """ setFullPage(self, arg__1: bool) -> None """
        pass

    def setMargins(self, m): # real signature unknown; restored from __doc__
        """ setMargins(self, m: PySide2.QtGui.QPagedPaintDevice.Margins) -> None """
        pass

    def setNumCopies(self, arg__1): # real signature unknown; restored from __doc__
        """ setNumCopies(self, arg__1: int) -> None """
        pass

    def setOrientation(self, arg__1): # real signature unknown; restored from __doc__
        """ setOrientation(self, arg__1: PySide2.QtPrintSupport.QPrinter.Orientation) -> None """
        pass

    def setOutputFileName(self, arg__1): # real signature unknown; restored from __doc__
        """ setOutputFileName(self, arg__1: str) -> None """
        pass

    def setOutputFormat(self, format): # real signature unknown; restored from __doc__
        """ setOutputFormat(self, format: PySide2.QtPrintSupport.QPrinter.OutputFormat) -> None """
        pass

    def setPageMargins(self, left, top, right, bottom, unit): # real signature unknown; restored from __doc__
        """
        setPageMargins(self, left: float, top: float, right: float, bottom: float, unit: PySide2.QtPrintSupport.QPrinter.Unit) -> None
        setPageMargins(self, margins: PySide2.QtCore.QMarginsF) -> bool
        """
        pass

    def setPageOrder(self, arg__1): # real signature unknown; restored from __doc__
        """ setPageOrder(self, arg__1: PySide2.QtPrintSupport.QPrinter.PageOrder) -> None """
        pass

    def setPageSize(self, arg__1): # real signature unknown; restored from __doc__
        """
        setPageSize(self, arg__1: PySide2.QtGui.QPageSize) -> bool
        setPageSize(self, arg__1: PySide2.QtGui.QPagedPaintDevice.PageSize) -> None
        """
        return False

    def setPageSizeMM(self, size): # real signature unknown; restored from __doc__
        """ setPageSizeMM(self, size: PySide2.QtCore.QSizeF) -> None """
        pass

    def setPaperName(self, paperName): # real signature unknown; restored from __doc__
        """ setPaperName(self, paperName: str) -> None """
        pass

    def setPaperSize(self, arg__1): # real signature unknown; restored from __doc__
        """
        setPaperSize(self, arg__1: PySide2.QtGui.QPagedPaintDevice.PageSize) -> None
        setPaperSize(self, paperSize: PySide2.QtCore.QSizeF, unit: PySide2.QtPrintSupport.QPrinter.Unit) -> None
        """
        pass

    def setPaperSource(self, arg__1): # real signature unknown; restored from __doc__
        """ setPaperSource(self, arg__1: PySide2.QtPrintSupport.QPrinter.PaperSource) -> None """
        pass

    def setPdfVersion(self, version): # real signature unknown; restored from __doc__
        """ setPdfVersion(self, version: PySide2.QtGui.QPagedPaintDevice.PdfVersion) -> None """
        pass

    def setPrinterName(self, arg__1): # real signature unknown; restored from __doc__
        """ setPrinterName(self, arg__1: str) -> None """
        pass

    def setPrintProgram(self, arg__1): # real signature unknown; restored from __doc__
        """ setPrintProgram(self, arg__1: str) -> None """
        pass

    def setPrintRange(self, range): # real signature unknown; restored from __doc__
        """ setPrintRange(self, range: PySide2.QtPrintSupport.QPrinter.PrintRange) -> None """
        pass

    def setResolution(self, arg__1): # real signature unknown; restored from __doc__
        """ setResolution(self, arg__1: int) -> None """
        pass

    def setWinPageSize(self, winPageSize): # real signature unknown; restored from __doc__
        """ setWinPageSize(self, winPageSize: int) -> None """
        pass

    def supportedPaperSources(self): # real signature unknown; restored from __doc__
        """ supportedPaperSources(self) -> typing.List[PySide2.QtPrintSupport.QPrinter.PaperSource] """
        pass

    def supportedResolutions(self): # real signature unknown; restored from __doc__
        """ supportedResolutions(self) -> typing.List[int] """
        pass

    def supportsMultipleCopies(self): # real signature unknown; restored from __doc__
        """ supportsMultipleCopies(self) -> bool """
        return False

    def toPage(self): # real signature unknown; restored from __doc__
        """ toPage(self) -> int """
        return 0

    def winPageSize(self): # real signature unknown; restored from __doc__
        """ winPageSize(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, mode=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Aborted = PySide2.QtPrintSupport.QPrinter.PrinterState.Aborted
    Active = PySide2.QtPrintSupport.QPrinter.PrinterState.Active
    AllPages = PySide2.QtPrintSupport.QPrinter.PrintRange.AllPages
    Auto = PySide2.QtPrintSupport.QPrinter.PaperSource.Auto
    Cassette = PySide2.QtPrintSupport.QPrinter.PaperSource.Cassette
    Cicero = PySide2.QtPrintSupport.QPrinter.Unit.Cicero
    Color = PySide2.QtPrintSupport.QPrinter.ColorMode.Color
    ColorMode = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.ColorMode'>"
    CurrentPage = PySide2.QtPrintSupport.QPrinter.PrintRange.CurrentPage
    CustomSource = PySide2.QtPrintSupport.QPrinter.PaperSource.CustomSource
    DevicePixel = PySide2.QtPrintSupport.QPrinter.Unit.DevicePixel
    Didot = PySide2.QtPrintSupport.QPrinter.Unit.Didot
    DuplexAuto = PySide2.QtPrintSupport.QPrinter.DuplexMode.DuplexAuto
    DuplexLongSide = PySide2.QtPrintSupport.QPrinter.DuplexMode.DuplexLongSide
    DuplexMode = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.DuplexMode'>"
    DuplexNone = PySide2.QtPrintSupport.QPrinter.DuplexMode.DuplexNone
    DuplexShortSide = PySide2.QtPrintSupport.QPrinter.DuplexMode.DuplexShortSide
    Envelope = PySide2.QtPrintSupport.QPrinter.PaperSource.Envelope
    EnvelopeManual = PySide2.QtPrintSupport.QPrinter.PaperSource.EnvelopeManual
    Error = PySide2.QtPrintSupport.QPrinter.PrinterState.Error
    FirstPageFirst = PySide2.QtPrintSupport.QPrinter.PageOrder.FirstPageFirst
    FormSource = PySide2.QtPrintSupport.QPrinter.PaperSource.FormSource
    GrayScale = PySide2.QtPrintSupport.QPrinter.ColorMode.GrayScale
    HighResolution = PySide2.QtPrintSupport.QPrinter.PrinterMode.HighResolution
    Idle = PySide2.QtPrintSupport.QPrinter.PrinterState.Idle
    Inch = PySide2.QtPrintSupport.QPrinter.Unit.Inch
    Landscape = PySide2.QtPrintSupport.QPrinter.Orientation.Landscape
    LargeCapacity = PySide2.QtPrintSupport.QPrinter.PaperSource.LargeCapacity
    LargeFormat = PySide2.QtPrintSupport.QPrinter.PaperSource.LargeFormat
    LastPageFirst = PySide2.QtPrintSupport.QPrinter.PageOrder.LastPageFirst
    LastPaperSource = PySide2.QtPrintSupport.QPrinter.PaperSource.LastPaperSource
    Lower = PySide2.QtPrintSupport.QPrinter.PaperSource.Lower
    Manual = PySide2.QtPrintSupport.QPrinter.PaperSource.Manual
    MaxPageSource = PySide2.QtPrintSupport.QPrinter.PaperSource.MaxPageSource
    Middle = PySide2.QtPrintSupport.QPrinter.PaperSource.Middle
    Millimeter = PySide2.QtPrintSupport.QPrinter.Unit.Millimeter
    NativeFormat = PySide2.QtPrintSupport.QPrinter.OutputFormat.NativeFormat
    OnlyOne = PySide2.QtPrintSupport.QPrinter.PaperSource.OnlyOne
    Orientation = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.Orientation'>"
    OutputFormat = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.OutputFormat'>"
    PageOrder = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.PageOrder'>"
    PageRange = PySide2.QtPrintSupport.QPrinter.PrintRange.PageRange
    PaperSource = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.PaperSource'>"
    PdfFormat = PySide2.QtPrintSupport.QPrinter.OutputFormat.PdfFormat
    Pica = PySide2.QtPrintSupport.QPrinter.Unit.Pica
    Point = PySide2.QtPrintSupport.QPrinter.Unit.Point
    Portrait = PySide2.QtPrintSupport.QPrinter.Orientation.Portrait
    PrinterMode = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.PrinterMode'>"
    PrinterResolution = PySide2.QtPrintSupport.QPrinter.PrinterMode.PrinterResolution
    PrinterState = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.PrinterState'>"
    PrintRange = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.PrintRange'>"
    ScreenResolution = PySide2.QtPrintSupport.QPrinter.PrinterMode.ScreenResolution
    Selection = PySide2.QtPrintSupport.QPrinter.PrintRange.Selection
    SmallFormat = PySide2.QtPrintSupport.QPrinter.PaperSource.SmallFormat
    Tractor = PySide2.QtPrintSupport.QPrinter.PaperSource.Tractor
    Unit = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrinter.Unit'>"
    Upper = PySide2.QtPrintSupport.QPrinter.PaperSource.Upper


class QPrinterInfo(__Shiboken.Object):
    """
    QPrinterInfo(self) -> None
    QPrinterInfo(self, other: PySide2.QtPrintSupport.QPrinterInfo) -> None
    QPrinterInfo(self, printer: PySide2.QtPrintSupport.QPrinter) -> None
    """
    def availablePrinterNames(self): # real signature unknown; restored from __doc__
        """ availablePrinterNames() -> typing.List[str] """
        pass

    def availablePrinters(self): # real signature unknown; restored from __doc__
        """ availablePrinters() -> typing.List[PySide2.QtPrintSupport.QPrinterInfo] """
        pass

    def defaultColorMode(self): # real signature unknown; restored from __doc__
        """ defaultColorMode(self) -> PySide2.QtPrintSupport.QPrinter.ColorMode """
        pass

    def defaultDuplexMode(self): # real signature unknown; restored from __doc__
        """ defaultDuplexMode(self) -> PySide2.QtPrintSupport.QPrinter.DuplexMode """
        pass

    def defaultPageSize(self): # real signature unknown; restored from __doc__
        """ defaultPageSize(self) -> PySide2.QtGui.QPageSize """
        pass

    def defaultPrinter(self): # real signature unknown; restored from __doc__
        """ defaultPrinter() -> PySide2.QtPrintSupport.QPrinterInfo """
        pass

    def defaultPrinterName(self): # real signature unknown; restored from __doc__
        """ defaultPrinterName() -> str """
        return ""

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def isDefault(self): # real signature unknown; restored from __doc__
        """ isDefault(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isRemote(self): # real signature unknown; restored from __doc__
        """ isRemote(self) -> bool """
        return False

    def location(self): # real signature unknown; restored from __doc__
        """ location(self) -> str """
        return ""

    def makeAndModel(self): # real signature unknown; restored from __doc__
        """ makeAndModel(self) -> str """
        return ""

    def maximumPhysicalPageSize(self): # real signature unknown; restored from __doc__
        """ maximumPhysicalPageSize(self) -> PySide2.QtGui.QPageSize """
        pass

    def minimumPhysicalPageSize(self): # real signature unknown; restored from __doc__
        """ minimumPhysicalPageSize(self) -> PySide2.QtGui.QPageSize """
        pass

    def printerInfo(self, printerName): # real signature unknown; restored from __doc__
        """ printerInfo(printerName: str) -> PySide2.QtPrintSupport.QPrinterInfo """
        pass

    def printerName(self): # real signature unknown; restored from __doc__
        """ printerName(self) -> str """
        return ""

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState """
        pass

    def supportedColorModes(self): # real signature unknown; restored from __doc__
        """ supportedColorModes(self) -> typing.List[PySide2.QtPrintSupport.QPrinter.ColorMode] """
        pass

    def supportedDuplexModes(self): # real signature unknown; restored from __doc__
        """ supportedDuplexModes(self) -> typing.List[PySide2.QtPrintSupport.QPrinter.DuplexMode] """
        pass

    def supportedPageSizes(self): # real signature unknown; restored from __doc__
        """ supportedPageSizes(self) -> typing.List[PySide2.QtGui.QPageSize] """
        pass

    def supportedPaperSizes(self): # real signature unknown; restored from __doc__
        """ supportedPaperSizes(self) -> typing.List[PySide2.QtGui.QPagedPaintDevice.PageSize] """
        pass

    def supportedResolutions(self): # real signature unknown; restored from __doc__
        """ supportedResolutions(self) -> typing.List[int] """
        pass

    def supportedSizesWithNames(self): # real signature unknown; restored from __doc__
        """ supportedSizesWithNames(self) -> typing.List[typing.Tuple[str, PySide2.QtCore.QSizeF]] """
        pass

    def supportsCustomPageSizes(self): # real signature unknown; restored from __doc__
        """ supportsCustomPageSizes(self) -> bool """
        return False

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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


class QPrintPreviewDialog(__PySide2_QtWidgets.QDialog):
    """
    QPrintPreviewDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QPrintPreviewDialog(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    """
    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) -> None """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def paintRequested(self, *args, **kwargs): # real signature unknown
        pass

    def printer(self): # real signature unknown; restored from __doc__
        """ printer(self) -> PySide2.QtPrintSupport.QPrinter """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025A0187CCC0>'


class QPrintPreviewWidget(__PySide2_QtWidgets.QWidget):
    """
    QPrintPreviewWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QPrintPreviewWidget(self, printer: PySide2.QtPrintSupport.QPrinter, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    """
    def currentPage(self): # real signature unknown; restored from __doc__
        """ currentPage(self) -> int """
        return 0

    def fitInView(self): # real signature unknown; restored from __doc__
        """ fitInView(self) -> None """
        pass

    def fitToWidth(self): # real signature unknown; restored from __doc__
        """ fitToWidth(self) -> None """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtPrintSupport.QPrinter.Orientation """
        pass

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def paintRequested(self, *args, **kwargs): # real signature unknown
        pass

    def previewChanged(self, *args, **kwargs): # real signature unknown
        pass

    def print_(self): # real signature unknown; restored from __doc__
        """ print_(self) -> None """
        pass

    def setAllPagesViewMode(self): # real signature unknown; restored from __doc__
        """ setAllPagesViewMode(self) -> None """
        pass

    def setCurrentPage(self, pageNumber): # real signature unknown; restored from __doc__
        """ setCurrentPage(self, pageNumber: int) -> None """
        pass

    def setFacingPagesViewMode(self): # real signature unknown; restored from __doc__
        """ setFacingPagesViewMode(self) -> None """
        pass

    def setLandscapeOrientation(self): # real signature unknown; restored from __doc__
        """ setLandscapeOrientation(self) -> None """
        pass

    def setOrientation(self, orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, orientation: PySide2.QtPrintSupport.QPrinter.Orientation) -> None """
        pass

    def setPortraitOrientation(self): # real signature unknown; restored from __doc__
        """ setPortraitOrientation(self) -> None """
        pass

    def setSinglePageViewMode(self): # real signature unknown; restored from __doc__
        """ setSinglePageViewMode(self) -> None """
        pass

    def setViewMode(self, viewMode): # real signature unknown; restored from __doc__
        """ setViewMode(self, viewMode: PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def setZoomFactor(self, zoomFactor): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, zoomFactor: float) -> None """
        pass

    def setZoomMode(self, zoomMode): # real signature unknown; restored from __doc__
        """ setZoomMode(self, zoomMode: PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode) -> None """
        pass

    def updatePreview(self): # real signature unknown; restored from __doc__
        """ updatePreview(self) -> None """
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode """
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

    def zoomIn(self, zoom=1.1): # real signature unknown; restored from __doc__
        """ zoomIn(self, zoom: float = 1.1) -> None """
        pass

    def zoomMode(self): # real signature unknown; restored from __doc__
        """ zoomMode(self) -> PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode """
        pass

    def zoomOut(self, zoom=1.1): # real signature unknown; restored from __doc__
        """ zoomOut(self, zoom: float = 1.1) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AllPagesView = PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode.AllPagesView
    CustomZoom = PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode.CustomZoom
    FacingPagesView = PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode.FacingPagesView
    FitInView = PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode.FitInView
    FitToWidth = PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode.FitToWidth
    SinglePageView = PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode.SinglePageView
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025A0187CBC0>'
    ViewMode = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode'>"
    ZoomMode = None # (!) real value is "<class 'PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode'>"


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025A007517B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtPrintSupport', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025A007517B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtPrintSupport.cp310-win_amd64.pyd')"

