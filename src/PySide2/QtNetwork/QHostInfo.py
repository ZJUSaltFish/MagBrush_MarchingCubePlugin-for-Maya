# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QHostInfo(__Shiboken.Object):
    """
    QHostInfo(self, d: PySide2.QtNetwork.QHostInfo) -> None
    QHostInfo(self, lookupId: int = -1) -> None
    """
    def abortHostLookup(self, lookupId): # real signature unknown; restored from __doc__
        """ abortHostLookup(lookupId: int) -> None """
        pass

    def addresses(self): # real signature unknown; restored from __doc__
        """ addresses(self) -> typing.List[PySide2.QtNetwork.QHostAddress] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtNetwork.QHostInfo.HostInfoError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fromName(self, name): # real signature unknown; restored from __doc__
        """ fromName(name: str) -> PySide2.QtNetwork.QHostInfo """
        pass

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def localDomainName(self): # real signature unknown; restored from __doc__
        """ localDomainName() -> str """
        return ""

    def localHostName(self): # real signature unknown; restored from __doc__
        """ localHostName() -> str """
        return ""

    def lookupId(self): # real signature unknown; restored from __doc__
        """ lookupId(self) -> int """
        return 0

    def setAddresses(self, addresses, PySide2_QtNetwork_QHostAddress=None): # real signature unknown; restored from __doc__
        """ setAddresses(self, addresses: typing.Sequence[PySide2.QtNetwork.QHostAddress]) -> None """
        pass

    def setError(self, error): # real signature unknown; restored from __doc__
        """ setError(self, error: PySide2.QtNetwork.QHostInfo.HostInfoError) -> None """
        pass

    def setErrorString(self, errorString): # real signature unknown; restored from __doc__
        """ setErrorString(self, errorString: str) -> None """
        pass

    def setHostName(self, name): # real signature unknown; restored from __doc__
        """ setHostName(self, name: str) -> None """
        pass

    def setLookupId(self, id): # real signature unknown; restored from __doc__
        """ setLookupId(self, id: int) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QHostInfo) -> None """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self, d): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    HostInfoError = None # (!) real value is "<class 'PySide2.QtNetwork.QHostInfo.HostInfoError'>"
    HostNotFound = PySide2.QtNetwork.QHostInfo.HostInfoError.HostNotFound
    NoError = PySide2.QtNetwork.QHostInfo.HostInfoError.NoError
    UnknownError = PySide2.QtNetwork.QHostInfo.HostInfoError.UnknownError


