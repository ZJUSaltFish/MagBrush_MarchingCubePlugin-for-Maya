# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSslCertificate(__Shiboken.Object):
    """
    QSslCertificate(self, data: PySide2.QtCore.QByteArray = Default(QByteArray), format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem) -> None
    QSslCertificate(self, device: PySide2.QtCore.QIODevice, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem) -> None
    QSslCertificate(self, other: PySide2.QtNetwork.QSslCertificate) -> None
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def digest(self, algorithm=None): # real signature unknown; restored from __doc__
        """ digest(self, algorithm: PySide2.QtCore.QCryptographicHash.Algorithm = PySide2.QtCore.QCryptographicHash.Algorithm.Md5) -> PySide2.QtCore.QByteArray """
        pass

    def effectiveDate(self): # real signature unknown; restored from __doc__
        """ effectiveDate(self) -> PySide2.QtCore.QDateTime """
        pass

    def expiryDate(self): # real signature unknown; restored from __doc__
        """ expiryDate(self) -> PySide2.QtCore.QDateTime """
        pass

    def extensions(self): # real signature unknown; restored from __doc__
        """ extensions(self) -> typing.List[PySide2.QtNetwork.QSslCertificateExtension] """
        pass

    def fromData(self, data, format=None): # real signature unknown; restored from __doc__
        """ fromData(data: PySide2.QtCore.QByteArray, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def fromDevice(self, device, format=None): # real signature unknown; restored from __doc__
        """ fromDevice(device: PySide2.QtCore.QIODevice, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def fromPath(self, path, format, syntax): # real signature unknown; restored from __doc__
        """
        fromPath(path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat, syntax: PySide2.QtCore.QRegExp.PatternSyntax) -> typing.List[PySide2.QtNetwork.QSslCertificate]
        fromPath(path: str, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem, syntax: PySide2.QtNetwork.QSslCertificate.PatternSyntax = PySide2.QtNetwork.QSslCertificate.PatternSyntax.FixedString) -> typing.List[PySide2.QtNetwork.QSslCertificate]
        """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def importPkcs12(self, device, key, cert, caCertificates, typing_Sequence=None, PySide2_QtNetwork_QSslCertificate=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ importPkcs12(device: PySide2.QtCore.QIODevice, key: PySide2.QtNetwork.QSslKey, cert: PySide2.QtNetwork.QSslCertificate, caCertificates: typing.Optional[typing.Sequence[PySide2.QtNetwork.QSslCertificate]] = None, passPhrase: PySide2.QtCore.QByteArray = Default(QByteArray)) -> bool """
        pass

    def isBlacklisted(self): # real signature unknown; restored from __doc__
        """ isBlacklisted(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isSelfSigned(self): # real signature unknown; restored from __doc__
        """ isSelfSigned(self) -> bool """
        return False

    def issuerDisplayName(self): # real signature unknown; restored from __doc__
        """ issuerDisplayName(self) -> str """
        return ""

    def issuerInfo(self, attribute): # real signature unknown; restored from __doc__
        """
        issuerInfo(self, attribute: PySide2.QtCore.QByteArray) -> typing.List[str]
        issuerInfo(self, info: PySide2.QtNetwork.QSslCertificate.SubjectInfo) -> typing.List[str]
        """
        pass

    def issuerInfoAttributes(self): # real signature unknown; restored from __doc__
        """ issuerInfoAttributes(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def publicKey(self): # real signature unknown; restored from __doc__
        """ publicKey(self) -> PySide2.QtNetwork.QSslKey """
        pass

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ serialNumber(self) -> PySide2.QtCore.QByteArray """
        pass

    def subjectAlternativeNames(self): # real signature unknown; restored from __doc__
        """ subjectAlternativeNames(self) -> typing.OrderedDict[PySide2.QtNetwork.QSsl.AlternativeNameEntryType, typing.List[str]] """
        pass

    def subjectDisplayName(self): # real signature unknown; restored from __doc__
        """ subjectDisplayName(self) -> str """
        return ""

    def subjectInfo(self, attribute): # real signature unknown; restored from __doc__
        """
        subjectInfo(self, attribute: PySide2.QtCore.QByteArray) -> typing.List[str]
        subjectInfo(self, info: PySide2.QtNetwork.QSslCertificate.SubjectInfo) -> typing.List[str]
        """
        pass

    def subjectInfoAttributes(self): # real signature unknown; restored from __doc__
        """ subjectInfoAttributes(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QSslCertificate) -> None """
        pass

    def toDer(self): # real signature unknown; restored from __doc__
        """ toDer(self) -> PySide2.QtCore.QByteArray """
        pass

    def toPem(self): # real signature unknown; restored from __doc__
        """ toPem(self) -> PySide2.QtCore.QByteArray """
        pass

    def toText(self): # real signature unknown; restored from __doc__
        """ toText(self) -> str """
        return ""

    def verify(self, certificateChain, PySide2_QtNetwork_QSslCertificate=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ verify(certificateChain: typing.Sequence[PySide2.QtNetwork.QSslCertificate], hostName: str = '') -> typing.List[PySide2.QtNetwork.QSslError] """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> PySide2.QtCore.QByteArray """
        pass

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

    def __init__(self, data=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    CommonName = PySide2.QtNetwork.QSslCertificate.SubjectInfo.CommonName
    CountryName = PySide2.QtNetwork.QSslCertificate.SubjectInfo.CountryName
    DistinguishedNameQualifier = PySide2.QtNetwork.QSslCertificate.SubjectInfo.DistinguishedNameQualifier
    EmailAddress = PySide2.QtNetwork.QSslCertificate.SubjectInfo.EmailAddress
    LocalityName = PySide2.QtNetwork.QSslCertificate.SubjectInfo.LocalityName
    Organization = PySide2.QtNetwork.QSslCertificate.SubjectInfo.Organization
    OrganizationalUnitName = PySide2.QtNetwork.QSslCertificate.SubjectInfo.OrganizationalUnitName
    PatternSyntax = None # (!) real value is "<class 'PySide2.QtNetwork.QSslCertificate.PatternSyntax'>"
    SerialNumber = PySide2.QtNetwork.QSslCertificate.SubjectInfo.SerialNumber
    StateOrProvinceName = PySide2.QtNetwork.QSslCertificate.SubjectInfo.StateOrProvinceName
    SubjectInfo = None # (!) real value is "<class 'PySide2.QtNetwork.QSslCertificate.SubjectInfo'>"
    __hash__ = None


