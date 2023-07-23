# encoding: utf-8
# module PyQt5.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QHostInfo(__sip.simplewrapper):
    """
    QHostInfo(id: int = -1)
    QHostInfo(d: QHostInfo)
    """
    def abortHostLookup(self, lookupId): # real signature unknown; restored from __doc__
        """ abortHostLookup(lookupId: int) """
        pass

    def addresses(self): # real signature unknown; restored from __doc__
        """ addresses(self) -> List[QHostAddress] """
        return []

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QHostInfo.HostInfoError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fromName(self, name): # real signature unknown; restored from __doc__
        """ fromName(name: str) -> QHostInfo """
        return QHostInfo

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def localDomainName(self): # real signature unknown; restored from __doc__
        """ localDomainName() -> str """
        return ""

    def localHostName(self): # real signature unknown; restored from __doc__
        """ localHostName() -> str """
        return ""

    def lookupHost(self, name, slot): # real signature unknown; restored from __doc__
        """ lookupHost(name: str, slot: PYQT_SLOT) -> int """
        return 0

    def lookupId(self): # real signature unknown; restored from __doc__
        """ lookupId(self) -> int """
        return 0

    def setAddresses(self, addresses, Union=None, QHostAddress=None, QHostAddress_SpecialAddress=None): # real signature unknown; restored from __doc__
        """ setAddresses(self, addresses: Iterable[Union[QHostAddress, QHostAddress.SpecialAddress]]) """
        pass

    def setError(self, error): # real signature unknown; restored from __doc__
        """ setError(self, error: QHostInfo.HostInfoError) """
        pass

    def setErrorString(self, errorString): # real signature unknown; restored from __doc__
        """ setErrorString(self, errorString: str) """
        pass

    def setHostName(self, name): # real signature unknown; restored from __doc__
        """ setHostName(self, name: str) """
        pass

    def setLookupId(self, id): # real signature unknown; restored from __doc__
        """ setLookupId(self, id: int) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QHostInfo) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    HostNotFound = 1
    NoError = 0
    UnknownError = 2


