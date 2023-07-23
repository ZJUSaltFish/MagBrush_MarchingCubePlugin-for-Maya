# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QSemaphore(__Shiboken.Object):
    """ QSemaphore(self, n: int = 0) -> None """
    def acquire(self, n=1): # real signature unknown; restored from __doc__
        """ acquire(self, n: int = 1) -> None """
        pass

    def available(self): # real signature unknown; restored from __doc__
        """ available(self) -> int """
        return 0

    def release(self, n=1): # real signature unknown; restored from __doc__
        """ release(self, n: int = 1) -> None """
        pass

    def tryAcquire(self, n, timeout): # real signature unknown; restored from __doc__
        """
        tryAcquire(self, n: int, timeout: int) -> bool
        tryAcquire(self, n: int = 1) -> bool
        """
        return False

    def __init__(self, n=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


