# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QGesture(__PySide2_QtCore.QObject):
    """ QGesture(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def gestureCancelPolicy(self): # real signature unknown; restored from __doc__
        """ gestureCancelPolicy(self) -> PySide2.QtWidgets.QGesture.GestureCancelPolicy """
        pass

    def gestureType(self): # real signature unknown; restored from __doc__
        """ gestureType(self) -> PySide2.QtCore.Qt.GestureType """
        pass

    def hasHotSpot(self): # real signature unknown; restored from __doc__
        """ hasHotSpot(self) -> bool """
        return False

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ hotSpot(self) -> PySide2.QtCore.QPointF """
        pass

    def setGestureCancelPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setGestureCancelPolicy(self, policy: PySide2.QtWidgets.QGesture.GestureCancelPolicy) -> None """
        pass

    def setHotSpot(self, value): # real signature unknown; restored from __doc__
        """ setHotSpot(self, value: PySide2.QtCore.QPointF) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtCore.Qt.GestureState """
        pass

    def unsetHotSpot(self): # real signature unknown; restored from __doc__
        """ unsetHotSpot(self) -> None """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    CancelAllInContext = PySide2.QtWidgets.QGesture.GestureCancelPolicy.CancelAllInContext
    CancelNone = PySide2.QtWidgets.QGesture.GestureCancelPolicy.CancelNone
    GestureCancelPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QGesture.GestureCancelPolicy'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F5085B380>'


