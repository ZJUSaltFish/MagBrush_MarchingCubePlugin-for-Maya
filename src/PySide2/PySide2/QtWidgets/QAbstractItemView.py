# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractScrollArea import QAbstractScrollArea

class QAbstractItemView(QAbstractScrollArea):
    """ QAbstractItemView(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def activated(self, *args, **kwargs): # real signature unknown
        pass

    def alternatingRowColors(self): # real signature unknown; restored from __doc__
        """ alternatingRowColors(self) -> bool """
        return False

    def autoScrollMargin(self): # real signature unknown; restored from __doc__
        """ autoScrollMargin(self) -> int """
        return 0

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) -> None """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        pass

    def closeEditor(self, editor, hint): # real signature unknown; restored from __doc__
        """ closeEditor(self, editor: PySide2.QtWidgets.QWidget, hint: PySide2.QtWidgets.QAbstractItemDelegate.EndEditHint) -> None """
        pass

    def closePersistentEditor(self, index): # real signature unknown; restored from __doc__
        """ closePersistentEditor(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def commitData(self, editor): # real signature unknown; restored from __doc__
        """ commitData(self, editor: PySide2.QtWidgets.QWidget) -> None """
        pass

    def currentChanged(self, current, previous): # real signature unknown; restored from __doc__
        """ currentChanged(self, current: PySide2.QtCore.QModelIndex, previous: PySide2.QtCore.QModelIndex) -> None """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> PySide2.QtCore.QModelIndex """
        pass

    def dataChanged(self, topLeft, bottomRight, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, topLeft: PySide2.QtCore.QModelIndex, bottomRight: PySide2.QtCore.QModelIndex, roles: typing.List[int] = Default(QVector< int >)) -> None """
        pass

    def defaultDropAction(self): # real signature unknown; restored from __doc__
        """ defaultDropAction(self) -> PySide2.QtCore.Qt.DropAction """
        pass

    def dirtyRegionOffset(self): # real signature unknown; restored from __doc__
        """ dirtyRegionOffset(self) -> PySide2.QtCore.QPoint """
        pass

    def doAutoScroll(self): # real signature unknown; restored from __doc__
        """ doAutoScroll(self) -> None """
        pass

    def doItemsLayout(self): # real signature unknown; restored from __doc__
        """ doItemsLayout(self) -> None """
        pass

    def doubleClicked(self, *args, **kwargs): # real signature unknown
        pass

    def dragDropMode(self): # real signature unknown; restored from __doc__
        """ dragDropMode(self) -> PySide2.QtWidgets.QAbstractItemView.DragDropMode """
        pass

    def dragDropOverwriteMode(self): # real signature unknown; restored from __doc__
        """ dragDropOverwriteMode(self) -> bool """
        return False

    def dragEnabled(self): # real signature unknown; restored from __doc__
        """ dragEnabled(self) -> bool """
        return False

    def dragEnterEvent(self, event): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None """
        pass

    def dragLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, event: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None """
        pass

    def dropIndicatorPosition(self): # real signature unknown; restored from __doc__
        """ dropIndicatorPosition(self) -> PySide2.QtWidgets.QAbstractItemView.DropIndicatorPosition """
        pass

    def edit(self, index): # real signature unknown; restored from __doc__
        """
        edit(self, index: PySide2.QtCore.QModelIndex) -> None
        edit(self, index: PySide2.QtCore.QModelIndex, trigger: PySide2.QtWidgets.QAbstractItemView.EditTrigger, event: PySide2.QtCore.QEvent) -> bool
        """
        pass

    def editorDestroyed(self, editor): # real signature unknown; restored from __doc__
        """ editorDestroyed(self, editor: PySide2.QtCore.QObject) -> None """
        pass

    def editTriggers(self): # real signature unknown; restored from __doc__
        """ editTriggers(self) -> PySide2.QtWidgets.QAbstractItemView.EditTriggers """
        pass

    def entered(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, p_object, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, object: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def executeDelayedItemsLayout(self): # real signature unknown; restored from __doc__
        """ executeDelayedItemsLayout(self) -> None """
        pass

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def hasAutoScroll(self): # real signature unknown; restored from __doc__
        """ hasAutoScroll(self) -> bool """
        return False

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, action: int) -> None """
        pass

    def horizontalScrollbarValueChanged(self, value): # real signature unknown; restored from __doc__
        """ horizontalScrollbarValueChanged(self, value: int) -> None """
        pass

    def horizontalScrollMode(self): # real signature unknown; restored from __doc__
        """ horizontalScrollMode(self) -> PySide2.QtWidgets.QAbstractItemView.ScrollMode """
        pass

    def horizontalStepsPerItem(self): # real signature unknown; restored from __doc__
        """ horizontalStepsPerItem(self) -> int """
        return 0

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> PySide2.QtCore.QSize """
        pass

    def iconSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def indexAt(self, point): # real signature unknown; restored from __doc__
        """ indexAt(self, point: PySide2.QtCore.QPoint) -> PySide2.QtCore.QModelIndex """
        pass

    def indexWidget(self, index): # real signature unknown; restored from __doc__
        """ indexWidget(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QWidget """
        pass

    def inputMethodEvent(self, event): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any """
        pass

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isPersistentEditorOpen(self, index): # real signature unknown; restored from __doc__
        """ isPersistentEditorOpen(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """
        itemDelegate(self) -> PySide2.QtWidgets.QAbstractItemDelegate
        itemDelegate(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QAbstractItemDelegate
        """
        pass

    def itemDelegateForColumn(self, column): # real signature unknown; restored from __doc__
        """ itemDelegateForColumn(self, column: int) -> PySide2.QtWidgets.QAbstractItemDelegate """
        pass

    def itemDelegateForRow(self, row): # real signature unknown; restored from __doc__
        """ itemDelegateForRow(self, row: int) -> PySide2.QtWidgets.QAbstractItemDelegate """
        pass

    def keyboardSearch(self, search): # real signature unknown; restored from __doc__
        """ keyboardSearch(self, search: str) -> None """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> PySide2.QtCore.QAbstractItemModel """
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

    def openPersistentEditor(self, index): # real signature unknown; restored from __doc__
        """ openPersistentEditor(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def pressed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resetHorizontalScrollMode(self): # real signature unknown; restored from __doc__
        """ resetHorizontalScrollMode(self) -> None """
        pass

    def resetVerticalScrollMode(self): # real signature unknown; restored from __doc__
        """ resetVerticalScrollMode(self) -> None """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def rootIndex(self): # real signature unknown; restored from __doc__
        """ rootIndex(self) -> PySide2.QtCore.QModelIndex """
        pass

    def rowsAboutToBeRemoved(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsAboutToBeRemoved(self, parent: PySide2.QtCore.QModelIndex, start: int, end: int) -> None """
        pass

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: PySide2.QtCore.QModelIndex, start: int, end: int) -> None """
        pass

    def scheduleDelayedItemsLayout(self): # real signature unknown; restored from __doc__
        """ scheduleDelayedItemsLayout(self) -> None """
        pass

    def scrollDirtyRegion(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollDirtyRegion(self, dx: int, dy: int) -> None """
        pass

    def scrollTo(self, index, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, index: PySide2.QtCore.QModelIndex, hint: PySide2.QtWidgets.QAbstractItemView.ScrollHint = PySide2.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible) -> None """
        pass

    def scrollToBottom(self): # real signature unknown; restored from __doc__
        """ scrollToBottom(self) -> None """
        pass

    def scrollToTop(self): # real signature unknown; restored from __doc__
        """ scrollToTop(self) -> None """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) -> None """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> typing.List[int] """
        pass

    def selectionBehavior(self): # real signature unknown; restored from __doc__
        """ selectionBehavior(self) -> PySide2.QtWidgets.QAbstractItemView.SelectionBehavior """
        pass

    def selectionChanged(self, selected, deselected): # real signature unknown; restored from __doc__
        """ selectionChanged(self, selected: PySide2.QtCore.QItemSelection, deselected: PySide2.QtCore.QItemSelection) -> None """
        pass

    def selectionCommand(self, index, event, PySide2_QtCore_QEvent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ selectionCommand(self, index: PySide2.QtCore.QModelIndex, event: typing.Optional[PySide2.QtCore.QEvent] = None) -> PySide2.QtCore.QItemSelectionModel.SelectionFlags """
        pass

    def selectionMode(self): # real signature unknown; restored from __doc__
        """ selectionMode(self) -> PySide2.QtWidgets.QAbstractItemView.SelectionMode """
        pass

    def selectionModel(self): # real signature unknown; restored from __doc__
        """ selectionModel(self) -> PySide2.QtCore.QItemSelectionModel """
        pass

    def setAlternatingRowColors(self, enable): # real signature unknown; restored from __doc__
        """ setAlternatingRowColors(self, enable: bool) -> None """
        pass

    def setAutoScroll(self, enable): # real signature unknown; restored from __doc__
        """ setAutoScroll(self, enable: bool) -> None """
        pass

    def setAutoScrollMargin(self, margin): # real signature unknown; restored from __doc__
        """ setAutoScrollMargin(self, margin: int) -> None """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setDefaultDropAction(self, dropAction): # real signature unknown; restored from __doc__
        """ setDefaultDropAction(self, dropAction: PySide2.QtCore.Qt.DropAction) -> None """
        pass

    def setDirtyRegion(self, region): # real signature unknown; restored from __doc__
        """ setDirtyRegion(self, region: PySide2.QtGui.QRegion) -> None """
        pass

    def setDragDropMode(self, behavior): # real signature unknown; restored from __doc__
        """ setDragDropMode(self, behavior: PySide2.QtWidgets.QAbstractItemView.DragDropMode) -> None """
        pass

    def setDragDropOverwriteMode(self, overwrite): # real signature unknown; restored from __doc__
        """ setDragDropOverwriteMode(self, overwrite: bool) -> None """
        pass

    def setDragEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, enable: bool) -> None """
        pass

    def setDropIndicatorShown(self, enable): # real signature unknown; restored from __doc__
        """ setDropIndicatorShown(self, enable: bool) -> None """
        pass

    def setEditTriggers(self, triggers): # real signature unknown; restored from __doc__
        """ setEditTriggers(self, triggers: PySide2.QtWidgets.QAbstractItemView.EditTriggers) -> None """
        pass

    def setHorizontalScrollMode(self, mode): # real signature unknown; restored from __doc__
        """ setHorizontalScrollMode(self, mode: PySide2.QtWidgets.QAbstractItemView.ScrollMode) -> None """
        pass

    def setHorizontalStepsPerItem(self, steps): # real signature unknown; restored from __doc__
        """ setHorizontalStepsPerItem(self, steps: int) -> None """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setIndexWidget(self, index, widget): # real signature unknown; restored from __doc__
        """ setIndexWidget(self, index: PySide2.QtCore.QModelIndex, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setItemDelegate(self, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, delegate: PySide2.QtWidgets.QAbstractItemDelegate) -> None """
        pass

    def setItemDelegateForColumn(self, column, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegateForColumn(self, column: int, delegate: PySide2.QtWidgets.QAbstractItemDelegate) -> None """
        pass

    def setItemDelegateForRow(self, row, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegateForRow(self, row: int, delegate: PySide2.QtWidgets.QAbstractItemDelegate) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setSelection(self, rect, command): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: PySide2.QtCore.QRect, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None """
        pass

    def setSelectionBehavior(self, behavior): # real signature unknown; restored from __doc__
        """ setSelectionBehavior(self, behavior: PySide2.QtWidgets.QAbstractItemView.SelectionBehavior) -> None """
        pass

    def setSelectionMode(self, mode): # real signature unknown; restored from __doc__
        """ setSelectionMode(self, mode: PySide2.QtWidgets.QAbstractItemView.SelectionMode) -> None """
        pass

    def setSelectionModel(self, selectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: PySide2.QtCore.QItemSelectionModel) -> None """
        pass

    def setState(self, state): # real signature unknown; restored from __doc__
        """ setState(self, state: PySide2.QtWidgets.QAbstractItemView.State) -> None """
        pass

    def setTabKeyNavigation(self, enable): # real signature unknown; restored from __doc__
        """ setTabKeyNavigation(self, enable: bool) -> None """
        pass

    def setTextElideMode(self, mode): # real signature unknown; restored from __doc__
        """ setTextElideMode(self, mode: PySide2.QtCore.Qt.TextElideMode) -> None """
        pass

    def setVerticalScrollMode(self, mode): # real signature unknown; restored from __doc__
        """ setVerticalScrollMode(self, mode: PySide2.QtWidgets.QAbstractItemView.ScrollMode) -> None """
        pass

    def setVerticalStepsPerItem(self, steps): # real signature unknown; restored from __doc__
        """ setVerticalStepsPerItem(self, steps: int) -> None """
        pass

    def showDropIndicator(self): # real signature unknown; restored from __doc__
        """ showDropIndicator(self) -> bool """
        return False

    def sizeHintForColumn(self, column): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, column: int) -> int """
        return 0

    def sizeHintForIndex(self, index): # real signature unknown; restored from __doc__
        """ sizeHintForIndex(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize """
        pass

    def sizeHintForRow(self, row): # real signature unknown; restored from __doc__
        """ sizeHintForRow(self, row: int) -> int """
        return 0

    def startAutoScroll(self): # real signature unknown; restored from __doc__
        """ startAutoScroll(self) -> None """
        pass

    def startDrag(self, supportedActions): # real signature unknown; restored from __doc__
        """ startDrag(self, supportedActions: PySide2.QtCore.Qt.DropActions) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtWidgets.QAbstractItemView.State """
        pass

    def stopAutoScroll(self): # real signature unknown; restored from __doc__
        """ stopAutoScroll(self) -> None """
        pass

    def tabKeyNavigation(self): # real signature unknown; restored from __doc__
        """ tabKeyNavigation(self) -> bool """
        return False

    def textElideMode(self): # real signature unknown; restored from __doc__
        """ textElideMode(self) -> PySide2.QtCore.Qt.TextElideMode """
        pass

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """
        update(self) -> None
        update(self, index: PySide2.QtCore.QModelIndex) -> None
        """
        pass

    def updateEditorData(self): # real signature unknown; restored from __doc__
        """ updateEditorData(self) -> None """
        pass

    def updateEditorGeometries(self): # real signature unknown; restored from __doc__
        """ updateEditorGeometries(self) -> None """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) -> None """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ verticalScrollbarAction(self, action: int) -> None """
        pass

    def verticalScrollbarValueChanged(self, value): # real signature unknown; restored from __doc__
        """ verticalScrollbarValueChanged(self, value: int) -> None """
        pass

    def verticalScrollMode(self): # real signature unknown; restored from __doc__
        """ verticalScrollMode(self) -> PySide2.QtWidgets.QAbstractItemView.ScrollMode """
        pass

    def verticalStepsPerItem(self): # real signature unknown; restored from __doc__
        """ verticalStepsPerItem(self) -> int """
        return 0

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ viewOptions(self) -> PySide2.QtWidgets.QStyleOptionViewItem """
        pass

    def viewportEntered(self, *args, **kwargs): # real signature unknown
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

    AboveItem = PySide2.QtWidgets.QAbstractItemView.DropIndicatorPosition.AboveItem
    AllEditTriggers = PySide2.QtWidgets.QAbstractItemView.EditTrigger.AllEditTriggers
    AnimatingState = PySide2.QtWidgets.QAbstractItemView.State.AnimatingState
    AnyKeyPressed = PySide2.QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed
    BelowItem = PySide2.QtWidgets.QAbstractItemView.DropIndicatorPosition.BelowItem
    CollapsingState = PySide2.QtWidgets.QAbstractItemView.State.CollapsingState
    ContiguousSelection = PySide2.QtWidgets.QAbstractItemView.SelectionMode.ContiguousSelection
    CurrentChanged = PySide2.QtWidgets.QAbstractItemView.EditTrigger.CurrentChanged
    CursorAction = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.CursorAction'>"
    DoubleClicked = PySide2.QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked
    DragDrop = PySide2.QtWidgets.QAbstractItemView.DragDropMode.DragDrop
    DragDropMode = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.DragDropMode'>"
    DraggingState = PySide2.QtWidgets.QAbstractItemView.State.DraggingState
    DragOnly = PySide2.QtWidgets.QAbstractItemView.DragDropMode.DragOnly
    DragSelectingState = PySide2.QtWidgets.QAbstractItemView.State.DragSelectingState
    DropIndicatorPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.DropIndicatorPosition'>"
    DropOnly = PySide2.QtWidgets.QAbstractItemView.DragDropMode.DropOnly
    EditingState = PySide2.QtWidgets.QAbstractItemView.State.EditingState
    EditKeyPressed = PySide2.QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed
    EditTrigger = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.EditTrigger'>"
    EditTriggers = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.EditTriggers'>"
    EnsureVisible = PySide2.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible
    ExpandingState = PySide2.QtWidgets.QAbstractItemView.State.ExpandingState
    ExtendedSelection = PySide2.QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection
    InternalMove = PySide2.QtWidgets.QAbstractItemView.DragDropMode.InternalMove
    MoveDown = PySide2.QtWidgets.QAbstractItemView.CursorAction.MoveDown
    MoveEnd = PySide2.QtWidgets.QAbstractItemView.CursorAction.MoveEnd
    MoveHome = PySide2.QtWidgets.QAbstractItemView.CursorAction.MoveHome
    MoveLeft = PySide2.QtWidgets.QAbstractItemView.CursorAction.MoveLeft
    MoveNext = PySide2.QtWidgets.QAbstractItemView.CursorAction.MoveNext
    MovePageDown = PySide2.QtWidgets.QAbstractItemView.CursorAction.MovePageDown
    MovePageUp = PySide2.QtWidgets.QAbstractItemView.CursorAction.MovePageUp
    MovePrevious = PySide2.QtWidgets.QAbstractItemView.CursorAction.MovePrevious
    MoveRight = PySide2.QtWidgets.QAbstractItemView.CursorAction.MoveRight
    MoveUp = PySide2.QtWidgets.QAbstractItemView.CursorAction.MoveUp
    MultiSelection = PySide2.QtWidgets.QAbstractItemView.SelectionMode.MultiSelection
    NoDragDrop = PySide2.QtWidgets.QAbstractItemView.DragDropMode.NoDragDrop
    NoEditTriggers = PySide2.QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
    NoSelection = PySide2.QtWidgets.QAbstractItemView.SelectionMode.NoSelection
    NoState = PySide2.QtWidgets.QAbstractItemView.State.NoState
    OnItem = PySide2.QtWidgets.QAbstractItemView.DropIndicatorPosition.OnItem
    OnViewport = PySide2.QtWidgets.QAbstractItemView.DropIndicatorPosition.OnViewport
    PositionAtBottom = PySide2.QtWidgets.QAbstractItemView.ScrollHint.PositionAtBottom
    PositionAtCenter = PySide2.QtWidgets.QAbstractItemView.ScrollHint.PositionAtCenter
    PositionAtTop = PySide2.QtWidgets.QAbstractItemView.ScrollHint.PositionAtTop
    ScrollHint = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.ScrollHint'>"
    ScrollMode = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.ScrollMode'>"
    ScrollPerItem = PySide2.QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem
    ScrollPerPixel = PySide2.QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel
    SelectColumns = PySide2.QtWidgets.QAbstractItemView.SelectionBehavior.SelectColumns
    SelectedClicked = PySide2.QtWidgets.QAbstractItemView.EditTrigger.SelectedClicked
    SelectionBehavior = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.SelectionBehavior'>"
    SelectionMode = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.SelectionMode'>"
    SelectItems = PySide2.QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems
    SelectRows = PySide2.QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
    SingleSelection = PySide2.QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
    State = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractItemView.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50800480>'


