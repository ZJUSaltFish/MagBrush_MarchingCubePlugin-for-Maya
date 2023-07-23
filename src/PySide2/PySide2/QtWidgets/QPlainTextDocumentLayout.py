# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QPlainTextDocumentLayout(__PySide2_QtGui.QAbstractTextDocumentLayout):
    """ QPlainTextDocumentLayout(self, document: PySide2.QtGui.QTextDocument) -> None """
    def blockBoundingRect(self, block): # real signature unknown; restored from __doc__
        """ blockBoundingRect(self, block: PySide2.QtGui.QTextBlock) -> PySide2.QtCore.QRectF """
        pass

    def cursorWidth(self): # real signature unknown; restored from __doc__
        """ cursorWidth(self) -> int """
        return 0

    def documentChanged(self, from_, arg__2, charsAdded): # real signature unknown; restored from __doc__
        """ documentChanged(self, from_: int, arg__2: int, charsAdded: int) -> None """
        pass

    def documentSize(self): # real signature unknown; restored from __doc__
        """ documentSize(self) -> PySide2.QtCore.QSizeF """
        pass

    def draw(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ draw(self, arg__1: PySide2.QtGui.QPainter, arg__2: PySide2.QtGui.QAbstractTextDocumentLayout.PaintContext) -> None """
        pass

    def ensureBlockLayout(self, block): # real signature unknown; restored from __doc__
        """ ensureBlockLayout(self, block: PySide2.QtGui.QTextBlock) -> None """
        pass

    def frameBoundingRect(self, arg__1): # real signature unknown; restored from __doc__
        """ frameBoundingRect(self, arg__1: PySide2.QtGui.QTextFrame) -> PySide2.QtCore.QRectF """
        pass

    def hitTest(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ hitTest(self, arg__1: PySide2.QtCore.QPointF, arg__2: PySide2.QtCore.Qt.HitTestAccuracy) -> int """
        return 0

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def requestUpdate(self): # real signature unknown; restored from __doc__
        """ requestUpdate(self) -> None """
        pass

    def setCursorWidth(self, width): # real signature unknown; restored from __doc__
        """ setCursorWidth(self, width: int) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, document): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50796EC0>'


