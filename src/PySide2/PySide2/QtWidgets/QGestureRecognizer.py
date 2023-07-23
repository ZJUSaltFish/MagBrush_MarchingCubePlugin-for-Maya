# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QGestureRecognizer(__Shiboken.Object):
    """ QGestureRecognizer(self) -> None """
    def create(self, target): # real signature unknown; restored from __doc__
        """ create(self, target: PySide2.QtCore.QObject) -> PySide2.QtWidgets.QGesture """
        pass

    def recognize(self, state, watched, event): # real signature unknown; restored from __doc__
        """ recognize(self, state: PySide2.QtWidgets.QGesture, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> PySide2.QtWidgets.QGestureRecognizer.Result """
        pass

    def registerRecognizer(self, recognizer): # real signature unknown; restored from __doc__
        """ registerRecognizer(recognizer: PySide2.QtWidgets.QGestureRecognizer) -> PySide2.QtCore.Qt.GestureType """
        pass

    def reset(self, state): # real signature unknown; restored from __doc__
        """ reset(self, state: PySide2.QtWidgets.QGesture) -> None """
        pass

    def unregisterRecognizer(self, type): # real signature unknown; restored from __doc__
        """ unregisterRecognizer(type: PySide2.QtCore.Qt.GestureType) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    CancelGesture = PySide2.QtWidgets.QGestureRecognizer.ResultFlag.CancelGesture
    ConsumeEventHint = PySide2.QtWidgets.QGestureRecognizer.ResultFlag.ConsumeEventHint
    FinishGesture = PySide2.QtWidgets.QGestureRecognizer.ResultFlag.FinishGesture
    Ignore = PySide2.QtWidgets.QGestureRecognizer.ResultFlag.Ignore
    MayBeGesture = PySide2.QtWidgets.QGestureRecognizer.ResultFlag.MayBeGesture
    Result = None # (!) real value is "<class 'PySide2.QtWidgets.QGestureRecognizer.Result'>"
    ResultFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QGestureRecognizer.ResultFlag'>"
    ResultHint_Mask = PySide2.QtWidgets.QGestureRecognizer.ResultFlag.ResultHint_Mask
    ResultState_Mask = PySide2.QtWidgets.QGestureRecognizer.ResultFlag.ResultState_Mask
    TriggerGesture = PySide2.QtWidgets.QGestureRecognizer.ResultFlag.TriggerGesture


