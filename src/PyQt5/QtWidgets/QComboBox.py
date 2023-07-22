# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QComboBox(QWidget):
    """ QComboBox(parent: typing.Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def activated(self, *args, **kwargs): # real signature unknown
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

    def addItem(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, text: str, userData: Any = None)
        addItem(self, icon: QIcon, text: str, userData: Any = None)
        """
        pass

    def addItems(self, texts, p_str=None): # real signature unknown; restored from __doc__
        """ addItems(self, texts: Iterable[str]) """
        pass

    def changeEvent(self, e): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearEditText(self): # real signature unknown; restored from __doc__
        """ clearEditText(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def completer(self): # real signature unknown; restored from __doc__
        """ completer(self) -> QCompleter """
        return QCompleter

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, e): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, e: QContextMenuEvent) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentData(self, role=None): # real signature unknown; restored from __doc__
        """ currentData(self, role: int = Qt.ItemDataRole.UserRole) -> Any """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentIndexChanged(self, *args, **kwargs): # real signature unknown
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

    def currentText(self): # real signature unknown; restored from __doc__
        """ currentText(self) -> str """
        return ""

    def currentTextChanged(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def duplicatesEnabled(self): # real signature unknown; restored from __doc__
        """ duplicatesEnabled(self) -> bool """
        return False

    def editTextChanged(self, *args, **kwargs): # real signature unknown
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

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
        return False

    def findData(self, data, role=None, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findData(self, data: Any, role: int = Qt.UserRole, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchExactly|Qt.MatchCaseSensitive) -> int """
        pass

    def findText(self, text, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findText(self, text: str, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchExactly|Qt.MatchCaseSensitive) -> int """
        pass

    def focusInEvent(self, e): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, e): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, e: QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hideEvent(self, e): # real signature unknown; restored from __doc__
        """ hideEvent(self, e: QHideEvent) """
        pass

    def hidePopup(self): # real signature unknown; restored from __doc__
        """ hidePopup(self) """
        pass

    def highlighted(self, *args, **kwargs): # real signature unknown
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

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: QStyleOptionComboBox) """
        pass

    def inputMethodEvent(self, a0): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, a0: QInputMethodEvent) """
        pass

    def inputMethodQuery(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        inputMethodQuery(self, a0: Qt.InputMethodQuery) -> Any
        inputMethodQuery(self, query: Qt.InputMethodQuery, argument: Any) -> Any
        """
        pass

    def insertItem(self, index, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertItem(self, index: int, text: str, userData: Any = None)
        insertItem(self, index: int, icon: QIcon, text: str, userData: Any = None)
        """
        pass

    def insertItems(self, index, texts, p_str=None): # real signature unknown; restored from __doc__
        """ insertItems(self, index: int, texts: Iterable[str]) """
        pass

    def insertPolicy(self): # real signature unknown; restored from __doc__
        """ insertPolicy(self) -> QComboBox.InsertPolicy """
        pass

    def insertSeparator(self, index): # real signature unknown; restored from __doc__
        """ insertSeparator(self, index: int) """
        pass

    def isEditable(self): # real signature unknown; restored from __doc__
        """ isEditable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemData(self, index, role=None): # real signature unknown; restored from __doc__
        """ itemData(self, index: int, role: int = Qt.UserRole) -> Any """
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def itemIcon(self, index): # real signature unknown; restored from __doc__
        """ itemIcon(self, index: int) -> QIcon """
        pass

    def itemText(self, index): # real signature unknown; restored from __doc__
        """ itemText(self, index: int) -> str """
        return ""

    def keyPressEvent(self, e): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: QKeyEvent) """
        pass

    def keyReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, e: QKeyEvent) """
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def lineEdit(self): # real signature unknown; restored from __doc__
        """ lineEdit(self) -> QLineEdit """
        return QLineEdit

    def maxCount(self): # real signature unknown; restored from __doc__
        """ maxCount(self) -> int """
        return 0

    def maxVisibleItems(self): # real signature unknown; restored from __doc__
        """ maxVisibleItems(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumContentsLength(self): # real signature unknown; restored from __doc__
        """ minimumContentsLength(self) -> int """
        return 0

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        pass

    def modelColumn(self): # real signature unknown; restored from __doc__
        """ modelColumn(self) -> int """
        return 0

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, e): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: QMouseEvent) """
        pass

    def mouseReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, e): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: QPaintEvent) """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> str """
        return ""

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeItem(self, index): # real signature unknown; restored from __doc__
        """ removeItem(self, index: int) """
        pass

    def resizeEvent(self, e): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: QResizeEvent) """
        pass

    def rootModelIndex(self): # real signature unknown; restored from __doc__
        """ rootModelIndex(self) -> QModelIndex """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCompleter(self, c): # real signature unknown; restored from __doc__
        """ setCompleter(self, c: QCompleter) """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) """
        pass

    def setCurrentText(self, text): # real signature unknown; restored from __doc__
        """ setCurrentText(self, text: str) """
        pass

    def setDuplicatesEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setDuplicatesEnabled(self, enable: bool) """
        pass

    def setEditable(self, editable): # real signature unknown; restored from __doc__
        """ setEditable(self, editable: bool) """
        pass

    def setEditText(self, text): # real signature unknown; restored from __doc__
        """ setEditText(self, text: str) """
        pass

    def setFrame(self, a0): # real signature unknown; restored from __doc__
        """ setFrame(self, a0: bool) """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: QSize) """
        pass

    def setInsertPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setInsertPolicy(self, policy: QComboBox.InsertPolicy) """
        pass

    def setItemData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: int, value: Any, role: int = Qt.ItemDataRole.UserRole) """
        pass

    def setItemDelegate(self, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, delegate: QAbstractItemDelegate) """
        pass

    def setItemIcon(self, index, icon): # real signature unknown; restored from __doc__
        """ setItemIcon(self, index: int, icon: QIcon) """
        pass

    def setItemText(self, index, text): # real signature unknown; restored from __doc__
        """ setItemText(self, index: int, text: str) """
        pass

    def setLineEdit(self, edit): # real signature unknown; restored from __doc__
        """ setLineEdit(self, edit: QLineEdit) """
        pass

    def setMaxCount(self, max): # real signature unknown; restored from __doc__
        """ setMaxCount(self, max: int) """
        pass

    def setMaxVisibleItems(self, maxItems): # real signature unknown; restored from __doc__
        """ setMaxVisibleItems(self, maxItems: int) """
        pass

    def setMinimumContentsLength(self, characters): # real signature unknown; restored from __doc__
        """ setMinimumContentsLength(self, characters: int) """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: QAbstractItemModel) """
        pass

    def setModelColumn(self, visibleColumn): # real signature unknown; restored from __doc__
        """ setModelColumn(self, visibleColumn: int) """
        pass

    def setPlaceholderText(self, placeholderText): # real signature unknown; restored from __doc__
        """ setPlaceholderText(self, placeholderText: str) """
        pass

    def setRootModelIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootModelIndex(self, index: QModelIndex) """
        pass

    def setSizeAdjustPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setSizeAdjustPolicy(self, policy: QComboBox.SizeAdjustPolicy) """
        pass

    def setValidator(self, v): # real signature unknown; restored from __doc__
        """ setValidator(self, v: QValidator) """
        pass

    def setView(self, itemView): # real signature unknown; restored from __doc__
        """ setView(self, itemView: QAbstractItemView) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, e): # real signature unknown; restored from __doc__
        """ showEvent(self, e: QShowEvent) """
        pass

    def showPopup(self): # real signature unknown; restored from __doc__
        """ showPopup(self) """
        pass

    def sizeAdjustPolicy(self): # real signature unknown; restored from __doc__
        """ sizeAdjustPolicy(self) -> QComboBox.SizeAdjustPolicy """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def textActivated(self, *args, **kwargs): # real signature unknown
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

    def textHighlighted(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validator(self): # real signature unknown; restored from __doc__
        """ validator(self) -> QValidator """
        pass

    def view(self): # real signature unknown; restored from __doc__
        """ view(self) -> QAbstractItemView """
        return QAbstractItemView

    def wheelEvent(self, e): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: QWheelEvent) """
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    AdjustToContents = 0
    AdjustToContentsOnFirstShow = 1
    AdjustToMinimumContentsLength = 2
    AdjustToMinimumContentsLengthWithIcon = 3
    InsertAfterCurrent = 4
    InsertAlphabetically = 6
    InsertAtBottom = 3
    InsertAtCurrent = 2
    InsertAtTop = 1
    InsertBeforeCurrent = 5
    NoInsert = 0


