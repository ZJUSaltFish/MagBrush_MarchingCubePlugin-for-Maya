# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkAddressEntry(__Shiboken.Object):
    """
    QNetworkAddressEntry(self) -> None
    QNetworkAddressEntry(self, other: PySide2.QtNetwork.QNetworkAddressEntry) -> None
    """
    def broadcast(self): # real signature unknown; restored from __doc__
        """ broadcast(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def clearAddressLifetime(self): # real signature unknown; restored from __doc__
        """ clearAddressLifetime(self) -> None """
        pass

    def dnsEligibility(self): # real signature unknown; restored from __doc__
        """ dnsEligibility(self) -> PySide2.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus """
        pass

    def ip(self): # real signature unknown; restored from __doc__
        """ ip(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def isLifetimeKnown(self): # real signature unknown; restored from __doc__
        """ isLifetimeKnown(self) -> bool """
        return False

    def isPermanent(self): # real signature unknown; restored from __doc__
        """ isPermanent(self) -> bool """
        return False

    def isTemporary(self): # real signature unknown; restored from __doc__
        """ isTemporary(self) -> bool """
        return False

    def netmask(self): # real signature unknown; restored from __doc__
        """ netmask(self) -> PySide2.QtNetwork.QHostAddress """
        pass

    def preferredLifetime(self): # real signature unknown; restored from __doc__
        """ preferredLifetime(self) -> PySide2.QtCore.QDeadlineTimer """
        pass

    def prefixLength(self): # real signature unknown; restored from __doc__
        """ prefixLength(self) -> int """
        return 0

    def setAddressLifetime(self, preferred, validity): # real signature unknown; restored from __doc__
        """ setAddressLifetime(self, preferred: PySide2.QtCore.QDeadlineTimer, validity: PySide2.QtCore.QDeadlineTimer) -> None """
        pass

    def setBroadcast(self, newBroadcast): # real signature unknown; restored from __doc__
        """ setBroadcast(self, newBroadcast: PySide2.QtNetwork.QHostAddress) -> None """
        pass

    def setDnsEligibility(self, status): # real signature unknown; restored from __doc__
        """ setDnsEligibility(self, status: PySide2.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus) -> None """
        pass

    def setIp(self, newIp): # real signature unknown; restored from __doc__
        """ setIp(self, newIp: PySide2.QtNetwork.QHostAddress) -> None """
        pass

    def setNetmask(self, newNetmask): # real signature unknown; restored from __doc__
        """ setNetmask(self, newNetmask: PySide2.QtNetwork.QHostAddress) -> None """
        pass

    def setPrefixLength(self, length): # real signature unknown; restored from __doc__
        """ setPrefixLength(self, length: int) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QNetworkAddressEntry) -> None """
        pass

    def validityLifetime(self): # real signature unknown; restored from __doc__
        """ validityLifetime(self) -> PySide2.QtCore.QDeadlineTimer """
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

    DnsEligibilityStatus = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus'>"
    DnsEligibilityUnknown = PySide2.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus.DnsEligibilityUnknown
    DnsEligible = PySide2.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus.DnsEligible
    DnsIneligible = PySide2.QtNetwork.QNetworkAddressEntry.DnsEligibilityStatus.DnsIneligible
    __hash__ = None


