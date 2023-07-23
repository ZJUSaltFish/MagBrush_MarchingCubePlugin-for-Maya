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

class QLineEdit(QWidget):
    """
    QLineEdit(self, arg__1: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QLineEdit(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def addAction(self, action): # real signature unknown; restored from __doc__
        """
        addAction(self, action: PySide2.QtWidgets.QAction) -> None
        addAction(self, action: PySide2.QtWidgets.QAction, position: PySide2.QtWidgets.QLineEdit.ActionPosition) -> None
        addAction(self, arg__1: PySide2.QtWidgets.QAction) -> None
        addAction(self, icon: PySide2.QtGui.QIcon, position: PySide2.QtWidgets.QLineEdit.ActionPosition) -> PySide2.QtWidgets.QAction
        """
        pass

    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def backspace(self): # real signature unknown; restored from __doc__
        """ backspace(self) -> None """
        pass

    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def completer(self): # real signature unknown; restored from __doc__
        """ completer(self) -> PySide2.QtWidgets.QCompleter """
        pass

    def contextMenuEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, arg__1: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> None """
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ createStandardContextMenu(self) -> PySide2.QtWidgets.QMenu """
        pass

    def cursorBackward(self, mark, steps=1): # real signature unknown; restored from __doc__
        """ cursorBackward(self, mark: bool, steps: int = 1) -> None """
        pass

    def cursorForward(self, mark, steps=1): # real signature unknown; restored from __doc__
        """ cursorForward(self, mark: bool, steps: int = 1) -> None """
        pass

    def cursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ cursorMoveStyle(self) -> PySide2.QtCore.Qt.CursorMoveStyle """
        pass

    def cursorPosition(self): # real signature unknown; restored from __doc__
        """ cursorPosition(self) -> int """
        return 0

    def cursorPositionAt(self, pos): # real signature unknown; restored from __doc__
        """ cursorPositionAt(self, pos: PySide2.QtCore.QPoint) -> int """
        return 0

    def cursorPositionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def cursorRect(self): # real signature unknown; restored from __doc__
        """ cursorRect(self) -> PySide2.QtCore.QRect """
        pass

    def cursorWordBackward(self, mark): # real signature unknown; restored from __doc__
        """ cursorWordBackward(self, mark: bool) -> None """
        pass

    def cursorWordForward(self, mark): # real signature unknown; restored from __doc__
        """ cursorWordForward(self, mark: bool) -> None """
        pass

    def cut(self): # real signature unknown; restored from __doc__
        """ cut(self) -> None """
        pass

    def del_(self): # real signature unknown; restored from __doc__
        """ del_(self) -> None """
        pass

    def deselect(self): # real signature unknown; restored from __doc__
        """ deselect(self) -> None """
        pass

    def displayText(self): # real signature unknown; restored from __doc__
        """ displayText(self) -> str """
        return ""

    def dragEnabled(self): # real signature unknown; restored from __doc__
        """ dragEnabled(self) -> bool """
        return False

    def dragEnterEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, arg__1: PySide2.QtGui.QDragEnterEvent) -> None """
        pass

    def dragLeaveEvent(self, e): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, e: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMoveEvent(self, e): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, e: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def dropEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dropEvent(self, arg__1: PySide2.QtGui.QDropEvent) -> None """
        pass

    def echoMode(self): # real signature unknown; restored from __doc__
        """ echoMode(self) -> PySide2.QtWidgets.QLineEdit.EchoMode """
        pass

    def editingFinished(self, *args, **kwargs): # real signature unknown
        pass

    def end(self, mark): # real signature unknown; restored from __doc__
        """ end(self, mark: bool) -> None """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def focusInEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusInEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusOutEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def getTextMargins(self): # real signature unknown; restored from __doc__
        """ getTextMargins(self) -> typing.Tuple[int, int, int, int] """
        pass

    def hasAcceptableInput(self): # real signature unknown; restored from __doc__
        """ hasAcceptableInput(self) -> bool """
        return False

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hasSelectedText(self): # real signature unknown; restored from __doc__
        """ hasSelectedText(self) -> bool """
        return False

    def home(self, mark): # real signature unknown; restored from __doc__
        """ home(self, mark: bool) -> None """
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionFrame) -> None """
        pass

    def inputMask(self): # real signature unknown; restored from __doc__
        """ inputMask(self) -> str """
        return ""

    def inputMethodEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, arg__1: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodQuery(self, arg__1): # real signature unknown; restored from __doc__
        """
        inputMethodQuery(self, arg__1: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any
        inputMethodQuery(self, property: PySide2.QtCore.Qt.InputMethodQuery, argument: typing.Any) -> typing.Any
        """
        pass

    def inputRejected(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, arg__1): # real signature unknown; restored from __doc__
        """ insert(self, arg__1: str) -> None """
        pass

    def isClearButtonEnabled(self): # real signature unknown; restored from __doc__
        """ isClearButtonEnabled(self) -> bool """
        return False

    def isModified(self): # real signature unknown; restored from __doc__
        """ isModified(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isRedoAvailable(self): # real signature unknown; restored from __doc__
        """ isRedoAvailable(self) -> bool """
        return False

    def isUndoAvailable(self): # real signature unknown; restored from __doc__
        """ isUndoAvailable(self) -> bool """
        return False

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def maxLength(self): # real signature unknown; restored from __doc__
        """ maxLength(self) -> int """
        return 0

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def mouseDoubleClickEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseMoveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def paste(self): # real signature unknown; restored from __doc__
        """ paste(self) -> None """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> str """
        return ""

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) -> None """
        pass

    def returnPressed(self, *args, **kwargs): # real signature unknown
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) -> None """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectionEnd(self): # real signature unknown; restored from __doc__
        """ selectionEnd(self) -> int """
        return 0

    def selectionLength(self): # real signature unknown; restored from __doc__
        """ selectionLength(self) -> int """
        return 0

    def selectionStart(self): # real signature unknown; restored from __doc__
        """ selectionStart(self) -> int """
        return 0

    def setAlignment(self, flag): # real signature unknown; restored from __doc__
        """ setAlignment(self, flag: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setClearButtonEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setClearButtonEnabled(self, enable: bool) -> None """
        pass

    def setCompleter(self, completer): # real signature unknown; restored from __doc__
        """ setCompleter(self, completer: PySide2.QtWidgets.QCompleter) -> None """
        pass

    def setCursorMoveStyle(self, style): # real signature unknown; restored from __doc__
        """ setCursorMoveStyle(self, style: PySide2.QtCore.Qt.CursorMoveStyle) -> None """
        pass

    def setCursorPosition(self, arg__1): # real signature unknown; restored from __doc__
        """ setCursorPosition(self, arg__1: int) -> None """
        pass

    def setDragEnabled(self, b): # real signature unknown; restored from __doc__
        """ setDragEnabled(self, b: bool) -> None """
        pass

    def setEchoMode(self, arg__1): # real signature unknown; restored from __doc__
        """ setEchoMode(self, arg__1: PySide2.QtWidgets.QLineEdit.EchoMode) -> None """
        pass

    def setFrame(self, arg__1): # real signature unknown; restored from __doc__
        """ setFrame(self, arg__1: bool) -> None """
        pass

    def setInputMask(self, inputMask): # real signature unknown; restored from __doc__
        """ setInputMask(self, inputMask: str) -> None """
        pass

    def setMaxLength(self, arg__1): # real signature unknown; restored from __doc__
        """ setMaxLength(self, arg__1: int) -> None """
        pass

    def setModified(self, arg__1): # real signature unknown; restored from __doc__
        """ setModified(self, arg__1: bool) -> None """
        pass

    def setPlaceholderText(self, arg__1): # real signature unknown; restored from __doc__
        """ setPlaceholderText(self, arg__1: str) -> None """
        pass

    def setReadOnly(self, arg__1): # real signature unknown; restored from __doc__
        """ setReadOnly(self, arg__1: bool) -> None """
        pass

    def setSelection(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ setSelection(self, arg__1: int, arg__2: int) -> None """
        pass

    def setText(self, arg__1): # real signature unknown; restored from __doc__
        """ setText(self, arg__1: str) -> None """
        pass

    def setTextMargins(self, left, top, right, bottom): # real signature unknown; restored from __doc__
        """
        setTextMargins(self, left: int, top: int, right: int, bottom: int) -> None
        setTextMargins(self, margins: PySide2.QtCore.QMargins) -> None
        """
        pass

    def setValidator(self, arg__1): # real signature unknown; restored from __doc__
        """ setValidator(self, arg__1: PySide2.QtGui.QValidator) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textEdited(self, *args, **kwargs): # real signature unknown
        pass

    def textMargins(self): # real signature unknown; restored from __doc__
        """ textMargins(self) -> PySide2.QtCore.QMargins """
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) -> None """
        pass

    def validator(self): # real signature unknown; restored from __doc__
        """ validator(self) -> PySide2.QtGui.QValidator """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ActionPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QLineEdit.ActionPosition'>"
    EchoMode = None # (!) real value is "<class 'PySide2.QtWidgets.QLineEdit.EchoMode'>"
    LeadingPosition = PySide2.QtWidgets.QLineEdit.ActionPosition.LeadingPosition
    NoEcho = PySide2.QtWidgets.QLineEdit.EchoMode.NoEcho
    Normal = PySide2.QtWidgets.QLineEdit.EchoMode.Normal
    Password = PySide2.QtWidgets.QLineEdit.EchoMode.Password
    PasswordEchoOnEdit = PySide2.QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507A6500>'
    TrailingPosition = PySide2.QtWidgets.QLineEdit.ActionPosition.TrailingPosition


