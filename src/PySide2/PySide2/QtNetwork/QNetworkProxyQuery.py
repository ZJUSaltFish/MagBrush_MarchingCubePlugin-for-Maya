# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkProxyQuery(__Shiboken.Object):
    """
    QNetworkProxyQuery(self) -> None
    QNetworkProxyQuery(self, bindPort: int, protocolTag: str = '', queryType: PySide2.QtNetwork.QNetworkProxyQuery.QueryType = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.TcpServer) -> None
    QNetworkProxyQuery(self, hostname: str, port: int, protocolTag: str = '', queryType: PySide2.QtNetwork.QNetworkProxyQuery.QueryType = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.TcpSocket) -> None
    QNetworkProxyQuery(self, networkConfiguration: PySide2.QtNetwork.QNetworkConfiguration, bindPort: int, protocolTag: str = '', queryType: PySide2.QtNetwork.QNetworkProxyQuery.QueryType = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.TcpServer) -> None
    QNetworkProxyQuery(self, networkConfiguration: PySide2.QtNetwork.QNetworkConfiguration, hostname: str, port: int, protocolTag: str = '', queryType: PySide2.QtNetwork.QNetworkProxyQuery.QueryType = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.TcpSocket) -> None
    QNetworkProxyQuery(self, networkConfiguration: PySide2.QtNetwork.QNetworkConfiguration, requestUrl: PySide2.QtCore.QUrl, queryType: PySide2.QtNetwork.QNetworkProxyQuery.QueryType = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.UrlRequest) -> None
    QNetworkProxyQuery(self, other: PySide2.QtNetwork.QNetworkProxyQuery) -> None
    QNetworkProxyQuery(self, requestUrl: PySide2.QtCore.QUrl, queryType: PySide2.QtNetwork.QNetworkProxyQuery.QueryType = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.UrlRequest) -> None
    """
    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def networkConfiguration(self): # real signature unknown; restored from __doc__
        """ networkConfiguration(self) -> PySide2.QtNetwork.QNetworkConfiguration """
        pass

    def peerHostName(self): # real signature unknown; restored from __doc__
        """ peerHostName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def protocolTag(self): # real signature unknown; restored from __doc__
        """ protocolTag(self) -> str """
        return ""

    def queryType(self): # real signature unknown; restored from __doc__
        """ queryType(self) -> PySide2.QtNetwork.QNetworkProxyQuery.QueryType """
        pass

    def setLocalPort(self, port): # real signature unknown; restored from __doc__
        """ setLocalPort(self, port: int) -> None """
        pass

    def setNetworkConfiguration(self, networkConfiguration): # real signature unknown; restored from __doc__
        """ setNetworkConfiguration(self, networkConfiguration: PySide2.QtNetwork.QNetworkConfiguration) -> None """
        pass

    def setPeerHostName(self, hostname): # real signature unknown; restored from __doc__
        """ setPeerHostName(self, hostname: str) -> None """
        pass

    def setPeerPort(self, port): # real signature unknown; restored from __doc__
        """ setPeerPort(self, port: int) -> None """
        pass

    def setProtocolTag(self, protocolTag): # real signature unknown; restored from __doc__
        """ setProtocolTag(self, protocolTag: str) -> None """
        pass

    def setQueryType(self, type): # real signature unknown; restored from __doc__
        """ setQueryType(self, type: PySide2.QtNetwork.QNetworkProxyQuery.QueryType) -> None """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QNetworkProxyQuery) -> None """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
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

    QueryType = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkProxyQuery.QueryType'>"
    SctpServer = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.SctpServer
    SctpSocket = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.SctpSocket
    TcpServer = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.TcpServer
    TcpSocket = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.TcpSocket
    UdpSocket = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.UdpSocket
    UrlRequest = PySide2.QtNetwork.QNetworkProxyQuery.QueryType.UrlRequest
    __hash__ = None


