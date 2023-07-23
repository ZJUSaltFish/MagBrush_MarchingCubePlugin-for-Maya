# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QHostAddress(__Shiboken.Object):
    """
    QHostAddress(self) -> None
    QHostAddress(self, address: PySide2.QtNetwork.QHostAddress.SpecialAddress) -> None
    QHostAddress(self, address: str) -> None
    QHostAddress(self, copy: PySide2.QtNetwork.QHostAddress) -> None
    QHostAddress(self, ip4Addr: int) -> None
    QHostAddress(self, ip6Addr: PySide2.QtNetwork.QIPv6Address) -> None
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def isBroadcast(self): # real signature unknown; restored from __doc__
        """ isBroadcast(self) -> bool """
        return False

    def isEqual(self, address, mode=None): # real signature unknown; restored from __doc__
        """ isEqual(self, address: PySide2.QtNetwork.QHostAddress, mode: PySide2.QtNetwork.QHostAddress.ConversionMode = PySide2.QtNetwork.QHostAddress.ConversionModeFlag.TolerantConversion) -> bool """
        return False

    def isGlobal(self): # real signature unknown; restored from __doc__
        """ isGlobal(self) -> bool """
        return False

    def isInSubnet(self, subnet, netmask): # real signature unknown; restored from __doc__
        """
        isInSubnet(self, subnet: PySide2.QtNetwork.QHostAddress, netmask: int) -> bool
        isInSubnet(self, subnet: typing.Tuple[PySide2.QtNetwork.QHostAddress, int]) -> bool
        """
        return False

    def isLinkLocal(self): # real signature unknown; restored from __doc__
        """ isLinkLocal(self) -> bool """
        return False

    def isLoopback(self): # real signature unknown; restored from __doc__
        """ isLoopback(self) -> bool """
        return False

    def isMulticast(self): # real signature unknown; restored from __doc__
        """ isMulticast(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isSiteLocal(self): # real signature unknown; restored from __doc__
        """ isSiteLocal(self) -> bool """
        return False

    def isUniqueLocalUnicast(self): # real signature unknown; restored from __doc__
        """ isUniqueLocalUnicast(self) -> bool """
        return False

    def parseSubnet(self, subnet): # real signature unknown; restored from __doc__
        """ parseSubnet(subnet: str) -> typing.Tuple[PySide2.QtNetwork.QHostAddress, int] """
        pass

    def protocol(self): # real signature unknown; restored from __doc__
        """ protocol(self) -> PySide2.QtNetwork.QAbstractSocket.NetworkLayerProtocol """
        pass

    def scopeId(self): # real signature unknown; restored from __doc__
        """ scopeId(self) -> str """
        return ""

    def setAddress(self, address): # real signature unknown; restored from __doc__
        """
        setAddress(self, address: PySide2.QtNetwork.QHostAddress.SpecialAddress) -> None
        setAddress(self, address: str) -> bool
        setAddress(self, ip4Addr: int) -> None
        setAddress(self, ip6Addr: PySide2.QtNetwork.QIPv6Address) -> None
        """
        pass

    def setScopeId(self, id): # real signature unknown; restored from __doc__
        """ setScopeId(self, id: str) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QHostAddress) -> None """
        pass

    def toIPv4Address(self): # real signature unknown; restored from __doc__
        """
        toIPv4Address(self) -> int
        toIPv4Address(self) -> typing.Tuple[int, bool]
        """
        return 0

    def toIPv6Address(self): # real signature unknown; restored from __doc__
        """ toIPv6Address(self) -> PySide2.QtNetwork.QIPv6Address """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    Any = PySide2.QtNetwork.QHostAddress.SpecialAddress.Any
    AnyIPv4 = PySide2.QtNetwork.QHostAddress.SpecialAddress.AnyIPv4
    AnyIPv6 = PySide2.QtNetwork.QHostAddress.SpecialAddress.AnyIPv6
    Broadcast = PySide2.QtNetwork.QHostAddress.SpecialAddress.Broadcast
    ConversionMode = None # (!) real value is "<class 'PySide2.QtNetwork.QHostAddress.ConversionMode'>"
    ConversionModeFlag = None # (!) real value is "<class 'PySide2.QtNetwork.QHostAddress.ConversionModeFlag'>"
    ConvertLocalHost = PySide2.QtNetwork.QHostAddress.ConversionModeFlag.ConvertLocalHost
    ConvertUnspecifiedAddress = PySide2.QtNetwork.QHostAddress.ConversionModeFlag.ConvertUnspecifiedAddress
    ConvertV4CompatToIPv4 = PySide2.QtNetwork.QHostAddress.ConversionModeFlag.ConvertV4CompatToIPv4
    ConvertV4MappedToIPv4 = PySide2.QtNetwork.QHostAddress.ConversionModeFlag.ConvertV4MappedToIPv4
    LocalHost = PySide2.QtNetwork.QHostAddress.SpecialAddress.LocalHost
    LocalHostIPv6 = PySide2.QtNetwork.QHostAddress.SpecialAddress.LocalHostIPv6
    Null = PySide2.QtNetwork.QHostAddress.SpecialAddress.Null
    SpecialAddress = None # (!) real value is "<class 'PySide2.QtNetwork.QHostAddress.SpecialAddress'>"
    StrictConversion = PySide2.QtNetwork.QHostAddress.ConversionModeFlag.StrictConversion
    TolerantConversion = PySide2.QtNetwork.QHostAddress.ConversionModeFlag.TolerantConversion


