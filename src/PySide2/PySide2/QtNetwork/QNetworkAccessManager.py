# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkAccessManager(__PySide2_QtCore.QObject):
    """ QNetworkAccessManager(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def activeConfiguration(self): # real signature unknown; restored from __doc__
        """ activeConfiguration(self) -> PySide2.QtNetwork.QNetworkConfiguration """
        pass

    def addStrictTransportSecurityHosts(self, knownHosts, PySide2_QtNetwork_QHstsPolicy=None): # real signature unknown; restored from __doc__
        """ addStrictTransportSecurityHosts(self, knownHosts: typing.List[PySide2.QtNetwork.QHstsPolicy]) -> None """
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def autoDeleteReplies(self): # real signature unknown; restored from __doc__
        """ autoDeleteReplies(self) -> bool """
        return False

    def cache(self): # real signature unknown; restored from __doc__
        """ cache(self) -> PySide2.QtNetwork.QAbstractNetworkCache """
        pass

    def clearAccessCache(self): # real signature unknown; restored from __doc__
        """ clearAccessCache(self) -> None """
        pass

    def clearConnectionCache(self): # real signature unknown; restored from __doc__
        """ clearConnectionCache(self) -> None """
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> PySide2.QtNetwork.QNetworkConfiguration """
        pass

    def connectToHost(self, hostName, port=80): # real signature unknown; restored from __doc__
        """ connectToHost(self, hostName: str, port: int = 80) -> None """
        pass

    def connectToHostEncrypted(self, hostName, port, sslConfiguration, peerName): # real signature unknown; restored from __doc__
        """
        connectToHostEncrypted(self, hostName: str, port: int, sslConfiguration: PySide2.QtNetwork.QSslConfiguration, peerName: str) -> None
        connectToHostEncrypted(self, hostName: str, port: int = 443, sslConfiguration: PySide2.QtNetwork.QSslConfiguration = Default(QSslConfiguration.defaultConfiguration)) -> None
        """
        pass

    def cookieJar(self): # real signature unknown; restored from __doc__
        """ cookieJar(self) -> PySide2.QtNetwork.QNetworkCookieJar """
        pass

    def createRequest(self, op, request, outgoingData, PySide2_QtCore_QIODevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createRequest(self, op: PySide2.QtNetwork.QNetworkAccessManager.Operation, request: PySide2.QtNetwork.QNetworkRequest, outgoingData: typing.Optional[PySide2.QtCore.QIODevice] = None) -> PySide2.QtNetwork.QNetworkReply """
        pass

    def deleteResource(self, request): # real signature unknown; restored from __doc__
        """ deleteResource(self, request: PySide2.QtNetwork.QNetworkRequest) -> PySide2.QtNetwork.QNetworkReply """
        pass

    def enableStrictTransportSecurityStore(self, enabled, storeDir=''): # real signature unknown; restored from __doc__
        """ enableStrictTransportSecurityStore(self, enabled: bool, storeDir: str = '') -> None """
        pass

    def encrypted(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, request): # real signature unknown; restored from __doc__
        """ get(self, request: PySide2.QtNetwork.QNetworkRequest) -> PySide2.QtNetwork.QNetworkReply """
        pass

    def head(self, request): # real signature unknown; restored from __doc__
        """ head(self, request: PySide2.QtNetwork.QNetworkRequest) -> PySide2.QtNetwork.QNetworkReply """
        pass

    def isStrictTransportSecurityEnabled(self): # real signature unknown; restored from __doc__
        """ isStrictTransportSecurityEnabled(self) -> bool """
        return False

    def isStrictTransportSecurityStoreEnabled(self): # real signature unknown; restored from __doc__
        """ isStrictTransportSecurityStoreEnabled(self) -> bool """
        return False

    def networkAccessible(self): # real signature unknown; restored from __doc__
        """ networkAccessible(self) -> PySide2.QtNetwork.QNetworkAccessManager.NetworkAccessibility """
        pass

    def networkAccessibleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def networkSessionConnected(self, *args, **kwargs): # real signature unknown
        pass

    def post(self, request, data): # real signature unknown; restored from __doc__
        """
        post(self, request: PySide2.QtNetwork.QNetworkRequest, data: PySide2.QtCore.QByteArray) -> PySide2.QtNetwork.QNetworkReply
        post(self, request: PySide2.QtNetwork.QNetworkRequest, data: PySide2.QtCore.QIODevice) -> PySide2.QtNetwork.QNetworkReply
        post(self, request: PySide2.QtNetwork.QNetworkRequest, multiPart: PySide2.QtNetwork.QHttpMultiPart) -> PySide2.QtNetwork.QNetworkReply
        """
        pass

    def preSharedKeyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> PySide2.QtNetwork.QNetworkProxy """
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def proxyFactory(self): # real signature unknown; restored from __doc__
        """ proxyFactory(self) -> PySide2.QtNetwork.QNetworkProxyFactory """
        pass

    def put(self, request, data): # real signature unknown; restored from __doc__
        """
        put(self, request: PySide2.QtNetwork.QNetworkRequest, data: PySide2.QtCore.QByteArray) -> PySide2.QtNetwork.QNetworkReply
        put(self, request: PySide2.QtNetwork.QNetworkRequest, data: PySide2.QtCore.QIODevice) -> PySide2.QtNetwork.QNetworkReply
        put(self, request: PySide2.QtNetwork.QNetworkRequest, multiPart: PySide2.QtNetwork.QHttpMultiPart) -> PySide2.QtNetwork.QNetworkReply
        """
        pass

    def redirectPolicy(self): # real signature unknown; restored from __doc__
        """ redirectPolicy(self) -> PySide2.QtNetwork.QNetworkRequest.RedirectPolicy """
        pass

    def sendCustomRequest(self, request, verb, data): # real signature unknown; restored from __doc__
        """
        sendCustomRequest(self, request: PySide2.QtNetwork.QNetworkRequest, verb: PySide2.QtCore.QByteArray, data: PySide2.QtCore.QByteArray) -> PySide2.QtNetwork.QNetworkReply
        sendCustomRequest(self, request: PySide2.QtNetwork.QNetworkRequest, verb: PySide2.QtCore.QByteArray, data: typing.Optional[PySide2.QtCore.QIODevice] = None) -> PySide2.QtNetwork.QNetworkReply
        sendCustomRequest(self, request: PySide2.QtNetwork.QNetworkRequest, verb: PySide2.QtCore.QByteArray, multiPart: PySide2.QtNetwork.QHttpMultiPart) -> PySide2.QtNetwork.QNetworkReply
        """
        pass

    def setAutoDeleteReplies(self, autoDelete): # real signature unknown; restored from __doc__
        """ setAutoDeleteReplies(self, autoDelete: bool) -> None """
        pass

    def setCache(self, cache): # real signature unknown; restored from __doc__
        """ setCache(self, cache: PySide2.QtNetwork.QAbstractNetworkCache) -> None """
        pass

    def setConfiguration(self, config): # real signature unknown; restored from __doc__
        """ setConfiguration(self, config: PySide2.QtNetwork.QNetworkConfiguration) -> None """
        pass

    def setCookieJar(self, cookieJar): # real signature unknown; restored from __doc__
        """ setCookieJar(self, cookieJar: PySide2.QtNetwork.QNetworkCookieJar) -> None """
        pass

    def setNetworkAccessible(self, accessible): # real signature unknown; restored from __doc__
        """ setNetworkAccessible(self, accessible: PySide2.QtNetwork.QNetworkAccessManager.NetworkAccessibility) -> None """
        pass

    def setProxy(self, proxy): # real signature unknown; restored from __doc__
        """ setProxy(self, proxy: PySide2.QtNetwork.QNetworkProxy) -> None """
        pass

    def setProxyFactory(self, factory): # real signature unknown; restored from __doc__
        """ setProxyFactory(self, factory: PySide2.QtNetwork.QNetworkProxyFactory) -> None """
        pass

    def setRedirectPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setRedirectPolicy(self, policy: PySide2.QtNetwork.QNetworkRequest.RedirectPolicy) -> None """
        pass

    def setStrictTransportSecurityEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setStrictTransportSecurityEnabled(self, enabled: bool) -> None """
        pass

    def setTransferTimeout(self, timeout, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setTransferTimeout(self, timeout: int = <class 'PySide2.QtNetwork.QNetworkRequest.TransferTimeoutConstant'>) -> None """
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def strictTransportSecurityHosts(self): # real signature unknown; restored from __doc__
        """ strictTransportSecurityHosts(self) -> typing.List[PySide2.QtNetwork.QHstsPolicy] """
        pass

    def supportedSchemes(self): # real signature unknown; restored from __doc__
        """ supportedSchemes(self) -> typing.List[str] """
        pass

    def supportedSchemesImplementation(self): # real signature unknown; restored from __doc__
        """ supportedSchemesImplementation(self) -> typing.List[str] """
        pass

    def transferTimeout(self): # real signature unknown; restored from __doc__
        """ transferTimeout(self) -> int """
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

    Accessible = PySide2.QtNetwork.QNetworkAccessManager.NetworkAccessibility.Accessible
    CustomOperation = PySide2.QtNetwork.QNetworkAccessManager.Operation.CustomOperation
    DeleteOperation = PySide2.QtNetwork.QNetworkAccessManager.Operation.DeleteOperation
    GetOperation = PySide2.QtNetwork.QNetworkAccessManager.Operation.GetOperation
    HeadOperation = PySide2.QtNetwork.QNetworkAccessManager.Operation.HeadOperation
    NetworkAccessibility = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkAccessManager.NetworkAccessibility'>"
    NotAccessible = PySide2.QtNetwork.QNetworkAccessManager.NetworkAccessibility.NotAccessible
    Operation = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkAccessManager.Operation'>"
    PostOperation = PySide2.QtNetwork.QNetworkAccessManager.Operation.PostOperation
    PutOperation = PySide2.QtNetwork.QNetworkAccessManager.Operation.PutOperation
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D86FBC0>'
    UnknownAccessibility = PySide2.QtNetwork.QNetworkAccessManager.NetworkAccessibility.UnknownAccessibility
    UnknownOperation = PySide2.QtNetwork.QNetworkAccessManager.Operation.UnknownOperation


