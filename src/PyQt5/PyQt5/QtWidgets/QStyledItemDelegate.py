# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractItemDelegate import QAbstractItemDelegate

class QStyledItemDelegate(QAbstractItemDelegate):
    """ QStyledItemDelegate(parent: typing.Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, parent, option, index): # real signature unknown; restored from __doc__
        """ createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget """
        return QWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def displayText(self, value, locale): # real signature unknown; restored from __doc__
        """ displayText(self, value: Any, locale: QLocale) -> str """
        return ""

    def editorEvent(self, event, model, option, index): # real signature unknown; restored from __doc__
        """ editorEvent(self, event: QEvent, model: QAbstractItemModel, option: QStyleOptionViewItem, index: QModelIndex) -> bool """
        return False

    def eventFilter(self, p_object, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, object: QObject, event: QEvent) -> bool """
        return False

    def initStyleOption(self, option, index): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: QStyleOptionViewItem, index: QModelIndex) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemEditorFactory(self): # real signature unknown; restored from __doc__
        """ itemEditorFactory(self) -> QItemEditorFactory """
        return QItemEditorFactory

    def paint(self, painter, option, index): # real signature unknown; restored from __doc__
        """ paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, editor, index): # real signature unknown; restored from __doc__
        """ setEditorData(self, editor: QWidget, index: QModelIndex) """
        pass

    def setItemEditorFactory(self, factory): # real signature unknown; restored from __doc__
        """ setItemEditorFactory(self, factory: QItemEditorFactory) """
        pass

    def setModelData(self, editor, model, index): # real signature unknown; restored from __doc__
        """ setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex) """
        pass

    def sizeHint(self, option, index): # real signature unknown; restored from __doc__
        """ sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometry(self, editor, option, index): # real signature unknown; restored from __doc__
        """ updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QModelIndex) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


