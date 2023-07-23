# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkConfiguration(__Shiboken.Object):
    """
    QNetworkConfiguration(self) -> None
    QNetworkConfiguration(self, other: PySide2.QtNetwork.QNetworkConfiguration) -> None
    """
    def bearerType(self): # real signature unknown; restored from __doc__
        """ bearerType(self) -> PySide2.QtNetwork.QNetworkConfiguration.BearerType """
        pass

    def bearerTypeFamily(self): # real signature unknown; restored from __doc__
        """ bearerTypeFamily(self) -> PySide2.QtNetwork.QNetworkConfiguration.BearerType """
        pass

    def bearerTypeName(self): # real signature unknown; restored from __doc__
        """ bearerTypeName(self) -> str """
        return ""

    def children(self): # real signature unknown; restored from __doc__
        """ children(self) -> typing.List[PySide2.QtNetwork.QNetworkConfiguration] """
        pass

    def connectTimeout(self): # real signature unknown; restored from __doc__
        """ connectTimeout(self) -> int """
        return 0

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> str """
        return ""

    def isRoamingAvailable(self): # real signature unknown; restored from __doc__
        """ isRoamingAvailable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def purpose(self): # real signature unknown; restored from __doc__
        """ purpose(self) -> PySide2.QtNetwork.QNetworkConfiguration.Purpose """
        pass

    def setConnectTimeout(self, timeout): # real signature unknown; restored from __doc__
        """ setConnectTimeout(self, timeout: int) -> bool """
        return False

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtNetwork.QNetworkConfiguration.StateFlags """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QNetworkConfiguration) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtNetwork.QNetworkConfiguration.Type """
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

    Active = PySide2.QtNetwork.QNetworkConfiguration.StateFlag.Active
    Bearer2G = PySide2.QtNetwork.QNetworkConfiguration.BearerType.Bearer2G
    Bearer3G = PySide2.QtNetwork.QNetworkConfiguration.BearerType.Bearer3G
    Bearer4G = PySide2.QtNetwork.QNetworkConfiguration.BearerType.Bearer4G
    BearerBluetooth = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerBluetooth
    BearerCDMA2000 = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerCDMA2000
    BearerEthernet = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerEthernet
    BearerEVDO = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerEVDO
    BearerHSPA = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerHSPA
    BearerLTE = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerLTE
    BearerType = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkConfiguration.BearerType'>"
    BearerUnknown = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerUnknown
    BearerWCDMA = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerWCDMA
    BearerWiMAX = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerWiMAX
    BearerWLAN = PySide2.QtNetwork.QNetworkConfiguration.BearerType.BearerWLAN
    Defined = PySide2.QtNetwork.QNetworkConfiguration.StateFlag.Defined
    Discovered = PySide2.QtNetwork.QNetworkConfiguration.StateFlag.Discovered
    InternetAccessPoint = PySide2.QtNetwork.QNetworkConfiguration.Type.InternetAccessPoint
    Invalid = PySide2.QtNetwork.QNetworkConfiguration.Type.Invalid
    PrivatePurpose = PySide2.QtNetwork.QNetworkConfiguration.Purpose.PrivatePurpose
    PublicPurpose = PySide2.QtNetwork.QNetworkConfiguration.Purpose.PublicPurpose
    Purpose = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkConfiguration.Purpose'>"
    ServiceNetwork = PySide2.QtNetwork.QNetworkConfiguration.Type.ServiceNetwork
    ServiceSpecificPurpose = PySide2.QtNetwork.QNetworkConfiguration.Purpose.ServiceSpecificPurpose
    StateFlag = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkConfiguration.StateFlag'>"
    StateFlags = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkConfiguration.StateFlags'>"
    Type = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkConfiguration.Type'>"
    Undefined = PySide2.QtNetwork.QNetworkConfiguration.StateFlag.Undefined
    UnknownPurpose = PySide2.QtNetwork.QNetworkConfiguration.Purpose.UnknownPurpose
    UserChoice = PySide2.QtNetwork.QNetworkConfiguration.Type.UserChoice
    __hash__ = None


