# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPlaceSearchResult(__Shiboken.Object):
    """
    QPlaceSearchResult(self) -> None
    QPlaceSearchResult(self, other: PySide2.QtLocation.QPlaceSearchResult) -> None
    """
    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtLocation.QPlaceIcon """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtLocation.QPlaceIcon) -> None """
        pass

    def setTitle(self, title): # real signature unknown; restored from __doc__
        """ setTitle(self, title: str) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtLocation.QPlaceSearchResult.SearchResultType """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    PlaceResult = PySide2.QtLocation.QPlaceSearchResult.SearchResultType.PlaceResult
    ProposedSearchResult = PySide2.QtLocation.QPlaceSearchResult.SearchResultType.ProposedSearchResult
    SearchResultType = None # (!) real value is "<class 'PySide2.QtLocation.QPlaceSearchResult.SearchResultType'>"
    UnknownSearchResult = PySide2.QtLocation.QPlaceSearchResult.SearchResultType.UnknownSearchResult
    __hash__ = None


