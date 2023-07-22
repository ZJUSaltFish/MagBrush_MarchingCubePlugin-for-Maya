# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QAbstractTransition(QObject):
    """ QAbstractTransition(self, sourceState: typing.Optional[PySide2.QtCore.QState] = None) -> None """
    def addAnimation(self, animation): # real signature unknown; restored from __doc__
        """ addAnimation(self, animation: PySide2.QtCore.QAbstractAnimation) -> None """
        pass

    def animations(self): # real signature unknown; restored from __doc__
        """ animations(self) -> typing.List[PySide2.QtCore.QAbstractAnimation] """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventTest(self, event): # real signature unknown; restored from __doc__
        """ eventTest(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def machine(self): # real signature unknown; restored from __doc__
        """ machine(self) -> PySide2.QtCore.QStateMachine """
        pass

    def onTransition(self, event): # real signature unknown; restored from __doc__
        """ onTransition(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def removeAnimation(self, animation): # real signature unknown; restored from __doc__
        """ removeAnimation(self, animation: PySide2.QtCore.QAbstractAnimation) -> None """
        pass

    def setTargetState(self, target): # real signature unknown; restored from __doc__
        """ setTargetState(self, target: PySide2.QtCore.QAbstractState) -> None """
        pass

    def setTargetStates(self, targets, PySide2_QtCore_QAbstractState=None): # real signature unknown; restored from __doc__
        """ setTargetStates(self, targets: typing.Sequence[PySide2.QtCore.QAbstractState]) -> None """
        pass

    def setTransitionType(self, type): # real signature unknown; restored from __doc__
        """ setTransitionType(self, type: PySide2.QtCore.QAbstractTransition.TransitionType) -> None """
        pass

    def sourceState(self): # real signature unknown; restored from __doc__
        """ sourceState(self) -> PySide2.QtCore.QState """
        pass

    def targetState(self): # real signature unknown; restored from __doc__
        """ targetState(self) -> PySide2.QtCore.QAbstractState """
        pass

    def targetStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def targetStates(self): # real signature unknown; restored from __doc__
        """ targetStates(self) -> typing.List[PySide2.QtCore.QAbstractState] """
        pass

    def targetStatesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def transitionType(self): # real signature unknown; restored from __doc__
        """ transitionType(self) -> PySide2.QtCore.QAbstractTransition.TransitionType """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, sourceState, PySide2_QtCore_QState=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ExternalTransition = PySide2.QtCore.QAbstractTransition.TransitionType.ExternalTransition
    InternalTransition = PySide2.QtCore.QAbstractTransition.TransitionType.InternalTransition
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E3FAC0>'
    TransitionType = None # (!) real value is "<class 'PySide2.QtCore.QAbstractTransition.TransitionType'>"


