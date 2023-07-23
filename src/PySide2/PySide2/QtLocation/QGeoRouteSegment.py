# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QGeoRouteSegment(__Shiboken.Object):
    """
    QGeoRouteSegment(self) -> None
    QGeoRouteSegment(self, other: PySide2.QtLocation.QGeoRouteSegment) -> None
    """
    def distance(self): # real signature unknown; restored from __doc__
        """ distance(self) -> float """
        return 0.0

    def isLegLastSegment(self): # real signature unknown; restored from __doc__
        """ isLegLastSegment(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def maneuver(self): # real signature unknown; restored from __doc__
        """ maneuver(self) -> PySide2.QtLocation.QGeoManeuver """
        pass

    def nextRouteSegment(self): # real signature unknown; restored from __doc__
        """ nextRouteSegment(self) -> PySide2.QtLocation.QGeoRouteSegment """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> typing.List[PySide2.QtPositioning.QGeoCoordinate] """
        pass

    def setDistance(self, distance): # real signature unknown; restored from __doc__
        """ setDistance(self, distance: float) -> None """
        pass

    def setManeuver(self, maneuver): # real signature unknown; restored from __doc__
        """ setManeuver(self, maneuver: PySide2.QtLocation.QGeoManeuver) -> None """
        pass

    def setNextRouteSegment(self, routeSegment): # real signature unknown; restored from __doc__
        """ setNextRouteSegment(self, routeSegment: PySide2.QtLocation.QGeoRouteSegment) -> None """
        pass

    def setPath(self, path, PySide2_QtPositioning_QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate]) -> None """
        pass

    def setTravelTime(self, secs): # real signature unknown; restored from __doc__
        """ setTravelTime(self, secs: int) -> None """
        pass

    def travelTime(self): # real signature unknown; restored from __doc__
        """ travelTime(self) -> int """
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


