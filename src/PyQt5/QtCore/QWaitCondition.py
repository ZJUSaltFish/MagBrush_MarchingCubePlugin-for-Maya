# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QWaitCondition(__sip.simplewrapper):
    """ QWaitCondition() """
    def wait(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        wait(self, mutex: QMutex, msecs: int = ULONG_MAX) -> bool
        wait(self, lockedMutex: QMutex, deadline: QDeadlineTimer) -> bool
        wait(self, readWriteLock: QReadWriteLock, msecs: int = ULONG_MAX) -> bool
        wait(self, lockedReadWriteLock: QReadWriteLock, deadline: QDeadlineTimer) -> bool
        """
        return False

    def wakeAll(self): # real signature unknown; restored from __doc__
        """ wakeAll(self) """
        pass

    def wakeOne(self): # real signature unknown; restored from __doc__
        """ wakeOne(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



