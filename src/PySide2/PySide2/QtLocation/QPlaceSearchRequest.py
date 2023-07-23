# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPlaceSearchRequest(__Shiboken.Object):
    """
    QPlaceSearchRequest(self) -> None
    QPlaceSearchRequest(self, other: PySide2.QtLocation.QPlaceSearchRequest) -> None
    """
    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> typing.List[PySide2.QtLocation.QPlaceCategory] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def limit(self): # real signature unknown; restored from __doc__
        """ limit(self) -> int """
        return 0

    def recommendationId(self): # real signature unknown; restored from __doc__
        """ recommendationId(self) -> str """
        return ""

    def relevanceHint(self): # real signature unknown; restored from __doc__
        """ relevanceHint(self) -> PySide2.QtLocation.QPlaceSearchRequest.RelevanceHint """
        pass

    def searchArea(self): # real signature unknown; restored from __doc__
        """ searchArea(self) -> PySide2.QtPositioning.QGeoShape """
        pass

    def searchContext(self): # real signature unknown; restored from __doc__
        """ searchContext(self) -> typing.Any """
        pass

    def searchTerm(self): # real signature unknown; restored from __doc__
        """ searchTerm(self) -> str """
        return ""

    def setCategories(self, categories, PySide2_QtLocation_QPlaceCategory=None): # real signature unknown; restored from __doc__
        """ setCategories(self, categories: typing.Sequence[PySide2.QtLocation.QPlaceCategory]) -> None """
        pass

    def setCategory(self, category): # real signature unknown; restored from __doc__
        """ setCategory(self, category: PySide2.QtLocation.QPlaceCategory) -> None """
        pass

    def setLimit(self, limit): # real signature unknown; restored from __doc__
        """ setLimit(self, limit: int) -> None """
        pass

    def setRecommendationId(self, recommendationId): # real signature unknown; restored from __doc__
        """ setRecommendationId(self, recommendationId: str) -> None """
        pass

    def setRelevanceHint(self, hint): # real signature unknown; restored from __doc__
        """ setRelevanceHint(self, hint: PySide2.QtLocation.QPlaceSearchRequest.RelevanceHint) -> None """
        pass

    def setSearchArea(self, area): # real signature unknown; restored from __doc__
        """ setSearchArea(self, area: PySide2.QtPositioning.QGeoShape) -> None """
        pass

    def setSearchContext(self, context): # real signature unknown; restored from __doc__
        """ setSearchContext(self, context: typing.Any) -> None """
        pass

    def setSearchTerm(self, term): # real signature unknown; restored from __doc__
        """ setSearchTerm(self, term: str) -> None """
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

    DistanceHint = PySide2.QtLocation.QPlaceSearchRequest.RelevanceHint.DistanceHint
    LexicalPlaceNameHint = PySide2.QtLocation.QPlaceSearchRequest.RelevanceHint.LexicalPlaceNameHint
    RelevanceHint = None # (!) real value is "<class 'PySide2.QtLocation.QPlaceSearchRequest.RelevanceHint'>"
    UnspecifiedHint = PySide2.QtLocation.QPlaceSearchRequest.RelevanceHint.UnspecifiedHint
    __hash__ = None


