# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QLocalSocket(__PySide2_QtCore.QIODevice):
    """ QLocalSocket(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

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

    def connectToServer(self, name, openMode=None): # real signature unknown; restored from __doc__
        """
        connectToServer(self, name: str, openMode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> None
        connectToServer(self, openMode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> None
        """
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectFromServer(self): # real signature unknown; restored from __doc__
        """ disconnectFromServer(self) -> None """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtNetwork.QLocalSocket.LocalSocketError """
        pass

    def errorOccurred(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def fullServerName(self): # real signature unknown; restored from __doc__
        """ fullServerName(self) -> str """
        return ""

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def open(self, openMode=None): # real signature unknown; restored from __doc__
        """ open(self, openMode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> bool """
        return False

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readData(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ readData(self, arg__1: bytes, arg__2: int) -> int """
        return 0

    def serverName(self): # real signature unknown; restored from __doc__
        """ serverName(self) -> str """
        return ""

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) -> None """
        pass

    def setServerName(self, name): # real signature unknown; restored from __doc__
        """ setServerName(self, name: str) -> None """
        pass

    def setSocketDescriptor(self, socketDescriptor, socketState=None, openMode=None): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, socketDescriptor: int, socketState: PySide2.QtNetwork.QLocalSocket.LocalSocketState = PySide2.QtNetwork.QAbstractSocket.SocketState.ConnectedState, openMode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> bool """
        return False

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtNetwork.QLocalSocket.LocalSocketState """
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

    def writeData(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ writeData(self, arg__1: bytes, arg__2: int) -> int """
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

    ClosingState = PySide2.QtNetwork.QLocalSocket.LocalSocketState.ClosingState
    ConnectedState = PySide2.QtNetwork.QLocalSocket.LocalSocketState.ConnectedState
    ConnectingState = PySide2.QtNetwork.QLocalSocket.LocalSocketState.ConnectingState
    ConnectionError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.ConnectionError
    ConnectionRefusedError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.ConnectionRefusedError
    DatagramTooLargeError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.DatagramTooLargeError
    LocalSocketError = None # (!) real value is "<class 'PySide2.QtNetwork.QLocalSocket.LocalSocketError'>"
    LocalSocketState = None # (!) real value is "<class 'PySide2.QtNetwork.QLocalSocket.LocalSocketState'>"
    OperationError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.OperationError
    PeerClosedError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.PeerClosedError
    ServerNotFoundError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.ServerNotFoundError
    SocketAccessError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.SocketAccessError
    SocketResourceError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.SocketResourceError
    SocketTimeoutError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.SocketTimeoutError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D86D2C0>'
    UnconnectedState = PySide2.QtNetwork.QLocalSocket.LocalSocketState.UnconnectedState
    UnknownSocketError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.UnknownSocketError
    UnsupportedSocketOperationError = PySide2.QtNetwork.QLocalSocket.LocalSocketError.UnsupportedSocketOperationError


