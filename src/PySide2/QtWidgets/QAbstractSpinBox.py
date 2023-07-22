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

class QAbstractSpinBox(QWidget):
    """ QAbstractSpinBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def buttonSymbols(self): # real signature unknown; restored from __doc__
        """ buttonSymbols(self) -> PySide2.QtWidgets.QAbstractSpinBox.ButtonSymbols """
        pass

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def closeEvent(self, event): # real signature unknown; restored from __doc__
        """ closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None """
        pass

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def correctionMode(self): # real signature unknown; restored from __doc__
        """ correctionMode(self) -> PySide2.QtWidgets.QAbstractSpinBox.CorrectionMode """
        pass

    def editingFinished(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def fixup(self, input): # real signature unknown; restored from __doc__
        """ fixup(self, input: str) -> None """
        pass

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def hasAcceptableInput(self): # real signature unknown; restored from __doc__
        """ hasAcceptableInput(self) -> bool """
        return False

    def hasFrame(self): # real signature unknown; restored from __doc__
        """ hasFrame(self) -> bool """
        return False

    def hideEvent(self, event): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: PySide2.QtGui.QHideEvent) -> None """
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionSpinBox) -> None """
        pass

    def inputMethodQuery(self, arg__1): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, arg__1: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any """
        pass

    def interpretText(self): # real signature unknown; restored from __doc__
        """ interpretText(self) -> None """
        pass

    def isAccelerated(self): # real signature unknown; restored from __doc__
        """ isAccelerated(self) -> bool """
        return False

    def isGroupSeparatorShown(self): # real signature unknown; restored from __doc__
        """ isGroupSeparatorShown(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def keyboardTracking(self): # real signature unknown; restored from __doc__
        """ keyboardTracking(self) -> bool """
        return False

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def lineEdit(self): # real signature unknown; restored from __doc__
        """ lineEdit(self) -> PySide2.QtWidgets.QLineEdit """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
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

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def selectAll(self): # real signature unknown; restored from __doc__
        """ selectAll(self) -> None """
        pass

    def setAccelerated(self, on): # real signature unknown; restored from __doc__
        """ setAccelerated(self, on: bool) -> None """
        pass

    def setAlignment(self, flag): # real signature unknown; restored from __doc__
        """ setAlignment(self, flag: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setButtonSymbols(self, bs): # real signature unknown; restored from __doc__
        """ setButtonSymbols(self, bs: PySide2.QtWidgets.QAbstractSpinBox.ButtonSymbols) -> None """
        pass

    def setCorrectionMode(self, cm): # real signature unknown; restored from __doc__
        """ setCorrectionMode(self, cm: PySide2.QtWidgets.QAbstractSpinBox.CorrectionMode) -> None """
        pass

    def setFrame(self, arg__1): # real signature unknown; restored from __doc__
        """ setFrame(self, arg__1: bool) -> None """
        pass

    def setGroupSeparatorShown(self, shown): # real signature unknown; restored from __doc__
        """ setGroupSeparatorShown(self, shown: bool) -> None """
        pass

    def setKeyboardTracking(self, kt): # real signature unknown; restored from __doc__
        """ setKeyboardTracking(self, kt: bool) -> None """
        pass

    def setLineEdit(self, edit): # real signature unknown; restored from __doc__
        """ setLineEdit(self, edit: PySide2.QtWidgets.QLineEdit) -> None """
        pass

    def setReadOnly(self, r): # real signature unknown; restored from __doc__
        """ setReadOnly(self, r: bool) -> None """
        pass

    def setSpecialValueText(self, txt): # real signature unknown; restored from __doc__
        """ setSpecialValueText(self, txt: str) -> None """
        pass

    def setWrapping(self, w): # real signature unknown; restored from __doc__
        """ setWrapping(self, w: bool) -> None """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def specialValueText(self): # real signature unknown; restored from __doc__
        """ specialValueText(self) -> str """
        return ""

    def stepBy(self, steps): # real signature unknown; restored from __doc__
        """ stepBy(self, steps: int) -> None """
        pass

    def stepDown(self): # real signature unknown; restored from __doc__
        """ stepDown(self) -> None """
        pass

    def stepEnabled(self): # real signature unknown; restored from __doc__
        """ stepEnabled(self) -> PySide2.QtWidgets.QAbstractSpinBox.StepEnabled """
        pass

    def stepUp(self): # real signature unknown; restored from __doc__
        """ stepUp(self) -> None """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def validate(self, input, pos): # real signature unknown; restored from __doc__
        """ validate(self, input: str, pos: int) -> PySide2.QtGui.QValidator.State """
        pass

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def wrapping(self): # real signature unknown; restored from __doc__
        """ wrapping(self) -> bool """
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

    AdaptiveDecimalStepType = PySide2.QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType
    ButtonSymbols = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractSpinBox.ButtonSymbols'>"
    CorrectionMode = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractSpinBox.CorrectionMode'>"
    CorrectToNearestValue = PySide2.QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue
    CorrectToPreviousValue = PySide2.QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue
    DefaultStepType = PySide2.QtWidgets.QAbstractSpinBox.StepType.DefaultStepType
    NoButtons = PySide2.QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons
    PlusMinus = PySide2.QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507D4FC0>'
    StepDownEnabled = PySide2.QtWidgets.QAbstractSpinBox.StepEnabledFlag.StepDownEnabled
    StepEnabled = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractSpinBox.StepEnabled'>"
    StepEnabledFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractSpinBox.StepEnabledFlag'>"
    StepNone = PySide2.QtWidgets.QAbstractSpinBox.StepEnabledFlag.StepNone
    StepType = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractSpinBox.StepType'>"
    StepUpEnabled = PySide2.QtWidgets.QAbstractSpinBox.StepEnabledFlag.StepUpEnabled
    UpDownArrows = PySide2.QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows


