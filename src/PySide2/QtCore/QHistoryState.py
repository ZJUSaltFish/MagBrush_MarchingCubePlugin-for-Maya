# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractState import QAbstractState

class QHistoryState(QAbstractState):
    """
    QHistoryState(self, parent: typing.Optional[PySide2.QtCore.QState] = None) -> None
    QHistoryState(self, type: PySide2.QtCore.QHistoryState.HistoryType, parent: typing.Optional[PySide2.QtCore.QState] = None) -> None
    """
    def defaultState(self): # real signature unknown; restored from __doc__
        """ defaultState(self) -> PySide2.QtCore.QAbstractState """
        pass

    def defaultStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def defaultTransition(self): # real signature unknown; restored from __doc__
        """ defaultTransition(self) -> PySide2.QtCore.QAbstractTransition """
        pass

    def defaultTransitionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def historyType(self): # real signature unknown; restored from __doc__
        """ historyType(self) -> PySide2.QtCore.QHistoryState.HistoryType """
        pass

    def historyTypeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def onEntry(self, event): # real signature unknown; restored from __doc__
        """ onEntry(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def onExit(self, event): # real signature unknown; restored from __doc__
        """ onExit(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def setDefaultState(self, state): # real signature unknown; restored from __doc__
        """ setDefaultState(self, state: PySide2.QtCore.QAbstractState) -> None """
        pass

    def setDefaultTransition(self, transition): # real signature unknown; restored from __doc__
        """ setDefaultTransition(self, transition: PySide2.QtCore.QAbstractTransition) -> None """
        pass

    def setHistoryType(self, type): # real signature unknown; restored from __doc__
        """ setHistoryType(self, type: PySide2.QtCore.QHistoryState.HistoryType) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QState=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    DeepHistory = PySide2.QtCore.QHistoryState.HistoryType.DeepHistory
    HistoryType = None # (!) real value is "<class 'PySide2.QtCore.QHistoryState.HistoryType'>"
    ShallowHistory = PySide2.QtCore.QHistoryState.HistoryType.ShallowHistory
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4DA80>'


