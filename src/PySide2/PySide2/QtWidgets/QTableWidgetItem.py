# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QTableWidgetItem(__Shiboken.Object):
    """
    QTableWidgetItem(self, icon: PySide2.QtGui.QIcon, text: str, type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTableWidgetItem(self, other: PySide2.QtWidgets.QTableWidgetItem) -> None
    QTableWidgetItem(self, text: str, type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    QTableWidgetItem(self, type: int = PySide2.QtWidgets.QListWidgetItem.ItemType.Type) -> None
    """
    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> PySide2.QtGui.QBrush """
        pass

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> PySide2.QtGui.QColor """
        pass

    def checkState(self): # real signature unknown; restored from __doc__
        """ checkState(self) -> PySide2.QtCore.Qt.CheckState """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def data(self, role): # real signature unknown; restored from __doc__
        """ data(self, role: int) -> typing.Any """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def foreground(self): # real signature unknown; restored from __doc__
        """ foreground(self) -> PySide2.QtGui.QBrush """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def read(self, in_): # real signature unknown; restored from __doc__
        """ read(self, in_: PySide2.QtCore.QDataStream) -> None """
        pass

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def setBackground(self, brush): # real signature unknown; restored from __doc__
        """ setBackground(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setBackgroundColor(self, color): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setCheckState(self, state): # real signature unknown; restored from __doc__
        """ setCheckState(self, state: PySide2.QtCore.Qt.CheckState) -> None """
        pass

    def setData(self, role, value): # real signature unknown; restored from __doc__
        """ setData(self, role: int, value: typing.Any) -> None """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: PySide2.QtCore.Qt.ItemFlags) -> None """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: PySide2.QtGui.QFont) -> None """
        pass

    def setForeground(self, brush): # real signature unknown; restored from __doc__
        """ setForeground(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setSelected(self, select): # real signature unknown; restored from __doc__
        """ setSelected(self, select: bool) -> None """
        pass

    def setSizeHint(self, size): # real signature unknown; restored from __doc__
        """ setSizeHint(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setStatusTip(self, statusTip): # real signature unknown; restored from __doc__
        """ setStatusTip(self, statusTip: str) -> None """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) -> None """
        pass

    def setTextAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setTextAlignment(self, alignment: int) -> None """
        pass

    def setTextColor(self, color): # real signature unknown; restored from __doc__
        """ setTextColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setToolTip(self, toolTip): # real signature unknown; restored from __doc__
        """ setToolTip(self, toolTip: str) -> None """
        pass

    def setWhatsThis(self, whatsThis): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, whatsThis: str) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def tableWidget(self): # real signature unknown; restored from __doc__
        """ tableWidget(self) -> PySide2.QtWidgets.QTableWidget """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ textAlignment(self) -> int """
        return 0

    def textColor(self): # real signature unknown; restored from __doc__
        """ textColor(self) -> PySide2.QtGui.QColor """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
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

    def __init__(self, icon, text, type=None): # real signature unknown; restored from __doc__
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

    ItemType = None # (!) real value is "<class 'PySide2.QtWidgets.QTableWidgetItem.ItemType'>"
    Type = PySide2.QtWidgets.QTableWidgetItem.ItemType.Type
    UserType = PySide2.QtWidgets.QTableWidgetItem.ItemType.UserType
    __hash__ = None


