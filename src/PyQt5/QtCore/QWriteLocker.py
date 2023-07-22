# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QWriteLocker(__sip.simplewrapper):
    """ QWriteLocker(areadWriteLock: QReadWriteLock) """
    def readWriteLock(self): # real signature unknown; restored from __doc__
        """ readWriteLock(self) -> QReadWriteLock """
        return QReadWriteLock

    def relock(self): # real signature unknown; restored from __doc__
        """ relock(self) """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__(self) -> object """
        return object()

    def __exit__(self, type, value, traceback): # real signature unknown; restored from __doc__
        """ __exit__(self, type: object, value: object, traceback: object) """
        pass

    def __init__(self, areadWriteLock): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



