# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMimeDatabase(__sip.simplewrapper):
    """ QMimeDatabase() """
    def allMimeTypes(self): # real signature unknown; restored from __doc__
        """ allMimeTypes(self) -> List[QMimeType] """
        return []

    def mimeTypeForData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForData(self, data: Union[QByteArray, bytes, bytearray]) -> QMimeType
        mimeTypeForData(self, device: QIODevice) -> QMimeType
        """
        return QMimeType

    def mimeTypeForFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForFile(self, fileName: str, mode: QMimeDatabase.MatchMode = QMimeDatabase.MatchDefault) -> QMimeType
        mimeTypeForFile(self, fileInfo: QFileInfo, mode: QMimeDatabase.MatchMode = QMimeDatabase.MatchDefault) -> QMimeType
        """
        return QMimeType

    def mimeTypeForFileNameAndData(self, fileName, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mimeTypeForFileNameAndData(self, fileName: str, device: QIODevice) -> QMimeType
        mimeTypeForFileNameAndData(self, fileName: str, data: Union[QByteArray, bytes, bytearray]) -> QMimeType
        """
        return QMimeType

    def mimeTypeForName(self, nameOrAlias): # real signature unknown; restored from __doc__
        """ mimeTypeForName(self, nameOrAlias: str) -> QMimeType """
        return QMimeType

    def mimeTypeForUrl(self, url): # real signature unknown; restored from __doc__
        """ mimeTypeForUrl(self, url: QUrl) -> QMimeType """
        return QMimeType

    def mimeTypesForFileName(self, fileName): # real signature unknown; restored from __doc__
        """ mimeTypesForFileName(self, fileName: str) -> List[QMimeType] """
        return []

    def suffixForFileName(self, fileName): # real signature unknown; restored from __doc__
        """ suffixForFileName(self, fileName: str) -> str """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    MatchContent = 2
    MatchDefault = 0
    MatchExtension = 1


