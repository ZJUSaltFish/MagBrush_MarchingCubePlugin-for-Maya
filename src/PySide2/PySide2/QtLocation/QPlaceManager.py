# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPlaceManager(__PySide2_QtCore.QObject):
    # no doc
    def category(self, categoryId): # real signature unknown; restored from __doc__
        """ category(self, categoryId: str) -> PySide2.QtLocation.QPlaceCategory """
        pass

    def categoryAdded(self, *args, **kwargs): # real signature unknown
        pass

    def categoryRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def categoryUpdated(self, *args, **kwargs): # real signature unknown
        pass

    def childCategories(self, parentId=''): # real signature unknown; restored from __doc__
        """ childCategories(self, parentId: str = '') -> typing.List[PySide2.QtLocation.QPlaceCategory] """
        pass

    def childCategoryIds(self, parentId=''): # real signature unknown; restored from __doc__
        """ childCategoryIds(self, parentId: str = '') -> typing.List[str] """
        pass

    def compatiblePlace(self, place): # real signature unknown; restored from __doc__
        """ compatiblePlace(self, place: PySide2.QtLocation.QPlace) -> PySide2.QtLocation.QPlace """
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def getPlaceContent(self, request): # real signature unknown; restored from __doc__
        """ getPlaceContent(self, request: PySide2.QtLocation.QPlaceContentRequest) -> PySide2.QtLocation.QPlaceContentReply """
        pass

    def getPlaceDetails(self, placeId): # real signature unknown; restored from __doc__
        """ getPlaceDetails(self, placeId: str) -> PySide2.QtLocation.QPlaceDetailsReply """
        pass

    def initializeCategories(self): # real signature unknown; restored from __doc__
        """ initializeCategories(self) -> PySide2.QtLocation.QPlaceReply """
        pass

    def locales(self): # real signature unknown; restored from __doc__
        """ locales(self) -> typing.List[PySide2.QtCore.QLocale] """
        pass

    def managerName(self): # real signature unknown; restored from __doc__
        """ managerName(self) -> str """
        return ""

    def managerVersion(self): # real signature unknown; restored from __doc__
        """ managerVersion(self) -> int """
        return 0

    def matchingPlaces(self, request): # real signature unknown; restored from __doc__
        """ matchingPlaces(self, request: PySide2.QtLocation.QPlaceMatchRequest) -> PySide2.QtLocation.QPlaceMatchReply """
        pass

    def parentCategoryId(self, categoryId): # real signature unknown; restored from __doc__
        """ parentCategoryId(self, categoryId: str) -> str """
        return ""

    def placeAdded(self, *args, **kwargs): # real signature unknown
        pass

    def placeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def placeUpdated(self, *args, **kwargs): # real signature unknown
        pass

    def removeCategory(self, categoryId): # real signature unknown; restored from __doc__
        """ removeCategory(self, categoryId: str) -> PySide2.QtLocation.QPlaceIdReply """
        pass

    def removePlace(self, placeId): # real signature unknown; restored from __doc__
        """ removePlace(self, placeId: str) -> PySide2.QtLocation.QPlaceIdReply """
        pass

    def saveCategory(self, category, parentId=''): # real signature unknown; restored from __doc__
        """ saveCategory(self, category: PySide2.QtLocation.QPlaceCategory, parentId: str = '') -> PySide2.QtLocation.QPlaceIdReply """
        pass

    def savePlace(self, place): # real signature unknown; restored from __doc__
        """ savePlace(self, place: PySide2.QtLocation.QPlace) -> PySide2.QtLocation.QPlaceIdReply """
        pass

    def search(self, query): # real signature unknown; restored from __doc__
        """ search(self, query: PySide2.QtLocation.QPlaceSearchRequest) -> PySide2.QtLocation.QPlaceSearchReply """
        pass

    def searchSuggestions(self, request): # real signature unknown; restored from __doc__
        """ searchSuggestions(self, request: PySide2.QtLocation.QPlaceSearchRequest) -> PySide2.QtLocation.QPlaceSearchSuggestionReply """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: PySide2.QtCore.QLocale) -> None """
        pass

    def setLocales(self, locale, PySide2_QtCore_QLocale=None): # real signature unknown; restored from __doc__
        """ setLocales(self, locale: typing.Sequence[PySide2.QtCore.QLocale]) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000013BA752F8C0>'


