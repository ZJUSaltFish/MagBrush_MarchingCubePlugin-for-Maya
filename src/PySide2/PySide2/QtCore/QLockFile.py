# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QLockFile(__Shiboken.Object):
    """ QLockFile(self, fileName: str) -> None """
    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtCore.QLockFile.LockError """
        pass

    def getLockInfo(self): # real signature unknown; restored from __doc__
        """ getLockInfo(self) -> typing.Tuple[bool, int, str, str] """
        pass

    def isLocked(self): # real signature unknown; restored from __doc__
        """ isLocked(self) -> bool """
        return False

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) -> bool """
        return False

    def removeStaleLockFile(self): # real signature unknown; restored from __doc__
        """ removeStaleLockFile(self) -> bool """
        return False

    def setStaleLockTime(self, arg__1): # real signature unknown; restored from __doc__
        """ setStaleLockTime(self, arg__1: int) -> None """
        pass

    def staleLockTime(self): # real signature unknown; restored from __doc__
        """ staleLockTime(self) -> int """
        return 0

    def tryLock(self, timeout=0): # real signature unknown; restored from __doc__
        """ tryLock(self, timeout: int = 0) -> bool """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) -> None """
        pass

    def __init__(self, fileName): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    LockError = None # (!) real value is "<class 'PySide2.QtCore.QLockFile.LockError'>"
    LockFailedError = PySide2.QtCore.QLockFile.LockError.LockFailedError
    NoError = PySide2.QtCore.QLockFile.LockError.NoError
    PermissionError = PySide2.QtCore.QLockFile.LockError.PermissionError
    UnknownError = PySide2.QtCore.QLockFile.LockError.UnknownError


