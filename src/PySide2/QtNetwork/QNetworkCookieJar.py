# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkCookieJar(__PySide2_QtCore.QObject):
    """ QNetworkCookieJar(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def allCookies(self): # real signature unknown; restored from __doc__
        """ allCookies(self) -> typing.List[PySide2.QtNetwork.QNetworkCookie] """
        pass

    def cookiesForUrl(self, url): # real signature unknown; restored from __doc__
        """ cookiesForUrl(self, url: PySide2.QtCore.QUrl) -> typing.List[PySide2.QtNetwork.QNetworkCookie] """
        pass

    def deleteCookie(self, cookie): # real signature unknown; restored from __doc__
        """ deleteCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie) -> bool """
        return False

    def insertCookie(self, cookie): # real signature unknown; restored from __doc__
        """ insertCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie) -> bool """
        return False

    def setAllCookies(self, cookieList, PySide2_QtNetwork_QNetworkCookie=None): # real signature unknown; restored from __doc__
        """ setAllCookies(self, cookieList: typing.Sequence[PySide2.QtNetwork.QNetworkCookie]) -> None """
        pass

    def setCookiesFromUrl(self, cookieList, PySide2_QtNetwork_QNetworkCookie=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCookiesFromUrl(self, cookieList: typing.Sequence[PySide2.QtNetwork.QNetworkCookie], url: PySide2.QtCore.QUrl) -> bool """
        pass

    def updateCookie(self, cookie): # real signature unknown; restored from __doc__
        """ updateCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie) -> bool """
        return False

    def validateCookie(self, cookie, url): # real signature unknown; restored from __doc__
        """ validateCookie(self, cookie: PySide2.QtNetwork.QNetworkCookie, url: PySide2.QtCore.QUrl) -> bool """
        return False

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D86EEC0>'


