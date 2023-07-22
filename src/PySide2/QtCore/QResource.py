# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QResource(__Shiboken.Object):
    """ QResource(self, file: str = '', locale: PySide2.QtCore.QLocale = Default(QLocale)) -> None """
    def absoluteFilePath(self): # real signature unknown; restored from __doc__
        """ absoluteFilePath(self) -> str """
        return ""

    def addSearchPath(self, path): # real signature unknown; restored from __doc__
        """ addSearchPath(path: str) -> None """
        pass

    def children(self): # real signature unknown; restored from __doc__
        """ children(self) -> typing.List[str] """
        pass

    def compressionAlgorithm(self): # real signature unknown; restored from __doc__
        """ compressionAlgorithm(self) -> PySide2.QtCore.QResource.Compression """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> bytes """
        return b""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isCompressed(self): # real signature unknown; restored from __doc__
        """ isCompressed(self) -> bool """
        return False

    def isDir(self): # real signature unknown; restored from __doc__
        """ isDir(self) -> bool """
        return False

    def isFile(self): # real signature unknown; restored from __doc__
        """ isFile(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ lastModified(self) -> PySide2.QtCore.QDateTime """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> PySide2.QtCore.QLocale """
        pass

    def registerResource(self, rccFilename, resourceRoot=''): # real signature unknown; restored from __doc__
        """ registerResource(rccFilename: str, resourceRoot: str = '') -> bool """
        return False

    def registerResourceData(self, rccData, resourceRoot=''): # real signature unknown; restored from __doc__
        """ registerResourceData(rccData: bytes, resourceRoot: str = '') -> bool """
        return False

    def searchPaths(self): # real signature unknown; restored from __doc__
        """ searchPaths() -> typing.List[str] """
        pass

    def setFileName(self, file): # real signature unknown; restored from __doc__
        """ setFileName(self, file: str) -> None """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: PySide2.QtCore.QLocale) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def uncompressedData(self): # real signature unknown; restored from __doc__
        """ uncompressedData(self) -> PySide2.QtCore.QByteArray """
        pass

    def uncompressedSize(self): # real signature unknown; restored from __doc__
        """ uncompressedSize(self) -> int """
        return 0

    def unregisterResource(self, rccFilename, resourceRoot=''): # real signature unknown; restored from __doc__
        """ unregisterResource(rccFilename: str, resourceRoot: str = '') -> bool """
        return False

    def unregisterResourceData(self, rccData, resourceRoot=''): # real signature unknown; restored from __doc__
        """ unregisterResourceData(rccData: bytes, resourceRoot: str = '') -> bool """
        return False

    def __init__(self, file='', locale=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Compression = None # (!) real value is "<class 'PySide2.QtCore.QResource.Compression'>"
    NoCompression = PySide2.QtCore.QResource.Compression.NoCompression
    ZlibCompression = PySide2.QtCore.QResource.Compression.ZlibCompression
    ZstdCompression = PySide2.QtCore.QResource.Compression.ZstdCompression


