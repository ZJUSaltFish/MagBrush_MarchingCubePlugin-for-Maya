# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QNetworkCookie(__Shiboken.Object):
    """
    QNetworkCookie(self, name: PySide2.QtCore.QByteArray = Default(QByteArray), value: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None
    QNetworkCookie(self, other: PySide2.QtNetwork.QNetworkCookie) -> None
    """
    def domain(self): # real signature unknown; restored from __doc__
        """ domain(self) -> str """
        return ""

    def expirationDate(self): # real signature unknown; restored from __doc__
        """ expirationDate(self) -> PySide2.QtCore.QDateTime """
        pass

    def hasSameIdentifier(self, other): # real signature unknown; restored from __doc__
        """ hasSameIdentifier(self, other: PySide2.QtNetwork.QNetworkCookie) -> bool """
        return False

    def isHttpOnly(self): # real signature unknown; restored from __doc__
        """ isHttpOnly(self) -> bool """
        return False

    def isSecure(self): # real signature unknown; restored from __doc__
        """ isSecure(self) -> bool """
        return False

    def isSessionCookie(self): # real signature unknown; restored from __doc__
        """ isSessionCookie(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> PySide2.QtCore.QByteArray """
        pass

    def normalize(self, url): # real signature unknown; restored from __doc__
        """ normalize(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def parseCookies(self, cookieString): # real signature unknown; restored from __doc__
        """ parseCookies(cookieString: PySide2.QtCore.QByteArray) -> typing.List[PySide2.QtNetwork.QNetworkCookie] """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def setDomain(self, domain): # real signature unknown; restored from __doc__
        """ setDomain(self, domain: str) -> None """
        pass

    def setExpirationDate(self, date): # real signature unknown; restored from __doc__
        """ setExpirationDate(self, date: PySide2.QtCore.QDateTime) -> None """
        pass

    def setHttpOnly(self, enable): # real signature unknown; restored from __doc__
        """ setHttpOnly(self, enable: bool) -> None """
        pass

    def setName(self, cookieName): # real signature unknown; restored from __doc__
        """ setName(self, cookieName: PySide2.QtCore.QByteArray) -> None """
        pass

    def setPath(self, path): # real signature unknown; restored from __doc__
        """ setPath(self, path: str) -> None """
        pass

    def setSecure(self, enable): # real signature unknown; restored from __doc__
        """ setSecure(self, enable: bool) -> None """
        pass

    def setValue(self, value): # real signature unknown; restored from __doc__
        """ setValue(self, value: PySide2.QtCore.QByteArray) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QNetworkCookie) -> None """
        pass

    def toRawForm(self, form=None): # real signature unknown; restored from __doc__
        """ toRawForm(self, form: PySide2.QtNetwork.QNetworkCookie.RawForm = PySide2.QtNetwork.QNetworkCookie.RawForm.Full) -> PySide2.QtCore.QByteArray """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> PySide2.QtCore.QByteArray """
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

    def __init__(self, name=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Full = PySide2.QtNetwork.QNetworkCookie.RawForm.Full
    NameAndValueOnly = PySide2.QtNetwork.QNetworkCookie.RawForm.NameAndValueOnly
    RawForm = None # (!) real value is "<class 'PySide2.QtNetwork.QNetworkCookie.RawForm'>"
    __hash__ = None


