# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkSession(__PySide2_QtCore.QObject):
    """ QNetworkSession(self, connConfig: PySide2.QtNetwork.QNetworkConfiguration, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) -> None """
        pass

    def activeTime(self): # real signature unknown; restored from __doc__
        """ activeTime(self) -> int """
        return 0

    def bytesReceived(self): # real signature unknown; restored from __doc__
        """ bytesReceived(self) -> int """
        return 0

    def bytesWritten(self): # real signature unknown; restored from __doc__
        """ bytesWritten(self) -> int """
        return 0

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def closed(self, *args, **kwargs): # real signature unknown
        pass

    def configuration(self): # real signature unknown; restored from __doc__
        """ configuration(self) -> PySide2.QtNetwork.QNetworkConfiguration """
        pass

    def connectNotify(self, signal): # real signature unknown; restored from __doc__
        """ connectNotify(self, signal: PySide2.QtCore.QMetaMethod) -> None """
        pass

    def disconnectNotify(self, signal): # real signature unknown; restored from __doc__
        """ disconnectNotify(self, signal: PySide2.QtCore.QMetaMethod) -> None """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtNetwork.QNetworkSession.SessionError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def ignore(self): # real signature unknown; restored from __doc__
        """ ignore(self) -> None """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> PySide2.QtNetwork.QNetworkInterface """
        pass

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def migrate(self): # real signature unknown; restored from __doc__
        """ migrate(self) -> None """
        pass

    def newConfigurationActivated(self, *args, **kwargs): # real signature unknown
        pass

    def open(self): # real signature unknown; restored from __doc__
        """ open(self) -> None """
        pass

    def opened(self, *args, **kwargs): # real signature unknown
        pass

    def preferredConfigurationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) -> None """
        pass

    def sessionProperty(self, key): # real signature unknown; restored from __doc__
        """ sessionProperty(self, key: str) -> typing.Any """
        pass

    def setSessionProperty(self, key, value): # real signature unknown; restored from __doc__
        """ setSessionProperty(self, key: str, value: typing.Any) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtNetwork.QNetworkSession.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def usagePolicies(self): # real signature unknown; restored from __doc__
        """ usagePolicies(self) -> PySide2.QtNetwork.QNetworkSession.UsagePolicies """
        pass

    def usagePoliciesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def waitForOpened(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForOpened(self, msecs: int = 30000) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, connConfig, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Closing = PySide2.QtNetwork.QNetworkSession.State.Closing
    Connected = PySide2.QtNetwork.QNetworkSession.State.Connected
    Connecting = PySide2.QtNetwork.QNetworkSession.State.Connecting
    Disconnected = PySide2.QtNetwork.QNetworkSession.State.Disconnected
    Invalid = PySide2.QtNetwork.QNetworkSession.State.Invalid
    InvalidConfigurationError = PySide2.QtNetwork.QNetworkSession.SessionError.InvalidConfigurationError
    NoBackgroundTrafficPolicy = PySide2.QtNetwork.QNetworkSession.UsagePolicy.NoBackgroundTrafficPolicy
    NoPolicy = PySide2.QtNetwork.QNetworkSession.UsagePolicy.NoPolicy
    NotAvailable = PySide2.QtNetwork.QNetworkSession.State.NotAvailable
    OperationNotSupportedError = PySide2.QtNetwork.QNetworkSession.SessionError.OperationNotSupportedError
    Roaming = PySide2.QtNetwork.QNetworkSession.State.Roaming
    RoamingError = PySide2.QtNetwork.QNetworkSession.SessionError.RoamingError
    SessionAbortedError = PySide2.QtNetwork.QNetworkSession.SessionError.SessionAbortedError
    SessionError = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkSession.SessionError'>"
    State = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkSession.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D86EC40>'
    UnknownSessionError = PySide2.QtNetwork.QNetworkSession.SessionError.UnknownSessionError
    UsagePolicies = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkSession.UsagePolicies'>"
    UsagePolicy = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkSession.UsagePolicy'>"


