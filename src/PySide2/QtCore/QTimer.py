# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QTimer(QObject):
    """ QTimer(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def interval(self): # real signature unknown; restored from __doc__
        """ interval(self) -> int """
        return 0

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSingleShot(self): # real signature unknown; restored from __doc__
        """ isSingleShot(self) -> bool """
        return False

    def killTimer(self, arg__1): # real signature unknown; restored from __doc__
        """ killTimer(self, arg__1: int) -> None """
        pass

    def remainingTime(self): # real signature unknown; restored from __doc__
        """ remainingTime(self) -> int """
        return 0

    def setInterval(self, msec): # real signature unknown; restored from __doc__
        """ setInterval(self, msec: int) -> None """
        pass

    def setSingleShot(self, singleShot): # real signature unknown; restored from __doc__
        """ setSingleShot(self, singleShot: bool) -> None """
        pass

    def setTimerType(self, atype): # real signature unknown; restored from __doc__
        """ setTimerType(self, atype: PySide2.QtCore.Qt.TimerType) -> None """
        pass

    def singleShot(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        singleShot(arg__1: int, arg__2: typing.Callable) -> None
        singleShot(msec: int, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        singleShot(msec: int, timerType: PySide2.QtCore.Qt.TimerType, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """
        start(self) -> None
        start(self, msec: int) -> None
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def timeout(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def timerId(self): # real signature unknown; restored from __doc__
        """ timerId(self) -> int """
        return 0

    def timerType(self): # real signature unknown; restored from __doc__
        """ timerType(self) -> PySide2.QtCore.Qt.TimerType """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DDEF00>'


