# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QDtls(__PySide2_QtCore.QObject):
    """ QDtls(self, mode: PySide2.QtNetwork.QSslSocket.SslMode, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def abortHandshake(self, socket): # real signature unknown; restored from __doc__
        """ abortHandshake(self, socket: PySide2.QtNetwork.QUdpSocket) -> bool """
        return False

    def decryptDatagram(self, socket, dgram): # real signature unknown; restored from __doc__
        """ decryptDatagram(self, socket: PySide2.QtNetwork.QUdpSocket, dgram: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray """
        pass

    def doHandshake(self, socket, dgram={}): # real signature unknown; restored from __doc__
        """ doHandshake(self, socket: PySide2.QtNetwork.QUdpSocket, dgram: PySide2.QtCore.QByteArray = {}) -> bool """
        return False

    def dtlsConfiguration(self): # real signature unknown; restored from __doc__
        """ dtlsConfiguration(self) -> PySide2.QtNetwork.QSslConfiguration """
        pass

    def dtlsError(self): # real signature unknown; restored from __doc__
        """ dtlsError(self) -> PySide2.QtNetwork.QDtlsError """
        pass

    def dtlsErrorString(self): # real signature unknown; restored from __doc__
        """ dtlsErrorString(self) -> str """
        return ""

    def handleTimeout(self, socket): # real signature unknown; restored from __doc__
        """ handleTimeout(self, socket: PySide2.QtNetwork.QUdpSocket) -> bool """
        return False

    def handshakeState(self): # real signature unknown; restored from __doc__
        """ handshakeState(self) -> PySide2.QtNetwork.QDtls.HandshakeState """
        pass

    def handshakeTimeout(self, *args, **kwargs): # real signature unknown
        pass

    def ignoreVerificationErrors(self, errorsToIgnore, PySide2_QtNetwork_QSslError=None): # real signature unknown; restored from __doc__
        """ ignoreVerificationErrors(self, errorsToIgnore: typing.List[PySide2.QtNetwork.QSslError]) -> None """
        pass

    def isConnectionEncrypted(self): # real signature unknown; restored from __doc__
        """ isConnectionEncrypted(self) -> bool """
        return False

    def mtuHint(self): # real signature unknown; restored from __doc__
        """ mtuHint(self) -> int """
        return 0

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ peerAddress(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def peerVerificationErrors(self): # real signature unknown; restored from __doc__
        """ peerVerificationErrors(self) -> typing.List[PySide2.QtNetwork.QSslError] """
        pass

    def peerVerificationName(self): # real signature unknown; restored from __doc__
        """ peerVerificationName(self) -> str """
        return ""

    def pskRequired(self, *args, **kwargs): # real signature unknown
        pass

    def resumeHandshake(self, socket): # real signature unknown; restored from __doc__
        """ resumeHandshake(self, socket: PySide2.QtNetwork.QUdpSocket) -> bool """
        return False

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ sessionCipher(self) -> PySide2.QtNetwork.QSslCipher """
        pass

    def sessionProtocol(self): # real signature unknown; restored from __doc__
        """ sessionProtocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol """
        pass

    def setDtlsConfiguration(self, configuration): # real signature unknown; restored from __doc__
        """ setDtlsConfiguration(self, configuration: PySide2.QtNetwork.QSslConfiguration) -> bool """
        return False

    def setMtuHint(self, mtuHint): # real signature unknown; restored from __doc__
        """ setMtuHint(self, mtuHint: int) -> None """
        pass

    def setPeer(self, address, port, verificationName={}): # real signature unknown; restored from __doc__
        """ setPeer(self, address: PySide2.QtNetwork.QHostAddress, port: int, verificationName: str = {}) -> bool """
        return False

    def setPeerVerificationName(self, name): # real signature unknown; restored from __doc__
        """ setPeerVerificationName(self, name: str) -> bool """
        return False

    def shutdown(self, socket): # real signature unknown; restored from __doc__
        """ shutdown(self, socket: PySide2.QtNetwork.QUdpSocket) -> bool """
        return False

    def sslMode(self): # real signature unknown; restored from __doc__
        """ sslMode(self) -> PySide2.QtNetwork.QSslSocket.SslMode """
        pass

    def writeDatagramEncrypted(self, socket, dgram): # real signature unknown; restored from __doc__
        """ writeDatagramEncrypted(self, socket: PySide2.QtNetwork.QUdpSocket, dgram: PySide2.QtCore.QByteArray) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, mode, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    HandshakeComplete = PySide2.QtNetwork.QDtls.HandshakeState.HandshakeComplete
    HandshakeInProgress = PySide2.QtNetwork.QDtls.HandshakeState.HandshakeInProgress
    HandshakeNotStarted = PySide2.QtNetwork.QDtls.HandshakeState.HandshakeNotStarted
    HandshakeState = None # (!) real value is "<class 'PySide2.QtNetwork.QDtls.HandshakeState'>"
    PeerVerificationFailed = PySide2.QtNetwork.QDtls.HandshakeState.PeerVerificationFailed
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D88EA00>'


