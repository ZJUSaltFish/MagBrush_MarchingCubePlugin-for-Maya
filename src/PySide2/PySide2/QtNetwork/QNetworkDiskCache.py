# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QAbstractNetworkCache import QAbstractNetworkCache

class QNetworkDiskCache(QAbstractNetworkCache):
    """ QNetworkDiskCache(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def cacheDirectory(self): # real signature unknown; restored from __doc__
        """ cacheDirectory(self) -> str """
        return ""

    def cacheSize(self): # real signature unknown; restored from __doc__
        """ cacheSize(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def data(self, url): # real signature unknown; restored from __doc__
        """ data(self, url: PySide2.QtCore.QUrl) -> PySide2.QtCore.QIODevice """
        pass

    def expire(self): # real signature unknown; restored from __doc__
        """ expire(self) -> int """
        return 0

    def fileMetaData(self, fileName): # real signature unknown; restored from __doc__
        """ fileMetaData(self, fileName: str) -> PySide2.QtNetwork.QNetworkCacheMetaData """
        pass

    def insert(self, device): # real signature unknown; restored from __doc__
        """ insert(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ maximumCacheSize(self) -> int """
        return 0

    def metaData(self, url): # real signature unknown; restored from __doc__
        """ metaData(self, url: PySide2.QtCore.QUrl) -> PySide2.QtNetwork.QNetworkCacheMetaData """
        pass

    def prepare(self, metaData): # real signature unknown; restored from __doc__
        """ prepare(self, metaData: PySide2.QtNetwork.QNetworkCacheMetaData) -> PySide2.QtCore.QIODevice """
        pass

    def remove(self, url): # real signature unknown; restored from __doc__
        """ remove(self, url: PySide2.QtCore.QUrl) -> bool """
        return False

    def setCacheDirectory(self, cacheDir): # real signature unknown; restored from __doc__
        """ setCacheDirectory(self, cacheDir: str) -> None """
        pass

    def setMaximumCacheSize(self, size): # real signature unknown; restored from __doc__
        """ setMaximumCacheSize(self, size: int) -> None """
        pass

    def updateMetaData(self, metaData): # real signature unknown; restored from __doc__
        """ updateMetaData(self, metaData: PySide2.QtNetwork.QNetworkCacheMetaData) -> None """
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D85E940>'


