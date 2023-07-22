# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QLocalServer(__PySide2_QtCore.QObject):
    """ QLocalServer(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fullServerName(self): # real signature unknown; restored from __doc__
        """ fullServerName(self) -> str """
        return ""

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def incomingConnection(self, socketDescriptor): # real signature unknown; restored from __doc__
        """ incomingConnection(self, socketDescriptor: int) -> None """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def listen(self, name): # real signature unknown; restored from __doc__
        """
        listen(self, name: str) -> bool
        listen(self, socketDescriptor: int) -> bool
        """
        return False

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def newConnection(self, *args, **kwargs): # real signature unknown
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> PySide2.QtNetwork.QLocalSocket """
        pass

    def removeServer(self, name): # real signature unknown; restored from __doc__
        """ removeServer(name: str) -> bool """
        return False

    def serverError(self): # real signature unknown; restored from __doc__
        """ serverError(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError """
        pass

    def serverName(self): # real signature unknown; restored from __doc__
        """ serverName(self) -> str """
        return ""

    def setMaxPendingConnections(self, numConnections): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, numConnections: int) -> None """
        pass

    def setSocketOptions(self, options): # real signature unknown; restored from __doc__
        """ setSocketOptions(self, options: PySide2.QtNetwork.QLocalServer.SocketOptions) -> None """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

    def socketOptions(self): # real signature unknown; restored from __doc__
        """ socketOptions(self) -> PySide2.QtNetwork.QLocalServer.SocketOptions """
        pass

    def waitForNewConnection(self, msec): # real signature unknown; restored from __doc__
        """ waitForNewConnection(self, msec: int) -> typing.Tuple[bool, bool] """
        pass

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

    GroupAccessOption = PySide2.QtNetwork.QLocalServer.SocketOption.GroupAccessOption
    NoOptions = PySide2.QtNetwork.QLocalServer.SocketOption.NoOptions
    OtherAccessOption = PySide2.QtNetwork.QLocalServer.SocketOption.OtherAccessOption
    SocketOption = None # (!) real value is "<class 'PySide2.QtNetwork.QLocalServer.SocketOption'>"
    SocketOptions = None # (!) real value is "<class 'PySide2.QtNetwork.QLocalServer.SocketOptions'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D88C200>'
    UserAccessOption = PySide2.QtNetwork.QLocalServer.SocketOption.UserAccessOption
    WorldAccessOption = PySide2.QtNetwork.QLocalServer.SocketOption.WorldAccessOption


