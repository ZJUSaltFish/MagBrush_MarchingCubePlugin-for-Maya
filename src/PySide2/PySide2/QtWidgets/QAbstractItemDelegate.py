# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QAbstractItemDelegate(__PySide2_QtCore.QObject):
    """ QAbstractItemDelegate(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def closeEditor(self, *args, **kwargs): # real signature unknown
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, parent, option, index): # real signature unknown; restored from __doc__
        """ createEditor(self, parent: PySide2.QtWidgets.QWidget, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QWidget """
        pass

    def destroyEditor(self, editor, index): # real signature unknown; restored from __doc__
        """ destroyEditor(self, editor: PySide2.QtWidgets.QWidget, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def editorEvent(self, event, model, option, index): # real signature unknown; restored from __doc__
        """ editorEvent(self, event: PySide2.QtCore.QEvent, model: PySide2.QtCore.QAbstractItemModel, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def elidedText(self, fontMetrics, width, mode, text): # real signature unknown; restored from __doc__
        """ elidedText(fontMetrics: PySide2.QtGui.QFontMetrics, width: int, mode: PySide2.QtCore.Qt.TextElideMode, text: str) -> str """
        return ""

    def helpEvent(self, event, view, option, index): # real signature unknown; restored from __doc__
        """ helpEvent(self, event: PySide2.QtGui.QHelpEvent, view: PySide2.QtWidgets.QAbstractItemView, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def paint(self, painter, option, index): # real signature unknown; restored from __doc__
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def paintingRoles(self): # real signature unknown; restored from __doc__
        """ paintingRoles(self) -> typing.List[int] """
        pass

    def setEditorData(self, editor, index): # real signature unknown; restored from __doc__
        """ setEditorData(self, editor: PySide2.QtWidgets.QWidget, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setModelData(self, editor, model, index): # real signature unknown; restored from __doc__
        """ setModelData(self, editor: PySide2.QtWidgets.QWidget, model: PySide2.QtCore.QAbstractItemModel, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def sizeHint(self, option, index): # real signature unknown; restored from __doc__
        """ sizeHint(self, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize """
        pass

    def sizeHintChanged(self, *args, **kwargs): # real signature unknown
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

    EditNextItem = PySide2.QtWidgets.QAbstractItemDelegate.EndEditHint.EditNextItem
    EditPreviousItem = PySide2.QtWidgets.QAbstractItemDelegate.EndEditHint.EditPreviousItem
    EndEditHint = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemDelegate.EndEditHint'>"
    NoHint = PySide2.QtWidgets.QAbstractItemDelegate.EndEditHint.NoHint
    RevertModelCache = PySide2.QtWidgets.QAbstractItemDelegate.EndEditHint.RevertModelCache
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50783200>'
    SubmitModelCache = PySide2.QtWidgets.QAbstractItemDelegate.EndEditHint.SubmitModelCache


