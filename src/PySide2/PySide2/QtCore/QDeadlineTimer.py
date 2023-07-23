# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDeadlineTimer(__Shiboken.Object):
    """
    QDeadlineTimer(self, QDeadlineTimer: PySide2.QtCore.QDeadlineTimer) -> None
    QDeadlineTimer(self, arg__1: PySide2.QtCore.QDeadlineTimer.ForeverConstant, type_: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> None
    QDeadlineTimer(self, msecs: int, type: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> None
    QDeadlineTimer(self, type_: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> None
    """
    def addNSecs(self, dt, nsecs): # real signature unknown; restored from __doc__
        """ addNSecs(dt: PySide2.QtCore.QDeadlineTimer, nsecs: int) -> PySide2.QtCore.QDeadlineTimer """
        pass

    def current(self, timerType=None): # real signature unknown; restored from __doc__
        """ current(timerType: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> PySide2.QtCore.QDeadlineTimer """
        pass

    def deadline(self): # real signature unknown; restored from __doc__
        """ deadline(self) -> int """
        return 0

    def deadlineNSecs(self): # real signature unknown; restored from __doc__
        """ deadlineNSecs(self) -> int """
        return 0

    def hasExpired(self): # real signature unknown; restored from __doc__
        """ hasExpired(self) -> bool """
        return False

    def isForever(self): # real signature unknown; restored from __doc__
        """ isForever(self) -> bool """
        return False

    def remainingTime(self): # real signature unknown; restored from __doc__
        """ remainingTime(self) -> int """
        return 0

    def remainingTimeNSecs(self): # real signature unknown; restored from __doc__
        """ remainingTimeNSecs(self) -> int """
        return 0

    def setDeadline(self, msecs, timerType=None): # real signature unknown; restored from __doc__
        """ setDeadline(self, msecs: int, timerType: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> None """
        pass

    def setPreciseDeadline(self, secs, nsecs=0, type=None): # real signature unknown; restored from __doc__
        """ setPreciseDeadline(self, secs: int, nsecs: int = 0, type: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> None """
        pass

    def setPreciseRemainingTime(self, secs, nsecs=0, type=None): # real signature unknown; restored from __doc__
        """ setPreciseRemainingTime(self, secs: int, nsecs: int = 0, type: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> None """
        pass

    def setRemainingTime(self, msecs, type=None): # real signature unknown; restored from __doc__
        """ setRemainingTime(self, msecs: int, type: PySide2.QtCore.Qt.TimerType = PySide2.QtCore.Qt.TimerType.CoarseTimer) -> None """
        pass

    def setTimerType(self, type): # real signature unknown; restored from __doc__
        """ setTimerType(self, type: PySide2.QtCore.Qt.TimerType) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QDeadlineTimer) -> None """
        pass

    def timerType(self): # real signature unknown; restored from __doc__
        """ timerType(self) -> PySide2.QtCore.Qt.TimerType """
        pass

    def _q_data(self): # real signature unknown; restored from __doc__
        """ _q_data(self) -> typing.Tuple[int, int] """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __iadd__(self, msecs): # real signature unknown; restored from __doc__
        """
        __iadd__(self, msecs: int) -> PySide2.QtCore.QDeadlineTimer
        
        Return self+=value.
        """
        pass

    def __init__(self, QDeadlineTimer): # real signature unknown; restored from __doc__
        pass

    def __isub__(self, msecs): # real signature unknown; restored from __doc__
        """
        __isub__(self, msecs: int) -> PySide2.QtCore.QDeadlineTimer
        
        Return self-=value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Forever = PySide2.QtCore.QDeadlineTimer.ForeverConstant.Forever
    ForeverConstant = None # (!) real value is "<class 'PySide2.QtCore.QDeadlineTimer.ForeverConstant'>"


