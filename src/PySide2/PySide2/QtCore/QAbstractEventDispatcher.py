# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QAbstractEventDispatcher(QObject):
    """ QAbstractEventDispatcher(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def aboutToBlock(self, *args, **kwargs): # real signature unknown
        pass

    def awake(self, *args, **kwargs): # real signature unknown
        pass

    def closingDown(self): # real signature unknown; restored from __doc__
        """ closingDown(self) -> None """
        pass

    def filterNativeEvent(self, eventType, message): # real signature unknown; restored from __doc__
        """ filterNativeEvent(self, eventType: PySide2.QtCore.QByteArray, message: int) -> typing.Tuple[bool, int] """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> None """
        pass

    def hasPendingEvents(self): # real signature unknown; restored from __doc__
        """ hasPendingEvents(self) -> bool """
        return False

    def installNativeEventFilter(self, filterObj): # real signature unknown; restored from __doc__
        """ installNativeEventFilter(self, filterObj: PySide2.QtCore.QAbstractNativeEventFilter) -> None """
        pass

    def instance(self, thread, PySide2_QtCore_QThread=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ instance(thread: typing.Optional[PySide2.QtCore.QThread] = None) -> PySide2.QtCore.QAbstractEventDispatcher """
        pass

    def interrupt(self): # real signature unknown; restored from __doc__
        """ interrupt(self) -> None """
        pass

    def processEvents(self, flags): # real signature unknown; restored from __doc__
        """ processEvents(self, flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags) -> bool """
        return False

    def registeredTimers(self, p_object): # real signature unknown; restored from __doc__
        """ registeredTimers(self, object: PySide2.QtCore.QObject) -> typing.List[PySide2.QtCore.QAbstractEventDispatcher.TimerInfo] """
        pass

    def registerEventNotifier(self, notifier): # real signature unknown; restored from __doc__
        """ registerEventNotifier(self, notifier: PySide2.QtCore.QWinEventNotifier) -> bool """
        return False

    def registerSocketNotifier(self, notifier): # real signature unknown; restored from __doc__
        """ registerSocketNotifier(self, notifier: PySide2.QtCore.QSocketNotifier) -> None """
        pass

    def registerTimer(self, interval, timerType, p_object): # real signature unknown; restored from __doc__
        """
        registerTimer(self, interval: int, timerType: PySide2.QtCore.Qt.TimerType, object: PySide2.QtCore.QObject) -> int
        registerTimer(self, timerId: int, interval: int, timerType: PySide2.QtCore.Qt.TimerType, object: PySide2.QtCore.QObject) -> None
        """
        return 0

    def remainingTime(self, timerId): # real signature unknown; restored from __doc__
        """ remainingTime(self, timerId: int) -> int """
        return 0

    def removeNativeEventFilter(self, filterObj): # real signature unknown; restored from __doc__
        """ removeNativeEventFilter(self, filterObj: PySide2.QtCore.QAbstractNativeEventFilter) -> None """
        pass

    def startingUp(self): # real signature unknown; restored from __doc__
        """ startingUp(self) -> None """
        pass

    def unregisterEventNotifier(self, notifier): # real signature unknown; restored from __doc__
        """ unregisterEventNotifier(self, notifier: PySide2.QtCore.QWinEventNotifier) -> None """
        pass

    def unregisterSocketNotifier(self, notifier): # real signature unknown; restored from __doc__
        """ unregisterSocketNotifier(self, notifier: PySide2.QtCore.QSocketNotifier) -> None """
        pass

    def unregisterTimer(self, timerId): # real signature unknown; restored from __doc__
        """ unregisterTimer(self, timerId: int) -> bool """
        return False

    def unregisterTimers(self, p_object): # real signature unknown; restored from __doc__
        """ unregisterTimers(self, object: PySide2.QtCore.QObject) -> bool """
        return False

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E640C0>'
    TimerInfo = None # (!) real value is "<class 'PySide2.QtCore.QAbstractEventDispatcher.TimerInfo'>"


