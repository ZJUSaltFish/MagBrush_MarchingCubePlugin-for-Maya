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

class QHeaderView(QAbstractItemView):
    """ QHeaderView(self, orientation: PySide2.QtCore.Qt.Orientation, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def cascadingSectionResizes(self): # real signature unknown; restored from __doc__
        """ cascadingSectionResizes(self) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentChanged(self, current, old): # real signature unknown; restored from __doc__
        """ currentChanged(self, current: PySide2.QtCore.QModelIndex, old: PySide2.QtCore.QModelIndex) -> None """
        pass

    def dataChanged(self, topLeft, bottomRight, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dataChanged(self, topLeft: PySide2.QtCore.QModelIndex, bottomRight: PySide2.QtCore.QModelIndex, roles: typing.List[int] = Default(QVector< int >)) -> None """
        pass

    def defaultAlignment(self): # real signature unknown; restored from __doc__
        """ defaultAlignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def defaultSectionSize(self): # real signature unknown; restored from __doc__
        """ defaultSectionSize(self) -> int """
        return 0

    def doItemsLayout(self): # real signature unknown; restored from __doc__
        """ doItemsLayout(self) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def geometriesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def headerDataChanged(self, orientation, logicalFirst, logicalLast): # real signature unknown; restored from __doc__
        """ headerDataChanged(self, orientation: PySide2.QtCore.Qt.Orientation, logicalFirst: int, logicalLast: int) -> None """
        pass

    def hiddenSectionCount(self): # real signature unknown; restored from __doc__
        """ hiddenSectionCount(self) -> int """
        return 0

    def hideSection(self, logicalIndex): # real signature unknown; restored from __doc__
        """ hideSection(self, logicalIndex: int) -> None """
        pass

    def highlightSections(self): # real signature unknown; restored from __doc__
        """ highlightSections(self) -> bool """
        return False

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def indexAt(self, p): # real signature unknown; restored from __doc__
        """ indexAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QModelIndex """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) -> None """
        pass

    def initializeSections(self): # real signature unknown; restored from __doc__
        """
        initializeSections(self) -> None
        initializeSections(self, start: int, end: int) -> None
        """
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """
        initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionFrame) -> None
        initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionHeader) -> None
        """
        pass

    def isFirstSectionMovable(self): # real signature unknown; restored from __doc__
        """ isFirstSectionMovable(self) -> bool """
        return False

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isSectionHidden(self, logicalIndex): # real signature unknown; restored from __doc__
        """ isSectionHidden(self, logicalIndex: int) -> bool """
        return False

    def isSortIndicatorShown(self): # real signature unknown; restored from __doc__
        """ isSortIndicatorShown(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def logicalIndex(self, visualIndex): # real signature unknown; restored from __doc__
        """ logicalIndex(self, visualIndex: int) -> int """
        return 0

    def logicalIndexAt(self, pos): # real signature unknown; restored from __doc__
        """
        logicalIndexAt(self, pos: PySide2.QtCore.QPoint) -> int
        logicalIndexAt(self, position: int) -> int
        logicalIndexAt(self, x: int, y: int) -> int
        """
        return 0

    def maximumSectionSize(self): # real signature unknown; restored from __doc__
        """ maximumSectionSize(self) -> int """
        return 0

    def minimumSectionSize(self): # real signature unknown; restored from __doc__
        """ minimumSectionSize(self) -> int """
        return 0

    def mouseDoubleClickEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseMoveEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, e): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def moveCursor(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ moveCursor(self, arg__1: PySide2.QtWidgets.QAbstractItemView.CursorAction, arg__2: PySide2.QtCore.Qt.KeyboardModifiers) -> PySide2.QtCore.QModelIndex """
        pass

    def moveSection(self, from_, to): # real signature unknown; restored from __doc__
        """ moveSection(self, from_: int, to: int) -> None """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def paintEvent(self, e): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def paintSection(self, painter, rect, logicalIndex): # real signature unknown; restored from __doc__
        """ paintSection(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, logicalIndex: int) -> None """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resetDefaultSectionSize(self): # real signature unknown; restored from __doc__
        """ resetDefaultSectionSize(self) -> None """
        pass

    def resizeContentsPrecision(self): # real signature unknown; restored from __doc__
        """ resizeContentsPrecision(self) -> int """
        return 0

    def resizeSection(self, logicalIndex, size): # real signature unknown; restored from __doc__
        """ resizeSection(self, logicalIndex: int, size: int) -> None """
        pass

    def resizeSections(self): # real signature unknown; restored from __doc__
        """
        resizeSections(self) -> None
        resizeSections(self, mode: PySide2.QtWidgets.QHeaderView.ResizeMode) -> None
        """
        pass

    def restoreState(self, state): # real signature unknown; restored from __doc__
        """ restoreState(self, state: PySide2.QtCore.QByteArray) -> bool """
        return False

    def rowsInserted(self, parent, start, end): # real signature unknown; restored from __doc__
        """ rowsInserted(self, parent: PySide2.QtCore.QModelIndex, start: int, end: int) -> None """
        pass

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> PySide2.QtCore.QByteArray """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) -> None """
        pass

    def scrollTo(self, index, hint): # real signature unknown; restored from __doc__
        """ scrollTo(self, index: PySide2.QtCore.QModelIndex, hint: PySide2.QtWidgets.QAbstractItemView.ScrollHint) -> None """
        pass

    def sectionClicked(self, *args, **kwargs): # real signature unknown
        pass

    def sectionCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sectionDoubleClicked(self, *args, **kwargs): # real signature unknown
        pass

    def sectionEntered(self, *args, **kwargs): # real signature unknown
        pass

    def sectionHandleDoubleClicked(self, *args, **kwargs): # real signature unknown
        pass

    def sectionMoved(self, *args, **kwargs): # real signature unknown
        pass

    def sectionPosition(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionPosition(self, logicalIndex: int) -> int """
        return 0

    def sectionPressed(self, *args, **kwargs): # real signature unknown
        pass

    def sectionResized(self, *args, **kwargs): # real signature unknown
        pass

    def sectionResizeMode(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionResizeMode(self, logicalIndex: int) -> PySide2.QtWidgets.QHeaderView.ResizeMode """
        pass

    def sectionsAboutToBeRemoved(self, parent, logicalFirst, logicalLast): # real signature unknown; restored from __doc__
        """ sectionsAboutToBeRemoved(self, parent: PySide2.QtCore.QModelIndex, logicalFirst: int, logicalLast: int) -> None """
        pass

    def sectionsClickable(self): # real signature unknown; restored from __doc__
        """ sectionsClickable(self) -> bool """
        return False

    def sectionsHidden(self): # real signature unknown; restored from __doc__
        """ sectionsHidden(self) -> bool """
        return False

    def sectionsInserted(self, parent, logicalFirst, logicalLast): # real signature unknown; restored from __doc__
        """ sectionsInserted(self, parent: PySide2.QtCore.QModelIndex, logicalFirst: int, logicalLast: int) -> None """
        pass

    def sectionSize(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionSize(self, logicalIndex: int) -> int """
        return 0

    def sectionSizeFromContents(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionSizeFromContents(self, logicalIndex: int) -> PySide2.QtCore.QSize """
        pass

    def sectionSizeHint(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionSizeHint(self, logicalIndex: int) -> int """
        return 0

    def sectionsMovable(self): # real signature unknown; restored from __doc__
        """ sectionsMovable(self) -> bool """
        return False

    def sectionsMoved(self): # real signature unknown; restored from __doc__
        """ sectionsMoved(self) -> bool """
        return False

    def sectionViewportPosition(self, logicalIndex): # real signature unknown; restored from __doc__
        """ sectionViewportPosition(self, logicalIndex: int) -> int """
        return 0

    def setCascadingSectionResizes(self, enable): # real signature unknown; restored from __doc__
        """ setCascadingSectionResizes(self, enable: bool) -> None """
        pass

    def setDefaultAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setDefaultAlignment(self, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setDefaultSectionSize(self, size): # real signature unknown; restored from __doc__
        """ setDefaultSectionSize(self, size: int) -> None """
        pass

    def setFirstSectionMovable(self, movable): # real signature unknown; restored from __doc__
        """ setFirstSectionMovable(self, movable: bool) -> None """
        pass

    def setHighlightSections(self, highlight): # real signature unknown; restored from __doc__
        """ setHighlightSections(self, highlight: bool) -> None """
        pass

    def setMaximumSectionSize(self, size): # real signature unknown; restored from __doc__
        """ setMaximumSectionSize(self, size: int) -> None """
        pass

    def setMinimumSectionSize(self, size): # real signature unknown; restored from __doc__
        """ setMinimumSectionSize(self, size: int) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setOffset(self, offset): # real signature unknown; restored from __doc__
        """ setOffset(self, offset: int) -> None """
        pass

    def setOffsetToLastSection(self): # real signature unknown; restored from __doc__
        """ setOffsetToLastSection(self) -> None """
        pass

    def setOffsetToSectionPosition(self, visualIndex): # real signature unknown; restored from __doc__
        """ setOffsetToSectionPosition(self, visualIndex: int) -> None """
        pass

    def setResizeContentsPrecision(self, precision): # real signature unknown; restored from __doc__
        """ setResizeContentsPrecision(self, precision: int) -> None """
        pass

    def setSectionHidden(self, logicalIndex, hide): # real signature unknown; restored from __doc__
        """ setSectionHidden(self, logicalIndex: int, hide: bool) -> None """
        pass

    def setSectionResizeMode(self, logicalIndex, mode): # real signature unknown; restored from __doc__
        """
        setSectionResizeMode(self, logicalIndex: int, mode: PySide2.QtWidgets.QHeaderView.ResizeMode) -> None
        setSectionResizeMode(self, mode: PySide2.QtWidgets.QHeaderView.ResizeMode) -> None
        """
        pass

    def setSectionsClickable(self, clickable): # real signature unknown; restored from __doc__
        """ setSectionsClickable(self, clickable: bool) -> None """
        pass

    def setSectionsMovable(self, movable): # real signature unknown; restored from __doc__
        """ setSectionsMovable(self, movable: bool) -> None """
        pass

    def setSelection(self, rect, flags): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: PySide2.QtCore.QRect, flags: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None """
        pass

    def setSortIndicator(self, logicalIndex, order): # real signature unknown; restored from __doc__
        """ setSortIndicator(self, logicalIndex: int, order: PySide2.QtCore.Qt.SortOrder) -> None """
        pass

    def setSortIndicatorShown(self, show): # real signature unknown; restored from __doc__
        """ setSortIndicatorShown(self, show: bool) -> None """
        pass

    def setStretchLastSection(self, stretch): # real signature unknown; restored from __doc__
        """ setStretchLastSection(self, stretch: bool) -> None """
        pass

    def setVisible(self, v): # real signature unknown; restored from __doc__
        """ setVisible(self, v: bool) -> None """
        pass

    def showSection(self, logicalIndex): # real signature unknown; restored from __doc__
        """ showSection(self, logicalIndex: int) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def sortIndicatorChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sortIndicatorOrder(self): # real signature unknown; restored from __doc__
        """ sortIndicatorOrder(self) -> PySide2.QtCore.Qt.SortOrder """
        pass

    def sortIndicatorSection(self): # real signature unknown; restored from __doc__
        """ sortIndicatorSection(self) -> int """
        return 0

    def stretchLastSection(self): # real signature unknown; restored from __doc__
        """ stretchLastSection(self) -> bool """
        return False

    def stretchSectionCount(self): # real signature unknown; restored from __doc__
        """ stretchSectionCount(self) -> int """
        return 0

    def swapSections(self, first, second): # real signature unknown; restored from __doc__
        """ swapSections(self, first: int, second: int) -> None """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) -> None """
        pass

    def updateSection(self, logicalIndex): # real signature unknown; restored from __doc__
        """ updateSection(self, logicalIndex: int) -> None """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def viewportEvent(self, e): # real signature unknown; restored from __doc__
        """ viewportEvent(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def visualIndex(self, logicalIndex): # real signature unknown; restored from __doc__
        """ visualIndex(self, logicalIndex: int) -> int """
        return 0

    def visualIndexAt(self, position): # real signature unknown; restored from __doc__
        """ visualIndexAt(self, position: int) -> int """
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

    def __init__(self, orientation, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Custom = PySide2.QtWidgets.QHeaderView.ResizeMode.Custom
    Fixed = PySide2.QtWidgets.QHeaderView.ResizeMode.Fixed
    Interactive = PySide2.QtWidgets.QHeaderView.ResizeMode.Interactive
    ResizeMode = None # (!) real value is "<class 'PySide2.QtWidgets.QHeaderView.ResizeMode'>"
    ResizeToContents = PySide2.QtWidgets.QHeaderView.ResizeMode.ResizeToContents
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50800E80>'
    Stretch = PySide2.QtWidgets.QHeaderView.ResizeMode.Stretch


