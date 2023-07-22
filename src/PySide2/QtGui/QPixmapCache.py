# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPixmapCache(__Shiboken.Object):
    """ QPixmapCache(self) -> None """
    def cacheLimit(self): # real signature unknown; restored from __doc__
        """ cacheLimit() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear() -> None """
        pass

    def find(self, key, pixmap): # real signature unknown; restored from __doc__
        """
        find(key: PySide2.QtGui.QPixmapCache.Key, pixmap: PySide2.QtGui.QPixmap) -> bool
        find(key: str) -> PySide2.QtGui.QPixmap
        find(key: str, pixmap: PySide2.QtGui.QPixmap) -> bool
        find(self, arg__1: PySide2.QtGui.QPixmapCache.Key) -> None
        """
        return False

    def insert(self, key, pixmap): # real signature unknown; restored from __doc__
        """
        insert(key: str, pixmap: PySide2.QtGui.QPixmap) -> bool
        insert(pixmap: PySide2.QtGui.QPixmap) -> PySide2.QtGui.QPixmapCache.Key
        """
        return False

    def remove(self, key): # real signature unknown; restored from __doc__
        """
        remove(key: PySide2.QtGui.QPixmapCache.Key) -> None
        remove(key: str) -> None
        """
        pass

    def replace(self, key, pixmap): # real signature unknown; restored from __doc__
        """ replace(key: PySide2.QtGui.QPixmapCache.Key, pixmap: PySide2.QtGui.QPixmap) -> bool """
        return False

    def setCacheLimit(self, arg__1): # real signature unknown; restored from __doc__
        """ setCacheLimit(arg__1: int) -> None """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Key = None # (!) real value is "<class 'PySide2.QtGui.QPixmapCache.Key'>"


