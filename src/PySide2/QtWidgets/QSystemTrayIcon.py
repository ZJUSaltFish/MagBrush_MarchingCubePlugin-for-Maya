# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QSystemTrayIcon(__PySide2_QtCore.QObject):
    """
    QSystemTrayIcon(self, icon: PySide2.QtGui.QIcon, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSystemTrayIcon(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def activated(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenu(self): # real signature unknown; restored from __doc__
        """ contextMenu(self) -> PySide2.QtWidgets.QMenu """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> PySide2.QtCore.QRect """
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) -> None """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def isSystemTrayAvailable(self): # real signature unknown; restored from __doc__
        """ isSystemTrayAvailable() -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def messageClicked(self, *args, **kwargs): # real signature unknown
        pass

    def setContextMenu(self, menu): # real signature unknown; restored from __doc__
        """ setContextMenu(self, menu: PySide2.QtWidgets.QMenu) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setToolTip(self, tip): # real signature unknown; restored from __doc__
        """ setToolTip(self, tip: str) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) -> None """
        pass

    def showMessage(self, title, msg, icon, msecs=10000): # real signature unknown; restored from __doc__
        """
        showMessage(self, title: str, msg: str, icon: PySide2.QtGui.QIcon, msecs: int = 10000) -> None
        showMessage(self, title: str, msg: str, icon: PySide2.QtWidgets.QSystemTrayIcon.MessageIcon = PySide2.QtWidgets.QSystemTrayIcon.MessageIcon.Information, msecs: int = 10000) -> None
        """
        pass

    def supportsMessages(self): # real signature unknown; restored from __doc__
        """ supportsMessages() -> bool """
        return False

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, icon, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ActivationReason = None # (!) real value is "<class 'PySide2.QtWidgets.QSystemTrayIcon.ActivationReason'>"
    Context = PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.Context
    Critical = PySide2.QtWidgets.QSystemTrayIcon.MessageIcon.Critical
    DoubleClick = PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick
    Information = PySide2.QtWidgets.QSystemTrayIcon.MessageIcon.Information
    MessageIcon = None # (!) real value is "<class 'PySide2.QtWidgets.QSystemTrayIcon.MessageIcon'>"
    MiddleClick = PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.MiddleClick
    NoIcon = PySide2.QtWidgets.QSystemTrayIcon.MessageIcon.NoIcon
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50870900>'
    Trigger = PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.Trigger
    Unknown = PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.Unknown
    Warning = PySide2.QtWidgets.QSystemTrayIcon.MessageIcon.Warning


