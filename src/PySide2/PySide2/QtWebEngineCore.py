# encoding: utf-8
# module PySide2.QtWebEngineCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWebEngineCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QWebEngineCookieStore(__PySide2_QtCore.QObject):
    # no doc
    def cookieAdded(self, *args, **kwargs): # real signature unknown
        pass

    def cookieRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def deleteAllCookies(self): # real signature unknown; restored from __doc__
        """ deleteAllCookies(self) -> None """
        pass

    def deleteCookie(self, cookie, origin=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ deleteCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie, origin: PySide2.QtCore.QUrl = Default(QUrl)) -> None """
        pass

    def deleteSessionCookies(self): # real signature unknown; restored from __doc__
        """ deleteSessionCookies(self) -> None """
        pass

    def loadAllCookies(self): # real signature unknown; restored from __doc__
        """ loadAllCookies(self) -> None """
        pass

    def setCookie(self, cookie, origin=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie, origin: PySide2.QtCore.QUrl = Default(QUrl)) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001FDC0D2D600>'


class QWebEngineHttpRequest(__Shiboken.Object):
    """
    QWebEngineHttpRequest(self, other: PySide2.QtWebEngineCore.QWebEngineHttpRequest) -> None
    QWebEngineHttpRequest(self, url: PySide2.QtCore.QUrl = Default(QUrl), method: PySide2.QtWebEngineCore.QWebEngineHttpRequest.Method = PySide2.QtWebEngineCore.QWebEngineHttpRequest.Method.Get) -> None
    """
    def hasHeader(self, headerName): # real signature unknown; restored from __doc__
        """ hasHeader(self, headerName: PySide2.QtCore.QByteArray) -> bool """
        return False

    def header(self, headerName): # real signature unknown; restored from __doc__
        """ header(self, headerName: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray """
        pass

    def headers(self): # real signature unknown; restored from __doc__
        """ headers(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def method(self): # real signature unknown; restored from __doc__
        """ method(self) -> PySide2.QtWebEngineCore.QWebEngineHttpRequest.Method """
        pass

    def postData(self): # real signature unknown; restored from __doc__
        """ postData(self) -> PySide2.QtCore.QByteArray """
        pass

    def postRequest(self, url, postData, p_str=None, p_str=None_1): # real signature unknown; restored from __doc__
        """ postRequest(url: PySide2.QtCore.QUrl, postData: typing.Dict[str, str]) -> PySide2.QtWebEngineCore.QWebEngineHttpRequest """
        pass

    def setHeader(self, headerName, value): # real signature unknown; restored from __doc__
        """ setHeader(self, headerName: PySide2.QtCore.QByteArray, value: PySide2.QtCore.QByteArray) -> None """
        pass

    def setMethod(self, method): # real signature unknown; restored from __doc__
        """ setMethod(self, method: PySide2.QtWebEngineCore.QWebEngineHttpRequest.Method) -> None """
        pass

    def setPostData(self, postData): # real signature unknown; restored from __doc__
        """ setPostData(self, postData: PySide2.QtCore.QByteArray) -> None """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtWebEngineCore.QWebEngineHttpRequest) -> None """
        pass

    def unsetHeader(self, headerName): # real signature unknown; restored from __doc__
        """ unsetHeader(self, headerName: PySide2.QtCore.QByteArray) -> None """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
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

    def __init__(self, other): # real signature unknown; restored from __doc__
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

    Get = PySide2.QtWebEngineCore.QWebEngineHttpRequest.Method.Get
    Method = None # (!) real value is "<class 'PySide2.QtWebEngineCore.QWebEngineHttpRequest.Method'>"
    Post = PySide2.QtWebEngineCore.QWebEngineHttpRequest.Method.Post
    __hash__ = None


class QWebEngineUrlRequestInfo(__Shiboken.Object):
    # no doc
    def block(self, shouldBlock): # real signature unknown; restored from __doc__
        """ block(self, shouldBlock: bool) -> None """
        pass

    def changed(self): # real signature unknown; restored from __doc__
        """ changed(self) -> bool """
        return False

    def firstPartyUrl(self): # real signature unknown; restored from __doc__
        """ firstPartyUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def initiator(self): # real signature unknown; restored from __doc__
        """ initiator(self) -> PySide2.QtCore.QUrl """
        pass

    def navigationType(self): # real signature unknown; restored from __doc__
        """ navigationType(self) -> PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType """
        pass

    def redirect(self, url): # real signature unknown; restored from __doc__
        """ redirect(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def requestMethod(self): # real signature unknown; restored from __doc__
        """ requestMethod(self) -> PySide2.QtCore.QByteArray """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def resourceType(self): # real signature unknown; restored from __doc__
        """ resourceType(self) -> PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType """
        pass

    def setHttpHeader(self, name, value): # real signature unknown; restored from __doc__
        """ setHttpHeader(self, name: PySide2.QtCore.QByteArray, value: PySide2.QtCore.QByteArray) -> None """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    NavigationType = None # (!) real value is "<class 'PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType'>"
    NavigationTypeBackForward = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType.NavigationTypeBackForward
    NavigationTypeFormSubmitted = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType.NavigationTypeFormSubmitted
    NavigationTypeLink = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType.NavigationTypeLink
    NavigationTypeOther = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType.NavigationTypeOther
    NavigationTypeRedirect = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType.NavigationTypeRedirect
    NavigationTypeReload = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType.NavigationTypeReload
    NavigationTypeTyped = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.NavigationType.NavigationTypeTyped
    ResourceType = None # (!) real value is "<class 'PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType'>"
    ResourceTypeCspReport = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeCspReport
    ResourceTypeFavicon = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeFavicon
    ResourceTypeFontResource = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeFontResource
    ResourceTypeImage = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeImage
    ResourceTypeLast = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeLast
    ResourceTypeMainFrame = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeMainFrame
    ResourceTypeMedia = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeMedia
    ResourceTypeNavigationPreloadMainFrame = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeNavigationPreloadMainFrame
    ResourceTypeNavigationPreloadSubFrame = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeNavigationPreloadSubFrame
    ResourceTypeObject = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeObject
    ResourceTypePing = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypePing
    ResourceTypePluginResource = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypePluginResource
    ResourceTypePrefetch = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypePrefetch
    ResourceTypeScript = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeScript
    ResourceTypeServiceWorker = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeServiceWorker
    ResourceTypeSharedWorker = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeSharedWorker
    ResourceTypeStylesheet = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeStylesheet
    ResourceTypeSubFrame = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeSubFrame
    ResourceTypeSubResource = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeSubResource
    ResourceTypeUnknown = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeUnknown
    ResourceTypeWorker = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeWorker
    ResourceTypeXhr = PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo.ResourceType.ResourceTypeXhr


class QWebEngineUrlRequestInterceptor(__PySide2_QtCore.QObject):
    """ QWebEngineUrlRequestInterceptor(self, p: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def interceptRequest(self, info): # real signature unknown; restored from __doc__
        """ interceptRequest(self, info: PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, p, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001FDC0D2D000>'


class QWebEngineUrlRequestJob(__PySide2_QtCore.QObject):
    # no doc
    def fail(self, error): # real signature unknown; restored from __doc__
        """ fail(self, error: PySide2.QtWebEngineCore.QWebEngineUrlRequestJob.Error) -> None """
        pass

    def initiator(self): # real signature unknown; restored from __doc__
        """ initiator(self) -> PySide2.QtCore.QUrl """
        pass

    def redirect(self, url): # real signature unknown; restored from __doc__
        """ redirect(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def reply(self, contentType, device): # real signature unknown; restored from __doc__
        """ reply(self, contentType: PySide2.QtCore.QByteArray, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def requestHeaders(self): # real signature unknown; restored from __doc__
        """ requestHeaders(self) -> typing.Dict[PySide2.QtCore.QByteArray, PySide2.QtCore.QByteArray] """
        pass

    def requestMethod(self): # real signature unknown; restored from __doc__
        """ requestMethod(self) -> PySide2.QtCore.QByteArray """
        pass

    def requestUrl(self): # real signature unknown; restored from __doc__
        """ requestUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Error = None # (!) real value is "<class 'PySide2.QtWebEngineCore.QWebEngineUrlRequestJob.Error'>"
    NoError = PySide2.QtWebEngineCore.QWebEngineUrlRequestJob.Error.NoError
    RequestAborted = PySide2.QtWebEngineCore.QWebEngineUrlRequestJob.Error.RequestAborted
    RequestDenied = PySide2.QtWebEngineCore.QWebEngineUrlRequestJob.Error.RequestDenied
    RequestFailed = PySide2.QtWebEngineCore.QWebEngineUrlRequestJob.Error.RequestFailed
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001FDC0D2CF40>'
    UrlInvalid = PySide2.QtWebEngineCore.QWebEngineUrlRequestJob.Error.UrlInvalid
    UrlNotFound = PySide2.QtWebEngineCore.QWebEngineUrlRequestJob.Error.UrlNotFound


class QWebEngineUrlScheme(__Shiboken.Object):
    """
    QWebEngineUrlScheme(self) -> None
    QWebEngineUrlScheme(self, name: PySide2.QtCore.QByteArray) -> None
    QWebEngineUrlScheme(self, that: PySide2.QtWebEngineCore.QWebEngineUrlScheme) -> None
    """
    def defaultPort(self): # real signature unknown; restored from __doc__
        """ defaultPort(self) -> int """
        return 0

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flags """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> PySide2.QtCore.QByteArray """
        pass

    def registerScheme(self, scheme): # real signature unknown; restored from __doc__
        """ registerScheme(scheme: PySide2.QtWebEngineCore.QWebEngineUrlScheme) -> None """
        pass

    def schemeByName(self, name): # real signature unknown; restored from __doc__
        """ schemeByName(name: PySide2.QtCore.QByteArray) -> PySide2.QtWebEngineCore.QWebEngineUrlScheme """
        pass

    def setDefaultPort(self, newValue): # real signature unknown; restored from __doc__
        """ setDefaultPort(self, newValue: int) -> None """
        pass

    def setFlags(self, newValue): # real signature unknown; restored from __doc__
        """ setFlags(self, newValue: PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flags) -> None """
        pass

    def setName(self, newValue): # real signature unknown; restored from __doc__
        """ setName(self, newValue: PySide2.QtCore.QByteArray) -> None """
        pass

    def setSyntax(self, newValue): # real signature unknown; restored from __doc__
        """ setSyntax(self, newValue: PySide2.QtWebEngineCore.QWebEngineUrlScheme.Syntax) -> None """
        pass

    def syntax(self): # real signature unknown; restored from __doc__
        """ syntax(self) -> PySide2.QtWebEngineCore.QWebEngineUrlScheme.Syntax """
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

    ContentSecurityPolicyIgnored = PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag.ContentSecurityPolicyIgnored
    CorsEnabled = PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag.CorsEnabled
    Flag = None # (!) real value is "<class 'PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag'>"
    Flags = None # (!) real value is "<class 'PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flags'>"
    LocalAccessAllowed = PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag.LocalAccessAllowed
    LocalScheme = PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag.LocalScheme
    NoAccessAllowed = PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag.NoAccessAllowed
    PortUnspecified = PySide2.QtWebEngineCore.QWebEngineUrlScheme.SpecialPort.PortUnspecified
    SecureScheme = PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag.SecureScheme
    ServiceWorkersAllowed = PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag.ServiceWorkersAllowed
    SpecialPort = None # (!) real value is "<class 'PySide2.QtWebEngineCore.QWebEngineUrlScheme.SpecialPort'>"
    Syntax = None # (!) real value is "<class 'PySide2.QtWebEngineCore.QWebEngineUrlScheme.Syntax'>"
    ViewSourceAllowed = PySide2.QtWebEngineCore.QWebEngineUrlScheme.Flag.ViewSourceAllowed
    __hash__ = None


class QWebEngineUrlSchemeHandler(__PySide2_QtCore.QObject):
    """ QWebEngineUrlSchemeHandler(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def requestStarted(self, arg__1): # real signature unknown; restored from __doc__
        """ requestStarted(self, arg__1: PySide2.QtWebEngineCore.QWebEngineUrlRequestJob) -> None """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001FDC0D2CB40>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FDBFF517B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtWebEngineCore', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FDBFF517B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtWebEngineCore.cp310-win_amd64.pyd')"

