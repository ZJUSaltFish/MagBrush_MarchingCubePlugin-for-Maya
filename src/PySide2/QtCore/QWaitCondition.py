# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QWaitCondition(__Shiboken.Object):
    """ QWaitCondition(self) -> None """
    def notify_all(self): # real signature unknown; restored from __doc__
        """ notify_all(self) -> None """
        pass

    def notify_one(self): # real signature unknown; restored from __doc__
        """ notify_one(self) -> None """
        pass

    def wait(self, lockedMutex, deadline=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        wait(self, lockedMutex: PySide2.QtCore.QMutex, deadline: PySide2.QtCore.QDeadlineTimer = Instance(PySide2.QtCore.QDeadlineTimer)) -> bool
        wait(self, lockedMutex: PySide2.QtCore.QMutex, time: int) -> bool
        wait(self, lockedReadWriteLock: PySide2.QtCore.QReadWriteLock, deadline: PySide2.QtCore.QDeadlineTimer = Instance(PySide2.QtCore.QDeadlineTimer)) -> bool
        wait(self, lockedReadWriteLock: PySide2.QtCore.QReadWriteLock, time: int) -> bool
        """
        pass

    def wakeAll(self): # real signature unknown; restored from __doc__
        """ wakeAll(self) -> None """
        pass

    def wakeOne(self): # real signature unknown; restored from __doc__
        """ wakeOne(self) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


