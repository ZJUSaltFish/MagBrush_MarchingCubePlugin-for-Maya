# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QSystemSemaphore(__Shiboken.Object):
    """ QSystemSemaphore(self, key: str, initialValue: int = 0, mode: PySide2.QtCore.QSystemSemaphore.AccessMode = PySide2.QtCore.QSystemSemaphore.AccessMode.Open) -> None """
    def acquire(self): # real signature unknown; restored from __doc__
        """ acquire(self) -> bool """
        return False

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def release(self, n=1): # real signature unknown; restored from __doc__
        """ release(self, n: int = 1) -> bool """
        return False

    def setKey(self, key, initialValue=0, mode=None): # real signature unknown; restored from __doc__
        """ setKey(self, key: str, initialValue: int = 0, mode: PySide2.QtCore.QSystemSemaphore.AccessMode = PySide2.QtCore.QSystemSemaphore.AccessMode.Open) -> None """
        pass

    def __init__(self, key, initialValue=0, mode=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AccessMode = None # (!) real value is "<class 'PySide2.QtCore.QSystemSemaphore.AccessMode'>"
    AlreadyExists = PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError.AlreadyExists
    Create = PySide2.QtCore.QSystemSemaphore.AccessMode.Create
    KeyError = PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError.KeyError
    NoError = PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError.NoError
    NotFound = PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError.NotFound
    Open = PySide2.QtCore.QSystemSemaphore.AccessMode.Open
    OutOfResources = PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError.OutOfResources
    PermissionDenied = PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError.PermissionDenied
    SystemSemaphoreError = None # (!) real value is "<class 'PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError'>"
    UnknownError = PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError.UnknownError


