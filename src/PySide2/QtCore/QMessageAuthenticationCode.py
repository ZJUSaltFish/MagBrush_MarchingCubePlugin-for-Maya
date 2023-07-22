# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QMessageAuthenticationCode(__Shiboken.Object):
    """ QMessageAuthenticationCode(self, method: PySide2.QtCore.QCryptographicHash.Algorithm, key: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None """
    def addData(self, data): # real signature unknown; restored from __doc__
        """
        addData(self, data: PySide2.QtCore.QByteArray) -> None
        addData(self, data: bytes, length: int) -> None
        addData(self, device: PySide2.QtCore.QIODevice) -> bool
        """
        pass

    def hash(self, message, key, method): # real signature unknown; restored from __doc__
        """ hash(message: PySide2.QtCore.QByteArray, key: PySide2.QtCore.QByteArray, method: PySide2.QtCore.QCryptographicHash.Algorithm) -> PySide2.QtCore.QByteArray """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> PySide2.QtCore.QByteArray """
        pass

    def setKey(self, key): # real signature unknown; restored from __doc__
        """ setKey(self, key: PySide2.QtCore.QByteArray) -> None """
        pass

    def __init__(self, method, key=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


