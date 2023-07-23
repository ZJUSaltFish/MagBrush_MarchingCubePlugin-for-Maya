# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSslError(__Shiboken.Object):
    """
    QSslError(self) -> None
    QSslError(self, error: PySide2.QtNetwork.QSslError.SslError) -> None
    QSslError(self, error: PySide2.QtNetwork.QSslError.SslError, certificate: PySide2.QtNetwork.QSslCertificate) -> None
    QSslError(self, other: PySide2.QtNetwork.QSslError) -> None
    """
    def certificate(self): # real signature unknown; restored from __doc__
        """ certificate(self) -> PySide2.QtNetwork.QSslCertificate """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtNetwork.QSslError.SslError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QSslError) -> None """
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

    AuthorityIssuerSerialNumberMismatch = PySide2.QtNetwork.QSslError.SslError.AuthorityIssuerSerialNumberMismatch
    CertificateBlacklisted = PySide2.QtNetwork.QSslError.SslError.CertificateBlacklisted
    CertificateExpired = PySide2.QtNetwork.QSslError.SslError.CertificateExpired
    CertificateNotYetValid = PySide2.QtNetwork.QSslError.SslError.CertificateNotYetValid
    CertificateRejected = PySide2.QtNetwork.QSslError.SslError.CertificateRejected
    CertificateRevoked = PySide2.QtNetwork.QSslError.SslError.CertificateRevoked
    CertificateSignatureFailed = PySide2.QtNetwork.QSslError.SslError.CertificateSignatureFailed
    CertificateStatusUnknown = PySide2.QtNetwork.QSslError.SslError.CertificateStatusUnknown
    CertificateUntrusted = PySide2.QtNetwork.QSslError.SslError.CertificateUntrusted
    HostNameMismatch = PySide2.QtNetwork.QSslError.SslError.HostNameMismatch
    InvalidCaCertificate = PySide2.QtNetwork.QSslError.SslError.InvalidCaCertificate
    InvalidNotAfterField = PySide2.QtNetwork.QSslError.SslError.InvalidNotAfterField
    InvalidNotBeforeField = PySide2.QtNetwork.QSslError.SslError.InvalidNotBeforeField
    InvalidPurpose = PySide2.QtNetwork.QSslError.SslError.InvalidPurpose
    NoError = PySide2.QtNetwork.QSslError.SslError.NoError
    NoPeerCertificate = PySide2.QtNetwork.QSslError.SslError.NoPeerCertificate
    NoSslSupport = PySide2.QtNetwork.QSslError.SslError.NoSslSupport
    OcspInternalError = PySide2.QtNetwork.QSslError.SslError.OcspInternalError
    OcspMalformedRequest = PySide2.QtNetwork.QSslError.SslError.OcspMalformedRequest
    OcspMalformedResponse = PySide2.QtNetwork.QSslError.SslError.OcspMalformedResponse
    OcspNoResponseFound = PySide2.QtNetwork.QSslError.SslError.OcspNoResponseFound
    OcspResponseCannotBeTrusted = PySide2.QtNetwork.QSslError.SslError.OcspResponseCannotBeTrusted
    OcspResponseCertIdUnknown = PySide2.QtNetwork.QSslError.SslError.OcspResponseCertIdUnknown
    OcspResponseExpired = PySide2.QtNetwork.QSslError.SslError.OcspResponseExpired
    OcspSigRequred = PySide2.QtNetwork.QSslError.SslError.OcspSigRequred
    OcspStatusUnknown = PySide2.QtNetwork.QSslError.SslError.OcspStatusUnknown
    OcspTryLater = PySide2.QtNetwork.QSslError.SslError.OcspTryLater
    OcspUnauthorized = PySide2.QtNetwork.QSslError.SslError.OcspUnauthorized
    PathLengthExceeded = PySide2.QtNetwork.QSslError.SslError.PathLengthExceeded
    SelfSignedCertificate = PySide2.QtNetwork.QSslError.SslError.SelfSignedCertificate
    SelfSignedCertificateInChain = PySide2.QtNetwork.QSslError.SslError.SelfSignedCertificateInChain
    SslError = None # (!) real value is "<class 'PySide2.QtNetwork.QSslError.SslError'>"
    SubjectIssuerMismatch = PySide2.QtNetwork.QSslError.SslError.SubjectIssuerMismatch
    UnableToDecodeIssuerPublicKey = PySide2.QtNetwork.QSslError.SslError.UnableToDecodeIssuerPublicKey
    UnableToDecryptCertificateSignature = PySide2.QtNetwork.QSslError.SslError.UnableToDecryptCertificateSignature
    UnableToGetIssuerCertificate = PySide2.QtNetwork.QSslError.SslError.UnableToGetIssuerCertificate
    UnableToGetLocalIssuerCertificate = PySide2.QtNetwork.QSslError.SslError.UnableToGetLocalIssuerCertificate
    UnableToVerifyFirstCertificate = PySide2.QtNetwork.QSslError.SslError.UnableToVerifyFirstCertificate
    UnspecifiedError = PySide2.QtNetwork.QSslError.SslError.UnspecifiedError
    __hash__ = None


