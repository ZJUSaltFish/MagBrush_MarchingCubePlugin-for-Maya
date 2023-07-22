# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QIODevice import QIODevice

class QBuffer(QIODevice):
    """
    QBuffer(self, buf: PySide2.QtCore.QByteArray, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QBuffer(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def buffer(self): # real signature unknown; restored from __doc__
        """ buffer(self) -> PySide2.QtCore.QByteArray """
        pass

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def connectNotify(self, arg__1): # real signature unknown; restored from __doc__
        """ connectNotify(self, arg__1: PySide2.QtCore.QMetaMethod) -> None """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> PySide2.QtCore.QByteArray """
        pass

    def disconnectNotify(self, arg__1): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, arg__1: PySide2.QtCore.QMetaMethod) -> None """
        pass

    def open(self, openMode): # real signature unknown; restored from __doc__
        """ open(self, openMode: PySide2.QtCore.QIODevice.OpenMode) -> bool """
        return False

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def readData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, data: bytes, maxlen: int) -> int """
        return 0

    def seek(self, off): # real signature unknown; restored from __doc__
        """ seek(self, off: int) -> bool """
        return False

    def setBuffer(self, a): # real signature unknown; restored from __doc__
        """ setBuffer(self, a: PySide2.QtCore.QByteArray) -> None """
        pass

    def setData(self, data): # real signature unknown; restored from __doc__
        """ setData(self, data: PySide2.QtCore.QByteArray) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def writeData(self, data, len): # real signature unknown; restored from __doc__
        """ writeData(self, data: bytes, len: int) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, buf, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E3EA80>'


