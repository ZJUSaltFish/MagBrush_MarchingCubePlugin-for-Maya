# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QTextFrame import QTextFrame

class QTextTable(QTextFrame):
    """ QTextTable(self, doc: PySide2.QtGui.QTextDocument) -> None """
    def appendColumns(self, count): # real signature unknown; restored from __doc__
        """ appendColumns(self, count: int) -> None """
        pass

    def appendRows(self, count): # real signature unknown; restored from __doc__
        """ appendRows(self, count: int) -> None """
        pass

    def cellAt(self, c): # real signature unknown; restored from __doc__
        """
        cellAt(self, c: PySide2.QtGui.QTextCursor) -> PySide2.QtGui.QTextTableCell
        cellAt(self, position: int) -> PySide2.QtGui.QTextTableCell
        cellAt(self, row: int, col: int) -> PySide2.QtGui.QTextTableCell
        """
        pass

    def columns(self): # real signature unknown; restored from __doc__
        """ columns(self) -> int """
        return 0

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QTextTableFormat """
        pass

    def insertColumns(self, pos, num): # real signature unknown; restored from __doc__
        """ insertColumns(self, pos: int, num: int) -> None """
        pass

    def insertRows(self, pos, num): # real signature unknown; restored from __doc__
        """ insertRows(self, pos: int, num: int) -> None """
        pass

    def mergeCells(self, cursor): # real signature unknown; restored from __doc__
        """
        mergeCells(self, cursor: PySide2.QtGui.QTextCursor) -> None
        mergeCells(self, row: int, col: int, numRows: int, numCols: int) -> None
        """
        pass

    def removeColumns(self, pos, num): # real signature unknown; restored from __doc__
        """ removeColumns(self, pos: int, num: int) -> None """
        pass

    def removeRows(self, pos, num): # real signature unknown; restored from __doc__
        """ removeRows(self, pos: int, num: int) -> None """
        pass

    def resize(self, rows, cols): # real signature unknown; restored from __doc__
        """ resize(self, rows: int, cols: int) -> None """
        pass

    def rowEnd(self, c): # real signature unknown; restored from __doc__
        """ rowEnd(self, c: PySide2.QtGui.QTextCursor) -> PySide2.QtGui.QTextCursor """
        pass

    def rows(self): # real signature unknown; restored from __doc__
        """ rows(self) -> int """
        return 0

    def rowStart(self, c): # real signature unknown; restored from __doc__
        """ rowStart(self, c: PySide2.QtGui.QTextCursor) -> PySide2.QtGui.QTextCursor """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """
        setFormat(self, format: PySide2.QtGui.QTextFormat) -> None
        setFormat(self, format: PySide2.QtGui.QTextTableFormat) -> None
        """
        pass

    def splitCell(self, row, col, numRows, numCols): # real signature unknown; restored from __doc__
        """ splitCell(self, row: int, col: int, numRows: int, numCols: int) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, doc): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00846E80>'


