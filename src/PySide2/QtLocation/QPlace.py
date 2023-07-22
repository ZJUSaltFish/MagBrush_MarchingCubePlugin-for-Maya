# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPlace(__Shiboken.Object):
    """
    QPlace(self) -> None
    QPlace(self, other: PySide2.QtLocation.QPlace) -> None
    """
    def appendContactDetail(self, contactType, detail): # real signature unknown; restored from __doc__
        """ appendContactDetail(self, contactType: str, detail: PySide2.QtLocation.QPlaceContactDetail) -> None """
        pass

    def attribution(self): # real signature unknown; restored from __doc__
        """ attribution(self) -> str """
        return ""

    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> typing.List[PySide2.QtLocation.QPlaceCategory] """
        pass

    def contactDetails(self, contactType): # real signature unknown; restored from __doc__
        """ contactDetails(self, contactType: str) -> typing.List[PySide2.QtLocation.QPlaceContactDetail] """
        pass

    def contactTypes(self): # real signature unknown; restored from __doc__
        """ contactTypes(self) -> typing.List[str] """
        pass

    def content(self, type): # real signature unknown; restored from __doc__
        """ content(self, type: PySide2.QtLocation.QPlaceContent.Type) -> typing.Dict[int, PySide2.QtLocation.QPlaceContent] """
        pass

    def detailsFetched(self): # real signature unknown; restored from __doc__
        """ detailsFetched(self) -> bool """
        return False

    def extendedAttribute(self, attributeType): # real signature unknown; restored from __doc__
        """ extendedAttribute(self, attributeType: str) -> PySide2.QtLocation.QPlaceAttribute """
        pass

    def extendedAttributeTypes(self): # real signature unknown; restored from __doc__
        """ extendedAttributeTypes(self) -> typing.List[str] """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtLocation.QPlaceIcon """
        pass

    def insertContent(self, type, content, p_int=None, PySide2_QtLocation_QPlaceContent=None): # real signature unknown; restored from __doc__
        """ insertContent(self, type: PySide2.QtLocation.QPlaceContent.Type, content: typing.Dict[int, PySide2.QtLocation.QPlaceContent]) -> None """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def location(self): # real signature unknown; restored from __doc__
        """ location(self) -> PySide2.QtPositioning.QGeoLocation """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def placeId(self): # real signature unknown; restored from __doc__
        """ placeId(self) -> str """
        return ""

    def primaryEmail(self): # real signature unknown; restored from __doc__
        """ primaryEmail(self) -> str """
        return ""

    def primaryFax(self): # real signature unknown; restored from __doc__
        """ primaryFax(self) -> str """
        return ""

    def primaryPhone(self): # real signature unknown; restored from __doc__
        """ primaryPhone(self) -> str """
        return ""

    def primaryWebsite(self): # real signature unknown; restored from __doc__
        """ primaryWebsite(self) -> PySide2.QtCore.QUrl """
        pass

    def ratings(self): # real signature unknown; restored from __doc__
        """ ratings(self) -> PySide2.QtLocation.QPlaceRatings """
        pass

    def removeContactDetails(self, contactType): # real signature unknown; restored from __doc__
        """ removeContactDetails(self, contactType: str) -> None """
        pass

    def removeExtendedAttribute(self, attributeType): # real signature unknown; restored from __doc__
        """ removeExtendedAttribute(self, attributeType: str) -> None """
        pass

    def setAttribution(self, attribution): # real signature unknown; restored from __doc__
        """ setAttribution(self, attribution: str) -> None """
        pass

    def setCategories(self, categories, PySide2_QtLocation_QPlaceCategory=None): # real signature unknown; restored from __doc__
        """ setCategories(self, categories: typing.Sequence[PySide2.QtLocation.QPlaceCategory]) -> None """
        pass

    def setCategory(self, category): # real signature unknown; restored from __doc__
        """ setCategory(self, category: PySide2.QtLocation.QPlaceCategory) -> None """
        pass

    def setContactDetails(self, contactType, details, PySide2_QtLocation_QPlaceContactDetail=None): # real signature unknown; restored from __doc__
        """ setContactDetails(self, contactType: str, details: typing.Sequence[PySide2.QtLocation.QPlaceContactDetail]) -> None """
        pass

    def setContent(self, type, content, p_int=None, PySide2_QtLocation_QPlaceContent=None): # real signature unknown; restored from __doc__
        """ setContent(self, type: PySide2.QtLocation.QPlaceContent.Type, content: typing.Dict[int, PySide2.QtLocation.QPlaceContent]) -> None """
        pass

    def setDetailsFetched(self, fetched): # real signature unknown; restored from __doc__
        """ setDetailsFetched(self, fetched: bool) -> None """
        pass

    def setExtendedAttribute(self, attributeType, attribute): # real signature unknown; restored from __doc__
        """ setExtendedAttribute(self, attributeType: str, attribute: PySide2.QtLocation.QPlaceAttribute) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtLocation.QPlaceIcon) -> None """
        pass

    def setLocation(self, location): # real signature unknown; restored from __doc__
        """ setLocation(self, location: PySide2.QtPositioning.QGeoLocation) -> None """
        pass

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def setPlaceId(self, identifier): # real signature unknown; restored from __doc__
        """ setPlaceId(self, identifier: str) -> None """
        pass

    def setRatings(self, ratings): # real signature unknown; restored from __doc__
        """ setRatings(self, ratings: PySide2.QtLocation.QPlaceRatings) -> None """
        pass

    def setSupplier(self, supplier): # real signature unknown; restored from __doc__
        """ setSupplier(self, supplier: PySide2.QtLocation.QPlaceSupplier) -> None """
        pass

    def setTotalContentCount(self, type, total): # real signature unknown; restored from __doc__
        """ setTotalContentCount(self, type: PySide2.QtLocation.QPlaceContent.Type, total: int) -> None """
        pass

    def supplier(self): # real signature unknown; restored from __doc__
        """ supplier(self) -> PySide2.QtLocation.QPlaceSupplier """
        pass

    def totalContentCount(self, type): # real signature unknown; restored from __doc__
        """ totalContentCount(self, type: PySide2.QtLocation.QPlaceContent.Type) -> int """
        return 0

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


