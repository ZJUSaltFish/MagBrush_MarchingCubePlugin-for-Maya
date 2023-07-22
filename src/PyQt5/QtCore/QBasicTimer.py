# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QBasicTimer(__sip.simplewrapper):
    """
    QBasicTimer()
    QBasicTimer(a0: QBasicTimer)
    """
    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def start(self, msec, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, msec: int, timerType: Qt.TimerType, obj: QObject)
        start(self, msec: int, obj: QObject)
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QBasicTimer) """
        pass

    def timerId(self): # real signature unknown; restored from __doc__
        """ timerId(self) -> int """
        return 0

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



