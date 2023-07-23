# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkProxy(__Shiboken.Object):
    """
    QNetworkProxy(self) -> None
    QNetworkProxy(self, other: PySide2.QtNetwork.QNetworkProxy) -> None
    QNetworkProxy(self, type: PySide2.QtNetwork.QNetworkProxy.ProxyType, hostName: str = '', port: int = 0, user: str = '', password: str = '') -> None
    """
    def applicationProxy(self): # real signature unknown; restored from __doc__
        """ applicationProxy() -> PySide2.QtNetwork.QNetworkProxy """
        pass

    def capabilities(self): # real signature unknown; restored from __doc__
        """ capabilities(self) -> PySide2.QtNetwork.QNetworkProxy.Capabilities """
        pass

    def hasRawHeader(self, headerName): # real signature unknown; restored from __doc__
        """ hasRawHeader(self, headerName: PySide2.QtCore.QByteArray) -> bool """
        return False

    def header(self, header): # real signature unknown; restored from __doc__
        """ header(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders) -> typing.Any """
        pass

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def isCachingProxy(self): # real signature unknown; restored from __doc__
        """ isCachingProxy(self) -> bool """
        return False

    def isTransparentProxy(self): # real signature unknown; restored from __doc__
        """ isTransparentProxy(self) -> bool """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ password(self) -> str """
        return ""

    def port(self): # real signature unknown; restored from __doc__
        """ port(self) -> int """
        return 0

    def rawHeader(self, headerName): # real signature unknown; restored from __doc__
        """ rawHeader(self, headerName: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ rawHeaderList(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def setApplicationProxy(self, proxy): # real signature unknown; restored from __doc__
        """ setApplicationProxy(proxy: PySide2.QtNetwork.QNetworkProxy) -> None """
        pass

    def setCapabilities(self, capab): # real signature unknown; restored from __doc__
        """ setCapabilities(self, capab: PySide2.QtNetwork.QNetworkProxy.Capabilities) -> None """
        pass

    def setHeader(self, header, value): # real signature unknown; restored from __doc__
        """ setHeader(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders, value: typing.Any) -> None """
        pass

    def setHostName(self, hostName): # real signature unknown; restored from __doc__
        """ setHostName(self, hostName: str) -> None """
        pass

    def setPassword(self, password): # real signature unknown; restored from __doc__
        """ setPassword(self, password: str) -> None """
        pass

    def setPort(self, port): # real signature unknown; restored from __doc__
        """ setPort(self, port: int) -> None """
        pass

    def setRawHeader(self, headerName, value): # real signature unknown; restored from __doc__
        """ setRawHeader(self, headerName: PySide2.QtCore.QByteArray, value: PySide2.QtCore.QByteArray) -> None """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: PySide2.QtNetwork.QNetworkProxy.ProxyType) -> None """
        pass

    def setUser(self, userName): # real signature unknown; restored from __doc__
        """ setUser(self, userName: str) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QNetworkProxy) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtNetwork.QNetworkProxy.ProxyType """
        pass

    def user(self): # real signature unknown; restored from __doc__
        """ user(self) -> str """
        return ""

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

    CachingCapability = PySide2.QtNetwork.QNetworkProxy.Capability.CachingCapability
    Capabilities = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkProxy.Capabilities'>"
    Capability = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkProxy.Capability'>"
    DefaultProxy = PySide2.QtNetwork.QNetworkProxy.ProxyType.DefaultProxy
    FtpCachingProxy = PySide2.QtNetwork.QNetworkProxy.ProxyType.FtpCachingProxy
    HostNameLookupCapability = PySide2.QtNetwork.QNetworkProxy.Capability.HostNameLookupCapability
    HttpCachingProxy = PySide2.QtNetwork.QNetworkProxy.ProxyType.HttpCachingProxy
    HttpProxy = PySide2.QtNetwork.QNetworkProxy.ProxyType.HttpProxy
    ListeningCapability = PySide2.QtNetwork.QNetworkProxy.Capability.ListeningCapability
    NoProxy = PySide2.QtNetwork.QNetworkProxy.ProxyType.NoProxy
    ProxyType = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkProxy.ProxyType'>"
    SctpListeningCapability = PySide2.QtNetwork.QNetworkProxy.Capability.SctpListeningCapability
    SctpTunnelingCapability = PySide2.QtNetwork.QNetworkProxy.Capability.SctpTunnelingCapability
    Socks5Proxy = PySide2.QtNetwork.QNetworkProxy.ProxyType.Socks5Proxy
    TunnelingCapability = PySide2.QtNetwork.QNetworkProxy.Capability.TunnelingCapability
    UdpTunnelingCapability = PySide2.QtNetwork.QNetworkProxy.Capability.UdpTunnelingCapability
    __hash__ = None


