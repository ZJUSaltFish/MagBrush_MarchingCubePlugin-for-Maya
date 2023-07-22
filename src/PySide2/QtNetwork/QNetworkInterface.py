# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkInterface(__Shiboken.Object):
    """
    QNetworkInterface(self) -> None
    QNetworkInterface(self, other: PySide2.QtNetwork.QNetworkInterface) -> None
    """
    def addressEntries(self): # real signature unknown; restored from __doc__
        """ addressEntries(self) -> typing.List[PySide2.QtNetwork.QNetworkAddressEntry] """
        pass

    def allAddresses(self): # real signature unknown; restored from __doc__
        """ allAddresses() -> typing.List[PySide2.QtNetwork.QHostAddress] """
        pass

    def allInterfaces(self): # real signature unknown; restored from __doc__
        """ allInterfaces() -> typing.List[PySide2.QtNetwork.QNetworkInterface] """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtNetwork.QNetworkInterface.InterfaceFlags """
        pass

    def hardwareAddress(self): # real signature unknown; restored from __doc__
        """ hardwareAddress(self) -> str """
        return ""

    def humanReadableName(self): # real signature unknown; restored from __doc__
        """ humanReadableName(self) -> str """
        return ""

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> int """
        return 0

    def interfaceFromIndex(self, index): # real signature unknown; restored from __doc__
        """ interfaceFromIndex(index: int) -> PySide2.QtNetwork.QNetworkInterface """
        pass

    def interfaceFromName(self, name): # real signature unknown; restored from __doc__
        """ interfaceFromName(name: str) -> PySide2.QtNetwork.QNetworkInterface """
        pass

    def interfaceIndexFromName(self, name): # real signature unknown; restored from __doc__
        """ interfaceIndexFromName(name: str) -> int """
        return 0

    def interfaceNameFromIndex(self, index): # real signature unknown; restored from __doc__
        """ interfaceNameFromIndex(index: int) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def maximumTransmissionUnit(self): # real signature unknown; restored from __doc__
        """ maximumTransmissionUnit(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QNetworkInterface) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtNetwork.QNetworkInterface.InterfaceType """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    CanBroadcast = PySide2.QtNetwork.QNetworkInterface.InterfaceFlag.CanBroadcast
    CanBus = PySide2.QtNetwork.QNetworkInterface.InterfaceType.CanBus
    CanMulticast = PySide2.QtNetwork.QNetworkInterface.InterfaceFlag.CanMulticast
    Ethernet = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Ethernet
    Fddi = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Fddi
    Ieee1394 = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Ieee1394
    Ieee80211 = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Ieee80211
    Ieee802154 = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Ieee802154
    Ieee80216 = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Ieee80216
    InterfaceFlag = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkInterface.InterfaceFlag'>"
    InterfaceFlags = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkInterface.InterfaceFlags'>"
    InterfaceType = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkInterface.InterfaceType'>"
    IsLoopBack = PySide2.QtNetwork.QNetworkInterface.InterfaceFlag.IsLoopBack
    IsPointToPoint = PySide2.QtNetwork.QNetworkInterface.InterfaceFlag.IsPointToPoint
    IsRunning = PySide2.QtNetwork.QNetworkInterface.InterfaceFlag.IsRunning
    IsUp = PySide2.QtNetwork.QNetworkInterface.InterfaceFlag.IsUp
    Loopback = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Loopback
    Phonet = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Phonet
    Ppp = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Ppp
    SixLoWPAN = PySide2.QtNetwork.QNetworkInterface.InterfaceType.SixLoWPAN
    Slip = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Slip
    Unknown = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Unknown
    Virtual = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Virtual
    Wifi = PySide2.QtNetwork.QNetworkInterface.InterfaceType.Wifi


