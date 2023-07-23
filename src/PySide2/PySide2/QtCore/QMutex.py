# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QBasicMutex import QBasicMutex

class QMutex(QBasicMutex):
    """
    QMutex(self) -> None
    QMutex(self, mode: PySide2.QtCore.QMutex.RecursionMode) -> None
    """
    def isRecursive(self): # real signature unknown; restored from __doc__
        """ isRecursive(self) -> bool """
        return False

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) -> None """
        pass

    def tryLock(self): # real signature unknown; restored from __doc__
        """
        tryLock(self) -> bool
        tryLock(self, timeout: int = 0) -> bool
        """
        return False

    def try_lock(self): # real signature unknown; restored from __doc__
        """ try_lock(self) -> bool """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    NonRecursive = PySide2.QtCore.QMutex.RecursionMode.NonRecursive
    RecursionMode = None # (!) real value is "<class 'PySide2.QtCore.QMutex.RecursionMode'>"
    Recursive = PySide2.QtCore.QMutex.RecursionMode.Recursive


