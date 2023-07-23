# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QAction(__PySide2_QtCore.QObject):
    """
    QAction(self, icon: PySide2.QtGui.QIcon, text: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QAction(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QAction(self, text: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def actionGroup(self): # real signature unknown; restored from __doc__
        """ actionGroup(self) -> PySide2.QtWidgets.QActionGroup """
        pass

    def activate(self, event): # real signature unknown; restored from __doc__
        """ activate(self, event: PySide2.QtWidgets.QAction.ActionEvent) -> None """
        pass

    def associatedGraphicsWidgets(self): # real signature unknown; restored from __doc__
        """ associatedGraphicsWidgets(self) -> typing.List[PySide2.QtWidgets.QGraphicsWidget] """
        pass

    def associatedWidgets(self): # real signature unknown; restored from __doc__
        """ associatedWidgets(self) -> typing.List[PySide2.QtWidgets.QWidget] """
        pass

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> typing.Any """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def hover(self): # real signature unknown; restored from __doc__
        """ hover(self) -> None """
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def iconText(self): # real signature unknown; restored from __doc__
        """ iconText(self) -> str """
        return ""

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isChecked(self): # real signature unknown; restored from __doc__
        """ isChecked(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isIconVisibleInMenu(self): # real signature unknown; restored from __doc__
        """ isIconVisibleInMenu(self) -> bool """
        return False

    def isSeparator(self): # real signature unknown; restored from __doc__
        """ isSeparator(self) -> bool """
        return False

    def isShortcutVisibleInContextMenu(self): # real signature unknown; restored from __doc__
        """ isShortcutVisibleInContextMenu(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def menu(self): # real signature unknown; restored from __doc__
        """ menu(self) -> PySide2.QtWidgets.QMenu """
        pass

    def menuRole(self): # real signature unknown; restored from __doc__
        """ menuRole(self) -> PySide2.QtWidgets.QAction.MenuRole """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def priority(self): # real signature unknown; restored from __doc__
        """ priority(self) -> PySide2.QtWidgets.QAction.Priority """
        pass

    def setActionGroup(self, group): # real signature unknown; restored from __doc__
        """ setActionGroup(self, group: PySide2.QtWidgets.QActionGroup) -> None """
        pass

    def setAutoRepeat(self, arg__1): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, arg__1: bool) -> None """
        pass

    def setCheckable(self, arg__1): # real signature unknown; restored from __doc__
        """ setCheckable(self, arg__1: bool) -> None """
        pass

    def setChecked(self, arg__1): # real signature unknown; restored from __doc__
        """ setChecked(self, arg__1: bool) -> None """
        pass

    def setData(self, var): # real signature unknown; restored from __doc__
        """ setData(self, var: typing.Any) -> None """
        pass

    def setDisabled(self, b): # real signature unknown; restored from __doc__
        """ setDisabled(self, b: bool) -> None """
        pass

    def setEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setEnabled(self, arg__1: bool) -> None """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: PySide2.QtGui.QFont) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setIconText(self, text): # real signature unknown; restored from __doc__
        """ setIconText(self, text: str) -> None """
        pass

    def setIconVisibleInMenu(self, visible): # real signature unknown; restored from __doc__
        """ setIconVisibleInMenu(self, visible: bool) -> None """
        pass

    def setMenu(self, menu): # real signature unknown; restored from __doc__
        """ setMenu(self, menu: PySide2.QtWidgets.QMenu) -> None """
        pass

    def setMenuRole(self, menuRole): # real signature unknown; restored from __doc__
        """ setMenuRole(self, menuRole: PySide2.QtWidgets.QAction.MenuRole) -> None """
        pass

    def setPriority(self, priority): # real signature unknown; restored from __doc__
        """ setPriority(self, priority: PySide2.QtWidgets.QAction.Priority) -> None """
        pass

    def setSeparator(self, b): # real signature unknown; restored from __doc__
        """ setSeparator(self, b: bool) -> None """
        pass

    def setShortcut(self, shortcut): # real signature unknown; restored from __doc__
        """ setShortcut(self, shortcut: PySide2.QtGui.QKeySequence) -> None """
        pass

    def setShortcutContext(self, context): # real signature unknown; restored from __doc__
        """ setShortcutContext(self, context: PySide2.QtCore.Qt.ShortcutContext) -> None """
        pass

    def setShortcuts(self, arg__1): # real signature unknown; restored from __doc__
        """
        setShortcuts(self, arg__1: PySide2.QtGui.QKeySequence.StandardKey) -> None
        setShortcuts(self, shortcuts: typing.Sequence[PySide2.QtGui.QKeySequence]) -> None
        """
        pass

    def setShortcutVisibleInContextMenu(self, show): # real signature unknown; restored from __doc__
        """ setShortcutVisibleInContextMenu(self, show: bool) -> None """
        pass

    def setStatusTip(self, statusTip): # real signature unknown; restored from __doc__
        """ setStatusTip(self, statusTip: str) -> None """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) -> None """
        pass

    def setToolTip(self, tip): # real signature unknown; restored from __doc__
        """ setToolTip(self, tip: str) -> None """
        pass

    def setVisible(self, arg__1): # real signature unknown; restored from __doc__
        """ setVisible(self, arg__1: bool) -> None """
        pass

    def setWhatsThis(self, what): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, what: str) -> None """
        pass

    def shortcut(self): # real signature unknown; restored from __doc__
        """ shortcut(self) -> PySide2.QtGui.QKeySequence """
        pass

    def shortcutContext(self): # real signature unknown; restored from __doc__
        """ shortcutContext(self) -> PySide2.QtCore.Qt.ShortcutContext """
        pass

    def shortcuts(self): # real signature unknown; restored from __doc__
        """ shortcuts(self) -> typing.List[PySide2.QtGui.QKeySequence] """
        pass

    def showStatusText(self, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ showStatusText(self, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> bool """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def toggle(self): # real signature unknown; restored from __doc__
        """ toggle(self) -> None """
        pass

    def toggled(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def trigger(self): # real signature unknown; restored from __doc__
        """ trigger(self) -> None """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, icon, text, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AboutQtRole = PySide2.QtWidgets.QAction.MenuRole.AboutQtRole
    AboutRole = PySide2.QtWidgets.QAction.MenuRole.AboutRole
    ActionEvent = None # (!) real value is "<class 'PySide2.QtWidgets.QAction.ActionEvent'>"
    ApplicationSpecificRole = PySide2.QtWidgets.QAction.MenuRole.ApplicationSpecificRole
    HighPriority = PySide2.QtWidgets.QAction.Priority.HighPriority
    Hover = PySide2.QtWidgets.QAction.ActionEvent.Hover
    LowPriority = PySide2.QtWidgets.QAction.Priority.LowPriority
    MenuRole = None # (!) real value is "<class 'PySide2.QtWidgets.QAction.MenuRole'>"
    NormalPriority = PySide2.QtWidgets.QAction.Priority.NormalPriority
    NoRole = PySide2.QtWidgets.QAction.MenuRole.NoRole
    PreferencesRole = PySide2.QtWidgets.QAction.MenuRole.PreferencesRole
    Priority = None # (!) real value is "<class 'PySide2.QtWidgets.QAction.Priority'>"
    QuitRole = PySide2.QtWidgets.QAction.MenuRole.QuitRole
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50764980>'
    TextHeuristicRole = PySide2.QtWidgets.QAction.MenuRole.TextHeuristicRole
    Trigger = PySide2.QtWidgets.QAction.ActionEvent.Trigger


