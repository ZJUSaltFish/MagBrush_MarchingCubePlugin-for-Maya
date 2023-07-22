# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QMimeDatabase(__Shiboken.Object):
    """ QMimeDatabase(self) -> None """
    def allMimeTypes(self): # real signature unknown; restored from __doc__
        """ allMimeTypes(self) -> typing.List[PySide2.QtCore.QMimeType] """
        pass

    def mimeTypeForData(self, data): # real signature unknown; restored from __doc__
        """
        mimeTypeForData(self, data: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QMimeType
        mimeTypeForData(self, device: PySide2.QtCore.QIODevice) -> PySide2.QtCore.QMimeType
        """
        pass

    def mimeTypeForFile(self, fileInfo, mode=None): # real signature unknown; restored from __doc__
        """
        mimeTypeForFile(self, fileInfo: PySide2.QtCore.QFileInfo, mode: PySide2.QtCore.QMimeDatabase.MatchMode = PySide2.QtCore.QMimeDatabase.MatchMode.MatchDefault) -> PySide2.QtCore.QMimeType
        mimeTypeForFile(self, fileName: str, mode: PySide2.QtCore.QMimeDatabase.MatchMode = PySide2.QtCore.QMimeDatabase.MatchMode.MatchDefault) -> PySide2.QtCore.QMimeType
        """
        pass

    def mimeTypeForFileNameAndData(self, fileName, data): # real signature unknown; restored from __doc__
        """
        mimeTypeForFileNameAndData(self, fileName: str, data: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QMimeType
        mimeTypeForFileNameAndData(self, fileName: str, device: PySide2.QtCore.QIODevice) -> PySide2.QtCore.QMimeType
        """
        pass

    def mimeTypeForName(self, nameOrAlias): # real signature unknown; restored from __doc__
        """ mimeTypeForName(self, nameOrAlias: str) -> PySide2.QtCore.QMimeType """
        pass

    def mimeTypeForUrl(self, url): # real signature unknown; restored from __doc__
        """ mimeTypeForUrl(self, url: PySide2.QtCore.QUrl) -> PySide2.QtCore.QMimeType """
        pass

    def mimeTypesForFileName(self, fileName): # real signature unknown; restored from __doc__
        """ mimeTypesForFileName(self, fileName: str) -> typing.List[PySide2.QtCore.QMimeType] """
        pass

    def suffixForFileName(self, fileName): # real signature unknown; restored from __doc__
        """ suffixForFileName(self, fileName: str) -> str """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    MatchContent = PySide2.QtCore.QMimeDatabase.MatchMode.MatchContent
    MatchDefault = PySide2.QtCore.QMimeDatabase.MatchMode.MatchDefault
    MatchExtension = PySide2.QtCore.QMimeDatabase.MatchMode.MatchExtension
    MatchMode = None # (!) real value is "<class 'PySide2.QtCore.QMimeDatabase.MatchMode'>"


