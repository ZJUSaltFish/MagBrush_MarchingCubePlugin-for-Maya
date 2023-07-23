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

class QTreeView(QAbstractItemView):
    """ QTreeView(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def allColumnsShowFocus(self): # real signature unknown; restored from __doc__
        """ allColumnsShowFocus(self) -> bool """
        return False

    def autoExpandDelay(self): # real signature unknown; restored from __doc__
        """ autoExpandDelay(self) -> int """
        return 0

    def collapse(self, index): # real signature unknown; restored from __doc__
        """ collapse(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def collapseAll(self): # real signature unknown; restored from __doc__
        """ collapseAll(self) -> None """
        pass

    def collapsed(self, *args, **kwargs): # real signature unknown
        pass

    def columnAt(self, x): # real signature unknown; restored from __doc__
        """ columnAt(self, x: int) -> int """
        return 0

    def columnCountChanged(self, oldCount, newCount): # real signature unknown; restored from __doc__
        """ columnCountChanged(self, oldCount: int, newCount: int) -> None """
        pass

    def columnMoved(self): # real signature unknown; restored from __doc__
        """ columnMoved(self) -> None """
        pass

    def columnResized(self, column, oldSize, newSize): # real signature unknown; restored from __doc__
        """ columnResized(self, column: int, oldSize: int, newSize: int) -> None """
        pass

    def columnViewportPosition(self, column): # real signature unknown; restored from __doc__
        """ columnViewportPosition(self, column: int) -> int """
        return 0

    def columnWidth(self, column): # real signature unknown; restored from __doc__
        """ columnWidth(self, column: int) -> int """
        return 0

    def currentChanged(self, current, previous): # real signature unknown; restored from __doc__
        """ currentChanged(self, current: PySide2.QtCore.QModelIndex, previous: PySide2.QtCore.QModelIndex) -> None """
        pass

    def dataChanged(self, topLeft, bottomRight, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, topLeft: PySide2.QtCore.QModelIndex, bottomRight: PySide2.QtCore.QModelIndex, roles: typing.List[int] = Default(QVector< int >)) -> None """
        pass

    def doItemsLayout(self): # real signature unknown; restored from __doc__
        """ doItemsLayout(self) -> None """
        pass

    def dragMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def drawBranches(self, painter, rect, index): # real signature unknown; restored from __doc__
        """ drawBranches(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def drawRow(self, painter, options, index): # real signature unknown; restored from __doc__
        """ drawRow(self, painter: PySide2.QtGui.QPainter, options: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def drawTree(self, painter, region): # real signature unknown; restored from __doc__
        """ drawTree(self, painter: PySide2.QtGui.QPainter, region: PySide2.QtGui.QRegion) -> None """
        pass

    def expand(self, index): # real signature unknown; restored from __doc__
        """ expand(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def expandAll(self): # real signature unknown; restored from __doc__
        """ expandAll(self) -> None """
        pass

    def expanded(self, *args, **kwargs): # real signature unknown
        pass

    def expandRecursively(self, index, depth=-1): # real signature unknown; restored from __doc__
        """ expandRecursively(self, index: PySide2.QtCore.QModelIndex, depth: int = -1) -> None """
        pass

    def expandsOnDoubleClick(self): # real signature unknown; restored from __doc__
        """ expandsOnDoubleClick(self) -> bool """
        return False

    def expandToDepth(self, depth): # real signature unknown; restored from __doc__
        """ expandToDepth(self, depth: int) -> None """
        pass

    def header(self): # real signature unknown; restored from __doc__
        """ header(self) -> PySide2.QtWidgets.QHeaderView """
        pass

    def hideColumn(self, column): # real signature unknown; restored from __doc__
        """ hideColumn(self, column: int) -> None """
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, action: int) -> None """
        pass

    def indentation(self): # real signature unknown; restored from __doc__
        """ indentation(self) -> int """
        return 0

    def indexAbove(self, index): # real signature unknown; restored from __doc__
        """ indexAbove(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def indexAt(self, p): # real signature unknown; restored from __doc__
        """ indexAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QModelIndex """
        pass

    def indexBelow(self, index): # real signature unknown; restored from __doc__
        """ indexBelow(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def indexRowSizeHint(self, index): # real signature unknown; restored from __doc__
        """ indexRowSizeHint(self, index: PySide2.QtCore.QModelIndex) -> int """
        return 0

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isColumnHidden(self, column): # real signature unknown; restored from __doc__
        """ isColumnHidden(self, column: int) -> bool """
        return False

    def isExpanded(self, index): # real signature unknown; restored from __doc__
        """ isExpanded(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isFirstColumnSpanned(self, row, parent): # real signature unknown; restored from __doc__
        """ isFirstColumnSpanned(self, row: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isHeaderHidden(self): # real signature unknown; restored from __doc__
        """ isHeaderHidden(self) -> bool """
        return False

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isRowHidden(self, row, parent): # real signature unknown; restored from __doc__
        """ isRowHidden(self, row: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def itemsExpandable(self): # real signature unknown; restored from __doc__
        """ itemsExpandable(self) -> bool """
        return False

    def keyboardSearch(self, search): # real signature unknown; restored from __doc__
        """ keyboardSearch(self, search: str) -> None """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def mouseDoubleClickEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, event): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def moveCursor(self, cursorAction, modifiers): # real signature unknown; restored from __doc__
        """ moveCursor(self, cursorAction: PySide2.QtWidgets.QAbstractItemView.CursorAction, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> PySide2.QtCore.QModelIndex """
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def reexpand(self): # real signature unknown; restored from __doc__
        """ reexpand(self) -> None """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resetIndentation(self): # real signature unknown; restored from __doc__
        """ resetIndentation(self) -> None """
        pass

    def resizeColumnToContents(self, column): # real signature unknown; restored from __doc__
        """ resizeColumnToContents(self, column: int) -> None """
        pass

    def rootIsDecorated(self): # real signature unknown; restored from __doc__
        """ rootIsDecorated(self) -> bool """
        return False

    def rowHeight(self, index): # real signature unknown; restored from __doc__
        """ rowHeight(self, index: PySide2.QtCore.QModelIndex) -> int """
        return 0

    def rowsAboutToBeRemoved(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, parent: PySide2.QtCore.QModelIndex, start: int, end: int) -> None """
        pass

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: PySide2.QtCore.QModelIndex, start: int, end: int) -> None """
        pass

    def rowsRemoved(self, parent, first, last): # real signature unknown; restored from __doc__
        """ rowsRemoved(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
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

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> typing.List[int] """
        pass

    def selectionChanged(self, selected, deselected): # real signature unknown; restored from __doc__
        """ selectionChanged(self, selected: PySide2.QtCore.QItemSelection, deselected: PySide2.QtCore.QItemSelection) -> None """
        pass

    def setAllColumnsShowFocus(self, enable): # real signature unknown; restored from __doc__
        """ setAllColumnsShowFocus(self, enable: bool) -> None """
        pass

    def setAnimated(self, enable): # real signature unknown; restored from __doc__
        """ setAnimated(self, enable: bool) -> None """
        pass

    def setAutoExpandDelay(self, delay): # real signature unknown; restored from __doc__
        """ setAutoExpandDelay(self, delay: int) -> None """
        pass

    def setColumnHidden(self, column, hide): # real signature unknown; restored from __doc__
        """ setColumnHidden(self, column: int, hide: bool) -> None """
        pass

    def setColumnWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnWidth(self, column: int, width: int) -> None """
        pass

    def setExpanded(self, index, expand): # real signature unknown; restored from __doc__
        """ setExpanded(self, index: PySide2.QtCore.QModelIndex, expand: bool) -> None """
        pass

    def setExpandsOnDoubleClick(self, enable): # real signature unknown; restored from __doc__
        """ setExpandsOnDoubleClick(self, enable: bool) -> None """
        pass

    def setFirstColumnSpanned(self, row, parent, span): # real signature unknown; restored from __doc__
        """ setFirstColumnSpanned(self, row: int, parent: PySide2.QtCore.QModelIndex, span: bool) -> None """
        pass

    def setHeader(self, header): # real signature unknown; restored from __doc__
        """ setHeader(self, header: PySide2.QtWidgets.QHeaderView) -> None """
        pass

    def setHeaderHidden(self, hide): # real signature unknown; restored from __doc__
        """ setHeaderHidden(self, hide: bool) -> None """
        pass

    def setIndentation(self, i): # real signature unknown; restored from __doc__
        """ setIndentation(self, i: int) -> None """
        pass

    def setItemsExpandable(self, enable): # real signature unknown; restored from __doc__
        """ setItemsExpandable(self, enable: bool) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setRootIsDecorated(self, show): # real signature unknown; restored from __doc__
        """ setRootIsDecorated(self, show: bool) -> None """
        pass

    def setRowHidden(self, row, parent, hide): # real signature unknown; restored from __doc__
        """ setRowHidden(self, row: int, parent: PySide2.QtCore.QModelIndex, hide: bool) -> None """
        pass

    def setSelection(self, rect, command): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: PySide2.QtCore.QRect, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None """
        pass

    def setSelectionModel(self, selectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: PySide2.QtCore.QItemSelectionModel) -> None """
        pass

    def setSortingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, enable: bool) -> None """
        pass

    def setTreePosition(self, logicalIndex): # real signature unknown; restored from __doc__
        """ setTreePosition(self, logicalIndex: int) -> None """
        pass

    def setUniformRowHeights(self, uniform): # real signature unknown; restored from __doc__
        """ setUniformRowHeights(self, uniform: bool) -> None """
        pass

    def setWordWrap(self, on): # real signature unknown; restored from __doc__
        """ setWordWrap(self, on: bool) -> None """
        pass

    def showColumn(self, column): # real signature unknown; restored from __doc__
        """ showColumn(self, column: int) -> None """
        pass

    def sizeHintForColumn(self, column): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, column: int) -> int """
        return 0

    def sortByColumn(self, column): # real signature unknown; restored from __doc__
        """
        sortByColumn(self, column: int) -> None
        sortByColumn(self, column: int, order: PySide2.QtCore.Qt.SortOrder) -> None
        """
        pass

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def treePosition(self): # real signature unknown; restored from __doc__
        """ treePosition(self) -> int """
        return 0

    def uniformRowHeights(self): # real signature unknown; restored from __doc__
        """ uniformRowHeights(self) -> bool """
        return False

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) -> None """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarValueChanged(self, value): # real signature unknown; restored from __doc__
        """ verticalScrollbarValueChanged(self, value: int) -> None """
        pass

    def viewportEvent(self, event): # real signature unknown; restored from __doc__
        """ viewportEvent(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def visualRect(self, index): # real signature unknown; restored from __doc__
        """ visualRect(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QRect """
        pass

    def visualRegionForSelection(self, selection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, selection: PySide2.QtCore.QItemSelection) -> PySide2.QtGui.QRegion """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50802900>'


