# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractTransition import QAbstractTransition

class QSignalTransition(QAbstractTransition):
    """
    QSignalTransition(self, arg__1: object, arg__2: typing.Optional[PySide2.QtCore.QState] = None) -> PySide2.QtCore.QSignalTransition
    QSignalTransition(self, sender: PySide2.QtCore.QObject, signal: bytes, sourceState: typing.Optional[PySide2.QtCore.QState] = None) -> None
    QSignalTransition(self, sourceState: typing.Optional[PySide2.QtCore.QState] = None) -> None
    """
    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventTest(self, event): # real signature unknown; restored from __doc__
        """ eventTest(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def onTransition(self, event): # real signature unknown; restored from __doc__
        """ onTransition(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def senderObject(self): # real signature unknown; restored from __doc__
        """ senderObject(self) -> PySide2.QtCore.QObject """
        pass

    def setSenderObject(self, sender): # real signature unknown; restored from __doc__
        """ setSenderObject(self, sender: PySide2.QtCore.QObject) -> None """
        pass

    def setSignal(self, signal): # real signature unknown; restored from __doc__
        """ setSignal(self, signal: PySide2.QtCore.QByteArray) -> None """
        pass

    def signal(self): # real signature unknown; restored from __doc__
        """ signal(self) -> PySide2.QtCore.QByteArray """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1, arg__2, PySide2_QtCore_QState=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E3FEC0>'


