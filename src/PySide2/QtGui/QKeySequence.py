# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QKeySequence(__Shiboken.Object):
    """
    QKeySequence(self) -> None
    QKeySequence(self, k1: int, k2: int = 0, k3: int = 0, k4: int = 0) -> None
    QKeySequence(self, key: PySide2.QtGui.QKeySequence.StandardKey) -> None
    QKeySequence(self, key: str, format: PySide2.QtGui.QKeySequence.SequenceFormat = PySide2.QtGui.QKeySequence.SequenceFormat.NativeText) -> None
    QKeySequence(self, ks: PySide2.QtGui.QKeySequence) -> None
    """
    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def fromString(self, p_str, format=None): # real signature unknown; restored from __doc__
        """ fromString(str: str, format: PySide2.QtGui.QKeySequence.SequenceFormat = PySide2.QtGui.QKeySequence.SequenceFormat.PortableText) -> PySide2.QtGui.QKeySequence """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def keyBindings(self, key): # real signature unknown; restored from __doc__
        """ keyBindings(key: PySide2.QtGui.QKeySequence.StandardKey) -> typing.List[PySide2.QtGui.QKeySequence] """
        pass

    def listFromString(self, p_str, format=None): # real signature unknown; restored from __doc__
        """ listFromString(str: str, format: PySide2.QtGui.QKeySequence.SequenceFormat = PySide2.QtGui.QKeySequence.SequenceFormat.PortableText) -> typing.List[PySide2.QtGui.QKeySequence] """
        pass

    def listToString(self, p_list, PySide2_QtGui_QKeySequence=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ listToString(list: typing.Sequence[PySide2.QtGui.QKeySequence], format: PySide2.QtGui.QKeySequence.SequenceFormat = PySide2.QtGui.QKeySequence.SequenceFormat.PortableText) -> str """
        pass

    def matches(self, seq): # real signature unknown; restored from __doc__
        """ matches(self, seq: PySide2.QtGui.QKeySequence) -> PySide2.QtGui.QKeySequence.SequenceMatch """
        pass

    def mnemonic(self, text): # real signature unknown; restored from __doc__
        """ mnemonic(text: str) -> PySide2.QtGui.QKeySequence """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QKeySequence) -> None """
        pass

    def toString(self, format=None): # real signature unknown; restored from __doc__
        """ toString(self, format: PySide2.QtGui.QKeySequence.SequenceFormat = PySide2.QtGui.QKeySequence.SequenceFormat.PortableText) -> str """
        return ""

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __lshift__(self, in_): # real signature unknown; restored from __doc__
        """
        __lshift__(self, in_: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__(self) -> object """
        return object()

    def __repr__(self): # real signature unknown; restored from __doc__
        """
        __repr__(self) -> object
        
        Return repr(self).
        """
        return object()

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, out): # real signature unknown; restored from __doc__
        """
        __rshift__(self, out: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    AddTab = PySide2.QtGui.QKeySequence.StandardKey.AddTab
    Back = PySide2.QtGui.QKeySequence.StandardKey.Back
    Backspace = PySide2.QtGui.QKeySequence.StandardKey.Backspace
    Bold = PySide2.QtGui.QKeySequence.StandardKey.Bold
    Cancel = PySide2.QtGui.QKeySequence.StandardKey.Cancel
    Close = PySide2.QtGui.QKeySequence.StandardKey.Close
    Copy = PySide2.QtGui.QKeySequence.StandardKey.Copy
    Cut = PySide2.QtGui.QKeySequence.StandardKey.Cut
    Delete = PySide2.QtGui.QKeySequence.StandardKey.Delete
    DeleteCompleteLine = PySide2.QtGui.QKeySequence.StandardKey.DeleteCompleteLine
    DeleteEndOfLine = PySide2.QtGui.QKeySequence.StandardKey.DeleteEndOfLine
    DeleteEndOfWord = PySide2.QtGui.QKeySequence.StandardKey.DeleteEndOfWord
    DeleteStartOfWord = PySide2.QtGui.QKeySequence.StandardKey.DeleteStartOfWord
    Deselect = PySide2.QtGui.QKeySequence.StandardKey.Deselect
    ExactMatch = PySide2.QtGui.QKeySequence.SequenceMatch.ExactMatch
    Find = PySide2.QtGui.QKeySequence.StandardKey.Find
    FindNext = PySide2.QtGui.QKeySequence.StandardKey.FindNext
    FindPrevious = PySide2.QtGui.QKeySequence.StandardKey.FindPrevious
    Forward = PySide2.QtGui.QKeySequence.StandardKey.Forward
    FullScreen = PySide2.QtGui.QKeySequence.StandardKey.FullScreen
    HelpContents = PySide2.QtGui.QKeySequence.StandardKey.HelpContents
    InsertLineSeparator = PySide2.QtGui.QKeySequence.StandardKey.InsertLineSeparator
    InsertParagraphSeparator = PySide2.QtGui.QKeySequence.StandardKey.InsertParagraphSeparator
    Italic = PySide2.QtGui.QKeySequence.StandardKey.Italic
    MoveToEndOfBlock = PySide2.QtGui.QKeySequence.StandardKey.MoveToEndOfBlock
    MoveToEndOfDocument = PySide2.QtGui.QKeySequence.StandardKey.MoveToEndOfDocument
    MoveToEndOfLine = PySide2.QtGui.QKeySequence.StandardKey.MoveToEndOfLine
    MoveToNextChar = PySide2.QtGui.QKeySequence.StandardKey.MoveToNextChar
    MoveToNextLine = PySide2.QtGui.QKeySequence.StandardKey.MoveToNextLine
    MoveToNextPage = PySide2.QtGui.QKeySequence.StandardKey.MoveToNextPage
    MoveToNextWord = PySide2.QtGui.QKeySequence.StandardKey.MoveToNextWord
    MoveToPreviousChar = PySide2.QtGui.QKeySequence.StandardKey.MoveToPreviousChar
    MoveToPreviousLine = PySide2.QtGui.QKeySequence.StandardKey.MoveToPreviousLine
    MoveToPreviousPage = PySide2.QtGui.QKeySequence.StandardKey.MoveToPreviousPage
    MoveToPreviousWord = PySide2.QtGui.QKeySequence.StandardKey.MoveToPreviousWord
    MoveToStartOfBlock = PySide2.QtGui.QKeySequence.StandardKey.MoveToStartOfBlock
    MoveToStartOfDocument = PySide2.QtGui.QKeySequence.StandardKey.MoveToStartOfDocument
    MoveToStartOfLine = PySide2.QtGui.QKeySequence.StandardKey.MoveToStartOfLine
    NativeText = PySide2.QtGui.QKeySequence.SequenceFormat.NativeText
    New = PySide2.QtGui.QKeySequence.StandardKey.New
    NextChild = PySide2.QtGui.QKeySequence.StandardKey.NextChild
    NoMatch = PySide2.QtGui.QKeySequence.SequenceMatch.NoMatch
    Open = PySide2.QtGui.QKeySequence.StandardKey.Open
    PartialMatch = PySide2.QtGui.QKeySequence.SequenceMatch.PartialMatch
    Paste = PySide2.QtGui.QKeySequence.StandardKey.Paste
    PortableText = PySide2.QtGui.QKeySequence.SequenceFormat.PortableText
    Preferences = PySide2.QtGui.QKeySequence.StandardKey.Preferences
    PreviousChild = PySide2.QtGui.QKeySequence.StandardKey.PreviousChild
    Print = PySide2.QtGui.QKeySequence.StandardKey.Print
    Quit = PySide2.QtGui.QKeySequence.StandardKey.Quit
    Redo = PySide2.QtGui.QKeySequence.StandardKey.Redo
    Refresh = PySide2.QtGui.QKeySequence.StandardKey.Refresh
    Replace = PySide2.QtGui.QKeySequence.StandardKey.Replace
    Save = PySide2.QtGui.QKeySequence.StandardKey.Save
    SaveAs = PySide2.QtGui.QKeySequence.StandardKey.SaveAs
    SelectAll = PySide2.QtGui.QKeySequence.StandardKey.SelectAll
    SelectEndOfBlock = PySide2.QtGui.QKeySequence.StandardKey.SelectEndOfBlock
    SelectEndOfDocument = PySide2.QtGui.QKeySequence.StandardKey.SelectEndOfDocument
    SelectEndOfLine = PySide2.QtGui.QKeySequence.StandardKey.SelectEndOfLine
    SelectNextChar = PySide2.QtGui.QKeySequence.StandardKey.SelectNextChar
    SelectNextLine = PySide2.QtGui.QKeySequence.StandardKey.SelectNextLine
    SelectNextPage = PySide2.QtGui.QKeySequence.StandardKey.SelectNextPage
    SelectNextWord = PySide2.QtGui.QKeySequence.StandardKey.SelectNextWord
    SelectPreviousChar = PySide2.QtGui.QKeySequence.StandardKey.SelectPreviousChar
    SelectPreviousLine = PySide2.QtGui.QKeySequence.StandardKey.SelectPreviousLine
    SelectPreviousPage = PySide2.QtGui.QKeySequence.StandardKey.SelectPreviousPage
    SelectPreviousWord = PySide2.QtGui.QKeySequence.StandardKey.SelectPreviousWord
    SelectStartOfBlock = PySide2.QtGui.QKeySequence.StandardKey.SelectStartOfBlock
    SelectStartOfDocument = PySide2.QtGui.QKeySequence.StandardKey.SelectStartOfDocument
    SelectStartOfLine = PySide2.QtGui.QKeySequence.StandardKey.SelectStartOfLine
    SequenceFormat = None # (!) real value is "<class 'PySide2.QtGui.QKeySequence.SequenceFormat'>"
    SequenceMatch = None # (!) real value is "<class 'PySide2.QtGui.QKeySequence.SequenceMatch'>"
    StandardKey = None # (!) real value is "<class 'PySide2.QtGui.QKeySequence.StandardKey'>"
    Underline = PySide2.QtGui.QKeySequence.StandardKey.Underline
    Undo = PySide2.QtGui.QKeySequence.StandardKey.Undo
    UnknownKey = PySide2.QtGui.QKeySequence.StandardKey.UnknownKey
    WhatsThis = PySide2.QtGui.QKeySequence.StandardKey.WhatsThis
    ZoomIn = PySide2.QtGui.QKeySequence.StandardKey.ZoomIn
    ZoomOut = PySide2.QtGui.QKeySequence.StandardKey.ZoomOut
    __hash__ = None


