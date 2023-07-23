# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractAnimation import QAbstractAnimation

class QVariantAnimation(QAbstractAnimation):
    """ QVariantAnimation(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def currentValue(self): # real signature unknown; restored from __doc__
        """ currentValue(self) -> typing.Any """
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ easingCurve(self) -> PySide2.QtCore.QEasingCurve """
        pass

    def endValue(self): # real signature unknown; restored from __doc__
        """ endValue(self) -> typing.Any """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def interpolated(self, from_, to, progress): # real signature unknown; restored from __doc__
        """ interpolated(self, from_: typing.Any, to: typing.Any, progress: float) -> typing.Any """
        pass

    def keyValueAt(self, step): # real signature unknown; restored from __doc__
        """ keyValueAt(self, step: float) -> typing.Any """
        pass

    def keyValues(self): # real signature unknown; restored from __doc__
        """ keyValues(self) -> typing.List[typing.Tuple[float, typing.Any]] """
        pass

    def setDuration(self, msecs): # real signature unknown; restored from __doc__
        """ setDuration(self, msecs: int) -> None """
        pass

    def setEasingCurve(self, easing): # real signature unknown; restored from __doc__
        """ setEasingCurve(self, easing: PySide2.QtCore.QEasingCurve) -> None """
        pass

    def setEndValue(self, value): # real signature unknown; restored from __doc__
        """ setEndValue(self, value: typing.Any) -> None """
        pass

    def setKeyValueAt(self, step, value): # real signature unknown; restored from __doc__
        """ setKeyValueAt(self, step: float, value: typing.Any) -> None """
        pass

    def setKeyValues(self, values, typing_Tuple=None, p_float=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setKeyValues(self, values: typing.List[typing.Tuple[float, typing.Any]]) -> None """
        pass

    def setStartValue(self, value): # real signature unknown; restored from __doc__
        """ setStartValue(self, value: typing.Any) -> None """
        pass

    def startValue(self): # real signature unknown; restored from __doc__
        """ startValue(self) -> typing.Any """
        pass

    def updateCurrentTime(self, arg__1): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, arg__1: int) -> None """
        pass

    def updateCurrentValue(self, value): # real signature unknown; restored from __doc__
        """ updateCurrentValue(self, value: typing.Any) -> None """
        pass

    def updateState(self, newState, oldState): # real signature unknown; restored from __doc__
        """ updateState(self, newState: PySide2.QtCore.QAbstractAnimation.State, oldState: PySide2.QtCore.QAbstractAnimation.State) -> None """
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E655C0>'


