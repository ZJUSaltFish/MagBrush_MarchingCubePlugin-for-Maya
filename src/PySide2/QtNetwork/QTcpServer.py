# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTcpServer(__PySide2_QtCore.QObject):
    """ QTcpServer(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def acceptError(self, *args, **kwargs): # real signature unknown
        pass

    def addPendingConnection(self, socket): # real signature unknown; restored from __doc__
        """ addPendingConnection(self, socket: PySide2.QtNetwork.QTcpSocket) -> None """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def incomingConnection(self, handle): # real signature unknown; restored from __doc__
        """ incomingConnection(self, handle: int) -> None """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def listen(self, address=None, port=0): # real signature unknown; restored from __doc__
        """ listen(self, address: PySide2.QtNetwork.QHostAddress = PySide2.QtNetwork.QHostAddress.SpecialAddress.Any, port: int = 0) -> bool """
        return False

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def newConnection(self, *args, **kwargs): # real signature unknown
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> PySide2.QtNetwork.QTcpSocket """
        pass

    def pauseAccepting(self): # real signature unknown; restored from __doc__
        """ pauseAccepting(self) -> None """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> PySide2.QtNetwork.QNetworkProxy """
        pass

    def resumeAccepting(self): # real signature unknown; restored from __doc__
        """ resumeAccepting(self) -> None """
        pass

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ serverAddress(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def serverError(self): # real signature unknown; restored from __doc__
        """ serverError(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError """
        pass

    def serverPort(self): # real signature unknown; restored from __doc__
        """ serverPort(self) -> int """
        return 0

    def setMaxPendingConnections(self, numConnections): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, numConnections: int) -> None """
        pass

    def setProxy(self, networkProxy): # real signature unknown; restored from __doc__
        """ setProxy(self, networkProxy: PySide2.QtNetwork.QNetworkProxy) -> None """
        pass

    def setSocketDescriptor(self, socketDescriptor): # real signature unknown; restored from __doc__
        """ setSocketDescriptor(self, socketDescriptor: int) -> bool """
        return False

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D88C940>'


