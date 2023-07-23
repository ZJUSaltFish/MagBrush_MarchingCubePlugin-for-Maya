# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCborStreamWriter(__Shiboken.Object):
    """
    QCborStreamWriter(self, data: PySide2.QtCore.QByteArray) -> None
    QCborStreamWriter(self, device: PySide2.QtCore.QIODevice) -> None
    """
    def append(self, b): # real signature unknown; restored from __doc__
        """
        append(self, b: bool) -> None
        append(self, ba: PySide2.QtCore.QByteArray) -> None
        append(self, d: float) -> None
        append(self, f: float) -> None
        append(self, i: int) -> None
        append(self, i: int) -> None
        append(self, st: PySide2.QtCore.QCborSimpleType) -> None
        append(self, str: bytes, size: int = -1) -> None
        append(self, tag: PySide2.QtCore.QCborKnownTags) -> None
        append(self, u: int) -> None
        append(self, u: int) -> None
        """
        pass

    def appendByteString(self, data, len): # real signature unknown; restored from __doc__
        """ appendByteString(self, data: bytes, len: int) -> None """
        pass

    def appendNull(self): # real signature unknown; restored from __doc__
        """ appendNull(self) -> None """
        pass

    def appendTextString(self, utf8, len): # real signature unknown; restored from __doc__
        """ appendTextString(self, utf8: bytes, len: int) -> None """
        pass

    def appendUndefined(self): # real signature unknown; restored from __doc__
        """ appendUndefined(self) -> None """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ endArray(self) -> bool """
        return False

    def endMap(self): # real signature unknown; restored from __doc__
        """ endMap(self) -> bool """
        return False

    def setDevice(self, device): # real signature unknown; restored from __doc__
        """ setDevice(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def startArray(self): # real signature unknown; restored from __doc__
        """
        startArray(self) -> None
        startArray(self, count: int) -> None
        """
        pass

    def startMap(self): # real signature unknown; restored from __doc__
        """
        startMap(self) -> None
        startMap(self, count: int) -> None
        """
        pass

    def __init__(self, data): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


