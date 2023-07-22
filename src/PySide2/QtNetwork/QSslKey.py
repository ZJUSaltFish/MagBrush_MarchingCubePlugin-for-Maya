# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSslKey(__Shiboken.Object):
    """
    QSslKey(self) -> None
    QSslKey(self, device: PySide2.QtCore.QIODevice, algorithm: PySide2.QtNetwork.QSsl.KeyAlgorithm, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem, type: PySide2.QtNetwork.QSsl.KeyType = PySide2.QtNetwork.QSsl.KeyType.PrivateKey, passPhrase: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None
    QSslKey(self, encoded: PySide2.QtCore.QByteArray, algorithm: PySide2.QtNetwork.QSsl.KeyAlgorithm, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem, type: PySide2.QtNetwork.QSsl.KeyType = PySide2.QtNetwork.QSsl.KeyType.PrivateKey, passPhrase: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None
    QSslKey(self, handle: int, type: PySide2.QtNetwork.QSsl.KeyType = PySide2.QtNetwork.QSsl.KeyType.PrivateKey) -> None
    QSslKey(self, other: PySide2.QtNetwork.QSslKey) -> None
    """
    def algorithm(self): # real signature unknown; restored from __doc__
        """ algorithm(self) -> PySide2.QtNetwork.QSsl.KeyAlgorithm """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QSslKey) -> None """
        pass

    def toDer(self, passPhrase=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toDer(self, passPhrase: PySide2.QtCore.QByteArray = Default(QByteArray)) -> PySide2.QtCore.QByteArray """
        pass

    def toPem(self, passPhrase=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toPem(self, passPhrase: PySide2.QtCore.QByteArray = Default(QByteArray)) -> PySide2.QtCore.QByteArray """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtNetwork.QSsl.KeyType """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __hash__ = None


