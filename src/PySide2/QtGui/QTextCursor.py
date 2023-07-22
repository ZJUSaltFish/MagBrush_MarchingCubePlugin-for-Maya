# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTextCursor(__Shiboken.Object):
    """
    QTextCursor(self) -> None
    QTextCursor(self, block: PySide2.QtGui.QTextBlock) -> None
    QTextCursor(self, cursor: PySide2.QtGui.QTextCursor) -> None
    QTextCursor(self, document: PySide2.QtGui.QTextDocument) -> None
    QTextCursor(self, frame: PySide2.QtGui.QTextFrame) -> None
    """
    def anchor(self): # real signature unknown; restored from __doc__
        """ anchor(self) -> int """
        return 0

    def atBlockEnd(self): # real signature unknown; restored from __doc__
        """ atBlockEnd(self) -> bool """
        return False

    def atBlockStart(self): # real signature unknown; restored from __doc__
        """ atBlockStart(self) -> bool """
        return False

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def atStart(self): # real signature unknown; restored from __doc__
        """ atStart(self) -> bool """
        return False

    def beginEditBlock(self): # real signature unknown; restored from __doc__
        """ beginEditBlock(self) -> None """
        pass

    def block(self): # real signature unknown; restored from __doc__
        """ block(self) -> PySide2.QtGui.QTextBlock """
        pass

    def blockCharFormat(self): # real signature unknown; restored from __doc__
        """ blockCharFormat(self) -> PySide2.QtGui.QTextCharFormat """
        pass

    def blockFormat(self): # real signature unknown; restored from __doc__
        """ blockFormat(self) -> PySide2.QtGui.QTextBlockFormat """
        pass

    def blockNumber(self): # real signature unknown; restored from __doc__
        """ blockNumber(self) -> int """
        return 0

    def charFormat(self): # real signature unknown; restored from __doc__
        """ charFormat(self) -> PySide2.QtGui.QTextCharFormat """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) -> None """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def createList(self, format): # real signature unknown; restored from __doc__
        """
        createList(self, format: PySide2.QtGui.QTextListFormat) -> PySide2.QtGui.QTextList
        createList(self, style: PySide2.QtGui.QTextListFormat.Style) -> PySide2.QtGui.QTextList
        """
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> PySide2.QtGui.QTextFrame """
        pass

    def currentList(self): # real signature unknown; restored from __doc__
        """ currentList(self) -> PySide2.QtGui.QTextList """
        pass

    def currentTable(self): # real signature unknown; restored from __doc__
        """ currentTable(self) -> PySide2.QtGui.QTextTable """
        pass

    def deleteChar(self): # real signature unknown; restored from __doc__
        """ deleteChar(self) -> None """
        pass

    def deletePreviousChar(self): # real signature unknown; restored from __doc__
        """ deletePreviousChar(self) -> None """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> PySide2.QtGui.QTextDocument """
        pass

    def endEditBlock(self): # real signature unknown; restored from __doc__
        """ endEditBlock(self) -> None """
        pass

    def hasComplexSelection(self): # real signature unknown; restored from __doc__
        """ hasComplexSelection(self) -> bool """
        return False

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def insertBlock(self): # real signature unknown; restored from __doc__
        """
        insertBlock(self) -> None
        insertBlock(self, format: PySide2.QtGui.QTextBlockFormat) -> None
        insertBlock(self, format: PySide2.QtGui.QTextBlockFormat, charFormat: PySide2.QtGui.QTextCharFormat) -> None
        """
        pass

    def insertFragment(self, fragment): # real signature unknown; restored from __doc__
        """ insertFragment(self, fragment: PySide2.QtGui.QTextDocumentFragment) -> None """
        pass

    def insertFrame(self, format): # real signature unknown; restored from __doc__
        """ insertFrame(self, format: PySide2.QtGui.QTextFrameFormat) -> PySide2.QtGui.QTextFrame """
        pass

    def insertHtml(self, html): # real signature unknown; restored from __doc__
        """ insertHtml(self, html: str) -> None """
        pass

    def insertImage(self, format): # real signature unknown; restored from __doc__
        """
        insertImage(self, format: PySide2.QtGui.QTextImageFormat) -> None
        insertImage(self, format: PySide2.QtGui.QTextImageFormat, alignment: PySide2.QtGui.QTextFrameFormat.Position) -> None
        insertImage(self, image: PySide2.QtGui.QImage, name: str = '') -> None
        insertImage(self, name: str) -> None
        """
        pass

    def insertList(self, format): # real signature unknown; restored from __doc__
        """
        insertList(self, format: PySide2.QtGui.QTextListFormat) -> PySide2.QtGui.QTextList
        insertList(self, style: PySide2.QtGui.QTextListFormat.Style) -> PySide2.QtGui.QTextList
        """
        pass

    def insertTable(self, rows, cols): # real signature unknown; restored from __doc__
        """
        insertTable(self, rows: int, cols: int) -> PySide2.QtGui.QTextTable
        insertTable(self, rows: int, cols: int, format: PySide2.QtGui.QTextTableFormat) -> PySide2.QtGui.QTextTable
        """
        pass

    def insertText(self, text): # real signature unknown; restored from __doc__
        """
        insertText(self, text: str) -> None
        insertText(self, text: str, format: PySide2.QtGui.QTextCharFormat) -> None
        """
        pass

    def isCopyOf(self, other): # real signature unknown; restored from __doc__
        """ isCopyOf(self, other: PySide2.QtGui.QTextCursor) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def joinPreviousEditBlock(self): # real signature unknown; restored from __doc__
        """ joinPreviousEditBlock(self) -> None """
        pass

    def keepPositionOnInsert(self): # real signature unknown; restored from __doc__
        """ keepPositionOnInsert(self) -> bool """
        return False

    def mergeBlockCharFormat(self, modifier): # real signature unknown; restored from __doc__
        """ mergeBlockCharFormat(self, modifier: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def mergeBlockFormat(self, modifier): # real signature unknown; restored from __doc__
        """ mergeBlockFormat(self, modifier: PySide2.QtGui.QTextBlockFormat) -> None """
        pass

    def mergeCharFormat(self, modifier): # real signature unknown; restored from __doc__
        """ mergeCharFormat(self, modifier: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def movePosition(self, op, arg__2=None, n=1): # real signature unknown; restored from __doc__
        """ movePosition(self, op: PySide2.QtGui.QTextCursor.MoveOperation, arg__2: PySide2.QtGui.QTextCursor.MoveMode = PySide2.QtGui.QTextCursor.MoveMode.MoveAnchor, n: int = 1) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionInBlock(self): # real signature unknown; restored from __doc__
        """ positionInBlock(self) -> int """
        return 0

    def removeSelectedText(self): # real signature unknown; restored from __doc__
        """ removeSelectedText(self) -> None """
        pass

    def select(self, selection): # real signature unknown; restored from __doc__
        """ select(self, selection: PySide2.QtGui.QTextCursor.SelectionType) -> None """
        pass

    def selectedTableCells(self): # real signature unknown; restored from __doc__
        """ selectedTableCells(self) -> typing.Tuple[int, int, int, int] """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selection(self): # real signature unknown; restored from __doc__
        """ selection(self) -> PySide2.QtGui.QTextDocumentFragment """
        pass

    def selectionEnd(self): # real signature unknown; restored from __doc__
        """ selectionEnd(self) -> int """
        return 0

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ selectionStart(self) -> int """
        return 0

    def setBlockCharFormat(self, format): # real signature unknown; restored from __doc__
        """ setBlockCharFormat(self, format: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def setBlockFormat(self, format): # real signature unknown; restored from __doc__
        """ setBlockFormat(self, format: PySide2.QtGui.QTextBlockFormat) -> None """
        pass

    def setCharFormat(self, format): # real signature unknown; restored from __doc__
        """ setCharFormat(self, format: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def setKeepPositionOnInsert(self, b): # real signature unknown; restored from __doc__
        """ setKeepPositionOnInsert(self, b: bool) -> None """
        pass

    def setPosition(self, pos, mode=None): # real signature unknown; restored from __doc__
        """ setPosition(self, pos: int, mode: PySide2.QtGui.QTextCursor.MoveMode = PySide2.QtGui.QTextCursor.MoveMode.MoveAnchor) -> None """
        pass

    def setVerticalMovementX(self, x): # real signature unknown; restored from __doc__
        """ setVerticalMovementX(self, x: int) -> None """
        pass

    def setVisualNavigation(self, b): # real signature unknown; restored from __doc__
        """ setVisualNavigation(self, b: bool) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QTextCursor) -> None """
        pass

    def verticalMovementX(self): # real signature unknown; restored from __doc__
        """ verticalMovementX(self) -> int """
        return 0

    def visualNavigation(self): # real signature unknown; restored from __doc__
        """ visualNavigation(self) -> bool """
        return False

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    BlockUnderCursor = PySide2.QtGui.QTextCursor.SelectionType.BlockUnderCursor
    Document = PySide2.QtGui.QTextCursor.SelectionType.Document
    Down = PySide2.QtGui.QTextCursor.MoveOperation.Down
    End = PySide2.QtGui.QTextCursor.MoveOperation.End
    EndOfBlock = PySide2.QtGui.QTextCursor.MoveOperation.EndOfBlock
    EndOfLine = PySide2.QtGui.QTextCursor.MoveOperation.EndOfLine
    EndOfWord = PySide2.QtGui.QTextCursor.MoveOperation.EndOfWord
    KeepAnchor = PySide2.QtGui.QTextCursor.MoveMode.KeepAnchor
    Left = PySide2.QtGui.QTextCursor.MoveOperation.Left
    LineUnderCursor = PySide2.QtGui.QTextCursor.SelectionType.LineUnderCursor
    MoveAnchor = PySide2.QtGui.QTextCursor.MoveMode.MoveAnchor
    MoveMode = None # (!) real value is "<class 'PySide2.QtGui.QTextCursor.MoveMode'>"
    MoveOperation = None # (!) real value is "<class 'PySide2.QtGui.QTextCursor.MoveOperation'>"
    NextBlock = PySide2.QtGui.QTextCursor.MoveOperation.NextBlock
    NextCell = PySide2.QtGui.QTextCursor.MoveOperation.NextCell
    NextCharacter = PySide2.QtGui.QTextCursor.MoveOperation.NextCharacter
    NextRow = PySide2.QtGui.QTextCursor.MoveOperation.NextRow
    NextWord = PySide2.QtGui.QTextCursor.MoveOperation.NextWord
    NoMove = PySide2.QtGui.QTextCursor.MoveOperation.NoMove
    PreviousBlock = PySide2.QtGui.QTextCursor.MoveOperation.PreviousBlock
    PreviousCell = PySide2.QtGui.QTextCursor.MoveOperation.PreviousCell
    PreviousCharacter = PySide2.QtGui.QTextCursor.MoveOperation.PreviousCharacter
    PreviousRow = PySide2.QtGui.QTextCursor.MoveOperation.PreviousRow
    PreviousWord = PySide2.QtGui.QTextCursor.MoveOperation.PreviousWord
    Right = PySide2.QtGui.QTextCursor.MoveOperation.Right
    SelectionType = None # (!) real value is "<class 'PySide2.QtGui.QTextCursor.SelectionType'>"
    Start = PySide2.QtGui.QTextCursor.MoveOperation.Start
    StartOfBlock = PySide2.QtGui.QTextCursor.MoveOperation.StartOfBlock
    StartOfLine = PySide2.QtGui.QTextCursor.MoveOperation.StartOfLine
    StartOfWord = PySide2.QtGui.QTextCursor.MoveOperation.StartOfWord
    Up = PySide2.QtGui.QTextCursor.MoveOperation.Up
    WordLeft = PySide2.QtGui.QTextCursor.MoveOperation.WordLeft
    WordRight = PySide2.QtGui.QTextCursor.MoveOperation.WordRight
    WordUnderCursor = PySide2.QtGui.QTextCursor.SelectionType.WordUnderCursor
    __hash__ = None


