# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkProxyFactory(__Shiboken.Object):
    """ QNetworkProxyFactory(self) -> None """
    def proxyForQuery(self, query): # real signature unknown; restored from __doc__
        """ proxyForQuery(query: PySide2.QtNetwork.QNetworkProxyQuery) -> typing.List[PySide2.QtNetwork.QNetworkProxy] """
        pass

    def queryProxy(self, query=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ queryProxy(self, query: PySide2.QtNetwork.QNetworkProxyQuery = Default(QNetworkProxyQuery)) -> typing.List[PySide2.QtNetwork.QNetworkProxy] """
        pass

    def setApplicationProxyFactory(self, factory): # real signature unknown; restored from __doc__
        """ setApplicationProxyFactory(factory: PySide2.QtNetwork.QNetworkProxyFactory) -> None """
        pass

    def setUseSystemConfiguration(self, enable): # real signature unknown; restored from __doc__
        """ setUseSystemConfiguration(enable: bool) -> None """
        pass

    def systemProxyForQuery(self, query=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ systemProxyForQuery(query: PySide2.QtNetwork.QNetworkProxyQuery = Default(QNetworkProxyQuery)) -> typing.List[PySide2.QtNetwork.QNetworkProxy] """
        pass

    def usesSystemConfiguration(self): # real signature unknown; restored from __doc__
        """ usesSystemConfiguration() -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


