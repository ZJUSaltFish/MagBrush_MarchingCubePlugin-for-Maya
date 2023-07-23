# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAbstractTextDocumentLayout(__PySide2_QtCore.QObject):
    """ QAbstractTextDocumentLayout(self, doc: PySide2.QtGui.QTextDocument) -> None """
    def anchorAt(self, pos): # real signature unknown; restored from __doc__
        """ anchorAt(self, pos: PySide2.QtCore.QPointF) -> str """
        return ""

    def blockBoundingRect(self, block): # real signature unknown; restored from __doc__
        """ blockBoundingRect(self, block: PySide2.QtGui.QTextBlock) -> PySide2.QtCore.QRectF """
        pass

    def blockWithMarkerAt(self, pos): # real signature unknown; restored from __doc__
        """ blockWithMarkerAt(self, pos: PySide2.QtCore.QPointF) -> PySide2.QtGui.QTextBlock """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> PySide2.QtGui.QTextDocument """
        pass

    def documentChanged(self, from_, charsRemoved, charsAdded): # real signature unknown; restored from __doc__
        """ documentChanged(self, from_: int, charsRemoved: int, charsAdded: int) -> None """
        pass

    def documentSize(self): # real signature unknown; restored from __doc__
        """ documentSize(self) -> PySide2.QtCore.QSizeF """
        pass

    def documentSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def draw(self, painter, context): # real signature unknown; restored from __doc__
        """ draw(self, painter: PySide2.QtGui.QPainter, context: PySide2.QtGui.QAbstractTextDocumentLayout.PaintContext) -> None """
        pass

    def drawInlineObject(self, painter, rect, p_object, posInDocument, format): # real signature unknown; restored from __doc__
        """ drawInlineObject(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRectF, object: PySide2.QtGui.QTextInlineObject, posInDocument: int, format: PySide2.QtGui.QTextFormat) -> None """
        pass

    def format(self, pos): # real signature unknown; restored from __doc__
        """ format(self, pos: int) -> PySide2.QtGui.QTextCharFormat """
        pass

    def formatAt(self, pos): # real signature unknown; restored from __doc__
        """ formatAt(self, pos: PySide2.QtCore.QPointF) -> PySide2.QtGui.QTextFormat """
        pass

    def formatIndex(self, pos): # real signature unknown; restored from __doc__
        """ formatIndex(self, pos: int) -> int """
        return 0

    def frameBoundingRect(self, frame): # real signature unknown; restored from __doc__
        """ frameBoundingRect(self, frame: PySide2.QtGui.QTextFrame) -> PySide2.QtCore.QRectF """
        pass

    def handlerForObject(self, objectType): # real signature unknown; restored from __doc__
        """ handlerForObject(self, objectType: int) -> PySide2.QtGui.QTextObjectInterface """
        pass

    def hitTest(self, point, accuracy): # real signature unknown; restored from __doc__
        """ hitTest(self, point: PySide2.QtCore.QPointF, accuracy: PySide2.QtCore.Qt.HitTestAccuracy) -> int """
        return 0

    def imageAt(self, pos): # real signature unknown; restored from __doc__
        """ imageAt(self, pos: PySide2.QtCore.QPointF) -> str """
        return ""

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def pageCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> PySide2.QtGui.QPaintDevice """
        pass

    def positionInlineObject(self, item, posInDocument, format): # real signature unknown; restored from __doc__
        """ positionInlineObject(self, item: PySide2.QtGui.QTextInlineObject, posInDocument: int, format: PySide2.QtGui.QTextFormat) -> None """
        pass

    def registerHandler(self, objectType, component): # real signature unknown; restored from __doc__
        """ registerHandler(self, objectType: int, component: PySide2.QtCore.QObject) -> None """
        pass

    def resizeInlineObject(self, item, posInDocument, format): # real signature unknown; restored from __doc__
        """ resizeInlineObject(self, item: PySide2.QtGui.QTextInlineObject, posInDocument: int, format: PySide2.QtGui.QTextFormat) -> None """
        pass

    def setPaintDevice(self, device): # real signature unknown; restored from __doc__
        """ setPaintDevice(self, device: PySide2.QtGui.QPaintDevice) -> None """
        pass

    def unregisterHandler(self, objectType, component, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ unregisterHandler(self, objectType: int, component: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def updateBlock(self, *args, **kwargs): # real signature unknown
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

    PaintContext = None # (!) real value is "<class 'PySide2.QtGui.QAbstractTextDocumentLayout.PaintContext'>"
    Selection = None # (!) real value is "<class 'PySide2.QtGui.QAbstractTextDocumentLayout.Selection'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00831700>'


