# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QFutureInterfaceBase(__Shiboken.Object):
    """
    QFutureInterfaceBase(self, initialState: PySide2.QtCore.QFutureInterfaceBase.State = PySide2.QtCore.QFutureInterfaceBase.State.NoState) -> None
    QFutureInterfaceBase(self, other: PySide2.QtCore.QFutureInterfaceBase) -> None
    """
    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) -> None """
        pass

    def derefT(self): # real signature unknown; restored from __doc__
        """ derefT(self) -> bool """
        return False

    def expectedResultCount(self): # real signature unknown; restored from __doc__
        """ expectedResultCount(self) -> int """
        return 0

    def isCanceled(self): # real signature unknown; restored from __doc__
        """ isCanceled(self) -> bool """
        return False

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isPaused(self): # real signature unknown; restored from __doc__
        """ isPaused(self) -> bool """
        return False

    def isProgressUpdateNeeded(self): # real signature unknown; restored from __doc__
        """ isProgressUpdateNeeded(self) -> bool """
        return False

    def isResultReadyAt(self, index): # real signature unknown; restored from __doc__
        """ isResultReadyAt(self, index: int) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isStarted(self): # real signature unknown; restored from __doc__
        """ isStarted(self) -> bool """
        return False

    def isThrottled(self): # real signature unknown; restored from __doc__
        """ isThrottled(self) -> bool """
        return False

    def mutex(self): # real signature unknown; restored from __doc__
        """
        mutex(self) -> PySide2.QtCore.QMutex
        mutex(self, arg__1: int) -> PySide2.QtCore.QMutex
        """
        pass

    def progressMaximum(self): # real signature unknown; restored from __doc__
        """ progressMaximum(self) -> int """
        return 0

    def progressMinimum(self): # real signature unknown; restored from __doc__
        """ progressMinimum(self) -> int """
        return 0

    def progressText(self): # real signature unknown; restored from __doc__
        """ progressText(self) -> str """
        return ""

    def progressValue(self): # real signature unknown; restored from __doc__
        """ progressValue(self) -> int """
        return 0

    def queryState(self, state): # real signature unknown; restored from __doc__
        """ queryState(self, state: PySide2.QtCore.QFutureInterfaceBase.State) -> bool """
        return False

    def refT(self): # real signature unknown; restored from __doc__
        """ refT(self) -> bool """
        return False

    def reportCanceled(self): # real signature unknown; restored from __doc__
        """ reportCanceled(self) -> None """
        pass

    def reportFinished(self): # real signature unknown; restored from __doc__
        """ reportFinished(self) -> None """
        pass

    def reportResultsReady(self, beginIndex, endIndex): # real signature unknown; restored from __doc__
        """ reportResultsReady(self, beginIndex: int, endIndex: int) -> None """
        pass

    def reportStarted(self): # real signature unknown; restored from __doc__
        """ reportStarted(self) -> None """
        pass

    def resultCount(self): # real signature unknown; restored from __doc__
        """ resultCount(self) -> int """
        return 0

    def setExpectedResultCount(self, resultCount): # real signature unknown; restored from __doc__
        """ setExpectedResultCount(self, resultCount: int) -> None """
        pass

    def setFilterMode(self, enable): # real signature unknown; restored from __doc__
        """ setFilterMode(self, enable: bool) -> None """
        pass

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) -> None """
        pass

    def setProgressRange(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setProgressRange(self, minimum: int, maximum: int) -> None """
        pass

    def setProgressValue(self, progressValue): # real signature unknown; restored from __doc__
        """ setProgressValue(self, progressValue: int) -> None """
        pass

    def setProgressValueAndText(self, progressValue, progressText): # real signature unknown; restored from __doc__
        """ setProgressValueAndText(self, progressValue: int, progressText: str) -> None """
        pass

    def setRunnable(self, runnable): # real signature unknown; restored from __doc__
        """ setRunnable(self, runnable: PySide2.QtCore.QRunnable) -> None """
        pass

    def setThreadPool(self, pool): # real signature unknown; restored from __doc__
        """ setThreadPool(self, pool: PySide2.QtCore.QThreadPool) -> None """
        pass

    def setThrottled(self, enable): # real signature unknown; restored from __doc__
        """ setThrottled(self, enable: bool) -> None """
        pass

    def togglePaused(self): # real signature unknown; restored from __doc__
        """ togglePaused(self) -> None """
        pass

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ waitForFinished(self) -> None """
        pass

    def waitForNextResult(self): # real signature unknown; restored from __doc__
        """ waitForNextResult(self) -> bool """
        return False

    def waitForResult(self, resultIndex): # real signature unknown; restored from __doc__
        """ waitForResult(self, resultIndex: int) -> None """
        pass

    def waitForResume(self): # real signature unknown; restored from __doc__
        """ waitForResume(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
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

    def __init__(self, initialState=None): # real signature unknown; restored from __doc__
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Canceled = PySide2.QtCore.QFutureInterfaceBase.State.Canceled
    Finished = PySide2.QtCore.QFutureInterfaceBase.State.Finished
    NoState = PySide2.QtCore.QFutureInterfaceBase.State.NoState
    Paused = PySide2.QtCore.QFutureInterfaceBase.State.Paused
    Running = PySide2.QtCore.QFutureInterfaceBase.State.Running
    Started = PySide2.QtCore.QFutureInterfaceBase.State.Started
    State = None # (!) real value is "<class 'PySide2.QtCore.QFutureInterfaceBase.State'>"
    Throttled = PySide2.QtCore.QFutureInterfaceBase.State.Throttled
    __hash__ = None


