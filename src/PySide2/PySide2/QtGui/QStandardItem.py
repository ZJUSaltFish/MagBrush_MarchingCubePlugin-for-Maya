# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QStandardItem(__Shiboken.Object):
    """
    QStandardItem(self) -> None
    QStandardItem(self, icon: PySide2.QtGui.QIcon, text: str) -> None
    QStandardItem(self, other: PySide2.QtGui.QStandardItem) -> None
    QStandardItem(self, rows: int, columns: int = 1) -> None
    QStandardItem(self, text: str) -> None
    """
    def accessibleDescription(self): # real signature unknown; restored from __doc__
        """ accessibleDescription(self) -> str """
        return ""

    def accessibleText(self): # real signature unknown; restored from __doc__
        """ accessibleText(self) -> str """
        return ""

    def appendColumn(self, items, PySide2_QtGui_QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendColumn(self, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None """
        pass

    def appendRow(self, item): # real signature unknown; restored from __doc__
        """
        appendRow(self, item: PySide2.QtGui.QStandardItem) -> None
        appendRow(self, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None
        """
        pass

    def appendRows(self, items, PySide2_QtGui_QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendRows(self, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> PySide2.QtGui.QBrush """
        pass

    def checkState(self): # real signature unknown; restored from __doc__
        """ checkState(self) -> PySide2.QtCore.Qt.CheckState """
        pass

    def child(self, row, column=0): # real signature unknown; restored from __doc__
        """ child(self, row: int, column: int = 0) -> PySide2.QtGui.QStandardItem """
        pass

    def clearData(self): # real signature unknown; restored from __doc__
        """ clearData(self) -> None """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> PySide2.QtGui.QStandardItem """
        pass

    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def data(self, role=257): # real signature unknown; restored from __doc__
        """ data(self, role: int = 257) -> typing.Any """
        pass

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ emitDataChanged(self) -> None """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def foreground(self): # real signature unknown; restored from __doc__
        """ foreground(self) -> PySide2.QtGui.QBrush """
        pass

    def hasChildren(self): # real signature unknown; restored from __doc__
        """ hasChildren(self) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> PySide2.QtCore.QModelIndex """
        pass

    def insertColumn(self, column, items, PySide2_QtGui_QStandardItem=None): # real signature unknown; restored from __doc__
        """ insertColumn(self, column: int, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None """
        pass

    def insertColumns(self, column, count): # real signature unknown; restored from __doc__
        """ insertColumns(self, column: int, count: int) -> None """
        pass

    def insertRow(self, row, item): # real signature unknown; restored from __doc__
        """
        insertRow(self, row: int, item: PySide2.QtGui.QStandardItem) -> None
        insertRow(self, row: int, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None
        """
        pass

    def insertRows(self, row, count): # real signature unknown; restored from __doc__
        """
        insertRows(self, row: int, count: int) -> None
        insertRows(self, row: int, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None
        """
        pass

    def isAutoTristate(self): # real signature unknown; restored from __doc__
        """ isAutoTristate(self) -> bool """
        return False

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isDragEnabled(self): # real signature unknown; restored from __doc__
        """ isDragEnabled(self) -> bool """
        return False

    def isDropEnabled(self): # real signature unknown; restored from __doc__
        """ isDropEnabled(self) -> bool """
        return False

    def isEditable(self): # real signature unknown; restored from __doc__
        """ isEditable(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isSelectable(self): # real signature unknown; restored from __doc__
        """ isSelectable(self) -> bool """
        return False

    def isTristate(self): # real signature unknown; restored from __doc__
        """ isTristate(self) -> bool """
        return False

    def isUserTristate(self): # real signature unknown; restored from __doc__
        """ isUserTristate(self) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> PySide2.QtGui.QStandardItemModel """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> PySide2.QtGui.QStandardItem """
        pass

    def read(self, in_): # real signature unknown; restored from __doc__
        """ read(self, in_: PySide2.QtCore.QDataStream) -> None """
        pass

    def removeColumn(self, column): # real signature unknown; restored from __doc__
        """ removeColumn(self, column: int) -> None """
        pass

    def removeColumns(self, column, count): # real signature unknown; restored from __doc__
        """ removeColumns(self, column: int, count: int) -> None """
        pass

    def removeRow(self, row): # real signature unknown; restored from __doc__
        """ removeRow(self, row: int) -> None """
        pass

    def removeRows(self, row, count): # real signature unknown; restored from __doc__
        """ removeRows(self, row: int, count: int) -> None """
        pass

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def setAccessibleDescription(self, accessibleDescription): # real signature unknown; restored from __doc__
        """ setAccessibleDescription(self, accessibleDescription: str) -> None """
        pass

    def setAccessibleText(self, accessibleText): # real signature unknown; restored from __doc__
        """ setAccessibleText(self, accessibleText: str) -> None """
        pass

    def setAutoTristate(self, tristate): # real signature unknown; restored from __doc__
        """ setAutoTristate(self, tristate: bool) -> None """
        pass

    def setBackground(self, brush): # real signature unknown; restored from __doc__
        """ setBackground(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setCheckable(self, checkable): # real signature unknown; restored from __doc__
        """ setCheckable(self, checkable: bool) -> None """
        pass

    def setCheckState(self, checkState): # real signature unknown; restored from __doc__
        """ setCheckState(self, checkState: PySide2.QtCore.Qt.CheckState) -> None """
        pass

    def setChild(self, row, column, item): # real signature unknown; restored from __doc__
        """
        setChild(self, row: int, column: int, item: PySide2.QtGui.QStandardItem) -> None
        setChild(self, row: int, item: PySide2.QtGui.QStandardItem) -> None
        """
        pass

    def setColumnCount(self, columns): # real signature unknown; restored from __doc__
        """ setColumnCount(self, columns: int) -> None """
        pass

    def setData(self, value, role=257): # real signature unknown; restored from __doc__
        """ setData(self, value: typing.Any, role: int = 257) -> None """
        pass

    def setDragEnabled(self, dragEnabled): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, dragEnabled: bool) -> None """
        pass

    def setDropEnabled(self, dropEnabled): # real signature unknown; restored from __doc__
        """ setDropEnabled(self, dropEnabled: bool) -> None """
        pass

    def setEditable(self, editable): # real signature unknown; restored from __doc__
        """ setEditable(self, editable: bool) -> None """
        pass

    def setEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setEnabled(self, enabled: bool) -> None """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: PySide2.QtCore.Qt.ItemFlags) -> None """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: PySide2.QtGui.QFont) -> None """
        pass

    def setForeground(self, brush): # real signature unknown; restored from __doc__
        """ setForeground(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setRowCount(self, rows): # real signature unknown; restored from __doc__
        """ setRowCount(self, rows: int) -> None """
        pass

    def setSelectable(self, selectable): # real signature unknown; restored from __doc__
        """ setSelectable(self, selectable: bool) -> None """
        pass

    def setSizeHint(self, sizeHint): # real signature unknown; restored from __doc__
        """ setSizeHint(self, sizeHint: PySide2.QtCore.QSize) -> None """
        pass

    def setStatusTip(self, statusTip): # real signature unknown; restored from __doc__
        """ setStatusTip(self, statusTip: str) -> None """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) -> None """
        pass

    def setTextAlignment(self, textAlignment): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, textAlignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setToolTip(self, toolTip): # real signature unknown; restored from __doc__
        """ setToolTip(self, toolTip: str) -> None """
        pass

    def setTristate(self, tristate): # real signature unknown; restored from __doc__
        """ setTristate(self, tristate: bool) -> None """
        pass

    def setUserTristate(self, tristate): # real signature unknown; restored from __doc__
        """ setUserTristate(self, tristate: bool) -> None """
        pass

    def setWhatsThis(self, whatsThis): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, whatsThis: str) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def sortChildren(self, column, order=None): # real signature unknown; restored from __doc__
        """ sortChildren(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def takeChild(self, row, column=0): # real signature unknown; restored from __doc__
        """ takeChild(self, row: int, column: int = 0) -> PySide2.QtGui.QStandardItem """
        pass

    def takeColumn(self, column): # real signature unknown; restored from __doc__
        """ takeColumn(self, column: int) -> typing.List[PySide2.QtGui.QStandardItem] """
        pass

    def takeRow(self, row): # real signature unknown; restored from __doc__
        """ takeRow(self, row: int) -> typing.List[PySide2.QtGui.QStandardItem] """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ textAlignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def write(self, out): # real signature unknown; restored from __doc__
        """ write(self, out: PySide2.QtCore.QDataStream) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, out): # real signature unknown; restored from __doc__
        """
        __lshift__(self, out: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, in_): # real signature unknown; restored from __doc__
        """
        __rshift__(self, in_: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ItemType = None # (!) real value is "<class 'PySide2.QtGui.QStandardItem.ItemType'>"
    Type = PySide2.QtGui.QStandardItem.ItemType.Type
    UserType = PySide2.QtGui.QStandardItem.ItemType.UserType
    __hash__ = None


