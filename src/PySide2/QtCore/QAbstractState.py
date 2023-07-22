# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QAbstractState(QObject):
    """ QAbstractState(self, parent: typing.Optional[PySide2.QtCore.QState] = None) -> None """
    def active(self): # real signature unknown; restored from __doc__
        """ active(self) -> bool """
        return False

    def activeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def entered(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def exited(self, *args, **kwargs): # real signature unknown
        pass

    def machine(self): # real signature unknown; restored from __doc__
        """ machine(self) -> PySide2.QtCore.QStateMachine """
        pass

    def onEntry(self, event): # real signature unknown; restored from __doc__
        """ onEntry(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def onExit(self, event): # real signature unknown; restored from __doc__
        """ onExit(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def parentState(self): # real signature unknown; restored from __doc__
        """ parentState(self) -> PySide2.QtCore.QState """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4C240>'


