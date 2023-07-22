# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAbstractSocket(__PySide2_QtCore.QIODevice):
    """ QAbstractSocket(self, socketType: PySide2.QtNetwork.QAbstractSocket.SocketType, parent: PySide2.QtCore.QObject) -> None """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bind(self, address, port=0, mode=None): # real signature unknown; restored from __doc__
        """
        bind(self, address: PySide2.QtNetwork.QHostAddress, port: int = 0, mode: PySide2.QtNetwork.QAbstractSocket.BindMode = PySide2.QtNetwork.QAbstractSocket.BindFlag.DefaultForPlatform) -> bool
        bind(self, port: int = 0, mode: PySide2.QtNetwork.QAbstractSocket.BindMode = PySide2.QtNetwork.QAbstractSocket.BindFlag.DefaultForPlatform) -> bool
        """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def connected(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHost(self, address, port, mode=None): # real signature unknown; restored from __doc__
        """
        connectToHost(self, address: PySide2.QtNetwork.QHostAddress, port: int, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> None
        connectToHost(self, hostName: str, port: int, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite, protocol: PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol = PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol) -> None
        """
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectFromHost(self): # real signature unknown; restored from __doc__
        """ disconnectFromHost(self) -> None """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError """
        pass

    def errorOccurred(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def hostFound(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
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

    def protocolTag(self): # real signature unknown; restored from __doc__
        """ protocolTag(self) -> str """
        return ""

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> PySide2.QtNetwork.QNetworkProxy """
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, data: bytes, maxlen: int) -> int """
        return 0

    def readLineData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readLineData(self, data: bytes, maxlen: int) -> int """
        return 0

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def setLocalAddress(self, address): # real signature unknown; restored from __doc__
        """ setLocalAddress(self, address: PySide2.QtNetwork.QHostAddress) -> None """
        pass

    def setLocalPort(self, port): # real signature unknown; restored from __doc__
        """ setLocalPort(self, port: int) -> None """
        pass

    def setPauseMode(self, pauseMode): # real signature unknown; restored from __doc__
        """ setPauseMode(self, pauseMode: PySide2.QtNetwork.QAbstractSocket.PauseModes) -> None """
        pass

    def setPeerAddress(self, address): # real signature unknown; restored from __doc__
        """ setPeerAddress(self, address: PySide2.QtNetwork.QHostAddress) -> None """
        pass

    def setPeerName(self, name): # real signature unknown; restored from __doc__
        """ setPeerName(self, name: str) -> None """
        pass

    def setPeerPort(self, port): # real signature unknown; restored from __doc__
        """ setPeerPort(self, port: int) -> None """
        pass

    def setProtocolTag(self, tag): # real signature unknown; restored from __doc__
        """ setProtocolTag(self, tag: str) -> None """
        pass

    def setProxy(self, networkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, networkProxy: PySide2.QtNetwork.QNetworkProxy) -> None """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) -> None """
        pass

    def setSocketDescriptor(self, socketDescriptor, state=None, openMode=None): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, socketDescriptor: int, state: PySide2.QtNetwork.QAbstractSocket.SocketState = PySide2.QtNetwork.QAbstractSocket.SocketState.ConnectedState, openMode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> bool """
        return False

    def setSocketError(self, socketError): # real signature unknown; restored from __doc__
        """ setSocketError(self, socketError: PySide2.QtNetwork.QAbstractSocket.SocketError) -> None """
        pass

    def setSocketOption(self, option, value): # real signature unknown; restored from __doc__
        """ setSocketOption(self, option: PySide2.QtNetwork.QAbstractSocket.SocketOption, value: typing.Any) -> None """
        pass

    def setSocketState(self, state): # real signature unknown; restored from __doc__
        """ setSocketState(self, state: PySide2.QtNetwork.QAbstractSocket.SocketState) -> None """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

    def socketOption(self, option): # real signature unknown; restored from __doc__
        """ socketOption(self, option: PySide2.QtNetwork.QAbstractSocket.SocketOption) -> typing.Any """
        pass

    def socketType(self): # real signature unknown; restored from __doc__
        """ socketType(self) -> PySide2.QtNetwork.QAbstractSocket.SocketType """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtNetwork.QAbstractSocket.SocketState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
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

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, data, len): # real signature unknown; restored from __doc__
        """ writeData(self, data: bytes, len: int) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, socketType, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AddressInUseError = PySide2.QtNetwork.QAbstractSocket.SocketError.AddressInUseError
    AnyIPProtocol = PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol
    BindFlag = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.BindFlag'>"
    BindMode = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.BindMode'>"
    BoundState = PySide2.QtNetwork.QAbstractSocket.SocketState.BoundState
    ClosingState = PySide2.QtNetwork.QAbstractSocket.SocketState.ClosingState
    ConnectedState = PySide2.QtNetwork.QAbstractSocket.SocketState.ConnectedState
    ConnectingState = PySide2.QtNetwork.QAbstractSocket.SocketState.ConnectingState
    ConnectionRefusedError = PySide2.QtNetwork.QAbstractSocket.SocketError.ConnectionRefusedError
    DatagramTooLargeError = PySide2.QtNetwork.QAbstractSocket.SocketError.DatagramTooLargeError
    DefaultForPlatform = PySide2.QtNetwork.QAbstractSocket.BindFlag.DefaultForPlatform
    DontShareAddress = PySide2.QtNetwork.QAbstractSocket.BindFlag.DontShareAddress
    HostLookupState = PySide2.QtNetwork.QAbstractSocket.SocketState.HostLookupState
    HostNotFoundError = PySide2.QtNetwork.QAbstractSocket.SocketError.HostNotFoundError
    IPv4Protocol = PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv4Protocol
    IPv6Protocol = PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv6Protocol
    KeepAliveOption = PySide2.QtNetwork.QAbstractSocket.SocketOption.KeepAliveOption
    ListeningState = PySide2.QtNetwork.QAbstractSocket.SocketState.ListeningState
    LowDelayOption = PySide2.QtNetwork.QAbstractSocket.SocketOption.LowDelayOption
    MulticastLoopbackOption = PySide2.QtNetwork.QAbstractSocket.SocketOption.MulticastLoopbackOption
    MulticastTtlOption = PySide2.QtNetwork.QAbstractSocket.SocketOption.MulticastTtlOption
    NetworkError = PySide2.QtNetwork.QAbstractSocket.SocketError.NetworkError
    NetworkLayerProtocol = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol'>"
    OperationError = PySide2.QtNetwork.QAbstractSocket.SocketError.OperationError
    PathMtuSocketOption = PySide2.QtNetwork.QAbstractSocket.SocketOption.PathMtuSocketOption
    PauseMode = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.PauseMode'>"
    PauseModes = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.PauseModes'>"
    PauseNever = PySide2.QtNetwork.QAbstractSocket.PauseMode.PauseNever
    PauseOnSslErrors = PySide2.QtNetwork.QAbstractSocket.PauseMode.PauseOnSslErrors
    ProxyAuthenticationRequiredError = PySide2.QtNetwork.QAbstractSocket.SocketError.ProxyAuthenticationRequiredError
    ProxyConnectionClosedError = PySide2.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionClosedError
    ProxyConnectionRefusedError = PySide2.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionRefusedError
    ProxyConnectionTimeoutError = PySide2.QtNetwork.QAbstractSocket.SocketError.ProxyConnectionTimeoutError
    ProxyNotFoundError = PySide2.QtNetwork.QAbstractSocket.SocketError.ProxyNotFoundError
    ProxyProtocolError = PySide2.QtNetwork.QAbstractSocket.SocketError.ProxyProtocolError
    ReceiveBufferSizeSocketOption = PySide2.QtNetwork.QAbstractSocket.SocketOption.ReceiveBufferSizeSocketOption
    RemoteHostClosedError = PySide2.QtNetwork.QAbstractSocket.SocketError.RemoteHostClosedError
    ReuseAddressHint = PySide2.QtNetwork.QAbstractSocket.BindFlag.ReuseAddressHint
    SctpSocket = PySide2.QtNetwork.QAbstractSocket.SocketType.SctpSocket
    SendBufferSizeSocketOption = PySide2.QtNetwork.QAbstractSocket.SocketOption.SendBufferSizeSocketOption
    ShareAddress = PySide2.QtNetwork.QAbstractSocket.BindFlag.ShareAddress
    SocketAccessError = PySide2.QtNetwork.QAbstractSocket.SocketError.SocketAccessError
    SocketAddressNotAvailableError = PySide2.QtNetwork.QAbstractSocket.SocketError.SocketAddressNotAvailableError
    SocketError = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.SocketError'>"
    SocketOption = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.SocketOption'>"
    SocketResourceError = PySide2.QtNetwork.QAbstractSocket.SocketError.SocketResourceError
    SocketState = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.SocketState'>"
    SocketTimeoutError = PySide2.QtNetwork.QAbstractSocket.SocketError.SocketTimeoutError
    SocketType = None # (!) real value is "<class 'PySide2.QtNetwork.QAbstractSocket.SocketType'>"
    SslHandshakeFailedError = PySide2.QtNetwork.QAbstractSocket.SocketError.SslHandshakeFailedError
    SslInternalError = PySide2.QtNetwork.QAbstractSocket.SocketError.SslInternalError
    SslInvalidUserDataError = PySide2.QtNetwork.QAbstractSocket.SocketError.SslInvalidUserDataError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D86C7C0>'
    TcpSocket = PySide2.QtNetwork.QAbstractSocket.SocketType.TcpSocket
    TemporaryError = PySide2.QtNetwork.QAbstractSocket.SocketError.TemporaryError
    TypeOfServiceOption = PySide2.QtNetwork.QAbstractSocket.SocketOption.TypeOfServiceOption
    UdpSocket = PySide2.QtNetwork.QAbstractSocket.SocketType.UdpSocket
    UnconnectedState = PySide2.QtNetwork.QAbstractSocket.SocketState.UnconnectedState
    UnfinishedSocketOperationError = PySide2.QtNetwork.QAbstractSocket.SocketError.UnfinishedSocketOperationError
    UnknownNetworkLayerProtocol = PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol.UnknownNetworkLayerProtocol
    UnknownSocketError = PySide2.QtNetwork.QAbstractSocket.SocketError.UnknownSocketError
    UnknownSocketType = PySide2.QtNetwork.QAbstractSocket.SocketType.UnknownSocketType
    UnsupportedSocketOperationError = PySide2.QtNetwork.QAbstractSocket.SocketError.UnsupportedSocketOperationError


