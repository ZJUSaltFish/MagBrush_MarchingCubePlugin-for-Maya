# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QThread(QObject):
    """ QThread(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def currentThread(self): # real signature unknown; restored from __doc__
        """ currentThread() -> PySide2.QtCore.QThread """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventDispatcher(self): # real signature unknown; restored from __doc__
        """ eventDispatcher(self) -> PySide2.QtCore.QAbstractEventDispatcher """
        pass

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def exit(self, retcode=0): # real signature unknown; restored from __doc__
        """ exit(self, retcode: int = 0) -> None """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def idealThreadCount(self): # real signature unknown; restored from __doc__
        """ idealThreadCount() -> int """
        return 0

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isInterruptionRequested(self): # real signature unknown; restored from __doc__
        """ isInterruptionRequested(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def loopLevel(self): # real signature unknown; restored from __doc__
        """ loopLevel(self) -> int """
        return 0

    def msleep(self, arg__1): # real signature unknown; restored from __doc__
        """ msleep(arg__1: int) -> None """
        pass

    def priority(self): # real signature unknown; restored from __doc__
        """ priority(self) -> PySide2.QtCore.QThread.Priority """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) -> None """
        pass

    def requestInterruption(self): # real signature unknown; restored from __doc__
        """ requestInterruption(self) -> None """
        pass

    def run(self): # real signature unknown; restored from __doc__
        """ run(self) -> None """
        pass

    def setEventDispatcher(self, eventDispatcher): # real signature unknown; restored from __doc__
        """ setEventDispatcher(self, eventDispatcher: PySide2.QtCore.QAbstractEventDispatcher) -> None """
        pass

    def setPriority(self, priority): # real signature unknown; restored from __doc__
        """ setPriority(self, priority: PySide2.QtCore.QThread.Priority) -> None """
        pass

    def setStackSize(self, stackSize): # real signature unknown; restored from __doc__
        """ setStackSize(self, stackSize: int) -> None """
        pass

    def setTerminationEnabled(self, enabled=True): # real signature unknown; restored from __doc__
        """ setTerminationEnabled(enabled: bool = True) -> None """
        pass

    def sleep(self, arg__1): # real signature unknown; restored from __doc__
        """ sleep(arg__1: int) -> None """
        pass

    def stackSize(self): # real signature unknown; restored from __doc__
        """ stackSize(self) -> int """
        return 0

    def start(self, priority=None): # real signature unknown; restored from __doc__
        """ start(self, priority: PySide2.QtCore.QThread.Priority = PySide2.QtCore.QThread.Priority.InheritPriority) -> None """
        pass

    def started(self, *args, **kwargs): # real signature unknown
        pass

    def terminate(self): # real signature unknown; restored from __doc__
        """ terminate(self) -> None """
        pass

    def usleep(self, arg__1): # real signature unknown; restored from __doc__
        """ usleep(arg__1: int) -> None """
        pass

    def wait(self, deadline=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        wait(self, deadline: PySide2.QtCore.QDeadlineTimer = Instance(PySide2.QtCore.QDeadlineTimer)) -> bool
        wait(self, time: int) -> bool
        """
        pass

    def yieldCurrentThread(self): # real signature unknown; restored from __doc__
        """ yieldCurrentThread() -> None """
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

    HighestPriority = PySide2.QtCore.QThread.Priority.HighestPriority
    HighPriority = PySide2.QtCore.QThread.Priority.HighPriority
    IdlePriority = PySide2.QtCore.QThread.Priority.IdlePriority
    InheritPriority = PySide2.QtCore.QThread.Priority.InheritPriority
    LowestPriority = PySide2.QtCore.QThread.Priority.LowestPriority
    LowPriority = PySide2.QtCore.QThread.Priority.LowPriority
    NormalPriority = PySide2.QtCore.QThread.Priority.NormalPriority
    Priority = None # (!) real value is "<class 'PySide2.QtCore.QThread.Priority'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E0BD00>'
    TimeCriticalPriority = PySide2.QtCore.QThread.Priority.TimeCriticalPriority


