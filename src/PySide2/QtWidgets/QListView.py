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

class QListView(QAbstractItemView):
    """ QListView(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def batchSize(self): # real signature unknown; restored from __doc__
        """ batchSize(self) -> int """
        return 0

    def clearPropertyFlags(self): # real signature unknown; restored from __doc__
        """ clearPropertyFlags(self) -> None """
        pass

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ contentsSize(self) -> PySide2.QtCore.QSize """
        pass

    def currentChanged(self, current, previous): # real signature unknown; restored from __doc__
        """ currentChanged(self, current: PySide2.QtCore.QModelIndex, previous: PySide2.QtCore.QModelIndex) -> None """
        pass

    def dataChanged(self, topLeft, bottomRight, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, topLeft: PySide2.QtCore.QModelIndex, bottomRight: PySide2.QtCore.QModelIndex, roles: typing.List[int] = Default(QVector< int >)) -> None """
        pass

    def doItemsLayout(self): # real signature unknown; restored from __doc__
        """ doItemsLayout(self) -> None """
        pass

    def dragLeaveEvent(self, e): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, e: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMoveEvent(self, e): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, e: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def dropEvent(self, e): # real signature unknown; restored from __doc__
        """ dropEvent(self, e: PySide2.QtGui.QDropEvent) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def flow(self): # real signature unknown; restored from __doc__
        """ flow(self) -> PySide2.QtWidgets.QListView.Flow """
        pass

    def gridSize(self): # real signature unknown; restored from __doc__
        """ gridSize(self) -> PySide2.QtCore.QSize """
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def indexAt(self, p): # real signature unknown; restored from __doc__
        """ indexAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QModelIndex """
        pass

    def indexesMoved(self, *args, **kwargs): # real signature unknown
        pass

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isRowHidden(self, row): # real signature unknown; restored from __doc__
        """ isRowHidden(self, row: int) -> bool """
        return False

    def isSelectionRectVisible(self): # real signature unknown; restored from __doc__
        """ isSelectionRectVisible(self) -> bool """
        return False

    def isWrapping(self): # real signature unknown; restored from __doc__
        """ isWrapping(self) -> bool """
        return False

    def itemAlignment(self): # real signature unknown; restored from __doc__
        """ itemAlignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def layoutMode(self): # real signature unknown; restored from __doc__
        """ layoutMode(self) -> PySide2.QtWidgets.QListView.LayoutMode """
        pass

    def modelColumn(self): # real signature unknown; restored from __doc__
        """ modelColumn(self) -> int """
        return 0

    def mouseMoveEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def moveCursor(self, cursorAction, modifiers): # real signature unknown; restored from __doc__
        """ moveCursor(self, cursorAction: PySide2.QtWidgets.QAbstractItemView.CursorAction, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> PySide2.QtCore.QModelIndex """
        pass

    def movement(self): # real signature unknown; restored from __doc__
        """ movement(self) -> PySide2.QtWidgets.QListView.Movement """
        pass

    def paintEvent(self, e): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def rectForIndex(self, index): # real signature unknown; restored from __doc__
        """ rectForIndex(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QRect """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resizeContents(self, width, height): # real signature unknown; restored from __doc__
        """ resizeContents(self, width: int, height: int) -> None """
        pass

    def resizeEvent(self, e): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ resizeMode(self) -> PySide2.QtWidgets.QListView.ResizeMode """
        pass

    def rowsAboutToBeRemoved(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, parent: PySide2.QtCore.QModelIndex, start: int, end: int) -> None """
        pass

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: PySide2.QtCore.QModelIndex, start: int, end: int) -> None """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) -> None """
        pass

    def scrollTo(self, index, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, index: PySide2.QtCore.QModelIndex, hint: PySide2.QtWidgets.QAbstractItemView.ScrollHint = PySide2.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible) -> None """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> typing.List[int] """
        pass

    def selectionChanged(self, selected, deselected): # real signature unknown; restored from __doc__
        """ selectionChanged(self, selected: PySide2.QtCore.QItemSelection, deselected: PySide2.QtCore.QItemSelection) -> None """
        pass

    def setBatchSize(self, batchSize): # real signature unknown; restored from __doc__
        """ setBatchSize(self, batchSize: int) -> None """
        pass

    def setFlow(self, flow): # real signature unknown; restored from __doc__
        """ setFlow(self, flow: PySide2.QtWidgets.QListView.Flow) -> None """
        pass

    def setGridSize(self, size): # real signature unknown; restored from __doc__
        """ setGridSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setItemAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setItemAlignment(self, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setLayoutMode(self, mode): # real signature unknown; restored from __doc__
        """ setLayoutMode(self, mode: PySide2.QtWidgets.QListView.LayoutMode) -> None """
        pass

    def setModelColumn(self, column): # real signature unknown; restored from __doc__
        """ setModelColumn(self, column: int) -> None """
        pass

    def setMovement(self, movement): # real signature unknown; restored from __doc__
        """ setMovement(self, movement: PySide2.QtWidgets.QListView.Movement) -> None """
        pass

    def setPositionForIndex(self, position, index): # real signature unknown; restored from __doc__
        """ setPositionForIndex(self, position: PySide2.QtCore.QPoint, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setResizeMode(self, mode): # real signature unknown; restored from __doc__
        """ setResizeMode(self, mode: PySide2.QtWidgets.QListView.ResizeMode) -> None """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setRowHidden(self, row, hide): # real signature unknown; restored from __doc__
        """ setRowHidden(self, row: int, hide: bool) -> None """
        pass

    def setSelection(self, rect, command): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: PySide2.QtCore.QRect, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None """
        pass

    def setSelectionRectVisible(self, show): # real signature unknown; restored from __doc__
        """ setSelectionRectVisible(self, show: bool) -> None """
        pass

    def setSpacing(self, space): # real signature unknown; restored from __doc__
        """ setSpacing(self, space: int) -> None """
        pass

    def setUniformItemSizes(self, enable): # real signature unknown; restored from __doc__
        """ setUniformItemSizes(self, enable: bool) -> None """
        pass

    def setViewMode(self, mode): # real signature unknown; restored from __doc__
        """ setViewMode(self, mode: PySide2.QtWidgets.QListView.ViewMode) -> None """
        pass

    def setWordWrap(self, on): # real signature unknown; restored from __doc__
        """ setWordWrap(self, on: bool) -> None """
        pass

    def setWrapping(self, enable): # real signature unknown; restored from __doc__
        """ setWrapping(self, enable: bool) -> None """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def startDrag(self, supportedActions): # real signature unknown; restored from __doc__
        """ startDrag(self, supportedActions: PySide2.QtCore.Qt.DropActions) -> None """
        pass

    def timerEvent(self, e): # real signature unknown; restored from __doc__
        """ timerEvent(self, e: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def uniformItemSizes(self): # real signature unknown; restored from __doc__
        """ uniformItemSizes(self) -> bool """
        return False

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) -> None """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> PySide2.QtWidgets.QListView.ViewMode """
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ viewOptions(self) -> PySide2.QtWidgets.QStyleOptionViewItem """
        pass

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def visualRect(self, index): # real signature unknown; restored from __doc__
        """ visualRect(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QRect """
        pass

    def visualRegionForSelection(self, selection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, selection: PySide2.QtCore.QItemSelection) -> PySide2.QtGui.QRegion """
        pass

    def wheelEvent(self, e): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

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

    Adjust = PySide2.QtWidgets.QListView.ResizeMode.Adjust
    Batched = PySide2.QtWidgets.QListView.LayoutMode.Batched
    Fixed = PySide2.QtWidgets.QListView.ResizeMode.Fixed
    Flow = None # (!) real value is "<class 'PySide2.QtWidgets.QListView.Flow'>"
    Free = PySide2.QtWidgets.QListView.Movement.Free
    IconMode = PySide2.QtWidgets.QListView.ViewMode.IconMode
    LayoutMode = None # (!) real value is "<class 'PySide2.QtWidgets.QListView.LayoutMode'>"
    LeftToRight = PySide2.QtWidgets.QListView.Flow.LeftToRight
    ListMode = PySide2.QtWidgets.QListView.ViewMode.ListMode
    Movement = None # (!) real value is "<class 'PySide2.QtWidgets.QListView.Movement'>"
    ResizeMode = None # (!) real value is "<class 'PySide2.QtWidgets.QListView.ResizeMode'>"
    SinglePass = PySide2.QtWidgets.QListView.LayoutMode.SinglePass
    Snap = PySide2.QtWidgets.QListView.Movement.Snap
    Static = PySide2.QtWidgets.QListView.Movement.Static
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50803F00>'
    TopToBottom = PySide2.QtWidgets.QListView.Flow.TopToBottom
    ViewMode = None # (!) real value is "<class 'PySide2.QtWidgets.QListView.ViewMode'>"


