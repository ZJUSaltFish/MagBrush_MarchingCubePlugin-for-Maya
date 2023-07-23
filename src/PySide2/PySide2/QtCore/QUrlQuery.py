# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QUrlQuery(__Shiboken.Object):
    """
    QUrlQuery(self) -> None
    QUrlQuery(self, other: PySide2.QtCore.QUrlQuery) -> None
    QUrlQuery(self, queryString: str) -> None
    QUrlQuery(self, url: PySide2.QtCore.QUrl) -> None
    """
    def addQueryItem(self, key, value): # real signature unknown; restored from __doc__
        """ addQueryItem(self, key: str, value: str) -> None """
        pass

    def allQueryItemValues(self, key, encoding=None): # real signature unknown; restored from __doc__
        """ allQueryItemValues(self, key: str, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> typing.List[str] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def defaultQueryPairDelimiter(self): # real signature unknown; restored from __doc__
        """ defaultQueryPairDelimiter() -> str """
        return ""

    def defaultQueryValueDelimiter(self): # real signature unknown; restored from __doc__
        """ defaultQueryValueDelimiter() -> str """
        return ""

    def hasQueryItem(self, key): # real signature unknown; restored from __doc__
        """ hasQueryItem(self, key: str) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def query(self, encoding=None): # real signature unknown; restored from __doc__
        """ query(self, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> str """
        return ""

    def queryItems(self, encoding=None): # real signature unknown; restored from __doc__
        """ queryItems(self, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> typing.List[typing.Tuple[str, str]] """
        pass

    def queryItemValue(self, key, encoding=None): # real signature unknown; restored from __doc__
        """ queryItemValue(self, key: str, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> str """
        return ""

    def queryPairDelimiter(self): # real signature unknown; restored from __doc__
        """ queryPairDelimiter(self) -> str """
        return ""

    def queryValueDelimiter(self): # real signature unknown; restored from __doc__
        """ queryValueDelimiter(self) -> str """
        return ""

    def removeAllQueryItems(self, key): # real signature unknown; restored from __doc__
        """ removeAllQueryItems(self, key: str) -> None """
        pass

    def removeQueryItem(self, key): # real signature unknown; restored from __doc__
        """ removeQueryItem(self, key: str) -> None """
        pass

    def setQuery(self, queryString): # real signature unknown; restored from __doc__
        """ setQuery(self, queryString: str) -> None """
        pass

    def setQueryDelimiters(self, valueDelimiter, pairDelimiter): # real signature unknown; restored from __doc__
        """ setQueryDelimiters(self, valueDelimiter: str, pairDelimiter: str) -> None """
        pass

    def setQueryItems(self, query, typing_Tuple=None, p_str=None, p_str=None_1): # real signature unknown; restored from __doc__
        """ setQueryItems(self, query: typing.Sequence[typing.Tuple[str, str]]) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QUrlQuery) -> None """
        pass

    def toString(self, encoding=None): # real signature unknown; restored from __doc__
        """ toString(self, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> str """
        return ""

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

    __hash__ = None


