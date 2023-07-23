# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractItemView import QAbstractItemView

class QColumnView(QAbstractItemView):
    """ QColumnView(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def columnWidths(self): # real signature unknown; restored from __doc__
        """ columnWidths(self) -> typing.List[int] """
        pass

    def createColumn(self, rootIndex): # real signature unknown; restored from __doc__
        """ createColumn(self, rootIndex: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QAbstractItemView """
        pass

    def currentChanged(self, current, previous): # real signature unknown; restored from __doc__
        """ currentChanged(self, current: PySide2.QtCore.QModelIndex, previous: PySide2.QtCore.QModelIndex) -> None """
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def indexAt(self, point): # real signature unknown; restored from __doc__
        """ indexAt(self, point: PySide2.QtCore.QPoint) -> PySide2.QtCore.QModelIndex """
        pass

    def initializeColumn(self, column): # real signature unknown; restored from __doc__
        """ initializeColumn(self, column: PySide2.QtWidgets.QAbstractItemView) -> None """
        pass

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def moveCursor(self, cursorAction, modifiers): # real signature unknown; restored from __doc__
        """ moveCursor(self, cursorAction: PySide2.QtWidgets.QAbstractItemView.CursorAction, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> PySide2.QtCore.QModelIndex """
        pass

    def previewWidget(self): # real signature unknown; restored from __doc__
        """ previewWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def resizeGripsVisible(self): # real signature unknown; restored from __doc__
        """ resizeGripsVisible(self) -> bool """
        return False

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: PySide2.QtCore.QModelIndex, start: int, end: int) -> None """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) -> None """
        pass

    def scrollTo(self, index, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, index: PySide2.QtCore.QModelIndex, hint: PySide2.QtWidgets.QAbstractItemView.ScrollHint = PySide2.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible) -> None """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) -> None """
        pass

    def setColumnWidths(self, p_list, p_int=None): # real signature unknown; restored from __doc__
        """ setColumnWidths(self, list: typing.Sequence[int]) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setPreviewWidget(self, widget): # real signature unknown; restored from __doc__
        """ setPreviewWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setResizeGripsVisible(self, visible): # real signature unknown; restored from __doc__
        """ setResizeGripsVisible(self, visible: bool) -> None """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setSelection(self, rect, command): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: PySide2.QtCore.QRect, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None """
        pass

    def setSelectionModel(self, selectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: PySide2.QtCore.QItemSelectionModel) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def updatePreviewWidget(self, *args, **kwargs): # real signature unknown
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def visualRect(self, index): # real signature unknown; restored from __doc__
        """ visualRect(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QRect """
        pass

    def visualRegionForSelection(self, selection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, selection: PySide2.QtCore.QItemSelection) -> PySide2.QtGui.QRegion """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50802280>'


