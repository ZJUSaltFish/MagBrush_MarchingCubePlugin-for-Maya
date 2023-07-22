# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QGeoRouteRequest(__Shiboken.Object):
    """
    QGeoRouteRequest(self, origin: PySide2.QtPositioning.QGeoCoordinate, destination: PySide2.QtPositioning.QGeoCoordinate) -> None
    QGeoRouteRequest(self, other: PySide2.QtLocation.QGeoRouteRequest) -> None
    QGeoRouteRequest(self, waypoints: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate] = Default(QList< QGeoCoordinate >)) -> None
    """
    def departureTime(self): # real signature unknown; restored from __doc__
        """ departureTime(self) -> PySide2.QtCore.QDateTime """
        pass

    def excludeAreas(self): # real signature unknown; restored from __doc__
        """ excludeAreas(self) -> typing.List[PySide2.QtPositioning.QGeoRectangle] """
        pass

    def extraParameters(self): # real signature unknown; restored from __doc__
        """ extraParameters(self) -> typing.Dict[str, typing.Any] """
        pass

    def featureTypes(self): # real signature unknown; restored from __doc__
        """ featureTypes(self) -> typing.List[PySide2.QtLocation.QGeoRouteRequest.FeatureType] """
        pass

    def featureWeight(self, featureType): # real signature unknown; restored from __doc__
        """ featureWeight(self, featureType: PySide2.QtLocation.QGeoRouteRequest.FeatureType) -> PySide2.QtLocation.QGeoRouteRequest.FeatureWeight """
        pass

    def maneuverDetail(self): # real signature unknown; restored from __doc__
        """ maneuverDetail(self) -> PySide2.QtLocation.QGeoRouteRequest.ManeuverDetail """
        pass

    def numberAlternativeRoutes(self): # real signature unknown; restored from __doc__
        """ numberAlternativeRoutes(self) -> int """
        return 0

    def routeOptimization(self): # real signature unknown; restored from __doc__
        """ routeOptimization(self) -> PySide2.QtLocation.QGeoRouteRequest.RouteOptimizations """
        pass

    def segmentDetail(self): # real signature unknown; restored from __doc__
        """ segmentDetail(self) -> PySide2.QtLocation.QGeoRouteRequest.SegmentDetail """
        pass

    def setDepartureTime(self, departureTime): # real signature unknown; restored from __doc__
        """ setDepartureTime(self, departureTime: PySide2.QtCore.QDateTime) -> None """
        pass

    def setExcludeAreas(self, areas, PySide2_QtPositioning_QGeoRectangle=None): # real signature unknown; restored from __doc__
        """ setExcludeAreas(self, areas: typing.Sequence[PySide2.QtPositioning.QGeoRectangle]) -> None """
        pass

    def setExtraParameters(self, extraParameters, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setExtraParameters(self, extraParameters: typing.Dict[str, typing.Any]) -> None """
        pass

    def setFeatureWeight(self, featureType, featureWeight): # real signature unknown; restored from __doc__
        """ setFeatureWeight(self, featureType: PySide2.QtLocation.QGeoRouteRequest.FeatureType, featureWeight: PySide2.QtLocation.QGeoRouteRequest.FeatureWeight) -> None """
        pass

    def setManeuverDetail(self, maneuverDetail): # real signature unknown; restored from __doc__
        """ setManeuverDetail(self, maneuverDetail: PySide2.QtLocation.QGeoRouteRequest.ManeuverDetail) -> None """
        pass

    def setNumberAlternativeRoutes(self, alternatives): # real signature unknown; restored from __doc__
        """ setNumberAlternativeRoutes(self, alternatives: int) -> None """
        pass

    def setRouteOptimization(self, optimization): # real signature unknown; restored from __doc__
        """ setRouteOptimization(self, optimization: PySide2.QtLocation.QGeoRouteRequest.RouteOptimizations) -> None """
        pass

    def setSegmentDetail(self, segmentDetail): # real signature unknown; restored from __doc__
        """ setSegmentDetail(self, segmentDetail: PySide2.QtLocation.QGeoRouteRequest.SegmentDetail) -> None """
        pass

    def setTravelModes(self, travelModes): # real signature unknown; restored from __doc__
        """ setTravelModes(self, travelModes: PySide2.QtLocation.QGeoRouteRequest.TravelModes) -> None """
        pass

    def setWaypoints(self, waypoints, PySide2_QtPositioning_QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setWaypoints(self, waypoints: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate]) -> None """
        pass

    def setWaypointsMetadata(self, waypointMetadata, typing_Dict=None, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setWaypointsMetadata(self, waypointMetadata: typing.Sequence[typing.Dict[str, typing.Any]]) -> None """
        pass

    def travelModes(self): # real signature unknown; restored from __doc__
        """ travelModes(self) -> PySide2.QtLocation.QGeoRouteRequest.TravelModes """
        pass

    def waypoints(self): # real signature unknown; restored from __doc__
        """ waypoints(self) -> typing.List[PySide2.QtPositioning.QGeoCoordinate] """
        pass

    def waypointsMetadata(self): # real signature unknown; restored from __doc__
        """ waypointsMetadata(self) -> typing.List[typing.Dict[str, typing.Any]] """
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

    def __init__(self, origin, destination): # real signature unknown; restored from __doc__
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

    AvoidFeatureWeight = PySide2.QtLocation.QGeoRouteRequest.FeatureWeight.AvoidFeatureWeight
    BasicManeuvers = PySide2.QtLocation.QGeoRouteRequest.ManeuverDetail.BasicManeuvers
    BasicSegmentData = PySide2.QtLocation.QGeoRouteRequest.SegmentDetail.BasicSegmentData
    BicycleTravel = PySide2.QtLocation.QGeoRouteRequest.TravelMode.BicycleTravel
    CarTravel = PySide2.QtLocation.QGeoRouteRequest.TravelMode.CarTravel
    DirtRoadFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.DirtRoadFeature
    DisallowFeatureWeight = PySide2.QtLocation.QGeoRouteRequest.FeatureWeight.DisallowFeatureWeight
    FastestRoute = PySide2.QtLocation.QGeoRouteRequest.RouteOptimization.FastestRoute
    FeatureType = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.FeatureType'>"
    FeatureTypes = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.FeatureTypes'>"
    FeatureWeight = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.FeatureWeight'>"
    FeatureWeights = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.FeatureWeights'>"
    FerryFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.FerryFeature
    HighwayFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.HighwayFeature
    ManeuverDetail = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.ManeuverDetail'>"
    ManeuverDetails = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.ManeuverDetails'>"
    MostEconomicRoute = PySide2.QtLocation.QGeoRouteRequest.RouteOptimization.MostEconomicRoute
    MostScenicRoute = PySide2.QtLocation.QGeoRouteRequest.RouteOptimization.MostScenicRoute
    MotorPoolLaneFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.MotorPoolLaneFeature
    NeutralFeatureWeight = PySide2.QtLocation.QGeoRouteRequest.FeatureWeight.NeutralFeatureWeight
    NoFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.NoFeature
    NoManeuvers = PySide2.QtLocation.QGeoRouteRequest.ManeuverDetail.NoManeuvers
    NoSegmentData = PySide2.QtLocation.QGeoRouteRequest.SegmentDetail.NoSegmentData
    ParksFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.ParksFeature
    PedestrianTravel = PySide2.QtLocation.QGeoRouteRequest.TravelMode.PedestrianTravel
    PreferFeatureWeight = PySide2.QtLocation.QGeoRouteRequest.FeatureWeight.PreferFeatureWeight
    PublicTransitFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.PublicTransitFeature
    PublicTransitTravel = PySide2.QtLocation.QGeoRouteRequest.TravelMode.PublicTransitTravel
    RequireFeatureWeight = PySide2.QtLocation.QGeoRouteRequest.FeatureWeight.RequireFeatureWeight
    RouteOptimization = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.RouteOptimization'>"
    RouteOptimizations = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.RouteOptimizations'>"
    SegmentDetail = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.SegmentDetail'>"
    SegmentDetails = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.SegmentDetails'>"
    ShortestRoute = PySide2.QtLocation.QGeoRouteRequest.RouteOptimization.ShortestRoute
    TollFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.TollFeature
    TrafficFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.TrafficFeature
    TravelMode = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.TravelMode'>"
    TravelModes = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteRequest.TravelModes'>"
    TruckTravel = PySide2.QtLocation.QGeoRouteRequest.TravelMode.TruckTravel
    TunnelFeature = PySide2.QtLocation.QGeoRouteRequest.FeatureType.TunnelFeature
    __hash__ = None


