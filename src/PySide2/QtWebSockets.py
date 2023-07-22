# encoding: utf-8
# module PySide2.QtWebSockets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWebSockets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QMaskGenerator(__PySide2_QtCore.QObject):
    """ QMaskGenerator(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def destroyed(self, *args, **kwargs): # real signature unknown
        pass

    def nextMask(self): # real signature unknown; restored from __doc__
        """ nextMask(self) -> int """
        return 0

    def objectNameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def seed(self): # real signature unknown; restored from __doc__
        """ seed(self) -> bool """
        return False

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000212895CC280>'


class QWebSocket(__PySide2_QtCore.QObject):
    """ QWebSocket(self, origin: str = '', version: PySide2.QtWebSockets.QWebSocketProtocol.Version = PySide2.QtWebSockets.QWebSocketProtocol.Version.VersionLatest, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

    def aboutToClose(self, *args, **kwargs): # real signature unknown
        pass

    def binaryFrameReceived(self, *args, **kwargs): # real signature unknown
        pass

    def binaryMessageReceived(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def bytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, closeCode=None, reason=''): # real signature unknown; restored from __doc__
        """ close(self, closeCode: PySide2.QtWebSockets.QWebSocketProtocol.CloseCode = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeNormal, reason: str = '') -> None """
        pass

    def closeCode(self): # real signature unknown; restored from __doc__
        """ closeCode(self) -> PySide2.QtWebSockets.QWebSocketProtocol.CloseCode """
        pass

    def closeReason(self): # real signature unknown; restored from __doc__
        """ closeReason(self) -> str """
        return ""

    def connected(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def maskGenerator(self): # real signature unknown; restored from __doc__
        """ maskGenerator(self) -> PySide2.QtWebSockets.QMaskGenerator """
        pass

    def maxAllowedIncomingFrameSize(self): # real signature unknown; restored from __doc__
        """ maxAllowedIncomingFrameSize(self) -> int """
        return 0

    def maxAllowedIncomingMessageSize(self): # real signature unknown; restored from __doc__
        """ maxAllowedIncomingMessageSize(self) -> int """
        return 0

    def maxIncomingFrameSize(self): # real signature unknown; restored from __doc__
        """ maxIncomingFrameSize() -> int """
        return 0

    def maxIncomingMessageSize(self): # real signature unknown; restored from __doc__
        """ maxIncomingMessageSize() -> int """
        return 0

    def maxOutgoingFrameSize(self): # real signature unknown; restored from __doc__
        """ maxOutgoingFrameSize() -> int """
        return 0

    def open(self, request): # real signature unknown; restored from __doc__
        """
        open(self, request: PySide2.QtNetwork.QNetworkRequest) -> None
        open(self, url: PySide2.QtCore.QUrl) -> None
        """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> str """
        return ""

    def outgoingFrameSize(self): # real signature unknown; restored from __doc__
        """ outgoingFrameSize(self) -> int """
        return 0

    def pauseMode(self): # real signature unknown; restored from __doc__
        """ pauseMode(self) -> PySide2.QtNetwork.QAbstractSocket.PauseModes """
        pass

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ peerAddress(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def peerName(self): # real signature unknown; restored from __doc__
        """ peerName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def ping(self, payload=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ping(self, payload: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None """
        pass

    def pong(self, *args, **kwargs): # real signature unknown
        pass

    def preSharedKeyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> PySide2.QtNetwork.QNetworkProxy """
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readChannelFinished(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> PySide2.QtNetwork.QNetworkRequest """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def resourceName(self): # real signature unknown; restored from __doc__
        """ resourceName(self) -> str """
        return ""

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def sendBinaryMessage(self, data): # real signature unknown; restored from __doc__
        """ sendBinaryMessage(self, data: PySide2.QtCore.QByteArray) -> int """
        return 0

    def sendTextMessage(self, message): # real signature unknown; restored from __doc__
        """ sendTextMessage(self, message: str) -> int """
        return 0

    def setMaskGenerator(self, maskGenerator): # real signature unknown; restored from __doc__
        """ setMaskGenerator(self, maskGenerator: PySide2.QtWebSockets.QMaskGenerator) -> None """
        pass

    def setMaxAllowedIncomingFrameSize(self, maxAllowedIncomingFrameSize): # real signature unknown; restored from __doc__
        """ setMaxAllowedIncomingFrameSize(self, maxAllowedIncomingFrameSize: int) -> None """
        pass

    def setMaxAllowedIncomingMessageSize(self, maxAllowedIncomingMessageSize): # real signature unknown; restored from __doc__
        """ setMaxAllowedIncomingMessageSize(self, maxAllowedIncomingMessageSize: int) -> None """
        pass

    def setOutgoingFrameSize(self, outgoingFrameSize): # real signature unknown; restored from __doc__
        """ setOutgoingFrameSize(self, outgoingFrameSize: int) -> None """
        pass

    def setPauseMode(self, pauseMode): # real signature unknown; restored from __doc__
        """ setPauseMode(self, pauseMode: PySide2.QtNetwork.QAbstractSocket.PauseModes) -> None """
        pass

    def setProxy(self, networkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, networkProxy: PySide2.QtNetwork.QNetworkProxy) -> None """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) -> None """
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtNetwork.QAbstractSocket.SocketState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textFrameReceived(self, *args, **kwargs): # real signature unknown
        pass

    def textMessageReceived(self, *args, **kwargs): # real signature unknown
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> PySide2.QtWebSockets.QWebSocketProtocol.Version """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, origin='', version=None, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000212895CC600>'


class QWebSocketCorsAuthenticator(__Shiboken.Object):
    """
    QWebSocketCorsAuthenticator(self, origin: str) -> None
    QWebSocketCorsAuthenticator(self, other: PySide2.QtWebSockets.QWebSocketCorsAuthenticator) -> None
    """
    def allowed(self): # real signature unknown; restored from __doc__
        """ allowed(self) -> bool """
        return False

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> str """
        return ""

    def setAllowed(self, allowed): # real signature unknown; restored from __doc__
        """ setAllowed(self, allowed: bool) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtWebSockets.QWebSocketCorsAuthenticator) -> None """
        pass

    def __init__(self, origin): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWebSocketProtocol(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CloseCode = None # (!) real value is "<class 'PySide2.QtWebSockets.QWebSocketProtocol.CloseCode'>"
    CloseCodeAbnormalDisconnection = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeAbnormalDisconnection
    CloseCodeBadOperation = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeBadOperation
    CloseCodeDatatypeNotSupported = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeDatatypeNotSupported
    CloseCodeGoingAway = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeGoingAway
    CloseCodeMissingExtension = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeMissingExtension
    CloseCodeMissingStatusCode = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeMissingStatusCode
    CloseCodeNormal = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeNormal
    CloseCodePolicyViolated = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodePolicyViolated
    CloseCodeProtocolError = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeProtocolError
    CloseCodeReserved1004 = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeReserved1004
    CloseCodeTlsHandshakeFailed = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeTlsHandshakeFailed
    CloseCodeTooMuchData = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeTooMuchData
    CloseCodeWrongDatatype = PySide2.QtWebSockets.QWebSocketProtocol.CloseCode.CloseCodeWrongDatatype
    Version = None # (!) real value is "<class 'PySide2.QtWebSockets.QWebSocketProtocol.Version'>"
    Version0 = PySide2.QtWebSockets.QWebSocketProtocol.Version.Version0
    Version13 = PySide2.QtWebSockets.QWebSocketProtocol.Version.Version13
    Version4 = PySide2.QtWebSockets.QWebSocketProtocol.Version.Version4
    Version5 = PySide2.QtWebSockets.QWebSocketProtocol.Version.Version5
    Version6 = PySide2.QtWebSockets.QWebSocketProtocol.Version.Version6
    Version7 = PySide2.QtWebSockets.QWebSocketProtocol.Version.Version7
    Version8 = PySide2.QtWebSockets.QWebSocketProtocol.Version.Version8
    VersionLatest = PySide2.QtWebSockets.QWebSocketProtocol.Version.VersionLatest
    VersionUnknown = PySide2.QtWebSockets.QWebSocketProtocol.Version.VersionUnknown


class QWebSocketServer(__PySide2_QtCore.QObject):
    """ QWebSocketServer(self, serverName: str, secureMode: PySide2.QtWebSockets.QWebSocketServer.SslMode, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def acceptError(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def closed(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtWebSockets.QWebSocketProtocol.CloseCode """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def handleConnection(self, socket): # real signature unknown; restored from __doc__
        """ handleConnection(self, socket: PySide2.QtNetwork.QTcpSocket) -> None """
        pass

    def handshakeTimeoutMS(self): # real signature unknown; restored from __doc__
        """ handshakeTimeoutMS(self) -> int """
        return 0

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def listen(self, address=None, port=0): # real signature unknown; restored from __doc__
        """ listen(self, address: PySide2.QtNetwork.QHostAddress = PySide2.QtNetwork.QHostAddress.SpecialAddress.Any, port: int = 0) -> bool """
        return False

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def nativeDescriptor(self): # real signature unknown; restored from __doc__
        """ nativeDescriptor(self) -> int """
        return 0

    def newConnection(self, *args, **kwargs): # real signature unknown
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> PySide2.QtWebSockets.QWebSocket """
        pass

    def originAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def pauseAccepting(self): # real signature unknown; restored from __doc__
        """ pauseAccepting(self) -> None """
        pass

    def peerVerifyError(self, *args, **kwargs): # real signature unknown
        pass

    def preSharedKeyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> PySide2.QtNetwork.QNetworkProxy """
        pass

    def resumeAccepting(self): # real signature unknown; restored from __doc__
        """ resumeAccepting(self) -> None """
        pass

    def secureMode(self): # real signature unknown; restored from __doc__
        """ secureMode(self) -> PySide2.QtWebSockets.QWebSocketServer.SslMode """
        pass

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ serverAddress(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def serverError(self, *args, **kwargs): # real signature unknown
        pass

    def serverName(self): # real signature unknown; restored from __doc__
        """ serverName(self) -> str """
        return ""

    def serverPort(self): # real signature unknown; restored from __doc__
        """ serverPort(self) -> int """
        return 0

    def serverUrl(self): # real signature unknown; restored from __doc__
        """ serverUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def setHandshakeTimeout(self, msec): # real signature unknown; restored from __doc__
        """ setHandshakeTimeout(self, msec: int) -> None """
        pass

    def setMaxPendingConnections(self, numConnections): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, numConnections: int) -> None """
        pass

    def setNativeDescriptor(self, descriptor): # real signature unknown; restored from __doc__
        """ setNativeDescriptor(self, descriptor: int) -> bool """
        return False

    def setProxy(self, networkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, networkProxy: PySide2.QtNetwork.QNetworkProxy) -> None """
        pass

    def setServerName(self, serverName): # real signature unknown; restored from __doc__
        """ setServerName(self, serverName: str) -> None """
        pass

    def setSocketDescriptor(self, socketDescriptor): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, socketDescriptor: int) -> bool """
        return False

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

    def sslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def supportedVersions(self): # real signature unknown; restored from __doc__
        """ supportedVersions(self) -> typing.List[PySide2.QtWebSockets.QWebSocketProtocol.Version] """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, serverName, secureMode, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    NonSecureMode = PySide2.QtWebSockets.QWebSocketServer.SslMode.NonSecureMode
    SecureMode = PySide2.QtWebSockets.QWebSocketServer.SslMode.SecureMode
    SslMode = None # (!) real value is "<class 'PySide2.QtWebSockets.QWebSocketServer.SslMode'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000212895CC080>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000212889A17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtWebSockets', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000212889A17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtWebSockets.cp310-win_amd64.pyd')"

