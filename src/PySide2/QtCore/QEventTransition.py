# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractTransition import QAbstractTransition

class QEventTransition(QAbstractTransition):
    """
    QEventTransition(self, object: PySide2.QtCore.QObject, type: PySide2.QtCore.QEvent.Type, sourceState: typing.Optional[PySide2.QtCore.QState] = None) -> None
    QEventTransition(self, sourceState: typing.Optional[PySide2.QtCore.QState] = None) -> None
    """
    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventSource(self): # real signature unknown; restored from __doc__
        """ eventSource(self) -> PySide2.QtCore.QObject """
        pass

    def eventTest(self, event): # real signature unknown; restored from __doc__
        """ eventTest(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventType(self): # real signature unknown; restored from __doc__
        """ eventType(self) -> PySide2.QtCore.QEvent.Type """
        pass

    def onTransition(self, event): # real signature unknown; restored from __doc__
        """ onTransition(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def setEventSource(self, p_object): # real signature unknown; restored from __doc__
        """ setEventSource(self, object: PySide2.QtCore.QObject) -> None """
        pass

    def setEventType(self, type): # real signature unknown; restored from __doc__
        """ setEventType(self, type: PySide2.QtCore.QEvent.Type) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, p_object, type, sourceState, PySide2_QtCore_QState=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E3FD00>'


