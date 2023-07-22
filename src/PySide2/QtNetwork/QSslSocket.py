# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QTcpSocket import QTcpSocket

class QSslSocket(QTcpSocket):
    """ QSslSocket(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

    def addCaCertificate(self, certificate): # real signature unknown; restored from __doc__
        """ addCaCertificate(self, certificate: PySide2.QtNetwork.QSslCertificate) -> None """
        pass

    def addCaCertificates(self, certificates, PySide2_QtNetwork_QSslCertificate=None): # real signature unknown; restored from __doc__
        """
        addCaCertificates(self, certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
        addCaCertificates(self, path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem, syntax: PySide2.QtCore.QRegExp.PatternSyntax = PySide2.QtCore.QRegExp.PatternSyntax.FixedString) -> bool
        """
        pass

    def addDefaultCaCertificate(self, certificate): # real signature unknown; restored from __doc__
        """ addDefaultCaCertificate(certificate: PySide2.QtNetwork.QSslCertificate) -> None """
        pass

    def addDefaultCaCertificates(self, certificates, PySide2_QtNetwork_QSslCertificate=None): # real signature unknown; restored from __doc__
        """
        addDefaultCaCertificates(certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
        addDefaultCaCertificates(path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem, syntax: PySide2.QtCore.QRegExp.PatternSyntax = PySide2.QtCore.QRegExp.PatternSyntax.FixedString) -> bool
        """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def caCertificates(self): # real signature unknown; restored from __doc__
        """ caCertificates(self) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def ciphers(self): # real signature unknown; restored from __doc__
        """ ciphers(self) -> typing.List[PySide2.QtNetwork.QSslCipher] """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def connectToHost(self, address, port, mode=None): # real signature unknown; restored from __doc__
        """
        connectToHost(self, address: PySide2.QtNetwork.QHostAddress, port: int, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> None
        connectToHost(self, hostName: str, port: int, openMode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite, protocol: PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol = PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol) -> None
        """
        pass

    def connectToHostEncrypted(self, hostName, port, mode=None, protocol=None): # real signature unknown; restored from __doc__
        """
        connectToHostEncrypted(self, hostName: str, port: int, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite, protocol: PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol = PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol) -> None
        connectToHostEncrypted(self, hostName: str, port: int, sslPeerName: str, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite, protocol: PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol = PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol) -> None
        """
        pass

    def defaultCaCertificates(self): # real signature unknown; restored from __doc__
        """ defaultCaCertificates() -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def defaultCiphers(self): # real signature unknown; restored from __doc__
        """ defaultCiphers() -> typing.List[PySide2.QtNetwork.QSslCipher] """
        pass

    def disconnectFromHost(self): # real signature unknown; restored from __doc__
        """ disconnectFromHost(self) -> None """
        pass

    def encrypted(self, *args, **kwargs): # real signature unknown
        pass

    def encryptedBytesAvailable(self): # real signature unknown; restored from __doc__
        """ encryptedBytesAvailable(self) -> int """
        return 0

    def encryptedBytesToWrite(self): # real signature unknown; restored from __doc__
        """ encryptedBytesToWrite(self) -> int """
        return 0

    def encryptedBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def ignoreSslErrors(self): # real signature unknown; restored from __doc__
        """
        ignoreSslErrors(self) -> None
        ignoreSslErrors(self, errors: typing.Sequence[PySide2.QtNetwork.QSslError]) -> None
        """
        pass

    def isEncrypted(self): # real signature unknown; restored from __doc__
        """ isEncrypted(self) -> bool """
        return False

    def localCertificate(self): # real signature unknown; restored from __doc__
        """ localCertificate(self) -> PySide2.QtNetwork.QSslCertificate """
        pass

    def localCertificateChain(self): # real signature unknown; restored from __doc__
        """ localCertificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> PySide2.QtNetwork.QSslSocket.SslMode """
        pass

    def modeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def newSessionTicketReceived(self, *args, **kwargs): # real signature unknown
        pass

    def ocspResponses(self): # real signature unknown; restored from __doc__
        """ ocspResponses(self) -> typing.List[PySide2.QtNetwork.QOcspResponse] """
        pass

    def peerCertificate(self): # real signature unknown; restored from __doc__
        """ peerCertificate(self) -> PySide2.QtNetwork.QSslCertificate """
        pass

    def peerCertificateChain(self): # real signature unknown; restored from __doc__
        """ peerCertificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def peerVerifyDepth(self): # real signature unknown; restored from __doc__
        """ peerVerifyDepth(self) -> int """
        return 0

    def peerVerifyError(self, *args, **kwargs): # real signature unknown
        pass

    def peerVerifyMode(self): # real signature unknown; restored from __doc__
        """ peerVerifyMode(self) -> PySide2.QtNetwork.QSslSocket.PeerVerifyMode """
        pass

    def peerVerifyName(self): # real signature unknown; restored from __doc__
        """ peerVerifyName(self) -> str """
        return ""

    def preSharedKeyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def privateKey(self): # real signature unknown; restored from __doc__
        """ privateKey(self) -> PySide2.QtNetwork.QSslKey """
        pass

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol """
        pass

    def readData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, data: bytes, maxlen: int) -> int """
        return 0

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ sessionCipher(self) -> PySide2.QtNetwork.QSslCipher """
        pass

    def sessionProtocol(self): # real signature unknown; restored from __doc__
        """ sessionProtocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol """
        pass

    def setCaCertificates(self, certificates, PySide2_QtNetwork_QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setCaCertificates(self, certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None """
        pass

    def setCiphers(self, ciphers, PySide2_QtNetwork_QSslCipher=None): # real signature unknown; restored from __doc__
        """
        setCiphers(self, ciphers: typing.Sequence[PySide2.QtNetwork.QSslCipher]) -> None
        setCiphers(self, ciphers: str) -> None
        """
        pass

    def setDefaultCaCertificates(self, certificates, PySide2_QtNetwork_QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setDefaultCaCertificates(certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None """
        pass

    def setDefaultCiphers(self, ciphers, PySide2_QtNetwork_QSslCipher=None): # real signature unknown; restored from __doc__
        """ setDefaultCiphers(ciphers: typing.Sequence[PySide2.QtNetwork.QSslCipher]) -> None """
        pass

    def setLocalCertificate(self, certificate): # real signature unknown; restored from __doc__
        """
        setLocalCertificate(self, certificate: PySide2.QtNetwork.QSslCertificate) -> None
        setLocalCertificate(self, fileName: str, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem) -> None
        """
        pass

    def setLocalCertificateChain(self, localChain, PySide2_QtNetwork_QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setLocalCertificateChain(self, localChain: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None """
        pass

    def setPeerVerifyDepth(self, depth): # real signature unknown; restored from __doc__
        """ setPeerVerifyDepth(self, depth: int) -> None """
        pass

    def setPeerVerifyMode(self, mode): # real signature unknown; restored from __doc__
        """ setPeerVerifyMode(self, mode: PySide2.QtNetwork.QSslSocket.PeerVerifyMode) -> None """
        pass

    def setPeerVerifyName(self, hostName): # real signature unknown; restored from __doc__
        """ setPeerVerifyName(self, hostName: str) -> None """
        pass

    def setPrivateKey(self, fileName, algorithm=None, format=None, passPhrase=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        setPrivateKey(self, fileName: str, algorithm: PySide2.QtNetwork.QSsl.KeyAlgorithm = PySide2.QtNetwork.QSsl.KeyAlgorithm.Rsa, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem, passPhrase: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None
        setPrivateKey(self, key: PySide2.QtNetwork.QSslKey) -> None
        """
        pass

    def setProtocol(self, protocol): # real signature unknown; restored from __doc__
        """ setProtocol(self, protocol: PySide2.QtNetwork.QSsl.SslProtocol) -> None """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) -> None """
        pass

    def setSocketDescriptor(self, socketDescriptor, state=None, openMode=None): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, socketDescriptor: int, state: PySide2.QtNetwork.QAbstractSocket.SocketState = PySide2.QtNetwork.QAbstractSocket.SocketState.ConnectedState, openMode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> bool """
        return False

    def setSocketOption(self, option, value): # real signature unknown; restored from __doc__
        """ setSocketOption(self, option: PySide2.QtNetwork.QAbstractSocket.SocketOption, value: typing.Any) -> None """
        pass

    def setSslConfiguration(self, config): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, config: PySide2.QtNetwork.QSslConfiguration) -> None """
        pass

    def socketOption(self, option): # real signature unknown; restored from __doc__
        """ socketOption(self, option: PySide2.QtNetwork.QAbstractSocket.SocketOption) -> typing.Any """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> PySide2.QtNetwork.QSslConfiguration """
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def sslErrors.overload(self, *args, **kwargs): # real signature unknown
        """ sslErrors(self) -> typing.List[PySide2.QtNetwork.QSslError] """
        pass

    def sslHandshakeErrors(self): # real signature unknown; restored from __doc__
        """ sslHandshakeErrors(self) -> typing.List[PySide2.QtNetwork.QSslError] """
        pass

    def sslLibraryBuildVersionNumber(self): # real signature unknown; restored from __doc__
        """ sslLibraryBuildVersionNumber() -> int """
        return 0

    def sslLibraryBuildVersionString(self): # real signature unknown; restored from __doc__
        """ sslLibraryBuildVersionString() -> str """
        return ""

    def sslLibraryVersionNumber(self): # real signature unknown; restored from __doc__
        """ sslLibraryVersionNumber() -> int """
        return 0

    def sslLibraryVersionString(self): # real signature unknown; restored from __doc__
        """ sslLibraryVersionString() -> str """
        return ""

    def startClientEncryption(self): # real signature unknown; restored from __doc__
        """ startClientEncryption(self) -> None """
        pass

    def startServerEncryption(self): # real signature unknown; restored from __doc__
        """ startServerEncryption(self) -> None """
        pass

    def supportedCiphers(self): # real signature unknown; restored from __doc__
        """ supportedCiphers() -> typing.List[PySide2.QtNetwork.QSslCipher] """
        pass

    def supportsSsl(self): # real signature unknown; restored from __doc__
        """ supportsSsl() -> bool """
        return False

    def systemCaCertificates(self): # real signature unknown; restored from __doc__
        """ systemCaCertificates() -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForConnected(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForConnected(self, msecs: int = 30000) -> bool """
        return False

    def waitForDisconnected(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForDisconnected(self, msecs: int = 30000) -> bool """
        return False

    def waitForEncrypted(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForEncrypted(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, data, len): # real signature unknown; restored from __doc__
        """ writeData(self, data: bytes, len: int) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AutoVerifyPeer = PySide2.QtNetwork.QSslSocket.PeerVerifyMode.AutoVerifyPeer
    PeerVerifyMode = None # (!) real value is "<class 'PySide2.QtNetwork.QSslSocket.PeerVerifyMode'>"
    QueryPeer = PySide2.QtNetwork.QSslSocket.PeerVerifyMode.QueryPeer
    SslClientMode = PySide2.QtNetwork.QSslSocket.SslMode.SslClientMode
    SslMode = None # (!) real value is "<class 'PySide2.QtNetwork.QSslSocket.SslMode'>"
    SslServerMode = PySide2.QtNetwork.QSslSocket.SslMode.SslServerMode
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D88E140>'
    UnencryptedMode = PySide2.QtNetwork.QSslSocket.SslMode.UnencryptedMode
    VerifyNone = PySide2.QtNetwork.QSslSocket.PeerVerifyMode.VerifyNone
    VerifyPeer = PySide2.QtNetwork.QSslSocket.PeerVerifyMode.VerifyPeer


