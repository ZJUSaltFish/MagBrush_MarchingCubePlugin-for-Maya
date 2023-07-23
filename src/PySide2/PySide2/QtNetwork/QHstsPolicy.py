# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QHstsPolicy(__Shiboken.Object):
    """
    QHstsPolicy(self) -> None
    QHstsPolicy(self, expiry: PySide2.QtCore.QDateTime, flags: PySide2.QtNetwork.QHstsPolicy.PolicyFlags, host: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.DecodedMode) -> None
    QHstsPolicy(self, rhs: PySide2.QtNetwork.QHstsPolicy) -> None
    """
    def expiry(self): # real signature unknown; restored from __doc__
        """ expiry(self) -> PySide2.QtCore.QDateTime """
        pass

    def host(self, options=None): # real signature unknown; restored from __doc__
        """ host(self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyDecoded) -> str """
        return ""

    def includesSubDomains(self): # real signature unknown; restored from __doc__
        """ includesSubDomains(self) -> bool """
        return False

    def isExpired(self): # real signature unknown; restored from __doc__
        """ isExpired(self) -> bool """
        return False

    def setExpiry(self, expiry): # real signature unknown; restored from __doc__
        """ setExpiry(self, expiry: PySide2.QtCore.QDateTime) -> None """
        pass

    def setHost(self, host, mode=None): # real signature unknown; restored from __doc__
        """ setHost(self, host: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.DecodedMode) -> None """
        pass

    def setIncludesSubDomains(self, include): # real signature unknown; restored from __doc__
        """ setIncludesSubDomains(self, include: bool) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QHstsPolicy) -> None """
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

    IncludeSubDomains = PySide2.QtNetwork.QHstsPolicy.PolicyFlag.IncludeSubDomains
    PolicyFlag = None # (!) real value is "<class 'PySide2.QtNetwork.QHstsPolicy.PolicyFlag'>"
    PolicyFlags = None # (!) real value is "<class 'PySide2.QtNetwork.QHstsPolicy.PolicyFlags'>"
    __hash__ = None


