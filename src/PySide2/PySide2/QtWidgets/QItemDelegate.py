# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractItemDelegate import QAbstractItemDelegate

class QItemDelegate(QAbstractItemDelegate):
    """ QItemDelegate(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def createEditor(self, parent, option, index): # real signature unknown; restored from __doc__
        """ createEditor(self, parent: PySide2.QtWidgets.QWidget, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QWidget """
        pass

    def decoration(self, option, variant): # real signature unknown; restored from __doc__
        """ decoration(self, option: PySide2.QtWidgets.QStyleOptionViewItem, variant: typing.Any) -> PySide2.QtGui.QPixmap """
        pass

    def doCheck(self, option, bounding, variant): # real signature unknown; restored from __doc__
        """ doCheck(self, option: PySide2.QtWidgets.QStyleOptionViewItem, bounding: PySide2.QtCore.QRect, variant: typing.Any) -> PySide2.QtCore.QRect """
        pass

    def drawBackground(self, painter, option, index): # real signature unknown; restored from __doc__
        """ drawBackground(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def drawCheck(self, painter, option, rect, state): # real signature unknown; restored from __doc__
        """ drawCheck(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionViewItem, rect: PySide2.QtCore.QRect, state: PySide2.QtCore.Qt.CheckState) -> None """
        pass

    def drawDecoration(self, painter, option, rect, pixmap): # real signature unknown; restored from __doc__
        """ drawDecoration(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionViewItem, rect: PySide2.QtCore.QRect, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def drawDisplay(self, painter, option, rect, text): # real signature unknown; restored from __doc__
        """ drawDisplay(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionViewItem, rect: PySide2.QtCore.QRect, text: str) -> None """
        pass

    def drawFocus(self, painter, option, rect): # real signature unknown; restored from __doc__
        """ drawFocus(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionViewItem, rect: PySide2.QtCore.QRect) -> None """
        pass

    def editorEvent(self, event, model, option, index): # real signature unknown; restored from __doc__
        """ editorEvent(self, event: PySide2.QtCore.QEvent, model: PySide2.QtCore.QAbstractItemModel, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def eventFilter(self, p_object, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, object: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def hasClipping(self): # real signature unknown; restored from __doc__
        """ hasClipping(self) -> bool """
        return False

    def itemEditorFactory(self): # real signature unknown; restored from __doc__
        """ itemEditorFactory(self) -> PySide2.QtWidgets.QItemEditorFactory """
        pass

    def paint(self, painter, option, index): # real signature unknown; restored from __doc__
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def rect(self, option, index, role): # real signature unknown; restored from __doc__
        """ rect(self, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex, role: int) -> PySide2.QtCore.QRect """
        pass

    def selectedPixmap(self, pixmap, palette, enabled): # real signature unknown; restored from __doc__
        """ selectedPixmap(pixmap: PySide2.QtGui.QPixmap, palette: PySide2.QtGui.QPalette, enabled: bool) -> PySide2.QtGui.QPixmap """
        pass

    def setClipping(self, clip): # real signature unknown; restored from __doc__
        """ setClipping(self, clip: bool) -> None """
        pass

    def setEditorData(self, editor, index): # real signature unknown; restored from __doc__
        """ setEditorData(self, editor: PySide2.QtWidgets.QWidget, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setItemEditorFactory(self, factory): # real signature unknown; restored from __doc__
        """ setItemEditorFactory(self, factory: PySide2.QtWidgets.QItemEditorFactory) -> None """
        pass

    def setModelData(self, editor, model, index): # real signature unknown; restored from __doc__
        """ setModelData(self, editor: PySide2.QtWidgets.QWidget, model: PySide2.QtCore.QAbstractItemModel, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setOptions(self, index, option): # real signature unknown; restored from __doc__
        """ setOptions(self, index: PySide2.QtCore.QModelIndex, option: PySide2.QtWidgets.QStyleOptionViewItem) -> PySide2.QtWidgets.QStyleOptionViewItem """
        pass

    def sizeHint(self, option, index): # real signature unknown; restored from __doc__
        """ sizeHint(self, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize """
        pass

    def textRectangle(self, painter, rect, font, text): # real signature unknown; restored from __doc__
        """ textRectangle(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, font: PySide2.QtGui.QFont, text: str) -> PySide2.QtCore.QRect """
        pass

    def updateEditorGeometry(self, editor, option, index): # real signature unknown; restored from __doc__
        """ updateEditorGeometry(self, editor: PySide2.QtWidgets.QWidget, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> None """
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50783600>'


