# encoding: utf-8
# module PySide2.QtConcurrent
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtConcurrent.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QFutureQString(__Shiboken.Object):
    """
    QFutureQString(self) -> None
    QFutureQString(self, QFutureQString: PySide2.QtConcurrent.QFutureQString) -> None
    """
    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) -> None """
        pass

    def isCanceled(self): # real signature unknown; restored from __doc__
        """ isCanceled(self) -> bool """
        return False

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isPaused(self): # real signature unknown; restored from __doc__
        """ isPaused(self) -> bool """
        return False

    def isResultReadyAt(self, resultIndex): # real signature unknown; restored from __doc__
        """ isResultReadyAt(self, resultIndex: int) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isStarted(self): # real signature unknown; restored from __doc__
        """ isStarted(self) -> bool """
        return False

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) -> None """
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

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> str """
        return ""

    def resultAt(self, index): # real signature unknown; restored from __doc__
        """ resultAt(self, index: int) -> str """
        return ""

    def resultCount(self): # real signature unknown; restored from __doc__
        """ resultCount(self) -> int """
        return 0

    def results(self): # real signature unknown; restored from __doc__
        """ results(self) -> typing.List[str] """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) -> None """
        pass

    def togglePaused(self): # real signature unknown; restored from __doc__
        """ togglePaused(self) -> None """
        pass

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ waitForFinished(self) -> None """
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

    __hash__ = None


class QFutureVoid(__Shiboken.Object):
    """
    QFutureVoid(self) -> None
    QFutureVoid(self, QFutureVoid: PySide2.QtConcurrent.QFutureVoid) -> None
    """
    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) -> None """
        pass

    def isCanceled(self): # real signature unknown; restored from __doc__
        """ isCanceled(self) -> bool """
        return False

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isPaused(self): # real signature unknown; restored from __doc__
        """ isPaused(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isStarted(self): # real signature unknown; restored from __doc__
        """ isStarted(self) -> bool """
        return False

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) -> None """
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

    def resultCount(self): # real signature unknown; restored from __doc__
        """ resultCount(self) -> int """
        return 0

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) -> None """
        pass

    def togglePaused(self): # real signature unknown; restored from __doc__
        """ togglePaused(self) -> None """
        pass

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ waitForFinished(self) -> None """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QFutureWatcherQString(__PySide2_QtCore.QObject):
    """ QFutureWatcherQString(self, _parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def canceled(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def future(self): # real signature unknown; restored from __doc__
        """ future(self) -> PySide2.QtConcurrent.QFutureQString """
        pass

    def paused(self, *args, **kwargs): # real signature unknown
        pass

    def progressRangeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def progressTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def progressValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> str """
        return ""

    def resultAt(self, index): # real signature unknown; restored from __doc__
        """ resultAt(self, index: int) -> str """
        return ""

    def resultReadyAt(self, *args, **kwargs): # real signature unknown
        pass

    def resultsReadyAt(self, *args, **kwargs): # real signature unknown
        pass

    def resumed(self, *args, **kwargs): # real signature unknown
        pass

    def setFuture(self, future): # real signature unknown; restored from __doc__
        """ setFuture(self, future: PySide2.QtConcurrent.QFutureQString) -> None """
        pass

    def started(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, _parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000024D8EBE4580>'


class QFutureWatcherVoid(__PySide2_QtCore.QObject):
    """ QFutureWatcherVoid(self, _parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def canceled(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def paused(self, *args, **kwargs): # real signature unknown
        pass

    def progressRangeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def progressTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def progressValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def resultReadyAt(self, *args, **kwargs): # real signature unknown
        pass

    def resultsReadyAt(self, *args, **kwargs): # real signature unknown
        pass

    def resumed(self, *args, **kwargs): # real signature unknown
        pass

    def started(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, _parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000024D8EBE43C0>'


class QtConcurrent(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    OrderedReduce = PySide2.QtConcurrent.QtConcurrent.ReduceOption.OrderedReduce
    ReduceOption = None # (!) real value is "<class 'PySide2.QtConcurrent.QtConcurrent.ReduceOption'>"
    ReduceOptions = None # (!) real value is "<class 'PySide2.QtConcurrent.QtConcurrent.ReduceOptions'>"
    SequentialReduce = PySide2.QtConcurrent.QtConcurrent.ReduceOption.SequentialReduce
    ThreadFinished = PySide2.QtConcurrent.QtConcurrent.ThreadFunctionResult.ThreadFinished
    ThreadFunctionResult = None # (!) real value is "<class 'PySide2.QtConcurrent.QtConcurrent.ThreadFunctionResult'>"
    ThrottleThread = PySide2.QtConcurrent.QtConcurrent.ThreadFunctionResult.ThrottleThread
    UnorderedReduce = PySide2.QtConcurrent.QtConcurrent.ReduceOption.UnorderedReduce


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024D8E0117B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtConcurrent', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024D8E0117B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtConcurrent.cp310-win_amd64.pyd')"

