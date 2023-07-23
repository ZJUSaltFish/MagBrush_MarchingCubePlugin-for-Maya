# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkConfigurationManager(__PySide2_QtCore.QObject):
    """ QNetworkConfigurationManager(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def allConfigurations(self, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ allConfigurations(self, flags: PySide2.QtNetwork.QNetworkConfiguration.StateFlags = Default(QNetworkConfiguration.StateFlags)) -> typing.List[PySide2.QtNetwork.QNetworkConfiguration] """
        pass

    def capabilities(self): # real signature unknown; restored from __doc__
        """ capabilities(self) -> PySide2.QtNetwork.QNetworkConfigurationManager.Capabilities """
        pass

    def configurationAdded(self, *args, **kwargs): # real signature unknown
        pass

    def configurationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def configurationFromIdentifier(self, identifier): # real signature unknown; restored from __doc__
        """ configurationFromIdentifier(self, identifier: str) -> PySide2.QtNetwork.QNetworkConfiguration """
        pass

    def configurationRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def defaultConfiguration(self): # real signature unknown; restored from __doc__
        """ defaultConfiguration(self) -> PySide2.QtNetwork.QNetworkConfiguration """
        pass

    def isOnline(self): # real signature unknown; restored from __doc__
        """ isOnline(self) -> bool """
        return False

    def onlineStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def updateCompleted(self, *args, **kwargs): # real signature unknown
        pass

    def updateConfigurations(self): # real signature unknown; restored from __doc__
        """ updateConfigurations(self) -> None """
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

    ApplicationLevelRoaming = PySide2.QtNetwork.QNetworkConfigurationManager.Capability.ApplicationLevelRoaming
    CanStartAndStopInterfaces = PySide2.QtNetwork.QNetworkConfigurationManager.Capability.CanStartAndStopInterfaces
    Capabilities = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkConfigurationManager.Capabilities'>"
    Capability = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkConfigurationManager.Capability'>"
    DataStatistics = PySide2.QtNetwork.QNetworkConfigurationManager.Capability.DataStatistics
    DirectConnectionRouting = PySide2.QtNetwork.QNetworkConfigurationManager.Capability.DirectConnectionRouting
    ForcedRoaming = PySide2.QtNetwork.QNetworkConfigurationManager.Capability.ForcedRoaming
    NetworkSessionRequired = PySide2.QtNetwork.QNetworkConfigurationManager.Capability.NetworkSessionRequired
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D86F3C0>'
    SystemSessionSupport = PySide2.QtNetwork.QNetworkConfigurationManager.Capability.SystemSessionSupport


