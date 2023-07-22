# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCryptographicHash(__Shiboken.Object):
    """ QCryptographicHash(self, method: PySide2.QtCore.QCryptographicHash.Algorithm) -> None """
    def addData(self, data): # real signature unknown; restored from __doc__
        """
        addData(self, data: PySide2.QtCore.QByteArray) -> None
        addData(self, data: bytes, length: int) -> None
        addData(self, device: PySide2.QtCore.QIODevice) -> bool
        """
        pass

    def hash(self, data, method): # real signature unknown; restored from __doc__
        """ hash(data: PySide2.QtCore.QByteArray, method: PySide2.QtCore.QCryptographicHash.Algorithm) -> PySide2.QtCore.QByteArray """
        pass

    def hashLength(self, method): # real signature unknown; restored from __doc__
        """ hashLength(method: PySide2.QtCore.QCryptographicHash.Algorithm) -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> PySide2.QtCore.QByteArray """
        pass

    def __init__(self, method): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Algorithm = None # (!) real value is "<class 'PySide2.QtCore.QCryptographicHash.Algorithm'>"
    Keccak_224 = PySide2.QtCore.QCryptographicHash.Algorithm.Keccak_224
    Keccak_256 = PySide2.QtCore.QCryptographicHash.Algorithm.Keccak_256
    Keccak_384 = PySide2.QtCore.QCryptographicHash.Algorithm.Keccak_384
    Keccak_512 = PySide2.QtCore.QCryptographicHash.Algorithm.Keccak_512
    Md4 = PySide2.QtCore.QCryptographicHash.Algorithm.Md4
    Md5 = PySide2.QtCore.QCryptographicHash.Algorithm.Md5
    RealSha3_224 = PySide2.QtCore.QCryptographicHash.Algorithm.RealSha3_224
    RealSha3_256 = PySide2.QtCore.QCryptographicHash.Algorithm.RealSha3_256
    RealSha3_384 = PySide2.QtCore.QCryptographicHash.Algorithm.RealSha3_384
    RealSha3_512 = PySide2.QtCore.QCryptographicHash.Algorithm.RealSha3_512
    Sha1 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha1
    Sha224 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha224
    Sha256 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha256
    Sha384 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha384
    Sha3_224 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha3_224
    Sha3_256 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha3_256
    Sha3_384 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha3_384
    Sha3_512 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha3_512
    Sha512 = PySide2.QtCore.QCryptographicHash.Algorithm.Sha512


