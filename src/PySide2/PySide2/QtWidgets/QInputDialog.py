# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QDialog import QDialog

class QInputDialog(QDialog):
    """ QInputDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def cancelButtonText(self): # real signature unknown; restored from __doc__
        """ cancelButtonText(self) -> str """
        return ""

    def comboBoxItems(self): # real signature unknown; restored from __doc__
        """ comboBoxItems(self) -> typing.List[str] """
        pass

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) -> None """
        pass

    def doubleDecimals(self): # real signature unknown; restored from __doc__
        """ doubleDecimals(self) -> int """
        return 0

    def doubleMaximum(self): # real signature unknown; restored from __doc__
        """ doubleMaximum(self) -> float """
        return 0.0

    def doubleMinimum(self): # real signature unknown; restored from __doc__
        """ doubleMinimum(self) -> float """
        return 0.0

    def doubleStep(self): # real signature unknown; restored from __doc__
        """ doubleStep(self) -> float """
        return 0.0

    def doubleValue(self): # real signature unknown; restored from __doc__
        """ doubleValue(self) -> float """
        return 0.0

    def doubleValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def doubleValueSelected(self, *args, **kwargs): # real signature unknown
        pass

    def getDouble(self, parent, title, label, value, minValue, maxValue, decimals, flags, step): # real signature unknown; restored from __doc__
        """
        getDouble(parent: PySide2.QtWidgets.QWidget, title: str, label: str, value: float, minValue: float, maxValue: float, decimals: int, flags: PySide2.QtCore.Qt.WindowFlags, step: float) -> typing.Tuple[float, bool]
        getDouble(parent: PySide2.QtWidgets.QWidget, title: str, label: str, value: float, minValue: float = 0, maxValue: float = -2147483647, decimals: int = 2147483647, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> typing.Tuple[float, bool]
        """
        pass

    def getInt(self, parent, title, label, value, minValue=0, maxValue=-2147483647, step=2147483647, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getInt(parent: PySide2.QtWidgets.QWidget, title: str, label: str, value: int, minValue: int = 0, maxValue: int = -2147483647, step: int = 2147483647, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> typing.Tuple[int, bool] """
        pass

    def getItem(self, parent, title, label, items, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getItem(parent: PySide2.QtWidgets.QWidget, title: str, label: str, items: typing.Sequence[str], current: int, editable: bool = 0, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags), inputMethodHints: PySide2.QtCore.Qt.InputMethodHints = PySide2.QtCore.Qt.InputMethodHint.ImhNone) -> typing.Tuple[str, bool] """
        pass

    def getMultiLineText(self, parent, title, label, text, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getMultiLineText(parent: PySide2.QtWidgets.QWidget, title: str, label: str, text: str, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags), inputMethodHints: PySide2.QtCore.Qt.InputMethodHints = PySide2.QtCore.Qt.InputMethodHint.ImhNone) -> typing.Tuple[str, bool] """
        pass

    def getText(self, parent, title, label, echo, text=None, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getText(parent: PySide2.QtWidgets.QWidget, title: str, label: str, echo: PySide2.QtWidgets.QLineEdit.EchoMode, text: str = PySide2.QtWidgets.QLineEdit.EchoMode.Normal, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags), inputMethodHints: PySide2.QtCore.Qt.InputMethodHints = PySide2.QtCore.Qt.InputMethodHint.ImhNone) -> typing.Tuple[str, bool] """
        pass

    def inputMode(self): # real signature unknown; restored from __doc__
        """ inputMode(self) -> PySide2.QtWidgets.QInputDialog.InputMode """
        pass

    def intMaximum(self): # real signature unknown; restored from __doc__
        """ intMaximum(self) -> int """
        return 0

    def intMinimum(self): # real signature unknown; restored from __doc__
        """ intMinimum(self) -> int """
        return 0

    def intStep(self): # real signature unknown; restored from __doc__
        """ intStep(self) -> int """
        return 0

    def intValue(self): # real signature unknown; restored from __doc__
        """ intValue(self) -> int """
        return 0

    def intValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def intValueSelected(self, *args, **kwargs): # real signature unknown
        pass

    def isComboBoxEditable(self): # real signature unknown; restored from __doc__
        """ isComboBoxEditable(self) -> bool """
        return False

    def labelText(self): # real signature unknown; restored from __doc__
        """ labelText(self) -> str """
        return ""

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def okButtonText(self): # real signature unknown; restored from __doc__
        """ okButtonText(self) -> str """
        return ""

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def setCancelButtonText(self, text): # real signature unknown; restored from __doc__
        """ setCancelButtonText(self, text: str) -> None """
        pass

    def setComboBoxEditable(self, editable): # real signature unknown; restored from __doc__
        """ setComboBoxEditable(self, editable: bool) -> None """
        pass

    def setComboBoxItems(self, items, p_str=None): # real signature unknown; restored from __doc__
        """ setComboBoxItems(self, items: typing.Sequence[str]) -> None """
        pass

    def setDoubleDecimals(self, decimals): # real signature unknown; restored from __doc__
        """ setDoubleDecimals(self, decimals: int) -> None """
        pass

    def setDoubleMaximum(self, max): # real signature unknown; restored from __doc__
        """ setDoubleMaximum(self, max: float) -> None """
        pass

    def setDoubleMinimum(self, min): # real signature unknown; restored from __doc__
        """ setDoubleMinimum(self, min: float) -> None """
        pass

    def setDoubleRange(self, min, max): # real signature unknown; restored from __doc__
        """ setDoubleRange(self, min: float, max: float) -> None """
        pass

    def setDoubleStep(self, step): # real signature unknown; restored from __doc__
        """ setDoubleStep(self, step: float) -> None """
        pass

    def setDoubleValue(self, value): # real signature unknown; restored from __doc__
        """ setDoubleValue(self, value: float) -> None """
        pass

    def setInputMode(self, mode): # real signature unknown; restored from __doc__
        """ setInputMode(self, mode: PySide2.QtWidgets.QInputDialog.InputMode) -> None """
        pass

    def setIntMaximum(self, max): # real signature unknown; restored from __doc__
        """ setIntMaximum(self, max: int) -> None """
        pass

    def setIntMinimum(self, min): # real signature unknown; restored from __doc__
        """ setIntMinimum(self, min: int) -> None """
        pass

    def setIntRange(self, min, max): # real signature unknown; restored from __doc__
        """ setIntRange(self, min: int, max: int) -> None """
        pass

    def setIntStep(self, step): # real signature unknown; restored from __doc__
        """ setIntStep(self, step: int) -> None """
        pass

    def setIntValue(self, value): # real signature unknown; restored from __doc__
        """ setIntValue(self, value: int) -> None """
        pass

    def setLabelText(self, text): # real signature unknown; restored from __doc__
        """ setLabelText(self, text: str) -> None """
        pass

    def setOkButtonText(self, text): # real signature unknown; restored from __doc__
        """ setOkButtonText(self, text: str) -> None """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtWidgets.QInputDialog.InputDialogOption, on: bool = True) -> None """
        pass

    def setTextEchoMode(self, mode): # real signature unknown; restored from __doc__
        """ setTextEchoMode(self, mode: PySide2.QtWidgets.QLineEdit.EchoMode) -> None """
        pass

    def setTextValue(self, text): # real signature unknown; restored from __doc__
        """ setTextValue(self, text: str) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: PySide2.QtWidgets.QInputDialog.InputDialogOption) -> bool """
        return False

    def textEchoMode(self): # real signature unknown; restored from __doc__
        """ textEchoMode(self) -> PySide2.QtWidgets.QLineEdit.EchoMode """
        pass

    def textValue(self): # real signature unknown; restored from __doc__
        """ textValue(self) -> str """
        return ""

    def textValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textValueSelected(self, *args, **kwargs): # real signature unknown
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

    DoubleInput = PySide2.QtWidgets.QInputDialog.InputMode.DoubleInput
    InputDialogOption = None # (!) real value is "<class 'PySide2.QtWidgets.QInputDialog.InputDialogOption'>"
    InputMode = None # (!) real value is "<class 'PySide2.QtWidgets.QInputDialog.InputMode'>"
    IntInput = PySide2.QtWidgets.QInputDialog.InputMode.IntInput
    NoButtons = PySide2.QtWidgets.QInputDialog.InputDialogOption.NoButtons
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50849E40>'
    TextInput = PySide2.QtWidgets.QInputDialog.InputMode.TextInput
    UseListViewForComboBoxItems = PySide2.QtWidgets.QInputDialog.InputDialogOption.UseListViewForComboBoxItems
    UsePlainTextEditForTextInput = PySide2.QtWidgets.QInputDialog.InputDialogOption.UsePlainTextEditForTextInput


