# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSyntaxHighlighter(__PySide2_QtCore.QObject):
    """
    QSyntaxHighlighter(self, parent: PySide2.QtCore.QObject) -> None
    QSyntaxHighlighter(self, parent: PySide2.QtGui.QTextDocument) -> None
    """
    def currentBlock(self): # real signature unknown; restored from __doc__
        """ currentBlock(self) -> PySide2.QtGui.QTextBlock """
        pass

    def currentBlockState(self): # real signature unknown; restored from __doc__
        """ currentBlockState(self) -> int """
        return 0

    def currentBlockUserData(self): # real signature unknown; restored from __doc__
        """ currentBlockUserData(self) -> PySide2.QtGui.QTextBlockUserData """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> PySide2.QtGui.QTextDocument """
        pass

    def format(self, pos): # real signature unknown; restored from __doc__
        """ format(self, pos: int) -> PySide2.QtGui.QTextCharFormat """
        pass

    def highlightBlock(self, text): # real signature unknown; restored from __doc__
        """ highlightBlock(self, text: str) -> None """
        pass

    def previousBlockState(self): # real signature unknown; restored from __doc__
        """ previousBlockState(self) -> int """
        return 0

    def rehighlight(self): # real signature unknown; restored from __doc__
        """ rehighlight(self) -> None """
        pass

    def rehighlightBlock(self, block): # real signature unknown; restored from __doc__
        """ rehighlightBlock(self, block: PySide2.QtGui.QTextBlock) -> None """
        pass

    def setCurrentBlockState(self, newState): # real signature unknown; restored from __doc__
        """ setCurrentBlockState(self, newState: int) -> None """
        pass

    def setCurrentBlockUserData(self, data): # real signature unknown; restored from __doc__
        """ setCurrentBlockUserData(self, data: PySide2.QtGui.QTextBlockUserData) -> None """
        pass

    def setDocument(self, doc): # real signature unknown; restored from __doc__
        """ setDocument(self, doc: PySide2.QtGui.QTextDocument) -> None """
        pass

    def setFormat(self, start, count, color): # real signature unknown; restored from __doc__
        """
        setFormat(self, start: int, count: int, color: PySide2.QtGui.QColor) -> None
        setFormat(self, start: int, count: int, font: PySide2.QtGui.QFont) -> None
        setFormat(self, start: int, count: int, format: PySide2.QtGui.QTextCharFormat) -> None
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00830A40>'


