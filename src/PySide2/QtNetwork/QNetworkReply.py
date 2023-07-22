# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkReply(__PySide2_QtCore.QIODevice):
    """ QNetworkReply(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

    def attribute(self, code): # real signature unknown; restored from __doc__
        """ attribute(self, code: PySide2.QtNetwork.QNetworkRequest.Attribute) -> typing.Any """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def downloadProgress(self, *args, **kwargs): # real signature unknown
        pass

    def encrypted(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtNetwork.QNetworkReply.NetworkError """
        pass

    def errorOccurred(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def hasRawHeader(self, headerName): # real signature unknown; restored from __doc__
        """ hasRawHeader(self, headerName: PySide2.QtCore.QByteArray) -> bool """
        return False

    def header(self, header): # real signature unknown; restored from __doc__
        """ header(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders) -> typing.Any """
        pass

    def ignoreSslErrors(self): # real signature unknown; restored from __doc__
        """
        ignoreSslErrors(self) -> None
        ignoreSslErrors(self, errors: typing.Sequence[PySide2.QtNetwork.QSslError]) -> None
        """
        pass

    def ignoreSslErrorsImplementation(self, arg__1, PySide2_QtNetwork_QSslError=None): # real signature unknown; restored from __doc__
        """ ignoreSslErrorsImplementation(self, arg__1: typing.Sequence[PySide2.QtNetwork.QSslError]) -> None """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def manager(self): # real signature unknown; restored from __doc__
        """ manager(self) -> PySide2.QtNetwork.QNetworkAccessManager """
        pass

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def operation(self): # real signature unknown; restored from __doc__
        """ operation(self) -> PySide2.QtNetwork.QNetworkAccessManager.Operation """
        pass

    def preSharedKeyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def rawHeader(self, headerName): # real signature unknown; restored from __doc__
        """ rawHeader(self, headerName: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ rawHeaderList(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def rawHeaderPairs(self): # real signature unknown; restored from __doc__
        """ rawHeaderPairs(self) -> typing.List[typing.Tuple[PySide2.QtCore.QByteArray, PySide2.QtCore.QByteArray]] """
        pass

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def redirectAllowed(self, *args, **kwargs): # real signature unknown
        pass

    def redirected(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> PySide2.QtNetwork.QNetworkRequest """
        pass

    def setAttribute(self, code, value): # real signature unknown; restored from __doc__
        """ setAttribute(self, code: PySide2.QtNetwork.QNetworkRequest.Attribute, value: typing.Any) -> None """
        pass

    def setError(self, errorCode, errorString): # real signature unknown; restored from __doc__
        """ setError(self, errorCode: PySide2.QtNetwork.QNetworkReply.NetworkError, errorString: str) -> None """
        pass

    def setFinished(self, arg__1): # real signature unknown; restored from __doc__
        """ setFinished(self, arg__1: bool) -> None """
        pass

    def setHeader(self, header, value): # real signature unknown; restored from __doc__
        """ setHeader(self, header: PySide2.QtNetwork.QNetworkRequest.KnownHeaders, value: typing.Any) -> None """
        pass

    def setOperation(self, operation): # real signature unknown; restored from __doc__
        """ setOperation(self, operation: PySide2.QtNetwork.QNetworkAccessManager.Operation) -> None """
        pass

    def setRawHeader(self, headerName, value): # real signature unknown; restored from __doc__
        """ setRawHeader(self, headerName: PySide2.QtCore.QByteArray, value: PySide2.QtCore.QByteArray) -> None """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) -> None """
        pass

    def setRequest(self, request): # real signature unknown; restored from __doc__
        """ setRequest(self, request: PySide2.QtNetwork.QNetworkRequest) -> None """
        pass

    def setSslConfiguration(self, configuration): # real signature unknown; restored from __doc__
        """ setSslConfiguration(self, configuration: PySide2.QtNetwork.QSslConfiguration) -> None """
        pass

    def setSslConfigurationImplementation(self, arg__1): # real signature unknown; restored from __doc__
        """ setSslConfigurationImplementation(self, arg__1: PySide2.QtNetwork.QSslConfiguration) -> None """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ sslConfiguration(self) -> PySide2.QtNetwork.QSslConfiguration """
        pass

    def sslConfigurationImplementation(self, arg__1): # real signature unknown; restored from __doc__
        """ sslConfigurationImplementation(self, arg__1: PySide2.QtNetwork.QSslConfiguration) -> None """
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def uploadProgress(self, *args, **kwargs): # real signature unknown
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def writeData(self, data, len): # real signature unknown; restored from __doc__
        """ writeData(self, data: bytes, len: int) -> int """
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

    AuthenticationRequiredError = PySide2.QtNetwork.QNetworkReply.NetworkError.AuthenticationRequiredError
    BackgroundRequestNotAllowedError = PySide2.QtNetwork.QNetworkReply.NetworkError.BackgroundRequestNotAllowedError
    ConnectionRefusedError = PySide2.QtNetwork.QNetworkReply.NetworkError.ConnectionRefusedError
    ContentAccessDenied = PySide2.QtNetwork.QNetworkReply.NetworkError.ContentAccessDenied
    ContentConflictError = PySide2.QtNetwork.QNetworkReply.NetworkError.ContentConflictError
    ContentGoneError = PySide2.QtNetwork.QNetworkReply.NetworkError.ContentGoneError
    ContentNotFoundError = PySide2.QtNetwork.QNetworkReply.NetworkError.ContentNotFoundError
    ContentOperationNotPermittedError = PySide2.QtNetwork.QNetworkReply.NetworkError.ContentOperationNotPermittedError
    ContentReSendError = PySide2.QtNetwork.QNetworkReply.NetworkError.ContentReSendError
    HostNotFoundError = PySide2.QtNetwork.QNetworkReply.NetworkError.HostNotFoundError
    InsecureRedirectError = PySide2.QtNetwork.QNetworkReply.NetworkError.InsecureRedirectError
    InternalServerError = PySide2.QtNetwork.QNetworkReply.NetworkError.InternalServerError
    NetworkError = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkReply.NetworkError'>"
    NetworkSessionFailedError = PySide2.QtNetwork.QNetworkReply.NetworkError.NetworkSessionFailedError
    NoError = PySide2.QtNetwork.QNetworkReply.NetworkError.NoError
    OperationCanceledError = PySide2.QtNetwork.QNetworkReply.NetworkError.OperationCanceledError
    OperationNotImplementedError = PySide2.QtNetwork.QNetworkReply.NetworkError.OperationNotImplementedError
    ProtocolFailure = PySide2.QtNetwork.QNetworkReply.NetworkError.ProtocolFailure
    ProtocolInvalidOperationError = PySide2.QtNetwork.QNetworkReply.NetworkError.ProtocolInvalidOperationError
    ProtocolUnknownError = PySide2.QtNetwork.QNetworkReply.NetworkError.ProtocolUnknownError
    ProxyAuthenticationRequiredError = PySide2.QtNetwork.QNetworkReply.NetworkError.ProxyAuthenticationRequiredError
    ProxyConnectionClosedError = PySide2.QtNetwork.QNetworkReply.NetworkError.ProxyConnectionClosedError
    ProxyConnectionRefusedError = PySide2.QtNetwork.QNetworkReply.NetworkError.ProxyConnectionRefusedError
    ProxyNotFoundError = PySide2.QtNetwork.QNetworkReply.NetworkError.ProxyNotFoundError
    ProxyTimeoutError = PySide2.QtNetwork.QNetworkReply.NetworkError.ProxyTimeoutError
    RemoteHostClosedError = PySide2.QtNetwork.QNetworkReply.NetworkError.RemoteHostClosedError
    ServiceUnavailableError = PySide2.QtNetwork.QNetworkReply.NetworkError.ServiceUnavailableError
    SslHandshakeFailedError = PySide2.QtNetwork.QNetworkReply.NetworkError.SslHandshakeFailedError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D86E000>'
    TemporaryNetworkFailureError = PySide2.QtNetwork.QNetworkReply.NetworkError.TemporaryNetworkFailureError
    TimeoutError = PySide2.QtNetwork.QNetworkReply.NetworkError.TimeoutError
    TooManyRedirectsError = PySide2.QtNetwork.QNetworkReply.NetworkError.TooManyRedirectsError
    UnknownContentError = PySide2.QtNetwork.QNetworkReply.NetworkError.UnknownContentError
    UnknownNetworkError = PySide2.QtNetwork.QNetworkReply.NetworkError.UnknownNetworkError
    UnknownProxyError = PySide2.QtNetwork.QNetworkReply.NetworkError.UnknownProxyError
    UnknownServerError = PySide2.QtNetwork.QNetworkReply.NetworkError.UnknownServerError


