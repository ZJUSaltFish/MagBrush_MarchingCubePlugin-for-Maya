# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QFileDevice import QFileDevice

class QSaveFile(QFileDevice):
    """
    QSaveFile(self, name: str) -> None
    QSaveFile(self, name: str, parent: PySide2.QtCore.QObject) -> None
    QSaveFile(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def cancelWriting(self): # real signature unknown; restored from __doc__
        """ cancelWriting(self) -> None """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit(self) -> bool """
        return False

    def directWriteFallback(self): # real signature unknown; restored from __doc__
        """ directWriteFallback(self) -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def open(self, flags): # real signature unknown; restored from __doc__
        """ open(self, flags: PySide2.QtCore.QIODevice.OpenMode) -> bool """
        return False

    def setDirectWriteFallback(self, enabled): # real signature unknown; restored from __doc__
        """ setDirectWriteFallback(self, enabled: bool) -> None """
        pass

    def setFileName(self, name): # real signature unknown; restored from __doc__
        """ setFileName(self, name: str) -> None """
        pass

    def writeData(self, data, len): # real signature unknown; restored from __doc__
        """ writeData(self, data: bytes, len: int) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, name): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DEFD00>'


