# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSslConfiguration(__Shiboken.Object):
    """
    QSslConfiguration(self) -> None
    QSslConfiguration(self, other: PySide2.QtNetwork.QSslConfiguration) -> None
    """
    def addCaCertificate(self, certificate): # real signature unknown; restored from __doc__
        """ addCaCertificate(self, certificate: PySide2.QtNetwork.QSslCertificate) -> None """
        pass

    def addCaCertificates(self, certificates, PySide2_QtNetwork_QSslCertificate=None): # real signature unknown; restored from __doc__
        """
        addCaCertificates(self, certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None
        addCaCertificates(self, path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem, syntax: PySide2.QtNetwork.QSslCertificate.PatternSyntax = PySide2.QtNetwork.QSslCertificate.PatternSyntax.FixedString) -> bool
        """
        pass

    def allowedNextProtocols(self): # real signature unknown; restored from __doc__
        """ allowedNextProtocols(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def backendConfiguration(self): # real signature unknown; restored from __doc__
        """ backendConfiguration(self) -> typing.Dict[PySide2.QtCore.QByteArray, typing.Any] """
        pass

    def caCertificates(self): # real signature unknown; restored from __doc__
        """ caCertificates(self) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def ciphers(self): # real signature unknown; restored from __doc__
        """ ciphers(self) -> typing.List[PySide2.QtNetwork.QSslCipher] """
        pass

    def defaultConfiguration(self): # real signature unknown; restored from __doc__
        """ defaultConfiguration() -> PySide2.QtNetwork.QSslConfiguration """
        pass

    def defaultDtlsConfiguration(self): # real signature unknown; restored from __doc__
        """ defaultDtlsConfiguration() -> PySide2.QtNetwork.QSslConfiguration """
        pass

    def diffieHellmanParameters(self): # real signature unknown; restored from __doc__
        """ diffieHellmanParameters(self) -> PySide2.QtNetwork.QSslDiffieHellmanParameters """
        pass

    def dtlsCookieVerificationEnabled(self): # real signature unknown; restored from __doc__
        """ dtlsCookieVerificationEnabled(self) -> bool """
        return False

    def ephemeralServerKey(self): # real signature unknown; restored from __doc__
        """ ephemeralServerKey(self) -> PySide2.QtNetwork.QSslKey """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def localCertificate(self): # real signature unknown; restored from __doc__
        """ localCertificate(self) -> PySide2.QtNetwork.QSslCertificate """
        pass

    def localCertificateChain(self): # real signature unknown; restored from __doc__
        """ localCertificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def nextNegotiatedProtocol(self): # real signature unknown; restored from __doc__
        """ nextNegotiatedProtocol(self) -> PySide2.QtCore.QByteArray """
        pass

    def nextProtocolNegotiationStatus(self): # real signature unknown; restored from __doc__
        """ nextProtocolNegotiationStatus(self) -> PySide2.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus """
        pass

    def ocspStaplingEnabled(self): # real signature unknown; restored from __doc__
        """ ocspStaplingEnabled(self) -> bool """
        return False

    def peerCertificate(self): # real signature unknown; restored from __doc__
        """ peerCertificate(self) -> PySide2.QtNetwork.QSslCertificate """
        pass

    def peerCertificateChain(self): # real signature unknown; restored from __doc__
        """ peerCertificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def peerVerifyDepth(self): # real signature unknown; restored from __doc__
        """ peerVerifyDepth(self) -> int """
        return 0

    def peerVerifyMode(self): # real signature unknown; restored from __doc__
        """ peerVerifyMode(self) -> PySide2.QtNetwork.QSslSocket.PeerVerifyMode """
        pass

    def preSharedKeyIdentityHint(self): # real signature unknown; restored from __doc__
        """ preSharedKeyIdentityHint(self) -> PySide2.QtCore.QByteArray """
        pass

    def privateKey(self): # real signature unknown; restored from __doc__
        """ privateKey(self) -> PySide2.QtNetwork.QSslKey """
        pass

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol """
        pass

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ sessionCipher(self) -> PySide2.QtNetwork.QSslCipher """
        pass

    def sessionProtocol(self): # real signature unknown; restored from __doc__
        """ sessionProtocol(self) -> PySide2.QtNetwork.QSsl.SslProtocol """
        pass

    def sessionTicket(self): # real signature unknown; restored from __doc__
        """ sessionTicket(self) -> PySide2.QtCore.QByteArray """
        pass

    def sessionTicketLifeTimeHint(self): # real signature unknown; restored from __doc__
        """ sessionTicketLifeTimeHint(self) -> int """
        return 0

    def setAllowedNextProtocols(self, protocols, PySide2_QtCore_QByteArray=None): # real signature unknown; restored from __doc__
        """ setAllowedNextProtocols(self, protocols: typing.Sequence[PySide2.QtCore.QByteArray]) -> None """
        pass

    def setBackendConfiguration(self, backendConfiguration, PySide2_QtCore_QByteArray=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setBackendConfiguration(self, backendConfiguration: typing.Dict[PySide2.QtCore.QByteArray, typing.Any] = Default(QMap< QByteArray,QVariant >)) -> None """
        pass

    def setBackendConfigurationOption(self, name, value): # real signature unknown; restored from __doc__
        """ setBackendConfigurationOption(self, name: PySide2.QtCore.QByteArray, value: typing.Any) -> None """
        pass

    def setCaCertificates(self, certificates, PySide2_QtNetwork_QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setCaCertificates(self, certificates: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None """
        pass

    def setCiphers(self, ciphers, PySide2_QtNetwork_QSslCipher=None): # real signature unknown; restored from __doc__
        """ setCiphers(self, ciphers: typing.Sequence[PySide2.QtNetwork.QSslCipher]) -> None """
        pass

    def setDefaultConfiguration(self, configuration): # real signature unknown; restored from __doc__
        """ setDefaultConfiguration(configuration: PySide2.QtNetwork.QSslConfiguration) -> None """
        pass

    def setDefaultDtlsConfiguration(self, configuration): # real signature unknown; restored from __doc__
        """ setDefaultDtlsConfiguration(configuration: PySide2.QtNetwork.QSslConfiguration) -> None """
        pass

    def setDiffieHellmanParameters(self, dhparams): # real signature unknown; restored from __doc__
        """ setDiffieHellmanParameters(self, dhparams: PySide2.QtNetwork.QSslDiffieHellmanParameters) -> None """
        pass

    def setDtlsCookieVerificationEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setDtlsCookieVerificationEnabled(self, enable: bool) -> None """
        pass

    def setLocalCertificate(self, certificate): # real signature unknown; restored from __doc__
        """ setLocalCertificate(self, certificate: PySide2.QtNetwork.QSslCertificate) -> None """
        pass

    def setLocalCertificateChain(self, localChain, PySide2_QtNetwork_QSslCertificate=None): # real signature unknown; restored from __doc__
        """ setLocalCertificateChain(self, localChain: typing.Sequence[PySide2.QtNetwork.QSslCertificate]) -> None """
        pass

    def setOcspStaplingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setOcspStaplingEnabled(self, enable: bool) -> None """
        pass

    def setPeerVerifyDepth(self, depth): # real signature unknown; restored from __doc__
        """ setPeerVerifyDepth(self, depth: int) -> None """
        pass

    def setPeerVerifyMode(self, mode): # real signature unknown; restored from __doc__
        """ setPeerVerifyMode(self, mode: PySide2.QtNetwork.QSslSocket.PeerVerifyMode) -> None """
        pass

    def setPreSharedKeyIdentityHint(self, hint): # real signature unknown; restored from __doc__
        """ setPreSharedKeyIdentityHint(self, hint: PySide2.QtCore.QByteArray) -> None """
        pass

    def setPrivateKey(self, key): # real signature unknown; restored from __doc__
        """ setPrivateKey(self, key: PySide2.QtNetwork.QSslKey) -> None """
        pass

    def setProtocol(self, protocol): # real signature unknown; restored from __doc__
        """ setProtocol(self, protocol: PySide2.QtNetwork.QSsl.SslProtocol) -> None """
        pass

    def setSessionTicket(self, sessionTicket): # real signature unknown; restored from __doc__
        """ setSessionTicket(self, sessionTicket: PySide2.QtCore.QByteArray) -> None """
        pass

    def setSslOption(self, option, on): # real signature unknown; restored from __doc__
        """ setSslOption(self, option: PySide2.QtNetwork.QSsl.SslOption, on: bool) -> None """
        pass

    def supportedCiphers(self): # real signature unknown; restored from __doc__
        """ supportedCiphers() -> typing.List[PySide2.QtNetwork.QSslCipher] """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QSslConfiguration) -> None """
        pass

    def systemCaCertificates(self): # real signature unknown; restored from __doc__
        """ systemCaCertificates() -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def testSslOption(self, option): # real signature unknown; restored from __doc__
        """ testSslOption(self, option: PySide2.QtNetwork.QSsl.SslOption) -> bool """
        return False

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    ALPNProtocolHTTP2 = 'h2'
    NextProtocolHttp1_1 = 'http/1.1'
    NextProtocolNegotiationNegotiated = PySide2.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus.NextProtocolNegotiationNegotiated
    NextProtocolNegotiationNone = PySide2.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus.NextProtocolNegotiationNone
    NextProtocolNegotiationStatus = None # (!) real value is "<class 'PySide2.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus'>"
    NextProtocolNegotiationUnsupported = PySide2.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus.NextProtocolNegotiationUnsupported
    NextProtocolSpdy3_0 = 'spdy/3'
    __hash__ = None


