# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QVariantAnimation import QVariantAnimation

class QPropertyAnimation(QVariantAnimation):
    """
    QPropertyAnimation(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QPropertyAnimation(self, target: PySide2.QtCore.QObject, propertyName: PySide2.QtCore.QByteArray, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def propertyName(self): # real signature unknown; restored from __doc__
        """ propertyName(self) -> PySide2.QtCore.QByteArray """
        pass

    def setPropertyName(self, propertyName): # real signature unknown; restored from __doc__
        """ setPropertyName(self, propertyName: PySide2.QtCore.QByteArray) -> None """
        pass

    def setTargetObject(self, target): # real signature unknown; restored from __doc__
        """ setTargetObject(self, target: PySide2.QtCore.QObject) -> None """
        pass

    def targetObject(self): # real signature unknown; restored from __doc__
        """ targetObject(self) -> PySide2.QtCore.QObject """
        pass

    def updateCurrentValue(self, value): # real signature unknown; restored from __doc__
        """ updateCurrentValue(self, value: typing.Any) -> None """
        pass

    def updateState(self, newState, oldState): # real signature unknown; restored from __doc__
        """ updateState(self, newState: PySide2.QtCore.QAbstractAnimation.State, oldState: PySide2.QtCore.QAbstractAnimation.State) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E657C0>'


