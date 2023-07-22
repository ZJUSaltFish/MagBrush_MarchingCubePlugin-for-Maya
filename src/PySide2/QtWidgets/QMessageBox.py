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

class QMessageBox(QDialog):
    """
    QMessageBox(self, icon: PySide2.QtWidgets.QMessageBox.Icon, title: str, text: str, buttons: PySide2.QtWidgets.QMessageBox.StandardButtons = PySide2.QtWidgets.QMessageBox.StandardButton.NoButton, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Instance(Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint)) -> None
    QMessageBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def about(self, parent, title, text): # real signature unknown; restored from __doc__
        """ about(parent: PySide2.QtWidgets.QWidget, title: str, text: str) -> None """
        pass

    def aboutQt(self, parent, title=''): # real signature unknown; restored from __doc__
        """ aboutQt(parent: PySide2.QtWidgets.QWidget, title: str = '') -> None """
        pass

    def addButton(self, button, role): # real signature unknown; restored from __doc__
        """
        addButton(self, button: PySide2.QtWidgets.QAbstractButton, role: PySide2.QtWidgets.QMessageBox.ButtonRole) -> None
        addButton(self, button: PySide2.QtWidgets.QMessageBox.StandardButton) -> PySide2.QtWidgets.QPushButton
        addButton(self, text: str, role: PySide2.QtWidgets.QMessageBox.ButtonRole) -> PySide2.QtWidgets.QPushButton
        """
        pass

    def button(self, which): # real signature unknown; restored from __doc__
        """ button(self, which: PySide2.QtWidgets.QMessageBox.StandardButton) -> PySide2.QtWidgets.QAbstractButton """
        pass

    def buttonClicked(self, *args, **kwargs): # real signature unknown
        pass

    def buttonRole(self, button): # real signature unknown; restored from __doc__
        """ buttonRole(self, button: PySide2.QtWidgets.QAbstractButton) -> PySide2.QtWidgets.QMessageBox.ButtonRole """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> typing.List[PySide2.QtWidgets.QAbstractButton] """
        pass

    def buttonText(self, button): # real signature unknown; restored from __doc__
        """ buttonText(self, button: int) -> str """
        return ""

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def checkBox(self): # real signature unknown; restored from __doc__
        """ checkBox(self) -> PySide2.QtWidgets.QCheckBox """
        pass

    def clickedButton(self): # real signature unknown; restored from __doc__
        """ clickedButton(self) -> PySide2.QtWidgets.QAbstractButton """
        pass

    def closeEvent(self, event): # real signature unknown; restored from __doc__
        """ closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None """
        pass

    def critical(self, parent, title, text, button0, button1): # real signature unknown; restored from __doc__
        """
        critical(parent: PySide2.QtWidgets.QWidget, title: str, text: str, button0: PySide2.QtWidgets.QMessageBox.StandardButton, button1: PySide2.QtWidgets.QMessageBox.StandardButton) -> int
        critical(parent: PySide2.QtWidgets.QWidget, title: str, text: str, buttons: PySide2.QtWidgets.QMessageBox.StandardButtons = PySide2.QtWidgets.QMessageBox.StandardButton.Ok, defaultButton: PySide2.QtWidgets.QMessageBox.StandardButton = PySide2.QtWidgets.QMessageBox.StandardButton.NoButton) -> PySide2.QtWidgets.QMessageBox.StandardButton
        """
        return 0

    def defaultButton(self): # real signature unknown; restored from __doc__
        """ defaultButton(self) -> PySide2.QtWidgets.QPushButton """
        pass

    def detailedText(self): # real signature unknown; restored from __doc__
        """ detailedText(self) -> str """
        return ""

    def escapeButton(self): # real signature unknown; restored from __doc__
        """ escapeButton(self) -> PySide2.QtWidgets.QAbstractButton """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtWidgets.QMessageBox.Icon """
        pass

    def iconPixmap(self): # real signature unknown; restored from __doc__
        """ iconPixmap(self) -> PySide2.QtGui.QPixmap """
        pass

    def information(self, parent, title, text, button0, button1=None): # real signature unknown; restored from __doc__
        """
        information(parent: PySide2.QtWidgets.QWidget, title: str, text: str, button0: PySide2.QtWidgets.QMessageBox.StandardButton, button1: PySide2.QtWidgets.QMessageBox.StandardButton = PySide2.QtWidgets.QMessageBox.StandardButton.NoButton) -> PySide2.QtWidgets.QMessageBox.StandardButton
        information(parent: PySide2.QtWidgets.QWidget, title: str, text: str, buttons: PySide2.QtWidgets.QMessageBox.StandardButtons = PySide2.QtWidgets.QMessageBox.StandardButton.Ok, defaultButton: PySide2.QtWidgets.QMessageBox.StandardButton = PySide2.QtWidgets.QMessageBox.StandardButton.NoButton) -> PySide2.QtWidgets.QMessageBox.StandardButton
        """
        pass

    def informativeText(self): # real signature unknown; restored from __doc__
        """ informativeText(self) -> str """
        return ""

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def question(self, parent, title, text, button0, button1): # real signature unknown; restored from __doc__
        """
        question(parent: PySide2.QtWidgets.QWidget, title: str, text: str, button0: PySide2.QtWidgets.QMessageBox.StandardButton, button1: PySide2.QtWidgets.QMessageBox.StandardButton) -> int
        question(parent: PySide2.QtWidgets.QWidget, title: str, text: str, buttons: PySide2.QtWidgets.QMessageBox.StandardButtons = Instance(QMessageBox.StandardButtons(QMessageBox.Yes | QMessageBox.No)), defaultButton: PySide2.QtWidgets.QMessageBox.StandardButton = PySide2.QtWidgets.QMessageBox.StandardButton.NoButton) -> PySide2.QtWidgets.QMessageBox.StandardButton
        """
        return 0

    def removeButton(self, button): # real signature unknown; restored from __doc__
        """ removeButton(self, button: PySide2.QtWidgets.QAbstractButton) -> None """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def setButtonText(self, button, text): # real signature unknown; restored from __doc__
        """ setButtonText(self, button: int, text: str) -> None """
        pass

    def setCheckBox(self, cb): # real signature unknown; restored from __doc__
        """ setCheckBox(self, cb: PySide2.QtWidgets.QCheckBox) -> None """
        pass

    def setDefaultButton(self, button): # real signature unknown; restored from __doc__
        """
        setDefaultButton(self, button: PySide2.QtWidgets.QMessageBox.StandardButton) -> None
        setDefaultButton(self, button: PySide2.QtWidgets.QPushButton) -> None
        """
        pass

    def setDetailedText(self, text): # real signature unknown; restored from __doc__
        """ setDetailedText(self, text: str) -> None """
        pass

    def setEscapeButton(self, button): # real signature unknown; restored from __doc__
        """
        setEscapeButton(self, button: PySide2.QtWidgets.QAbstractButton) -> None
        setEscapeButton(self, button: PySide2.QtWidgets.QMessageBox.StandardButton) -> None
        """
        pass

    def setIcon(self, arg__1): # real signature unknown; restored from __doc__
        """ setIcon(self, arg__1: PySide2.QtWidgets.QMessageBox.Icon) -> None """
        pass

    def setIconPixmap(self, pixmap): # real signature unknown; restored from __doc__
        """ setIconPixmap(self, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def setInformativeText(self, text): # real signature unknown; restored from __doc__
        """ setInformativeText(self, text: str) -> None """
        pass

    def setStandardButtons(self, buttons): # real signature unknown; restored from __doc__
        """ setStandardButtons(self, buttons: PySide2.QtWidgets.QMessageBox.StandardButtons) -> None """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) -> None """
        pass

    def setTextFormat(self, format): # real signature unknown; restored from __doc__
        """ setTextFormat(self, format: PySide2.QtCore.Qt.TextFormat) -> None """
        pass

    def setTextInteractionFlags(self, flags): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, flags: PySide2.QtCore.Qt.TextInteractionFlags) -> None """
        pass

    def setWindowModality(self, windowModality): # real signature unknown; restored from __doc__
        """ setWindowModality(self, windowModality: PySide2.QtCore.Qt.WindowModality) -> None """
        pass

    def setWindowTitle(self, title): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, title: str) -> None """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: PySide2.QtGui.QShowEvent) -> None """
        pass

    def standardButton(self, button): # real signature unknown; restored from __doc__
        """ standardButton(self, button: PySide2.QtWidgets.QAbstractButton) -> PySide2.QtWidgets.QMessageBox.StandardButton """
        pass

    def standardButtons(self): # real signature unknown; restored from __doc__
        """ standardButtons(self) -> PySide2.QtWidgets.QMessageBox.StandardButtons """
        pass

    def standardIcon(self, icon): # real signature unknown; restored from __doc__
        """ standardIcon(icon: PySide2.QtWidgets.QMessageBox.Icon) -> PySide2.QtGui.QPixmap """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textFormat(self): # real signature unknown; restored from __doc__
        """ textFormat(self) -> PySide2.QtCore.Qt.TextFormat """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> PySide2.QtCore.Qt.TextInteractionFlags """
        pass

    def warning(self, parent, title, text, button0, button1): # real signature unknown; restored from __doc__
        """
        warning(parent: PySide2.QtWidgets.QWidget, title: str, text: str, button0: PySide2.QtWidgets.QMessageBox.StandardButton, button1: PySide2.QtWidgets.QMessageBox.StandardButton) -> int
        warning(parent: PySide2.QtWidgets.QWidget, title: str, text: str, buttons: PySide2.QtWidgets.QMessageBox.StandardButtons = PySide2.QtWidgets.QMessageBox.StandardButton.Ok, defaultButton: PySide2.QtWidgets.QMessageBox.StandardButton = PySide2.QtWidgets.QMessageBox.StandardButton.NoButton) -> PySide2.QtWidgets.QMessageBox.StandardButton
        """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, icon, title, text, buttons=None, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Abort = PySide2.QtWidgets.QMessageBox.StandardButton.Abort
    AcceptRole = PySide2.QtWidgets.QMessageBox.ButtonRole.AcceptRole
    ActionRole = PySide2.QtWidgets.QMessageBox.ButtonRole.ActionRole
    Apply = PySide2.QtWidgets.QMessageBox.StandardButton.Apply
    ApplyRole = PySide2.QtWidgets.QMessageBox.ButtonRole.ApplyRole
    ButtonMask = PySide2.QtWidgets.QMessageBox.StandardButton.ButtonMask
    ButtonRole = None # (!) real value is "<class 'PySide2.QtWidgets.QMessageBox.ButtonRole'>"
    Cancel = PySide2.QtWidgets.QMessageBox.StandardButton.Cancel
    Close = PySide2.QtWidgets.QMessageBox.StandardButton.Close
    Critical = PySide2.QtWidgets.QMessageBox.Icon.Critical
    Default = PySide2.QtWidgets.QMessageBox.StandardButton.Default
    DestructiveRole = PySide2.QtWidgets.QMessageBox.ButtonRole.DestructiveRole
    Discard = PySide2.QtWidgets.QMessageBox.StandardButton.Discard
    Escape = PySide2.QtWidgets.QMessageBox.StandardButton.Escape
    FirstButton = PySide2.QtWidgets.QMessageBox.StandardButton.FirstButton
    FlagMask = PySide2.QtWidgets.QMessageBox.StandardButton.FlagMask
    Help = PySide2.QtWidgets.QMessageBox.StandardButton.Help
    HelpRole = PySide2.QtWidgets.QMessageBox.ButtonRole.HelpRole
    Icon = None # (!) real value is "<class 'PySide2.QtWidgets.QMessageBox.Icon'>"
    Ignore = PySide2.QtWidgets.QMessageBox.StandardButton.Ignore
    Information = PySide2.QtWidgets.QMessageBox.Icon.Information
    InvalidRole = PySide2.QtWidgets.QMessageBox.ButtonRole.InvalidRole
    LastButton = PySide2.QtWidgets.QMessageBox.StandardButton.LastButton
    No = PySide2.QtWidgets.QMessageBox.StandardButton.No
    NoAll = PySide2.QtWidgets.QMessageBox.StandardButton.NoAll
    NoButton = PySide2.QtWidgets.QMessageBox.StandardButton.NoButton
    NoIcon = PySide2.QtWidgets.QMessageBox.Icon.NoIcon
    NoRole = PySide2.QtWidgets.QMessageBox.ButtonRole.NoRole
    NoToAll = PySide2.QtWidgets.QMessageBox.StandardButton.NoToAll
    NRoles = PySide2.QtWidgets.QMessageBox.ButtonRole.NRoles
    Ok = PySide2.QtWidgets.QMessageBox.StandardButton.Ok
    Open = PySide2.QtWidgets.QMessageBox.StandardButton.Open
    Question = PySide2.QtWidgets.QMessageBox.Icon.Question
    RejectRole = PySide2.QtWidgets.QMessageBox.ButtonRole.RejectRole
    Reset = PySide2.QtWidgets.QMessageBox.StandardButton.Reset
    ResetRole = PySide2.QtWidgets.QMessageBox.ButtonRole.ResetRole
    RestoreDefaults = PySide2.QtWidgets.QMessageBox.StandardButton.RestoreDefaults
    Retry = PySide2.QtWidgets.QMessageBox.StandardButton.Retry
    Save = PySide2.QtWidgets.QMessageBox.StandardButton.Save
    SaveAll = PySide2.QtWidgets.QMessageBox.StandardButton.SaveAll
    StandardButton = None # (!) real value is "<class 'PySide2.QtWidgets.QMessageBox.StandardButton'>"
    StandardButtons = None # (!) real value is "<class 'PySide2.QtWidgets.QMessageBox.StandardButtons'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50848C80>'
    Warning = PySide2.QtWidgets.QMessageBox.Icon.Warning
    Yes = PySide2.QtWidgets.QMessageBox.StandardButton.Yes
    YesAll = PySide2.QtWidgets.QMessageBox.StandardButton.YesAll
    YesRole = PySide2.QtWidgets.QMessageBox.ButtonRole.YesRole
    YesToAll = PySide2.QtWidgets.QMessageBox.StandardButton.YesToAll


