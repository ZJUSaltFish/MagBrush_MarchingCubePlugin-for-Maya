# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QThreadPool(QObject):
    """ QThreadPool(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def activeThreadCount(self): # real signature unknown; restored from __doc__
        """ activeThreadCount(self) -> int """
        return 0

    def cancel(self, runnable): # real signature unknown; restored from __doc__
        """ cancel(self, runnable: PySide2.QtCore.QRunnable) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def contains(self, thread): # real signature unknown; restored from __doc__
        """ contains(self, thread: PySide2.QtCore.QThread) -> bool """
        return False

    def expiryTimeout(self): # real signature unknown; restored from __doc__
        """ expiryTimeout(self) -> int """
        return 0

    def globalInstance(self): # real signature unknown; restored from __doc__
        """ globalInstance() -> PySide2.QtCore.QThreadPool """
        pass

    def maxThreadCount(self): # real signature unknown; restored from __doc__
        """ maxThreadCount(self) -> int """
        return 0

    def releaseThread(self): # real signature unknown; restored from __doc__
        """ releaseThread(self) -> None """
        pass

    def reserveThread(self): # real signature unknown; restored from __doc__
        """ reserveThread(self) -> None """
        pass

    def setExpiryTimeout(self, expiryTimeout): # real signature unknown; restored from __doc__
        """ setExpiryTimeout(self, expiryTimeout: int) -> None """
        pass

    def setMaxThreadCount(self, maxThreadCount): # real signature unknown; restored from __doc__
        """ setMaxThreadCount(self, maxThreadCount: int) -> None """
        pass

    def setStackSize(self, stackSize): # real signature unknown; restored from __doc__
        """ setStackSize(self, stackSize: int) -> None """
        pass

    def stackSize(self): # real signature unknown; restored from __doc__
        """ stackSize(self) -> int """
        return 0

    def start(self, runnable, priority=0): # real signature unknown; restored from __doc__
        """ start(self, runnable: PySide2.QtCore.QRunnable, priority: int = 0) -> None """
        pass

    def tryStart(self, runnable): # real signature unknown; restored from __doc__
        """ tryStart(self, runnable: PySide2.QtCore.QRunnable) -> bool """
        return False

    def tryTake(self, runnable): # real signature unknown; restored from __doc__
        """ tryTake(self, runnable: PySide2.QtCore.QRunnable) -> bool """
        return False

    def waitForDone(self, msecs=-1): # real signature unknown; restored from __doc__
        """ waitForDone(self, msecs: int = -1) -> bool """
        return False

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DEC380>'


