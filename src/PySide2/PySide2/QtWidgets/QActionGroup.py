# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QActionGroup(__PySide2_QtCore.QObject):
    """ QActionGroup(self, parent: PySide2.QtCore.QObject) -> None """
    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> typing.List[PySide2.QtWidgets.QAction] """
        pass

    def addAction(self, a): # real signature unknown; restored from __doc__
        """
        addAction(self, a: PySide2.QtWidgets.QAction) -> PySide2.QtWidgets.QAction
        addAction(self, icon: PySide2.QtGui.QIcon, text: str) -> PySide2.QtWidgets.QAction
        addAction(self, text: str) -> PySide2.QtWidgets.QAction
        """
        pass

    def checkedAction(self): # real signature unknown; restored from __doc__
        """ checkedAction(self) -> PySide2.QtWidgets.QAction """
        pass

    def exclusionPolicy(self): # real signature unknown; restored from __doc__
        """ exclusionPolicy(self) -> PySide2.QtWidgets.QActionGroup.ExclusionPolicy """
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isExclusive(self): # real signature unknown; restored from __doc__
        """ isExclusive(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def removeAction(self, a): # real signature unknown; restored from __doc__
        """ removeAction(self, a: PySide2.QtWidgets.QAction) -> None """
        pass

    def setDisabled(self, b): # real signature unknown; restored from __doc__
        """ setDisabled(self, b: bool) -> None """
        pass

    def setEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setEnabled(self, arg__1: bool) -> None """
        pass

    def setExclusionPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setExclusionPolicy(self, policy: PySide2.QtWidgets.QActionGroup.ExclusionPolicy) -> None """
        pass

    def setExclusive(self, arg__1): # real signature unknown; restored from __doc__
        """ setExclusive(self, arg__1: bool) -> None """
        pass

    def setVisible(self, arg__1): # real signature unknown; restored from __doc__
        """ setVisible(self, arg__1: bool) -> None """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ExclusionPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QActionGroup.ExclusionPolicy'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F5071E100>'


