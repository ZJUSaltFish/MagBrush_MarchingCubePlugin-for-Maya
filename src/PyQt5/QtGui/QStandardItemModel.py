# encoding: utf-8
# module PyQt5.QtGui
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QStandardItemModel(__PyQt5_QtCore.QAbstractItemModel):
    """
    QStandardItemModel(parent: typing.Optional[QObject] = None)
    QStandardItemModel(rows: int, columns: int, parent: typing.Optional[QObject] = None)
    """
    def appendColumn(self, items, QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendColumn(self, items: Iterable[QStandardItem]) """
        pass

    def appendRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        appendRow(self, items: Iterable[QStandardItem])
        appendRow(self, aitem: QStandardItem)
        """
        pass

    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearItemData(self, index): # real signature unknown; restored from __doc__
        """ clearItemData(self, index: QModelIndex) -> bool """
        return False

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, data, action, row, column, parent): # real signature unknown; restored from __doc__
        """ dropMimeData(self, data: QMimeData, action: Qt.DropAction, row: int, column: int, parent: QModelIndex) -> bool """
        return False

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def findItems(self, text, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findItems(self, text: str, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchExactly, column: int = 0) -> List[QStandardItem] """
        pass

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def horizontalHeaderItem(self, column): # real signature unknown; restored from __doc__
        """ horizontalHeaderItem(self, column: int) -> QStandardItem """
        return QStandardItem

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def indexFromItem(self, item): # real signature unknown; restored from __doc__
        """ indexFromItem(self, item: QStandardItem) -> QModelIndex """
        pass

    def insertColumn(self, column, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertColumn(self, column: int, items: Iterable[QStandardItem])
        insertColumn(self, column: int, parent: QModelIndex = QModelIndex()) -> bool
        """
        pass

    def insertColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, column: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def insertRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRow(self, row: int, items: Iterable[QStandardItem])
        insertRow(self, arow: int, aitem: QStandardItem)
        insertRow(self, row: int, parent: QModelIndex = QModelIndex()) -> bool
        """
        pass

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ invisibleRootItem(self) -> QStandardItem """
        return QStandardItem

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def item(self, row, column=0): # real signature unknown; restored from __doc__
        """ item(self, row: int, column: int = 0) -> QStandardItem """
        return QStandardItem

    def itemChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def itemData(self, index): # real signature unknown; restored from __doc__
        """ itemData(self, index: QModelIndex) -> Dict[int, Any] """
        return {}

    def itemFromIndex(self, index): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, index: QModelIndex) -> QStandardItem """
        return QStandardItem

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ itemPrototype(self) -> QStandardItem """
        return QStandardItem

    def mimeData(self, indexes, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: Iterable[QModelIndex]) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def parent(self, child=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self, child: QModelIndex) -> QModelIndex
        parent(self) -> QObject
        """
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def removeRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColumnCount(self, columns): # real signature unknown; restored from __doc__
        """ setColumnCount(self, columns: int) """
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: QModelIndex, value: Any, role: int = Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: Qt.Orientation, value: Any, role: int = Qt.EditRole) -> bool """
        return False

    def setHorizontalHeaderItem(self, column, item): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderItem(self, column: int, item: QStandardItem) """
        pass

    def setHorizontalHeaderLabels(self, labels, p_str=None): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderLabels(self, labels: Iterable[str]) """
        pass

    def setItem(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setItem(self, row: int, column: int, item: QStandardItem)
        setItem(self, arow: int, aitem: QStandardItem)
        """
        pass

    def setItemData(self, index, roles, p_int=None, Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: QModelIndex, roles: Dict[int, Any]) -> bool """
        return False

    def setItemPrototype(self, item): # real signature unknown; restored from __doc__
        """ setItemPrototype(self, item: QStandardItem) """
        pass

    def setItemRoleNames(self, roleNames, p_int=None, Union=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setItemRoleNames(self, roleNames: Dict[int, Union[QByteArray, bytes, bytearray]]) """
        pass

    def setRowCount(self, rows): # real signature unknown; restored from __doc__
        """ setRowCount(self, rows: int) """
        pass

    def setSortRole(self, role): # real signature unknown; restored from __doc__
        """ setSortRole(self, role: int) """
        pass

    def setVerticalHeaderItem(self, row, item): # real signature unknown; restored from __doc__
        """ setVerticalHeaderItem(self, row: int, item: QStandardItem) """
        pass

    def setVerticalHeaderLabels(self, labels, p_str=None): # real signature unknown; restored from __doc__
        """ setVerticalHeaderLabels(self, labels: Iterable[str]) """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def sortRole(self): # real signature unknown; restored from __doc__
        """ sortRole(self) -> int """
        return 0

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def takeColumn(self, column): # real signature unknown; restored from __doc__
        """ takeColumn(self, column: int) -> List[QStandardItem] """
        return []

    def takeHorizontalHeaderItem(self, column): # real signature unknown; restored from __doc__
        """ takeHorizontalHeaderItem(self, column: int) -> QStandardItem """
        return QStandardItem

    def takeItem(self, row, column=0): # real signature unknown; restored from __doc__
        """ takeItem(self, row: int, column: int = 0) -> QStandardItem """
        return QStandardItem

    def takeRow(self, row): # real signature unknown; restored from __doc__
        """ takeRow(self, row: int) -> List[QStandardItem] """
        return []

    def takeVerticalHeaderItem(self, row): # real signature unknown; restored from __doc__
        """ takeVerticalHeaderItem(self, row: int) -> QStandardItem """
        return QStandardItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalHeaderItem(self, row): # real signature unknown; restored from __doc__
        """ verticalHeaderItem(self, row: int) -> QStandardItem """
        return QStandardItem

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


