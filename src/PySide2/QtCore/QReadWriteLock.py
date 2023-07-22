# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QReadWriteLock(__Shiboken.Object):
    """ QReadWriteLock(self, recursionMode: PySide2.QtCore.QReadWriteLock.RecursionMode = PySide2.QtCore.QReadWriteLock.RecursionMode.NonRecursive) -> None """
    def lockForRead(self): # real signature unknown; restored from __doc__
        """ lockForRead(self) -> None """
        pass

    def lockForWrite(self): # real signature unknown; restored from __doc__
        """ lockForWrite(self) -> None """
        pass

    def tryLockForRead(self): # real signature unknown; restored from __doc__
        """
        tryLockForRead(self) -> bool
        tryLockForRead(self, timeout: int) -> bool
        """
        return False

    def tryLockForWrite(self): # real signature unknown; restored from __doc__
        """
        tryLockForWrite(self) -> bool
        tryLockForWrite(self, timeout: int) -> bool
        """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) -> None """
        pass

    def __init__(self, recursionMode=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    NonRecursive = PySide2.QtCore.QReadWriteLock.RecursionMode.NonRecursive
    RecursionMode = None # (!) real value is "<class 'PySide2.QtCore.QReadWriteLock.RecursionMode'>"
    Recursive = PySide2.QtCore.QReadWriteLock.RecursionMode.Recursive


