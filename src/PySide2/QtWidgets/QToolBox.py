# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QFrame import QFrame

class QToolBox(QFrame):
    """ QToolBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def addItem(self, widget, icon, text): # real signature unknown; restored from __doc__
        """
        addItem(self, widget: PySide2.QtWidgets.QWidget, icon: PySide2.QtGui.QIcon, text: str) -> int
        addItem(self, widget: PySide2.QtWidgets.QWidget, text: str) -> int
        """
        return 0

    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ currentWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def indexOf(self, widget): # real signature unknown; restored from __doc__
        """ indexOf(self, widget: PySide2.QtWidgets.QWidget) -> int """
        return 0

    def insertItem(self, index, widget, icon, text): # real signature unknown; restored from __doc__
        """
        insertItem(self, index: int, widget: PySide2.QtWidgets.QWidget, icon: PySide2.QtGui.QIcon, text: str) -> int
        insertItem(self, index: int, widget: PySide2.QtWidgets.QWidget, text: str) -> int
        """
        return 0

    def isItemEnabled(self, index): # real signature unknown; restored from __doc__
        """ isItemEnabled(self, index: int) -> bool """
        return False

    def itemIcon(self, index): # real signature unknown; restored from __doc__
        """ itemIcon(self, index: int) -> PySide2.QtGui.QIcon """
        pass

    def itemInserted(self, index): # real signature unknown; restored from __doc__
        """ itemInserted(self, index: int) -> None """
        pass

    def itemRemoved(self, index): # real signature unknown; restored from __doc__
        """ itemRemoved(self, index: int) -> None """
        pass

    def itemText(self, index): # real signature unknown; restored from __doc__
        """ itemText(self, index: int) -> str """
        return ""

    def itemToolTip(self, index): # real signature unknown; restored from __doc__
        """ itemToolTip(self, index: int) -> str """
        return ""

    def removeItem(self, index): # real signature unknown; restored from __doc__
        """ removeItem(self, index: int) -> None """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) -> None """
        pass

    def setCurrentWidget(self, widget): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setItemEnabled(self, index, enabled): # real signature unknown; restored from __doc__
        """ setItemEnabled(self, index: int, enabled: bool) -> None """
        pass

    def setItemIcon(self, index, icon): # real signature unknown; restored from __doc__
        """ setItemIcon(self, index: int, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setItemText(self, index, text): # real signature unknown; restored from __doc__
        """ setItemText(self, index: int, text: str) -> None """
        pass

    def setItemToolTip(self, index, toolTip): # real signature unknown; restored from __doc__
        """ setItemToolTip(self, index: int, toolTip: str) -> None """
        pass

    def showEvent(self, e): # real signature unknown; restored from __doc__
        """ showEvent(self, e: PySide2.QtGui.QShowEvent) -> None """
        pass

    def widget(self, index): # real signature unknown; restored from __doc__
        """ widget(self, index: int) -> PySide2.QtWidgets.QWidget """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50816A00>'


