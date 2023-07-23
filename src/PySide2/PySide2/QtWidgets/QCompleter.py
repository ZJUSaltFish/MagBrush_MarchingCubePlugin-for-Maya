# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QCompleter(__PySide2_QtCore.QObject):
    """
    QCompleter(self, completions: typing.Sequence[str], parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QCompleter(self, model: PySide2.QtCore.QAbstractItemModel, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QCompleter(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def activated(self, *args, **kwargs): # real signature unknown
        pass

    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ caseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity """
        pass

    def complete(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ complete(self, rect: PySide2.QtCore.QRect = Default(QRect)) -> None """
        pass

    def completionColumn(self): # real signature unknown; restored from __doc__
        """ completionColumn(self) -> int """
        return 0

    def completionCount(self): # real signature unknown; restored from __doc__
        """ completionCount(self) -> int """
        return 0

    def completionMode(self): # real signature unknown; restored from __doc__
        """ completionMode(self) -> PySide2.QtWidgets.QCompleter.CompletionMode """
        pass

    def completionModel(self): # real signature unknown; restored from __doc__
        """ completionModel(self) -> PySide2.QtCore.QAbstractItemModel """
        pass

    def completionPrefix(self): # real signature unknown; restored from __doc__
        """ completionPrefix(self) -> str """
        return ""

    def completionRole(self): # real signature unknown; restored from __doc__
        """ completionRole(self) -> int """
        return 0

    def currentCompletion(self): # real signature unknown; restored from __doc__
        """ currentCompletion(self) -> str """
        return ""

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> PySide2.QtCore.QModelIndex """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ currentRow(self) -> int """
        return 0

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, o, e): # real signature unknown; restored from __doc__
        """ eventFilter(self, o: PySide2.QtCore.QObject, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def filterMode(self): # real signature unknown; restored from __doc__
        """ filterMode(self) -> PySide2.QtCore.Qt.MatchFlags """
        pass

    def highlighted(self, *args, **kwargs): # real signature unknown
        pass

    def maxVisibleItems(self): # real signature unknown; restored from __doc__
        """ maxVisibleItems(self) -> int """
        return 0

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> PySide2.QtCore.QAbstractItemModel """
        pass

    def modelSorting(self): # real signature unknown; restored from __doc__
        """ modelSorting(self) -> PySide2.QtWidgets.QCompleter.ModelSorting """
        pass

    def pathFromIndex(self, index): # real signature unknown; restored from __doc__
        """ pathFromIndex(self, index: PySide2.QtCore.QModelIndex) -> str """
        return ""

    def popup(self): # real signature unknown; restored from __doc__
        """ popup(self) -> PySide2.QtWidgets.QAbstractItemView """
        pass

    def setCaseSensitivity(self, caseSensitivity): # real signature unknown; restored from __doc__
        """ setCaseSensitivity(self, caseSensitivity: PySide2.QtCore.Qt.CaseSensitivity) -> None """
        pass

    def setCompletionColumn(self, column): # real signature unknown; restored from __doc__
        """ setCompletionColumn(self, column: int) -> None """
        pass

    def setCompletionMode(self, mode): # real signature unknown; restored from __doc__
        """ setCompletionMode(self, mode: PySide2.QtWidgets.QCompleter.CompletionMode) -> None """
        pass

    def setCompletionPrefix(self, prefix): # real signature unknown; restored from __doc__
        """ setCompletionPrefix(self, prefix: str) -> None """
        pass

    def setCompletionRole(self, role): # real signature unknown; restored from __doc__
        """ setCompletionRole(self, role: int) -> None """
        pass

    def setCurrentRow(self, row): # real signature unknown; restored from __doc__
        """ setCurrentRow(self, row: int) -> bool """
        return False

    def setFilterMode(self, filterMode): # real signature unknown; restored from __doc__
        """ setFilterMode(self, filterMode: PySide2.QtCore.Qt.MatchFlags) -> None """
        pass

    def setMaxVisibleItems(self, maxItems): # real signature unknown; restored from __doc__
        """ setMaxVisibleItems(self, maxItems: int) -> None """
        pass

    def setModel(self, c): # real signature unknown; restored from __doc__
        """ setModel(self, c: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setModelSorting(self, sorting): # real signature unknown; restored from __doc__
        """ setModelSorting(self, sorting: PySide2.QtWidgets.QCompleter.ModelSorting) -> None """
        pass

    def setPopup(self, popup): # real signature unknown; restored from __doc__
        """ setPopup(self, popup: PySide2.QtWidgets.QAbstractItemView) -> None """
        pass

    def setWidget(self, widget): # real signature unknown; restored from __doc__
        """ setWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setWrapAround(self, wrap): # real signature unknown; restored from __doc__
        """ setWrapAround(self, wrap: bool) -> None """
        pass

    def splitPath(self, path): # real signature unknown; restored from __doc__
        """ splitPath(self, path: str) -> typing.List[str] """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def wrapAround(self): # real signature unknown; restored from __doc__
        """ wrapAround(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, completions, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    CaseInsensitivelySortedModel = PySide2.QtWidgets.QCompleter.ModelSorting.CaseInsensitivelySortedModel
    CaseSensitivelySortedModel = PySide2.QtWidgets.QCompleter.ModelSorting.CaseSensitivelySortedModel
    CompletionMode = None # (!) real value is "<class 'PySide2.QtWidgets.QCompleter.CompletionMode'>"
    InlineCompletion = PySide2.QtWidgets.QCompleter.CompletionMode.InlineCompletion
    ModelSorting = None # (!) real value is "<class 'PySide2.QtWidgets.QCompleter.ModelSorting'>"
    PopupCompletion = PySide2.QtWidgets.QCompleter.CompletionMode.PopupCompletion
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F508717C0>'
    UnfilteredPopupCompletion = PySide2.QtWidgets.QCompleter.CompletionMode.UnfilteredPopupCompletion
    UnsortedModel = PySide2.QtWidgets.QCompleter.ModelSorting.UnsortedModel


