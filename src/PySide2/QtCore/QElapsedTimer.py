# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QElapsedTimer(__Shiboken.Object):
    """
    QElapsedTimer(self) -> None
    QElapsedTimer(self, QElapsedTimer: PySide2.QtCore.QElapsedTimer) -> None
    """
    def clockType(self): # real signature unknown; restored from __doc__
        """ clockType() -> PySide2.QtCore.QElapsedTimer.ClockType """
        pass

    def elapsed(self): # real signature unknown; restored from __doc__
        """ elapsed(self) -> int """
        return 0

    def hasExpired(self, timeout): # real signature unknown; restored from __doc__
        """ hasExpired(self, timeout: int) -> bool """
        return False

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def isMonotonic(self): # real signature unknown; restored from __doc__
        """ isMonotonic() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def msecsSinceReference(self): # real signature unknown; restored from __doc__
        """ msecsSinceReference(self) -> int """
        return 0

    def msecsTo(self, other): # real signature unknown; restored from __doc__
        """ msecsTo(self, other: PySide2.QtCore.QElapsedTimer) -> int """
        return 0

    def nsecsElapsed(self): # real signature unknown; restored from __doc__
        """ nsecsElapsed(self) -> int """
        return 0

    def restart(self): # real signature unknown; restored from __doc__
        """ restart(self) -> int """
        return 0

    def secsTo(self, other): # real signature unknown; restored from __doc__
        """ secsTo(self, other: PySide2.QtCore.QElapsedTimer) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    ClockType = None # (!) real value is "<class 'PySide2.QtCore.QElapsedTimer.ClockType'>"
    MachAbsoluteTime = PySide2.QtCore.QElapsedTimer.ClockType.MachAbsoluteTime
    MonotonicClock = PySide2.QtCore.QElapsedTimer.ClockType.MonotonicClock
    PerformanceCounter = PySide2.QtCore.QElapsedTimer.ClockType.PerformanceCounter
    SystemTime = PySide2.QtCore.QElapsedTimer.ClockType.SystemTime
    TickCounter = PySide2.QtCore.QElapsedTimer.ClockType.TickCounter
    __hash__ = None


