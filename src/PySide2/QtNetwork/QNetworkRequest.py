# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkRequest(__Shiboken.Object):
    """
    QNetworkRequest(self) -> None
    QNetworkRequest(self, other: PySide2.QtNetwork.QNetworkRequest) -> None
    QNetworkRequest(self, url: PySide2.QtCore.QUrl) -> None
    """
    def attribute(self, code, defaultValue=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ attribute(self, code: PySide2.QtNetwork.QNetworkRequest.Attribute, defaultValue: typing.Any = Invalid(typing.Any)) -> typing.Any """
        pass

    def hasRawHeader(self, headerName): # real signature unknown; restored from __doc__
        """ hasRawHeader(self, headerName: PySide2.QtCore.QByteArray) -> bool """
        return False

    def header(self, header): # real signature unknown; restored from __doc__
        """ header(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders) -> typing.Any """
        pass

    def maximumRedirectsAllowed(self): # real signature unknown; restored from __doc__
        """ maximumRedirectsAllowed(self) -> int """
        return 0

    def originatingObject(self): # real signature unknown; restored from __doc__
        """ originatingObject(self) -> PySide2.QtCore.QObject """
        pass

    def peerVerifyName(self): # real signature unknown; restored from __doc__
        """ peerVerifyName(self) -> str """
        return ""

    def priority(self): # real signature unknown; restored from __doc__
        """ priority(self) -> PySide2.QtNetwork.QNetworkRequest.Priority """
        pass

    def rawHeader(self, headerName): # real signature unknown; restored from __doc__
        """ rawHeader(self, headerName: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ rawHeaderList(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def setAttribute(self, code, value): # real signature unknown; restored from __doc__
        """ setAttribute(self, code: PySide2.QtNetwork.QNetworkRequest.Attribute, value: typing.Any) -> None """
        pass

    def setHeader(self, header, value): # real signature unknown; restored from __doc__
        """ setHeader(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders, value: typing.Any) -> None """
        pass

    def setMaximumRedirectsAllowed(self, maximumRedirectsAllowed): # real signature unknown; restored from __doc__
        """ setMaximumRedirectsAllowed(self, maximumRedirectsAllowed: int) -> None """
        pass

    def setOriginatingObject(self, p_object): # real signature unknown; restored from __doc__
        """ setOriginatingObject(self, object: PySide2.QtCore.QObject) -> None """
        pass

    def setPeerVerifyName(self, peerName): # real signature unknown; restored from __doc__
        """ setPeerVerifyName(self, peerName: str) -> None """
        pass

    def setPriority(self, priority): # real signature unknown; restored from __doc__
        """ setPriority(self, priority: PySide2.QtNetwork.QNetworkRequest.Priority) -> None """
        pass

    def setRawHeader(self, headerName, value): # real signature unknown; restored from __doc__
        """ setRawHeader(self, headerName: PySide2.QtCore.QByteArray, value: PySide2.QtCore.QByteArray) -> None """
        pass

    def setSslConfiguration(self, configuration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, configuration: PySide2.QtNetwork.QSslConfiguration) -> None """
        pass

    def setTransferTimeout(self, timeout, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setTransferTimeout(self, timeout: int = <class 'PySide2.QtNetwork.QNetworkRequest.TransferTimeoutConstant'>) -> None """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> PySide2.QtNetwork.QSslConfiguration """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QNetworkRequest) -> None """
        pass

    def transferTimeout(self): # real signature unknown; restored from __doc__
        """ transferTimeout(self) -> int """
        return 0

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

    AlwaysCache = PySide2.QtNetwork.QNetworkRequest.CacheLoadControl.AlwaysCache
    AlwaysNetwork = PySide2.QtNetwork.QNetworkRequest.CacheLoadControl.AlwaysNetwork
    Attribute = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkRequest.Attribute'>"
    AuthenticationReuseAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.AuthenticationReuseAttribute
    AutoDeleteReplyOnFinishAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.AutoDeleteReplyOnFinishAttribute
    Automatic = PySide2.QtNetwork.QNetworkRequest.LoadControl.Automatic
    BackgroundRequestAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.BackgroundRequestAttribute
    CacheLoadControl = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkRequest.CacheLoadControl'>"
    CacheLoadControlAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.CacheLoadControlAttribute
    CacheSaveControlAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.CacheSaveControlAttribute
    ConnectionEncryptedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.ConnectionEncryptedAttribute
    ContentDispositionHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.ContentDispositionHeader
    ContentLengthHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.ContentLengthHeader
    ContentTypeHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.ContentTypeHeader
    CookieHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.CookieHeader
    CookieLoadControlAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.CookieLoadControlAttribute
    CookieSaveControlAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.CookieSaveControlAttribute
    CustomVerbAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.CustomVerbAttribute
    DefaultTransferTimeoutConstant = PySide2.QtNetwork.QNetworkRequest.TransferTimeoutConstant.DefaultTransferTimeoutConstant
    DoNotBufferUploadDataAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.DoNotBufferUploadDataAttribute
    DownloadBufferAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.DownloadBufferAttribute
    EmitAllUploadProgressSignalsAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.EmitAllUploadProgressSignalsAttribute
    ETagHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.ETagHeader
    FollowRedirectsAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.FollowRedirectsAttribute
    HighPriority = PySide2.QtNetwork.QNetworkRequest.Priority.HighPriority
    Http2AllowedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.Http2AllowedAttribute
    HTTP2AllowedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.HTTP2AllowedAttribute
    Http2DirectAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.Http2DirectAttribute
    Http2WasUsedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.Http2WasUsedAttribute
    HTTP2WasUsedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.HTTP2WasUsedAttribute
    HttpPipeliningAllowedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.HttpPipeliningAllowedAttribute
    HttpPipeliningWasUsedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.HttpPipeliningWasUsedAttribute
    HttpReasonPhraseAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.HttpReasonPhraseAttribute
    HttpStatusCodeAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.HttpStatusCodeAttribute
    IfMatchHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.IfMatchHeader
    IfModifiedSinceHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.IfModifiedSinceHeader
    IfNoneMatchHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.IfNoneMatchHeader
    KnownHeaders = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkRequest.KnownHeaders'>"
    LastModifiedHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.LastModifiedHeader
    LoadControl = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkRequest.LoadControl'>"
    LocationHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.LocationHeader
    LowPriority = PySide2.QtNetwork.QNetworkRequest.Priority.LowPriority
    Manual = PySide2.QtNetwork.QNetworkRequest.LoadControl.Manual
    ManualRedirectPolicy = PySide2.QtNetwork.QNetworkRequest.RedirectPolicy.ManualRedirectPolicy
    MaximumDownloadBufferSizeAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.MaximumDownloadBufferSizeAttribute
    NoLessSafeRedirectPolicy = PySide2.QtNetwork.QNetworkRequest.RedirectPolicy.NoLessSafeRedirectPolicy
    NormalPriority = PySide2.QtNetwork.QNetworkRequest.Priority.NormalPriority
    OriginalContentLengthAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.OriginalContentLengthAttribute
    PreferCache = PySide2.QtNetwork.QNetworkRequest.CacheLoadControl.PreferCache
    PreferNetwork = PySide2.QtNetwork.QNetworkRequest.CacheLoadControl.PreferNetwork
    Priority = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkRequest.Priority'>"
    RedirectionTargetAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.RedirectionTargetAttribute
    RedirectPolicy = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkRequest.RedirectPolicy'>"
    RedirectPolicyAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.RedirectPolicyAttribute
    ResourceTypeAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.ResourceTypeAttribute
    SameOriginRedirectPolicy = PySide2.QtNetwork.QNetworkRequest.RedirectPolicy.SameOriginRedirectPolicy
    ServerHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.ServerHeader
    SetCookieHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.SetCookieHeader
    SourceIsFromCacheAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.SourceIsFromCacheAttribute
    SpdyAllowedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.SpdyAllowedAttribute
    SpdyWasUsedAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.SpdyWasUsedAttribute
    SynchronousRequestAttribute = PySide2.QtNetwork.QNetworkRequest.Attribute.SynchronousRequestAttribute
    TransferTimeoutConstant = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkRequest.TransferTimeoutConstant'>"
    User = PySide2.QtNetwork.QNetworkRequest.Attribute.User
    UserAgentHeader = PySide2.QtNetwork.QNetworkRequest.KnownHeaders.UserAgentHeader
    UserMax = PySide2.QtNetwork.QNetworkRequest.Attribute.UserMax
    UserVerifiedRedirectPolicy = PySide2.QtNetwork.QNetworkRequest.RedirectPolicy.UserVerifiedRedirectPolicy
    __hash__ = None


