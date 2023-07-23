# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QGeoServiceProvider(__PySide2_QtCore.QObject):
    """ QGeoServiceProvider(self, providerName: str, parameters: typing.Dict[str, typing.Any] = Default(QVariantMap), allowExperimental: bool = False) -> None """
    def availableServiceProviders(self): # real signature unknown; restored from __doc__
        """ availableServiceProviders() -> typing.List[str] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtLocation.QGeoServiceProvider.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def geocodingError(self): # real signature unknown; restored from __doc__
        """ geocodingError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error """
        pass

    def geocodingErrorString(self): # real signature unknown; restored from __doc__
        """ geocodingErrorString(self) -> str """
        return ""

    def geocodingFeatures(self): # real signature unknown; restored from __doc__
        """ geocodingFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.GeocodingFeatures """
        pass

    def geocodingManager(self): # real signature unknown; restored from __doc__
        """ geocodingManager(self) -> PySide2.QtLocation.QGeoCodingManager """
        pass

    def mappingError(self): # real signature unknown; restored from __doc__
        """ mappingError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error """
        pass

    def mappingErrorString(self): # real signature unknown; restored from __doc__
        """ mappingErrorString(self) -> str """
        return ""

    def mappingFeatures(self): # real signature unknown; restored from __doc__
        """ mappingFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.MappingFeatures """
        pass

    def navigationError(self): # real signature unknown; restored from __doc__
        """ navigationError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error """
        pass

    def navigationErrorString(self): # real signature unknown; restored from __doc__
        """ navigationErrorString(self) -> str """
        return ""

    def navigationFeatures(self): # real signature unknown; restored from __doc__
        """ navigationFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.NavigationFeatures """
        pass

    def placeManager(self): # real signature unknown; restored from __doc__
        """ placeManager(self) -> PySide2.QtLocation.QPlaceManager """
        pass

    def placesError(self): # real signature unknown; restored from __doc__
        """ placesError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error """
        pass

    def placesErrorString(self): # real signature unknown; restored from __doc__
        """ placesErrorString(self) -> str """
        return ""

    def placesFeatures(self): # real signature unknown; restored from __doc__
        """ placesFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.PlacesFeatures """
        pass

    def routingError(self): # real signature unknown; restored from __doc__
        """ routingError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error """
        pass

    def routingErrorString(self): # real signature unknown; restored from __doc__
        """ routingErrorString(self) -> str """
        return ""

    def routingFeatures(self): # real signature unknown; restored from __doc__
        """ routingFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.RoutingFeatures """
        pass

    def routingManager(self): # real signature unknown; restored from __doc__
        """ routingManager(self) -> PySide2.QtLocation.QGeoRoutingManager """
        pass

    def setAllowExperimental(self, allow): # real signature unknown; restored from __doc__
        """ setAllowExperimental(self, allow: bool) -> None """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: PySide2.QtCore.QLocale) -> None """
        pass

    def setParameters(self, parameters, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setParameters(self, parameters: typing.Dict[str, typing.Any]) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, providerName, parameters, p_str=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AlternativeRoutesFeature = PySide2.QtLocation.QGeoServiceProvider.RoutingFeature.AlternativeRoutesFeature
    AnyGeocodingFeatures = PySide2.QtLocation.QGeoServiceProvider.GeocodingFeature.AnyGeocodingFeatures
    AnyMappingFeatures = PySide2.QtLocation.QGeoServiceProvider.MappingFeature.AnyMappingFeatures
    AnyNavigationFeatures = PySide2.QtLocation.QGeoServiceProvider.NavigationFeature.AnyNavigationFeatures
    AnyPlacesFeatures = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.AnyPlacesFeatures
    AnyRoutingFeatures = PySide2.QtLocation.QGeoServiceProvider.RoutingFeature.AnyRoutingFeatures
    ConnectionError = PySide2.QtLocation.QGeoServiceProvider.Error.ConnectionError
    Error = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.Error'>"
    ExcludeAreasRoutingFeature = PySide2.QtLocation.QGeoServiceProvider.RoutingFeature.ExcludeAreasRoutingFeature
    GeocodingFeature = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.GeocodingFeature'>"
    GeocodingFeatures = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.GeocodingFeatures'>"
    LoaderError = PySide2.QtLocation.QGeoServiceProvider.Error.LoaderError
    LocalizedGeocodingFeature = PySide2.QtLocation.QGeoServiceProvider.GeocodingFeature.LocalizedGeocodingFeature
    LocalizedMappingFeature = PySide2.QtLocation.QGeoServiceProvider.MappingFeature.LocalizedMappingFeature
    LocalizedPlacesFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.LocalizedPlacesFeature
    LocalizedRoutingFeature = PySide2.QtLocation.QGeoServiceProvider.RoutingFeature.LocalizedRoutingFeature
    MappingFeature = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.MappingFeature'>"
    MappingFeatures = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.MappingFeatures'>"
    MissingRequiredParameterError = PySide2.QtLocation.QGeoServiceProvider.Error.MissingRequiredParameterError
    NavigationFeature = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.NavigationFeature'>"
    NavigationFeatures = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.NavigationFeatures'>"
    NoError = PySide2.QtLocation.QGeoServiceProvider.Error.NoError
    NoGeocodingFeatures = PySide2.QtLocation.QGeoServiceProvider.GeocodingFeature.NoGeocodingFeatures
    NoMappingFeatures = PySide2.QtLocation.QGeoServiceProvider.MappingFeature.NoMappingFeatures
    NoNavigationFeatures = PySide2.QtLocation.QGeoServiceProvider.NavigationFeature.NoNavigationFeatures
    NoPlacesFeatures = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.NoPlacesFeatures
    NoRoutingFeatures = PySide2.QtLocation.QGeoServiceProvider.RoutingFeature.NoRoutingFeatures
    NotificationsFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.NotificationsFeature
    NotSupportedError = PySide2.QtLocation.QGeoServiceProvider.Error.NotSupportedError
    OfflineGeocodingFeature = PySide2.QtLocation.QGeoServiceProvider.GeocodingFeature.OfflineGeocodingFeature
    OfflineMappingFeature = PySide2.QtLocation.QGeoServiceProvider.MappingFeature.OfflineMappingFeature
    OfflineNavigationFeature = PySide2.QtLocation.QGeoServiceProvider.NavigationFeature.OfflineNavigationFeature
    OfflinePlacesFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.OfflinePlacesFeature
    OfflineRoutingFeature = PySide2.QtLocation.QGeoServiceProvider.RoutingFeature.OfflineRoutingFeature
    OnlineGeocodingFeature = PySide2.QtLocation.QGeoServiceProvider.GeocodingFeature.OnlineGeocodingFeature
    OnlineMappingFeature = PySide2.QtLocation.QGeoServiceProvider.MappingFeature.OnlineMappingFeature
    OnlineNavigationFeature = PySide2.QtLocation.QGeoServiceProvider.NavigationFeature.OnlineNavigationFeature
    OnlinePlacesFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.OnlinePlacesFeature
    OnlineRoutingFeature = PySide2.QtLocation.QGeoServiceProvider.RoutingFeature.OnlineRoutingFeature
    PlaceMatchingFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.PlaceMatchingFeature
    PlaceRecommendationsFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.PlaceRecommendationsFeature
    PlacesFeature = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.PlacesFeature'>"
    PlacesFeatures = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.PlacesFeatures'>"
    RemoveCategoryFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.RemoveCategoryFeature
    RemovePlaceFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.RemovePlaceFeature
    ReverseGeocodingFeature = PySide2.QtLocation.QGeoServiceProvider.GeocodingFeature.ReverseGeocodingFeature
    RouteUpdatesFeature = PySide2.QtLocation.QGeoServiceProvider.RoutingFeature.RouteUpdatesFeature
    RoutingFeature = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.RoutingFeature'>"
    RoutingFeatures = None # (!) real value is "<class 'PySide2.QtLocation.QGeoServiceProvider.RoutingFeatures'>"
    SaveCategoryFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.SaveCategoryFeature
    SavePlaceFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.SavePlaceFeature
    SearchSuggestionsFeature = PySide2.QtLocation.QGeoServiceProvider.PlacesFeature.SearchSuggestionsFeature
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000013BA7555200>'
    UnknownParameterError = PySide2.QtLocation.QGeoServiceProvider.Error.UnknownParameterError


