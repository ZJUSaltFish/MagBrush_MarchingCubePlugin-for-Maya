# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTextDocument(__PySide2_QtCore.QObject):
    """
    QTextDocument(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QTextDocument(self, text: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def addResource(self, type, name, resource): # real signature unknown; restored from __doc__
        """ addResource(self, type: int, name: PySide2.QtCore.QUrl, resource: typing.Any) -> None """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) -> None """
        pass

    def allFormats(self): # real signature unknown; restored from __doc__
        """ allFormats(self) -> typing.List[PySide2.QtGui.QTextFormat] """
        pass

    def availableRedoSteps(self): # real signature unknown; restored from __doc__
        """ availableRedoSteps(self) -> int """
        return 0

    def availableUndoSteps(self): # real signature unknown; restored from __doc__
        """ availableUndoSteps(self) -> int """
        return 0

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def baseUrlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def begin(self): # real signature unknown; restored from __doc__
        """ begin(self) -> PySide2.QtGui.QTextBlock """
        pass

    def blockCount(self): # real signature unknown; restored from __doc__
        """ blockCount(self) -> int """
        return 0

    def blockCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def characterAt(self, pos): # real signature unknown; restored from __doc__
        """ characterAt(self, pos: int) -> str """
        return ""

    def characterCount(self): # real signature unknown; restored from __doc__
        """ characterCount(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearUndoRedoStacks(self, historyToClear=None): # real signature unknown; restored from __doc__
        """ clearUndoRedoStacks(self, historyToClear: PySide2.QtGui.QTextDocument.Stacks = PySide2.QtGui.QTextDocument.Stacks.UndoAndRedoStacks) -> None """
        pass

    def clone(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ clone(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> PySide2.QtGui.QTextDocument """
        pass

    def contentsChange(self, *args, **kwargs): # real signature unknown
        pass

    def contentsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def createObject(self, f): # real signature unknown; restored from __doc__
        """ createObject(self, f: PySide2.QtGui.QTextFormat) -> PySide2.QtGui.QTextObject """
        pass

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ defaultCursorMoveStyle(self) -> PySide2.QtCore.Qt.CursorMoveStyle """
        pass

    def defaultFont(self): # real signature unknown; restored from __doc__
        """ defaultFont(self) -> PySide2.QtGui.QFont """
        pass

    def defaultStyleSheet(self): # real signature unknown; restored from __doc__
        """ defaultStyleSheet(self) -> str """
        return ""

    def defaultTextOption(self): # real signature unknown; restored from __doc__
        """ defaultTextOption(self) -> PySide2.QtGui.QTextOption """
        pass

    def documentLayout(self): # real signature unknown; restored from __doc__
        """ documentLayout(self) -> PySide2.QtGui.QAbstractTextDocumentLayout """
        pass

    def documentLayoutChanged(self, *args, **kwargs): # real signature unknown
        pass

    def documentMargin(self): # real signature unknown; restored from __doc__
        """ documentMargin(self) -> float """
        return 0.0

    def drawContents(self, painter, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawContents(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRectF = Default(QRectF)) -> None """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> PySide2.QtGui.QTextBlock """
        pass

    def find(self, expr, cursor, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        find(self, expr: PySide2.QtCore.QRegExp, cursor: PySide2.QtGui.QTextCursor, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor
        find(self, expr: PySide2.QtCore.QRegExp, from_: int = 0, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor
        find(self, expr: PySide2.QtCore.QRegularExpression, cursor: PySide2.QtGui.QTextCursor, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor
        find(self, expr: PySide2.QtCore.QRegularExpression, from_: int = 0, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor
        find(self, subString: str, cursor: PySide2.QtGui.QTextCursor, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor
        find(self, subString: str, from_: int = 0, options: PySide2.QtGui.QTextDocument.FindFlags = Default(QTextDocument.FindFlags)) -> PySide2.QtGui.QTextCursor
        """
        pass

    def findBlock(self, pos): # real signature unknown; restored from __doc__
        """ findBlock(self, pos: int) -> PySide2.QtGui.QTextBlock """
        pass

    def findBlockByLineNumber(self, blockNumber): # real signature unknown; restored from __doc__
        """ findBlockByLineNumber(self, blockNumber: int) -> PySide2.QtGui.QTextBlock """
        pass

    def findBlockByNumber(self, blockNumber): # real signature unknown; restored from __doc__
        """ findBlockByNumber(self, blockNumber: int) -> PySide2.QtGui.QTextBlock """
        pass

    def firstBlock(self): # real signature unknown; restored from __doc__
        """ firstBlock(self) -> PySide2.QtGui.QTextBlock """
        pass

    def frameAt(self, pos): # real signature unknown; restored from __doc__
        """ frameAt(self, pos: int) -> PySide2.QtGui.QTextFrame """
        pass

    def idealWidth(self): # real signature unknown; restored from __doc__
        """ idealWidth(self) -> float """
        return 0.0

    def indentWidth(self): # real signature unknown; restored from __doc__
        """ indentWidth(self) -> float """
        return 0.0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ isRedoAvailable(self) -> bool """
        return False

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ isUndoAvailable(self) -> bool """
        return False

    def isUndoRedoEnabled(self): # real signature unknown; restored from __doc__
        """ isUndoRedoEnabled(self) -> bool """
        return False

    def lastBlock(self): # real signature unknown; restored from __doc__
        """ lastBlock(self) -> PySide2.QtGui.QTextBlock """
        pass

    def lineCount(self): # real signature unknown; restored from __doc__
        """ lineCount(self) -> int """
        return 0

    def loadResource(self, type, name): # real signature unknown; restored from __doc__
        """ loadResource(self, type: int, name: PySide2.QtCore.QUrl) -> typing.Any """
        pass

    def markContentsDirty(self, from_, length): # real signature unknown; restored from __doc__
        """ markContentsDirty(self, from_: int, length: int) -> None """
        pass

    def maximumBlockCount(self): # real signature unknown; restored from __doc__
        """ maximumBlockCount(self) -> int """
        return 0

    def metaInformation(self, info): # real signature unknown; restored from __doc__
        """ metaInformation(self, info: PySide2.QtGui.QTextDocument.MetaInformation) -> str """
        return ""

    def modificationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def object(self, objectIndex): # real signature unknown; restored from __doc__
        """ object(self, objectIndex: int) -> PySide2.QtGui.QTextObject """
        pass

    def objectForFormat(self, arg__1): # real signature unknown; restored from __doc__
        """ objectForFormat(self, arg__1: PySide2.QtGui.QTextFormat) -> PySide2.QtGui.QTextObject """
        pass

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def pageSize(self): # real signature unknown; restored from __doc__
        """ pageSize(self) -> PySide2.QtCore.QSizeF """
        pass

    def print_(self, printer): # real signature unknown; restored from __doc__
        """ print_(self, printer: PySide2.QtGui.QPagedPaintDevice) -> None """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """
        redo(self) -> None
        redo(self, cursor: PySide2.QtGui.QTextCursor) -> None
        """
        pass

    def redoAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def resource(self, type, name): # real signature unknown; restored from __doc__
        """ resource(self, type: int, name: PySide2.QtCore.QUrl) -> typing.Any """
        pass

    def revision(self): # real signature unknown; restored from __doc__
        """ revision(self) -> int """
        return 0

    def rootFrame(self): # real signature unknown; restored from __doc__
        """ rootFrame(self) -> PySide2.QtGui.QTextFrame """
        pass

    def setBaseUrl(self, url): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def setDefaultCursorMoveStyle(self, style): # real signature unknown; restored from __doc__
        """ setDefaultCursorMoveStyle(self, style: PySide2.QtCore.Qt.CursorMoveStyle) -> None """
        pass

    def setDefaultFont(self, font): # real signature unknown; restored from __doc__
        """ setDefaultFont(self, font: PySide2.QtGui.QFont) -> None """
        pass

    def setDefaultStyleSheet(self, sheet): # real signature unknown; restored from __doc__
        """ setDefaultStyleSheet(self, sheet: str) -> None """
        pass

    def setDefaultTextOption(self, option): # real signature unknown; restored from __doc__
        """ setDefaultTextOption(self, option: PySide2.QtGui.QTextOption) -> None """
        pass

    def setDocumentLayout(self, layout): # real signature unknown; restored from __doc__
        """ setDocumentLayout(self, layout: PySide2.QtGui.QAbstractTextDocumentLayout) -> None """
        pass

    def setDocumentMargin(self, margin): # real signature unknown; restored from __doc__
        """ setDocumentMargin(self, margin: float) -> None """
        pass

    def setHtml(self, html): # real signature unknown; restored from __doc__
        """ setHtml(self, html: str) -> None """
        pass

    def setIndentWidth(self, width): # real signature unknown; restored from __doc__
        """ setIndentWidth(self, width: float) -> None """
        pass

    def setMarkdown(self, markdown, features=None): # real signature unknown; restored from __doc__
        """ setMarkdown(self, markdown: str, features: PySide2.QtGui.QTextDocument.MarkdownFeatures = PySide2.QtGui.QTextDocument.MarkdownFeature.MarkdownDialectGitHub) -> None """
        pass

    def setMaximumBlockCount(self, maximum): # real signature unknown; restored from __doc__
        """ setMaximumBlockCount(self, maximum: int) -> None """
        pass

    def setMetaInformation(self, info, arg__2): # real signature unknown; restored from __doc__
        """ setMetaInformation(self, info: PySide2.QtGui.QTextDocument.MetaInformation, arg__2: str) -> None """
        pass

    def setModified(self, m=True): # real signature unknown; restored from __doc__
        """ setModified(self, m: bool = True) -> None """
        pass

    def setPageSize(self, size): # real signature unknown; restored from __doc__
        """ setPageSize(self, size: PySide2.QtCore.QSizeF) -> None """
        pass

    def setPlainText(self, text): # real signature unknown; restored from __doc__
        """ setPlainText(self, text: str) -> None """
        pass

    def setTextWidth(self, width): # real signature unknown; restored from __doc__
        """ setTextWidth(self, width: float) -> None """
        pass

    def setUndoRedoEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setUndoRedoEnabled(self, enable: bool) -> None """
        pass

    def setUseDesignMetrics(self, b): # real signature unknown; restored from __doc__
        """ setUseDesignMetrics(self, b: bool) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSizeF """
        pass

    def textWidth(self): # real signature unknown; restored from __doc__
        """ textWidth(self) -> float """
        return 0.0

    def toHtml(self, encoding=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toHtml(self, encoding: PySide2.QtCore.QByteArray = Default(QByteArray)) -> str """
        pass

    def toMarkdown(self, features=None): # real signature unknown; restored from __doc__
        """ toMarkdown(self, features: PySide2.QtGui.QTextDocument.MarkdownFeatures = PySide2.QtGui.QTextDocument.MarkdownFeature.MarkdownDialectGitHub) -> str """
        return ""

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def toRawText(self): # real signature unknown; restored from __doc__
        """ toRawText(self) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """
        undo(self) -> None
        undo(self, cursor: PySide2.QtGui.QTextCursor) -> None
        """
        pass

    def undoAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def undoCommandAdded(self, *args, **kwargs): # real signature unknown
        pass

    def useDesignMetrics(self): # real signature unknown; restored from __doc__
        """ useDesignMetrics(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    DocumentTitle = PySide2.QtGui.QTextDocument.MetaInformation.DocumentTitle
    DocumentUrl = PySide2.QtGui.QTextDocument.MetaInformation.DocumentUrl
    FindBackward = PySide2.QtGui.QTextDocument.FindFlag.FindBackward
    FindCaseSensitively = PySide2.QtGui.QTextDocument.FindFlag.FindCaseSensitively
    FindFlag = None # (!) real value is "<class 'PySide2.QtGui.QTextDocument.FindFlag'>"
    FindFlags = None # (!) real value is "<class 'PySide2.QtGui.QTextDocument.FindFlags'>"
    FindWholeWords = PySide2.QtGui.QTextDocument.FindFlag.FindWholeWords
    HtmlResource = PySide2.QtGui.QTextDocument.ResourceType.HtmlResource
    ImageResource = PySide2.QtGui.QTextDocument.ResourceType.ImageResource
    MarkdownDialectCommonMark = PySide2.QtGui.QTextDocument.MarkdownFeature.MarkdownDialectCommonMark
    MarkdownDialectGitHub = PySide2.QtGui.QTextDocument.MarkdownFeature.MarkdownDialectGitHub
    MarkdownFeature = None # (!) real value is "<class 'PySide2.QtGui.QTextDocument.MarkdownFeature'>"
    MarkdownFeatures = None # (!) real value is "<class 'PySide2.QtGui.QTextDocument.MarkdownFeatures'>"
    MarkdownNoHTML = PySide2.QtGui.QTextDocument.MarkdownFeature.MarkdownNoHTML
    MarkdownResource = PySide2.QtGui.QTextDocument.ResourceType.MarkdownResource
    MetaInformation = None # (!) real value is "<class 'PySide2.QtGui.QTextDocument.MetaInformation'>"
    RedoStack = PySide2.QtGui.QTextDocument.Stacks.RedoStack
    ResourceType = None # (!) real value is "<class 'PySide2.QtGui.QTextDocument.ResourceType'>"
    Stacks = None # (!) real value is "<class 'PySide2.QtGui.QTextDocument.Stacks'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F008733C0>'
    StyleSheetResource = PySide2.QtGui.QTextDocument.ResourceType.StyleSheetResource
    UndoAndRedoStacks = PySide2.QtGui.QTextDocument.Stacks.UndoAndRedoStacks
    UndoStack = PySide2.QtGui.QTextDocument.Stacks.UndoStack
    UnknownResource = PySide2.QtGui.QTextDocument.ResourceType.UnknownResource
    UserResource = PySide2.QtGui.QTextDocument.ResourceType.UserResource


