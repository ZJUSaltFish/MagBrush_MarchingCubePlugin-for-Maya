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

class QDialogButtonBox(QWidget):
    """
    QDialogButtonBox(self, buttons: PySide2.QtWidgets.QDialogButtonBox.StandardButtons, orientation: PySide2.QtCore.Qt.Orientation, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QDialogButtonBox(self, buttons: PySide2.QtWidgets.QDialogButtonBox.StandardButtons, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QDialogButtonBox(self, orientation: PySide2.QtCore.Qt.Orientation, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QDialogButtonBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def accepted(self, *args, **kwargs): # real signature unknown
        pass

    def addButton(self, button, role): # real signature unknown; restored from __doc__
        """
        addButton(self, button: PySide2.QtWidgets.QAbstractButton, role: PySide2.QtWidgets.QDialogButtonBox.ButtonRole) -> None
        addButton(self, button: PySide2.QtWidgets.QDialogButtonBox.StandardButton) -> PySide2.QtWidgets.QPushButton
        addButton(self, text: str, role: PySide2.QtWidgets.QDialogButtonBox.ButtonRole) -> PySide2.QtWidgets.QPushButton
        """
        pass

    def button(self, which): # real signature unknown; restored from __doc__
        """ button(self, which: PySide2.QtWidgets.QDialogButtonBox.StandardButton) -> PySide2.QtWidgets.QPushButton """
        pass

    def buttonRole(self, button): # real signature unknown; restored from __doc__
        """ buttonRole(self, button: PySide2.QtWidgets.QAbstractButton) -> PySide2.QtWidgets.QDialogButtonBox.ButtonRole """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> typing.List[PySide2.QtWidgets.QAbstractButton] """
        pass

    def centerButtons(self): # real signature unknown; restored from __doc__
        """ centerButtons(self) -> bool """
        return False

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def helpRequested(self, *args, **kwargs): # real signature unknown
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def rejected(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, button): # real signature unknown; restored from __doc__
        """ removeButton(self, button: PySide2.QtWidgets.QAbstractButton) -> None """
        pass

    def setCenterButtons(self, center): # real signature unknown; restored from __doc__
        """ setCenterButtons(self, center: bool) -> None """
        pass

    def setOrientation(self, orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, orientation: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def setStandardButtons(self, buttons): # real signature unknown; restored from __doc__
        """ setStandardButtons(self, buttons: PySide2.QtWidgets.QDialogButtonBox.StandardButtons) -> None """
        pass

    def standardButton(self, button): # real signature unknown; restored from __doc__
        """ standardButton(self, button: PySide2.QtWidgets.QAbstractButton) -> PySide2.QtWidgets.QDialogButtonBox.StandardButton """
        pass

    def standardButtons(self): # real signature unknown; restored from __doc__
        """ standardButtons(self) -> PySide2.QtWidgets.QDialogButtonBox.StandardButtons """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, buttons, orientation, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Abort = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Abort
    AcceptRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.AcceptRole
    ActionRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.ActionRole
    AndroidLayout = PySide2.QtWidgets.QDialogButtonBox.ButtonLayout.AndroidLayout
    Apply = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Apply
    ApplyRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.ApplyRole
    ButtonLayout = None # (!) real value is "<class 'PySide2.QtWidgets.QDialogButtonBox.ButtonLayout'>"
    ButtonRole = None # (!) real value is "<class 'PySide2.QtWidgets.QDialogButtonBox.ButtonRole'>"
    Cancel = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Cancel
    Close = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Close
    DestructiveRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.DestructiveRole
    Discard = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Discard
    FirstButton = PySide2.QtWidgets.QDialogButtonBox.StandardButton.FirstButton
    GnomeLayout = PySide2.QtWidgets.QDialogButtonBox.ButtonLayout.GnomeLayout
    Help = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Help
    HelpRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.HelpRole
    Ignore = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Ignore
    InvalidRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.InvalidRole
    KdeLayout = PySide2.QtWidgets.QDialogButtonBox.ButtonLayout.KdeLayout
    LastButton = PySide2.QtWidgets.QDialogButtonBox.StandardButton.LastButton
    MacLayout = PySide2.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout
    No = PySide2.QtWidgets.QDialogButtonBox.StandardButton.No
    NoButton = PySide2.QtWidgets.QDialogButtonBox.StandardButton.NoButton
    NoRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.NoRole
    NoToAll = PySide2.QtWidgets.QDialogButtonBox.StandardButton.NoToAll
    NRoles = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.NRoles
    Ok = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Ok
    Open = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Open
    RejectRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.RejectRole
    Reset = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Reset
    ResetRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.ResetRole
    RestoreDefaults = PySide2.QtWidgets.QDialogButtonBox.StandardButton.RestoreDefaults
    Retry = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Retry
    Save = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Save
    SaveAll = PySide2.QtWidgets.QDialogButtonBox.StandardButton.SaveAll
    StandardButton = None # (!) real value is "<class 'PySide2.QtWidgets.QDialogButtonBox.StandardButton'>"
    StandardButtons = None # (!) real value is "<class 'PySide2.QtWidgets.QDialogButtonBox.StandardButtons'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50833000>'
    WinLayout = PySide2.QtWidgets.QDialogButtonBox.ButtonLayout.WinLayout
    Yes = PySide2.QtWidgets.QDialogButtonBox.StandardButton.Yes
    YesRole = PySide2.QtWidgets.QDialogButtonBox.ButtonRole.YesRole
    YesToAll = PySide2.QtWidgets.QDialogButtonBox.StandardButton.YesToAll


