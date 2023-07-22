# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QDnsLookup(__PySide2_QtCore.QObject):
    """
    QDnsLookup(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QDnsLookup(self, type: PySide2.QtNetwork.QDnsLookup.Type, name: str, nameserver: PySide2.QtNetwork.QHostAddress, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QDnsLookup(self, type: PySide2.QtNetwork.QDnsLookup.Type, name: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

    def canonicalNameRecords(self): # real signature unknown; restored from __doc__
        """ canonicalNameRecords(self) -> typing.List[PySide2.QtNetwork.QDnsDomainNameRecord] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtNetwork.QDnsLookup.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def hostAddressRecords(self): # real signature unknown; restored from __doc__
        """ hostAddressRecords(self) -> typing.List[PySide2.QtNetwork.QDnsHostAddressRecord] """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def lookup(self): # real signature unknown; restored from __doc__
        """ lookup(self) -> None """
        pass

    def mailExchangeRecords(self): # real signature unknown; restored from __doc__
        """ mailExchangeRecords(self) -> typing.List[PySide2.QtNetwork.QDnsMailExchangeRecord] """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def nameserver(self): # real signature unknown; restored from __doc__
        """ nameserver(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def nameserverChanged(self, *args, **kwargs): # real signature unknown
        pass

    def nameServerRecords(self): # real signature unknown; restored from __doc__
        """ nameServerRecords(self) -> typing.List[PySide2.QtNetwork.QDnsDomainNameRecord] """
        pass

    def pointerRecords(self): # real signature unknown; restored from __doc__
        """ pointerRecords(self) -> typing.List[PySide2.QtNetwork.QDnsDomainNameRecord] """
        pass

    def serviceRecords(self): # real signature unknown; restored from __doc__
        """ serviceRecords(self) -> typing.List[PySide2.QtNetwork.QDnsServiceRecord] """
        pass

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def setNameserver(self, nameserver): # real signature unknown; restored from __doc__
        """ setNameserver(self, nameserver: PySide2.QtNetwork.QHostAddress) -> None """
        pass

    def setType(self, arg__1): # real signature unknown; restored from __doc__
        """ setType(self, arg__1: PySide2.QtNetwork.QDnsLookup.Type) -> None """
        pass

    def textRecords(self): # real signature unknown; restored from __doc__
        """ textRecords(self) -> typing.List[PySide2.QtNetwork.QDnsTextRecord] """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtNetwork.QDnsLookup.Type """
        pass

    def typeChanged(self, *args, **kwargs): # real signature unknown
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

    A = PySide2.QtNetwork.QDnsLookup.Type.A
    AAAA = PySide2.QtNetwork.QDnsLookup.Type.AAAA
    ANY = PySide2.QtNetwork.QDnsLookup.Type.ANY
    CNAME = PySide2.QtNetwork.QDnsLookup.Type.CNAME
    Error = None # (!) real value is "<class 'PySide2.QtNetwork.QDnsLookup.Error'>"
    InvalidReplyError = PySide2.QtNetwork.QDnsLookup.Error.InvalidReplyError
    InvalidRequestError = PySide2.QtNetwork.QDnsLookup.Error.InvalidRequestError
    MX = PySide2.QtNetwork.QDnsLookup.Type.MX
    NoError = PySide2.QtNetwork.QDnsLookup.Error.NoError
    NotFoundError = PySide2.QtNetwork.QDnsLookup.Error.NotFoundError
    NS = PySide2.QtNetwork.QDnsLookup.Type.NS
    OperationCancelledError = PySide2.QtNetwork.QDnsLookup.Error.OperationCancelledError
    PTR = PySide2.QtNetwork.QDnsLookup.Type.PTR
    ResolverError = PySide2.QtNetwork.QDnsLookup.Error.ResolverError
    ServerFailureError = PySide2.QtNetwork.QDnsLookup.Error.ServerFailureError
    ServerRefusedError = PySide2.QtNetwork.QDnsLookup.Error.ServerRefusedError
    SRV = PySide2.QtNetwork.QDnsLookup.Type.SRV
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D85E640>'
    TXT = PySide2.QtNetwork.QDnsLookup.Type.TXT
    Type = None # (!) real value is "<class 'PySide2.QtNetwork.QDnsLookup.Type'>"


