# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QTreeWidgetItem(__Shiboken.Object):
    """
    QTreeWidgetItem(self, other: PySide2.QtWidgets.QTreeWidgetItem) -> None
    QTreeWidgetItem(self, parent: PySide2.QtWidgets.QTreeWidgetItem, after: PySide2.QtWidgets.QTreeWidgetItem, type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTreeWidgetItem(self, parent: PySide2.QtWidgets.QTreeWidgetItem, strings: typing.Sequence[str], type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTreeWidgetItem(self, parent: PySide2.QtWidgets.QTreeWidgetItem, type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTreeWidgetItem(self, strings: typing.Sequence[str], type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTreeWidgetItem(self, treeview: PySide2.QtWidgets.QTreeWidget, after: PySide2.QtWidgets.QTreeWidgetItem, type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTreeWidgetItem(self, treeview: PySide2.QtWidgets.QTreeWidget, strings: typing.Sequence[str], type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTreeWidgetItem(self, treeview: PySide2.QtWidgets.QTreeWidget, type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTreeWidgetItem(self, type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    """
    def addChild(self, child): # real signature unknown; restored from __doc__
        """ addChild(self, child: PySide2.QtWidgets.QTreeWidgetItem) -> None """
        pass

    def addChildren(self, children, PySide2_QtWidgets_QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addChildren(self, children: typing.Sequence[PySide2.QtWidgets.QTreeWidgetItem]) -> None """
        pass

    def background(self, column): # real signature unknown; restored from __doc__
        """ background(self, column: int) -> PySide2.QtGui.QBrush """
        pass

    def backgroundColor(self, column): # real signature unknown; restored from __doc__
        """ backgroundColor(self, column: int) -> PySide2.QtGui.QColor """
        pass

    def checkState(self, column): # real signature unknown; restored from __doc__
        """ checkState(self, column: int) -> PySide2.QtCore.Qt.CheckState """
        pass

    def child(self, index): # real signature unknown; restored from __doc__
        """ child(self, index: int) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def childIndicatorPolicy(self): # real signature unknown; restored from __doc__
        """ childIndicatorPolicy(self) -> PySide2.QtWidgets.QTreeWidgetItem.ChildIndicatorPolicy """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def data(self, column, role): # real signature unknown; restored from __doc__
        """ data(self, column: int, role: int) -> typing.Any """
        pass

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ emitDataChanged(self) -> None """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def font(self, column): # real signature unknown; restored from __doc__
        """ font(self, column: int) -> PySide2.QtGui.QFont """
        pass

    def foreground(self, column): # real signature unknown; restored from __doc__
        """ foreground(self, column: int) -> PySide2.QtGui.QBrush """
        pass

    def icon(self, column): # real signature unknown; restored from __doc__
        """ icon(self, column: int) -> PySide2.QtGui.QIcon """
        pass

    def indexOfChild(self, child): # real signature unknown; restored from __doc__
        """ indexOfChild(self, child: PySide2.QtWidgets.QTreeWidgetItem) -> int """
        return 0

    def insertChild(self, index, child): # real signature unknown; restored from __doc__
        """ insertChild(self, index: int, child: PySide2.QtWidgets.QTreeWidgetItem) -> None """
        pass

    def insertChildren(self, index, children, PySide2_QtWidgets_QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertChildren(self, index: int, children: typing.Sequence[PySide2.QtWidgets.QTreeWidgetItem]) -> None """
        pass

    def isDisabled(self): # real signature unknown; restored from __doc__
        """ isDisabled(self) -> bool """
        return False

    def isExpanded(self): # real signature unknown; restored from __doc__
        """ isExpanded(self) -> bool """
        return False

    def isFirstColumnSpanned(self): # real signature unknown; restored from __doc__
        """ isFirstColumnSpanned(self) -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def read(self, in_): # real signature unknown; restored from __doc__
        """ read(self, in_: PySide2.QtCore.QDataStream) -> None """
        pass

    def removeChild(self, child): # real signature unknown; restored from __doc__
        """ removeChild(self, child: PySide2.QtWidgets.QTreeWidgetItem) -> None """
        pass

    def setBackground(self, column, brush): # real signature unknown; restored from __doc__
        """ setBackground(self, column: int, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setBackgroundColor(self, column, color): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, column: int, color: PySide2.QtGui.QColor) -> None """
        pass

    def setCheckState(self, column, state): # real signature unknown; restored from __doc__
        """ setCheckState(self, column: int, state: PySide2.QtCore.Qt.CheckState) -> None """
        pass

    def setChildIndicatorPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setChildIndicatorPolicy(self, policy: PySide2.QtWidgets.QTreeWidgetItem.ChildIndicatorPolicy) -> None """
        pass

    def setData(self, column, role, value): # real signature unknown; restored from __doc__
        """ setData(self, column: int, role: int, value: typing.Any) -> None """
        pass

    def setDisabled(self, disabled): # real signature unknown; restored from __doc__
        """ setDisabled(self, disabled: bool) -> None """
        pass

    def setExpanded(self, expand): # real signature unknown; restored from __doc__
        """ setExpanded(self, expand: bool) -> None """
        pass

    def setFirstColumnSpanned(self, span): # real signature unknown; restored from __doc__
        """ setFirstColumnSpanned(self, span: bool) -> None """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: PySide2.QtCore.Qt.ItemFlags) -> None """
        pass

    def setFont(self, column, font): # real signature unknown; restored from __doc__
        """ setFont(self, column: int, font: PySide2.QtGui.QFont) -> None """
        pass

    def setForeground(self, column, brush): # real signature unknown; restored from __doc__
        """ setForeground(self, column: int, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setHidden(self, hide): # real signature unknown; restored from __doc__
        """ setHidden(self, hide: bool) -> None """
        pass

    def setIcon(self, column, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, column: int, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setSelected(self, select): # real signature unknown; restored from __doc__
        """ setSelected(self, select: bool) -> None """
        pass

    def setSizeHint(self, column, size): # real signature unknown; restored from __doc__
        """ setSizeHint(self, column: int, size: PySide2.QtCore.QSize) -> None """
        pass

    def setStatusTip(self, column, statusTip): # real signature unknown; restored from __doc__
        """ setStatusTip(self, column: int, statusTip: str) -> None """
        pass

    def setText(self, column, text): # real signature unknown; restored from __doc__
        """ setText(self, column: int, text: str) -> None """
        pass

    def setTextAlignment(self, column, alignment): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, column: int, alignment: int) -> None """
        pass

    def setTextColor(self, column, color): # real signature unknown; restored from __doc__
        """ setTextColor(self, column: int, color: PySide2.QtGui.QColor) -> None """
        pass

    def setToolTip(self, column, toolTip): # real signature unknown; restored from __doc__
        """ setToolTip(self, column: int, toolTip: str) -> None """
        pass

    def setWhatsThis(self, column, whatsThis): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, column: int, whatsThis: str) -> None """
        pass

    def sizeHint(self, column): # real signature unknown; restored from __doc__
        """ sizeHint(self, column: int) -> PySide2.QtCore.QSize """
        pass

    def sortChildren(self, column, order): # real signature unknown; restored from __doc__
        """ sortChildren(self, column: int, order: PySide2.QtCore.Qt.SortOrder) -> None """
        pass

    def statusTip(self, column): # real signature unknown; restored from __doc__
        """ statusTip(self, column: int) -> str """
        return ""

    def takeChild(self, index): # real signature unknown; restored from __doc__
        """ takeChild(self, index: int) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def takeChildren(self): # real signature unknown; restored from __doc__
        """ takeChildren(self) -> typing.List[PySide2.QtWidgets.QTreeWidgetItem] """
        pass

    def text(self, column): # real signature unknown; restored from __doc__
        """ text(self, column: int) -> str """
        return ""

    def textAlignment(self, column): # real signature unknown; restored from __doc__
        """ textAlignment(self, column: int) -> int """
        return 0

    def textColor(self, column): # real signature unknown; restored from __doc__
        """ textColor(self, column: int) -> PySide2.QtGui.QColor """
        pass

    def toolTip(self, column): # real signature unknown; restored from __doc__
        """ toolTip(self, column: int) -> str """
        return ""

    def treeWidget(self): # real signature unknown; restored from __doc__
        """ treeWidget(self) -> PySide2.QtWidgets.QTreeWidget """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def whatsThis(self, column): # real signature unknown; restored from __doc__
        """ whatsThis(self, column: int) -> str """
        return ""

    def write(self, out): # real signature unknown; restored from __doc__
        """ write(self, out: PySide2.QtCore.QDataStream) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, other): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, out): # real signature unknown; restored from __doc__
        """
        __lshift__(self, out: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, in_): # real signature unknown; restored from __doc__
        """
        __rshift__(self, in_: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ChildIndicatorPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QTreeWidgetItem.ChildIndicatorPolicy'>"
    DontShowIndicator = PySide2.QtWidgets.QTreeWidgetItem.ChildIndicatorPolicy.DontShowIndicator
    DontShowIndicatorWhenChildless = PySide2.QtWidgets.QTreeWidgetItem.ChildIndicatorPolicy.DontShowIndicatorWhenChildless
    ItemType = None # (!) real value is "<class 'PySide2.QtWidgets.QTreeWidgetItem.ItemType'>"
    ShowIndicator = PySide2.QtWidgets.QTreeWidgetItem.ChildIndicatorPolicy.ShowIndicator
    Type = PySide2.QtWidgets.QTreeWidgetItem.ItemType.Type
    UserType = PySide2.QtWidgets.QTreeWidgetItem.ItemType.UserType


