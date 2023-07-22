# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QWidget import QWidget

class QComboBox(QWidget):
    """ QComboBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def activated(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, icon, text, userData=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addItem(self, icon: PySide2.QtGui.QIcon, text: str, userData: typing.Any = Invalid(typing.Any)) -> None
        addItem(self, text: str, userData: typing.Any = Invalid(typing.Any)) -> None
        """
        pass

    def addItems(self, texts, p_str=None): # real signature unknown; restored from __doc__
        """ addItems(self, texts: typing.Sequence[str]) -> None """
        pass

    def autoCompletion(self): # real signature unknown; restored from __doc__
        """ autoCompletion(self) -> bool """
        return False

    def autoCompletionCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ autoCompletionCaseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity """
        pass

    def changeEvent(self, e): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: PySide2.QtCore.QEvent) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearEditText(self): # real signature unknown; restored from __doc__
        """ clearEditText(self) -> None """
        pass

    def completer(self): # real signature unknown; restored from __doc__
        """ completer(self) -> PySide2.QtWidgets.QCompleter """
        pass

    def contextMenuEvent(self, e): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, e: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentData(self, role=None): # real signature unknown; restored from __doc__
        """ currentData(self, role: int = PySide2.QtCore.Qt.ItemDataRole.UserRole) -> typing.Any """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentIndexChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentText(self): # real signature unknown; restored from __doc__
        """ currentText(self) -> str """
        return ""

    def currentTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def duplicatesEnabled(self): # real signature unknown; restored from __doc__
        """ duplicatesEnabled(self) -> bool """
        return False

    def editTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def findData(self, data, role=None, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findData(self, data: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.UserRole, flags: PySide2.QtCore.Qt.MatchFlags = Instance(Qt.MatchFlags(Qt.MatchExactly | Qt.MatchCaseSensitive))) -> int """
        pass

    def findText(self, text, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findText(self, text: str, flags: PySide2.QtCore.Qt.MatchFlags = Instance(Qt.MatchFlags(Qt.MatchExactly | Qt.MatchCaseSensitive))) -> int """
        pass

    def focusInEvent(self, e): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusOutEvent(self, e): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, e: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hideEvent(self, e): # real signature unknown; restored from __doc__
        """ hideEvent(self, e: PySide2.QtGui.QHideEvent) -> None """
        pass

    def hidePopup(self): # real signature unknown; restored from __doc__
        """ hidePopup(self) -> None """
        pass

    def highlighted(self, *args, **kwargs): # real signature unknown
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> PySide2.QtCore.QSize """
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionComboBox) -> None """
        pass

    def inputMethodEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, arg__1: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodQuery(self, arg__1): # real signature unknown; restored from __doc__
        """
        inputMethodQuery(self, arg__1: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any
        inputMethodQuery(self, query: PySide2.QtCore.Qt.InputMethodQuery, argument: typing.Any) -> typing.Any
        """
        pass

    def insertItem(self, index, icon, text, userData=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        insertItem(self, index: int, icon: PySide2.QtGui.QIcon, text: str, userData: typing.Any = Invalid(typing.Any)) -> None
        insertItem(self, index: int, text: str, userData: typing.Any = Invalid(typing.Any)) -> None
        """
        pass

    def insertItems(self, index, texts, p_str=None): # real signature unknown; restored from __doc__
        """ insertItems(self, index: int, texts: typing.Sequence[str]) -> None """
        pass

    def insertPolicy(self): # real signature unknown; restored from __doc__
        """ insertPolicy(self) -> PySide2.QtWidgets.QComboBox.InsertPolicy """
        pass

    def insertSeparator(self, index): # real signature unknown; restored from __doc__
        """ insertSeparator(self, index: int) -> None """
        pass

    def isEditable(self): # real signature unknown; restored from __doc__
        """ isEditable(self) -> bool """
        return False

    def itemData(self, index, role=None): # real signature unknown; restored from __doc__
        """ itemData(self, index: int, role: int = PySide2.QtCore.Qt.ItemDataRole.UserRole) -> typing.Any """
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> PySide2.QtWidgets.QAbstractItemDelegate """
        pass

    def itemIcon(self, index): # real signature unknown; restored from __doc__
        """ itemIcon(self, index: int) -> PySide2.QtGui.QIcon """
        pass

    def itemText(self, index): # real signature unknown; restored from __doc__
        """ itemText(self, index: int) -> str """
        return ""

    def keyPressEvent(self, e): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, e: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def lineEdit(self): # real signature unknown; restored from __doc__
        """ lineEdit(self) -> PySide2.QtWidgets.QLineEdit """
        pass

    def maxCount(self): # real signature unknown; restored from __doc__
        """ maxCount(self) -> int """
        return 0

    def maxVisibleItems(self): # real signature unknown; restored from __doc__
        """ maxVisibleItems(self) -> int """
        return 0

    def minimumContentsLength(self): # real signature unknown; restored from __doc__
        """ minimumContentsLength(self) -> int """
        return 0

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> PySide2.QtCore.QAbstractItemModel """
        pass

    def modelColumn(self): # real signature unknown; restored from __doc__
        """ modelColumn(self) -> int """
        return 0

    def mousePressEvent(self, e): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def paintEvent(self, e): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> str """
        return ""

    def removeItem(self, index): # real signature unknown; restored from __doc__
        """ removeItem(self, index: int) -> None """
        pass

    def resizeEvent(self, e): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def rootModelIndex(self): # real signature unknown; restored from __doc__
        """ rootModelIndex(self) -> PySide2.QtCore.QModelIndex """
        pass

    def setAutoCompletion(self, enable): # real signature unknown; restored from __doc__
        """ setAutoCompletion(self, enable: bool) -> None """
        pass

    def setAutoCompletionCaseSensitivity(self, sensitivity): # real signature unknown; restored from __doc__
        """ setAutoCompletionCaseSensitivity(self, sensitivity: PySide2.QtCore.Qt.CaseSensitivity) -> None """
        pass

    def setCompleter(self, c): # real signature unknown; restored from __doc__
        """ setCompleter(self, c: PySide2.QtWidgets.QCompleter) -> None """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) -> None """
        pass

    def setCurrentText(self, text): # real signature unknown; restored from __doc__
        """ setCurrentText(self, text: str) -> None """
        pass

    def setDuplicatesEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setDuplicatesEnabled(self, enable: bool) -> None """
        pass

    def setEditable(self, editable): # real signature unknown; restored from __doc__
        """ setEditable(self, editable: bool) -> None """
        pass

    def setEditText(self, text): # real signature unknown; restored from __doc__
        """ setEditText(self, text: str) -> None """
        pass

    def setFrame(self, arg__1): # real signature unknown; restored from __doc__
        """ setFrame(self, arg__1: bool) -> None """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setInsertPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setInsertPolicy(self, policy: PySide2.QtWidgets.QComboBox.InsertPolicy) -> None """
        pass

    def setItemData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: int, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.UserRole) -> None """
        pass

    def setItemDelegate(self, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, delegate: PySide2.QtWidgets.QAbstractItemDelegate) -> None """
        pass

    def setItemIcon(self, index, icon): # real signature unknown; restored from __doc__
        """ setItemIcon(self, index: int, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setItemText(self, index, text): # real signature unknown; restored from __doc__
        """ setItemText(self, index: int, text: str) -> None """
        pass

    def setLineEdit(self, edit): # real signature unknown; restored from __doc__
        """ setLineEdit(self, edit: PySide2.QtWidgets.QLineEdit) -> None """
        pass

    def setMaxCount(self, max): # real signature unknown; restored from __doc__
        """ setMaxCount(self, max: int) -> None """
        pass

    def setMaxVisibleItems(self, maxItems): # real signature unknown; restored from __doc__
        """ setMaxVisibleItems(self, maxItems: int) -> None """
        pass

    def setMinimumContentsLength(self, characters): # real signature unknown; restored from __doc__
        """ setMinimumContentsLength(self, characters: int) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setModelColumn(self, visibleColumn): # real signature unknown; restored from __doc__
        """ setModelColumn(self, visibleColumn: int) -> None """
        pass

    def setPlaceholderText(self, placeholderText): # real signature unknown; restored from __doc__
        """ setPlaceholderText(self, placeholderText: str) -> None """
        pass

    def setRootModelIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootModelIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setSizeAdjustPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setSizeAdjustPolicy(self, policy: PySide2.QtWidgets.QComboBox.SizeAdjustPolicy) -> None """
        pass

    def setValidator(self, v): # real signature unknown; restored from __doc__
        """ setValidator(self, v: PySide2.QtGui.QValidator) -> None """
        pass

    def setView(self, itemView): # real signature unknown; restored from __doc__
        """ setView(self, itemView: PySide2.QtWidgets.QAbstractItemView) -> None """
        pass

    def showEvent(self, e): # real signature unknown; restored from __doc__
        """ showEvent(self, e: PySide2.QtGui.QShowEvent) -> None """
        pass

    def showPopup(self): # real signature unknown; restored from __doc__
        """ showPopup(self) -> None """
        pass

    def sizeAdjustPolicy(self): # real signature unknown; restored from __doc__
        """ sizeAdjustPolicy(self) -> PySide2.QtWidgets.QComboBox.SizeAdjustPolicy """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def textActivated(self, *args, **kwargs): # real signature unknown
        pass

    def textHighlighted(self, *args, **kwargs): # real signature unknown
        pass

    def validator(self): # real signature unknown; restored from __doc__
        """ validator(self) -> PySide2.QtGui.QValidator """
        pass

    def view(self): # real signature unknown; restored from __doc__
        """ view(self) -> PySide2.QtWidgets.QAbstractItemView """
        pass

    def wheelEvent(self, e): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: PySide2.QtGui.QWheelEvent) -> None """
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

    AdjustToContents = PySide2.QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents
    AdjustToContentsOnFirstShow = PySide2.QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow
    AdjustToMinimumContentsLength = PySide2.QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLength
    AdjustToMinimumContentsLengthWithIcon = PySide2.QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon
    InsertAfterCurrent = PySide2.QtWidgets.QComboBox.InsertPolicy.InsertAfterCurrent
    InsertAlphabetically = PySide2.QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically
    InsertAtBottom = PySide2.QtWidgets.QComboBox.InsertPolicy.InsertAtBottom
    InsertAtCurrent = PySide2.QtWidgets.QComboBox.InsertPolicy.InsertAtCurrent
    InsertAtTop = PySide2.QtWidgets.QComboBox.InsertPolicy.InsertAtTop
    InsertBeforeCurrent = PySide2.QtWidgets.QComboBox.InsertPolicy.InsertBeforeCurrent
    InsertPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QComboBox.InsertPolicy'>"
    NoInsert = PySide2.QtWidgets.QComboBox.InsertPolicy.NoInsert
    SizeAdjustPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QComboBox.SizeAdjustPolicy'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507BD4C0>'


