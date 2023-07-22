# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QEventLoop(QObject):
    """ QEventLoop(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def exec_(self, flags=None): # real signature unknown; restored from __doc__
        """ exec_(self, flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags = PySide2.QtCore.QEventLoop.ProcessEventsFlag.AllEvents) -> int """
        return 0

    def exit(self, returnCode=0): # real signature unknown; restored from __doc__
        """ exit(self, returnCode: int = 0) -> None """
        pass

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def processEvents(self, flags, maximumTime): # real signature unknown; restored from __doc__
        """
        processEvents(self, flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags, maximumTime: int) -> None
        processEvents(self, flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags = PySide2.QtCore.QEventLoop.ProcessEventsFlag.AllEvents) -> bool
        """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) -> None """
        pass

    def wakeUp(self): # real signature unknown; restored from __doc__
        """ wakeUp(self) -> None """
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

    AllEvents = PySide2.QtCore.QEventLoop.ProcessEventsFlag.AllEvents
    DialogExec = PySide2.QtCore.QEventLoop.ProcessEventsFlag.DialogExec
    EventLoopExec = PySide2.QtCore.QEventLoop.ProcessEventsFlag.EventLoopExec
    ExcludeSocketNotifiers = PySide2.QtCore.QEventLoop.ProcessEventsFlag.ExcludeSocketNotifiers
    ExcludeUserInputEvents = PySide2.QtCore.QEventLoop.ProcessEventsFlag.ExcludeUserInputEvents
    ProcessEventsFlag = None # (!) real value is "<class 'PySide2.QtCore.QEventLoop.ProcessEventsFlag'>"
    ProcessEventsFlags = None # (!) real value is "<class 'PySide2.QtCore.QEventLoop.ProcessEventsFlags'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DFCC00>'
    WaitForMoreEvents = PySide2.QtCore.QEventLoop.ProcessEventsFlag.WaitForMoreEvents
    X11ExcludeTimers = PySide2.QtCore.QEventLoop.ProcessEventsFlag.X11ExcludeTimers


