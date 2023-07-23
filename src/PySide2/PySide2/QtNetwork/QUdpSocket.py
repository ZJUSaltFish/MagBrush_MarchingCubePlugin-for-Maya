# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QAbstractSocket import QAbstractSocket

class QUdpSocket(QAbstractSocket):
    """ QUdpSocket(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def hasPendingDatagrams(self): # real signature unknown; restored from __doc__
        """ hasPendingDatagrams(self) -> bool """
        return False

    def joinMulticastGroup(self, groupAddress): # real signature unknown; restored from __doc__
        """
        joinMulticastGroup(self, groupAddress: PySide2.QtNetwork.QHostAddress) -> bool
        joinMulticastGroup(self, groupAddress: PySide2.QtNetwork.QHostAddress, iface: PySide2.QtNetwork.QNetworkInterface) -> bool
        """
        return False

    def leaveMulticastGroup(self, groupAddress): # real signature unknown; restored from __doc__
        """
        leaveMulticastGroup(self, groupAddress: PySide2.QtNetwork.QHostAddress) -> bool
        leaveMulticastGroup(self, groupAddress: PySide2.QtNetwork.QHostAddress, iface: PySide2.QtNetwork.QNetworkInterface) -> bool
        """
        return False

    def multicastInterface(self): # real signature unknown; restored from __doc__
        """ multicastInterface(self) -> PySide2.QtNetwork.QNetworkInterface """
        pass

    def pendingDatagramSize(self): # real signature unknown; restored from __doc__
        """ pendingDatagramSize(self) -> int """
        return 0

    def readDatagram(self, data, maxlen, host): # real signature unknown; restored from __doc__
        """ readDatagram(self, data: bytes, maxlen: int, host: PySide2.QtNetwork.QHostAddress) -> typing.Tuple[int, int] """
        pass

    def receiveDatagram(self, maxSize=-1): # real signature unknown; restored from __doc__
        """ receiveDatagram(self, maxSize: int = -1) -> PySide2.QtNetwork.QNetworkDatagram """
        pass

    def setMulticastInterface(self, iface): # real signature unknown; restored from __doc__
        """ setMulticastInterface(self, iface: PySide2.QtNetwork.QNetworkInterface) -> None """
        pass

    def writeDatagram(self, datagram, host, port): # real signature unknown; restored from __doc__
        """
        writeDatagram(self, datagram: PySide2.QtCore.QByteArray, host: PySide2.QtNetwork.QHostAddress, port: int) -> int
        writeDatagram(self, datagram: PySide2.QtNetwork.QNetworkDatagram) -> int
        """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D86CA40>'


