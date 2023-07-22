# encoding: utf-8
# module PySide2.QtPositioning
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtPositioning.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QGeoAddress(__Shiboken.Object):
    """
    QGeoAddress(self) -> None
    QGeoAddress(self, other: PySide2.QtPositioning.QGeoAddress) -> None
    """
    def city(self): # real signature unknown; restored from __doc__
        """ city(self) -> str """
        return ""

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def country(self): # real signature unknown; restored from __doc__
        """ country(self) -> str """
        return ""

    def countryCode(self): # real signature unknown; restored from __doc__
        """ countryCode(self) -> str """
        return ""

    def county(self): # real signature unknown; restored from __doc__
        """ county(self) -> str """
        return ""

    def district(self): # real signature unknown; restored from __doc__
        """ district(self) -> str """
        return ""

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isTextGenerated(self): # real signature unknown; restored from __doc__
        """ isTextGenerated(self) -> bool """
        return False

    def postalCode(self): # real signature unknown; restored from __doc__
        """ postalCode(self) -> str """
        return ""

    def setCity(self, city): # real signature unknown; restored from __doc__
        """ setCity(self, city: str) -> None """
        pass

    def setCountry(self, country): # real signature unknown; restored from __doc__
        """ setCountry(self, country: str) -> None """
        pass

    def setCountryCode(self, countryCode): # real signature unknown; restored from __doc__
        """ setCountryCode(self, countryCode: str) -> None """
        pass

    def setCounty(self, county): # real signature unknown; restored from __doc__
        """ setCounty(self, county: str) -> None """
        pass

    def setDistrict(self, district): # real signature unknown; restored from __doc__
        """ setDistrict(self, district: str) -> None """
        pass

    def setPostalCode(self, postalCode): # real signature unknown; restored from __doc__
        """ setPostalCode(self, postalCode: str) -> None """
        pass

    def setState(self, state): # real signature unknown; restored from __doc__
        """ setState(self, state: str) -> None """
        pass

    def setStreet(self, street): # real signature unknown; restored from __doc__
        """ setStreet(self, street: str) -> None """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def street(self): # real signature unknown; restored from __doc__
        """ street(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
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


class QGeoAreaMonitorInfo(__Shiboken.Object):
    """
    QGeoAreaMonitorInfo(self, name: str = '') -> None
    QGeoAreaMonitorInfo(self, other: PySide2.QtPositioning.QGeoAreaMonitorInfo) -> None
    """
    def area(self): # real signature unknown; restored from __doc__
        """ area(self) -> PySide2.QtPositioning.QGeoShape """
        pass

    def expiration(self): # real signature unknown; restored from __doc__
        """ expiration(self) -> PySide2.QtCore.QDateTime """
        pass

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> str """
        return ""

    def isPersistent(self): # real signature unknown; restored from __doc__
        """ isPersistent(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def notificationParameters(self): # real signature unknown; restored from __doc__
        """ notificationParameters(self) -> typing.Dict[str, typing.Any] """
        pass

    def setArea(self, newShape): # real signature unknown; restored from __doc__
        """ setArea(self, newShape: PySide2.QtPositioning.QGeoShape) -> None """
        pass

    def setExpiration(self, expiry): # real signature unknown; restored from __doc__
        """ setExpiration(self, expiry: PySide2.QtCore.QDateTime) -> None """
        pass

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def setNotificationParameters(self, parameters, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setNotificationParameters(self, parameters: typing.Dict[str, typing.Any]) -> None """
        pass

    def setPersistent(self, isPersistent): # real signature unknown; restored from __doc__
        """ setPersistent(self, isPersistent: bool) -> None """
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

    def __init__(self, name=''): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    __hash__ = None


class QGeoAreaMonitorSource(__PySide2_QtCore.QObject):
    """ QGeoAreaMonitorSource(self, parent: PySide2.QtCore.QObject) -> None """
    def activeMonitors(self): # real signature unknown; restored from __doc__
        """
        activeMonitors(self) -> typing.List[PySide2.QtPositioning.QGeoAreaMonitorInfo]
        activeMonitors(self, lookupArea: PySide2.QtPositioning.QGeoShape) -> typing.List[PySide2.QtPositioning.QGeoAreaMonitorInfo]
        """
        pass

    def areaEntered(self, *args, **kwargs): # real signature unknown
        pass

    def areaExited(self, *args, **kwargs): # real signature unknown
        pass

    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> typing.List[str] """
        pass

    def createDefaultSource(self, parent): # real signature unknown; restored from __doc__
        """ createDefaultSource(parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource """
        pass

    def createSource(self, sourceName, parent): # real signature unknown; restored from __doc__
        """ createSource(sourceName: str, parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtPositioning.QGeoAreaMonitorSource.Error """
        pass

    def monitorExpired(self, *args, **kwargs): # real signature unknown
        pass

    def positionInfoSource(self): # real signature unknown; restored from __doc__
        """ positionInfoSource(self) -> PySide2.QtPositioning.QGeoPositionInfoSource """
        pass

    def requestUpdate(self, monitor, signal): # real signature unknown; restored from __doc__
        """ requestUpdate(self, monitor: PySide2.QtPositioning.QGeoAreaMonitorInfo, signal: bytes) -> bool """
        return False

    def setPositionInfoSource(self, source): # real signature unknown; restored from __doc__
        """ setPositionInfoSource(self, source: PySide2.QtPositioning.QGeoPositionInfoSource) -> None """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startMonitoring(self, monitor): # real signature unknown; restored from __doc__
        """ startMonitoring(self, monitor: PySide2.QtPositioning.QGeoAreaMonitorInfo) -> bool """
        return False

    def stopMonitoring(self, monitor): # real signature unknown; restored from __doc__
        """ stopMonitoring(self, monitor: PySide2.QtPositioning.QGeoAreaMonitorInfo) -> bool """
        return False

    def supportedAreaMonitorFeatures(self): # real signature unknown; restored from __doc__
        """ supportedAreaMonitorFeatures(self) -> PySide2.QtPositioning.QGeoAreaMonitorSource.AreaMonitorFeatures """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AccessError = PySide2.QtPositioning.QGeoAreaMonitorSource.Error.AccessError
    AnyAreaMonitorFeature = PySide2.QtPositioning.QGeoAreaMonitorSource.AreaMonitorFeature.AnyAreaMonitorFeature
    AreaMonitorFeature = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoAreaMonitorSource.AreaMonitorFeature'>"
    AreaMonitorFeatures = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoAreaMonitorSource.AreaMonitorFeatures'>"
    Error = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoAreaMonitorSource.Error'>"
    InsufficientPositionInfo = PySide2.QtPositioning.QGeoAreaMonitorSource.Error.InsufficientPositionInfo
    NoError = PySide2.QtPositioning.QGeoAreaMonitorSource.Error.NoError
    PersistentAreaMonitorFeature = PySide2.QtPositioning.QGeoAreaMonitorSource.AreaMonitorFeature.PersistentAreaMonitorFeature
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000142721A6C80>'
    UnknownSourceError = PySide2.QtPositioning.QGeoAreaMonitorSource.Error.UnknownSourceError


class QGeoShape(__Shiboken.Object):
    """
    QGeoShape(self) -> None
    QGeoShape(self, other: PySide2.QtPositioning.QGeoShape) -> None
    """
    def boundingGeoRectangle(self): # real signature unknown; restored from __doc__
        """ boundingGeoRectangle(self) -> PySide2.QtPositioning.QGeoRectangle """
        pass

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def contains(self, coordinate): # real signature unknown; restored from __doc__
        """ contains(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> bool """
        return False

    def extendShape(self, coordinate): # real signature unknown; restored from __doc__
        """ extendShape(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtPositioning.QGeoShape.ShapeType """
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

    def __lshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __lshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __rshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    CircleType = PySide2.QtPositioning.QGeoShape.ShapeType.CircleType
    PathType = PySide2.QtPositioning.QGeoShape.ShapeType.PathType
    PolygonType = PySide2.QtPositioning.QGeoShape.ShapeType.PolygonType
    RectangleType = PySide2.QtPositioning.QGeoShape.ShapeType.RectangleType
    ShapeType = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoShape.ShapeType'>"
    UnknownType = PySide2.QtPositioning.QGeoShape.ShapeType.UnknownType
    __hash__ = None


class QGeoCircle(QGeoShape):
    """
    QGeoCircle(self) -> None
    QGeoCircle(self, center: PySide2.QtPositioning.QGeoCoordinate, radius: float = -1.0) -> None
    QGeoCircle(self, other: PySide2.QtPositioning.QGeoCircle) -> None
    QGeoCircle(self, other: PySide2.QtPositioning.QGeoShape) -> None
    """
    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def extendCircle(self, coordinate): # real signature unknown; restored from __doc__
        """ extendCircle(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def radius(self): # real signature unknown; restored from __doc__
        """ radius(self) -> float """
        return 0.0

    def setCenter(self, center): # real signature unknown; restored from __doc__
        """ setCenter(self, center: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setRadius(self, radius): # real signature unknown; restored from __doc__
        """ setRadius(self, radius: float) -> None """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translate(self, degreesLatitude: float, degreesLongitude: float) -> None """
        pass

    def translated(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translated(self, degreesLatitude: float, degreesLongitude: float) -> PySide2.QtPositioning.QGeoCircle """
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

    __hash__ = None


class QGeoCoordinate(__Shiboken.Object):
    """
    QGeoCoordinate(self) -> None
    QGeoCoordinate(self, latitude: float, longitude: float) -> None
    QGeoCoordinate(self, latitude: float, longitude: float, altitude: float) -> None
    QGeoCoordinate(self, other: PySide2.QtPositioning.QGeoCoordinate) -> None
    """
    def altitude(self): # real signature unknown; restored from __doc__
        """ altitude(self) -> float """
        return 0.0

    def atDistanceAndAzimuth(self, distance, azimuth, distanceUp=0.0): # real signature unknown; restored from __doc__
        """ atDistanceAndAzimuth(self, distance: float, azimuth: float, distanceUp: float = 0.0) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def azimuthTo(self, other): # real signature unknown; restored from __doc__
        """ azimuthTo(self, other: PySide2.QtPositioning.QGeoCoordinate) -> float """
        return 0.0

    def distanceTo(self, other): # real signature unknown; restored from __doc__
        """ distanceTo(self, other: PySide2.QtPositioning.QGeoCoordinate) -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def latitude(self): # real signature unknown; restored from __doc__
        """ latitude(self) -> float """
        return 0.0

    def longitude(self): # real signature unknown; restored from __doc__
        """ longitude(self) -> float """
        return 0.0

    def setAltitude(self, altitude): # real signature unknown; restored from __doc__
        """ setAltitude(self, altitude: float) -> None """
        pass

    def setLatitude(self, latitude): # real signature unknown; restored from __doc__
        """ setLatitude(self, latitude: float) -> None """
        pass

    def setLongitude(self, longitude): # real signature unknown; restored from __doc__
        """ setLongitude(self, longitude: float) -> None """
        pass

    def toString(self, format=None): # real signature unknown; restored from __doc__
        """ toString(self, format: PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat = PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesSecondsWithHemisphere) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtPositioning.QGeoCoordinate.CoordinateType """
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

    def __lshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __lshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __rshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    Coordinate2D = PySide2.QtPositioning.QGeoCoordinate.CoordinateType.Coordinate2D
    Coordinate3D = PySide2.QtPositioning.QGeoCoordinate.CoordinateType.Coordinate3D
    CoordinateFormat = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat'>"
    CoordinateType = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoCoordinate.CoordinateType'>"
    Degrees = PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat.Degrees
    DegreesMinutes = PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutes
    DegreesMinutesSeconds = PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesSeconds
    DegreesMinutesSecondsWithHemisphere = PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesSecondsWithHemisphere
    DegreesMinutesWithHemisphere = PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesMinutesWithHemisphere
    DegreesWithHemisphere = PySide2.QtPositioning.QGeoCoordinate.CoordinateFormat.DegreesWithHemisphere
    InvalidCoordinate = PySide2.QtPositioning.QGeoCoordinate.CoordinateType.InvalidCoordinate
    __hash__ = None


class QGeoLocation(__Shiboken.Object):
    """
    QGeoLocation(self) -> None
    QGeoLocation(self, other: PySide2.QtPositioning.QGeoLocation) -> None
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> PySide2.QtPositioning.QGeoAddress """
        pass

    def boundingBox(self): # real signature unknown; restored from __doc__
        """ boundingBox(self) -> PySide2.QtPositioning.QGeoRectangle """
        pass

    def coordinate(self): # real signature unknown; restored from __doc__
        """ coordinate(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def extendedAttributes(self): # real signature unknown; restored from __doc__
        """ extendedAttributes(self) -> typing.Dict[str, typing.Any] """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def setAddress(self, address): # real signature unknown; restored from __doc__
        """ setAddress(self, address: PySide2.QtPositioning.QGeoAddress) -> None """
        pass

    def setBoundingBox(self, box): # real signature unknown; restored from __doc__
        """ setBoundingBox(self, box: PySide2.QtPositioning.QGeoRectangle) -> None """
        pass

    def setCoordinate(self, position): # real signature unknown; restored from __doc__
        """ setCoordinate(self, position: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setExtendedAttributes(self, data, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setExtendedAttributes(self, data: typing.Dict[str, typing.Any]) -> None """
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

    __hash__ = None


class QGeoPath(QGeoShape):
    """
    QGeoPath(self) -> None
    QGeoPath(self, other: PySide2.QtPositioning.QGeoPath) -> None
    QGeoPath(self, other: PySide2.QtPositioning.QGeoShape) -> None
    QGeoPath(self, path: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate], width: float = 0.0) -> None
    """
    def addCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ addCoordinate(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def clearPath(self): # real signature unknown; restored from __doc__
        """ clearPath(self) -> None """
        pass

    def containsCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ containsCoordinate(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> bool """
        return False

    def coordinateAt(self, index): # real signature unknown; restored from __doc__
        """ coordinateAt(self, index: int) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def insertCoordinate(self, index, coordinate): # real signature unknown; restored from __doc__
        """ insertCoordinate(self, index: int, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def length(self, indexFrom=0, indexTo=-1): # real signature unknown; restored from __doc__
        """ length(self, indexFrom: int = 0, indexTo: int = -1) -> float """
        return 0.0

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> typing.List[PySide2.QtPositioning.QGeoCoordinate] """
        pass

    def removeCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """
        removeCoordinate(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None
        removeCoordinate(self, index: int) -> None
        """
        pass

    def replaceCoordinate(self, index, coordinate): # real signature unknown; restored from __doc__
        """ replaceCoordinate(self, index: int, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setPath(self, path, PySide2_QtPositioning_QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate]) -> None """
        pass

    def setVariantPath(self, path, typing_Any=None): # real signature unknown; restored from __doc__
        """ setVariantPath(self, path: typing.Sequence[typing.Any]) -> None """
        pass

    def setWidth(self, width): # real signature unknown; restored from __doc__
        """ setWidth(self, width: float) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translate(self, degreesLatitude: float, degreesLongitude: float) -> None """
        pass

    def translated(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translated(self, degreesLatitude: float, degreesLongitude: float) -> PySide2.QtPositioning.QGeoPath """
        pass

    def variantPath(self): # real signature unknown; restored from __doc__
        """ variantPath(self) -> typing.List[typing.Any] """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

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


class QGeoPolygon(QGeoShape):
    """
    QGeoPolygon(self) -> None
    QGeoPolygon(self, other: PySide2.QtPositioning.QGeoPolygon) -> None
    QGeoPolygon(self, other: PySide2.QtPositioning.QGeoShape) -> None
    QGeoPolygon(self, path: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate]) -> None
    """
    def addCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ addCoordinate(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def addHole(self, holePath, PySide2_QtPositioning_QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """
        addHole(self, holePath: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate]) -> None
        addHole(self, holePath: typing.Any) -> None
        """
        pass

    def containsCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ containsCoordinate(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> bool """
        return False

    def coordinateAt(self, index): # real signature unknown; restored from __doc__
        """ coordinateAt(self, index: int) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def hole(self, index): # real signature unknown; restored from __doc__
        """ hole(self, index: int) -> typing.List[typing.Any] """
        pass

    def holePath(self, index): # real signature unknown; restored from __doc__
        """ holePath(self, index: int) -> typing.List[PySide2.QtPositioning.QGeoCoordinate] """
        pass

    def holesCount(self): # real signature unknown; restored from __doc__
        """ holesCount(self) -> int """
        return 0

    def insertCoordinate(self, index, coordinate): # real signature unknown; restored from __doc__
        """ insertCoordinate(self, index: int, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def length(self, indexFrom=0, indexTo=-1): # real signature unknown; restored from __doc__
        """ length(self, indexFrom: int = 0, indexTo: int = -1) -> float """
        return 0.0

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> typing.List[PySide2.QtPositioning.QGeoCoordinate] """
        pass

    def perimeter(self): # real signature unknown; restored from __doc__
        """ perimeter(self) -> typing.List[typing.Any] """
        pass

    def removeCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """
        removeCoordinate(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None
        removeCoordinate(self, index: int) -> None
        """
        pass

    def removeHole(self, index): # real signature unknown; restored from __doc__
        """ removeHole(self, index: int) -> None """
        pass

    def replaceCoordinate(self, index, coordinate): # real signature unknown; restored from __doc__
        """ replaceCoordinate(self, index: int, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setPath(self, path, PySide2_QtPositioning_QGeoCoordinate=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate]) -> None """
        pass

    def setPerimeter(self, path, typing_Any=None): # real signature unknown; restored from __doc__
        """ setPerimeter(self, path: typing.Sequence[typing.Any]) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translate(self, degreesLatitude: float, degreesLongitude: float) -> None """
        pass

    def translated(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translated(self, degreesLatitude: float, degreesLongitude: float) -> PySide2.QtPositioning.QGeoPolygon """
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

    __hash__ = None


class QGeoPositionInfo(__Shiboken.Object):
    """
    QGeoPositionInfo(self) -> None
    QGeoPositionInfo(self, coordinate: PySide2.QtPositioning.QGeoCoordinate, updateTime: PySide2.QtCore.QDateTime) -> None
    QGeoPositionInfo(self, other: PySide2.QtPositioning.QGeoPositionInfo) -> None
    """
    def attribute(self, attribute): # real signature unknown; restored from __doc__
        """ attribute(self, attribute: PySide2.QtPositioning.QGeoPositionInfo.Attribute) -> float """
        return 0.0

    def coordinate(self): # real signature unknown; restored from __doc__
        """ coordinate(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def hasAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ hasAttribute(self, attribute: PySide2.QtPositioning.QGeoPositionInfo.Attribute) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def removeAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ removeAttribute(self, attribute: PySide2.QtPositioning.QGeoPositionInfo.Attribute) -> None """
        pass

    def setAttribute(self, attribute, value): # real signature unknown; restored from __doc__
        """ setAttribute(self, attribute: PySide2.QtPositioning.QGeoPositionInfo.Attribute, value: float) -> None """
        pass

    def setCoordinate(self, coordinate): # real signature unknown; restored from __doc__
        """ setCoordinate(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setTimestamp(self, timestamp): # real signature unknown; restored from __doc__
        """ setTimestamp(self, timestamp: PySide2.QtCore.QDateTime) -> None """
        pass

    def timestamp(self): # real signature unknown; restored from __doc__
        """ timestamp(self) -> PySide2.QtCore.QDateTime """
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

    def __lshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __lshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __rshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    Attribute = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoPositionInfo.Attribute'>"
    Direction = PySide2.QtPositioning.QGeoPositionInfo.Attribute.Direction
    GroundSpeed = PySide2.QtPositioning.QGeoPositionInfo.Attribute.GroundSpeed
    HorizontalAccuracy = PySide2.QtPositioning.QGeoPositionInfo.Attribute.HorizontalAccuracy
    MagneticVariation = PySide2.QtPositioning.QGeoPositionInfo.Attribute.MagneticVariation
    VerticalAccuracy = PySide2.QtPositioning.QGeoPositionInfo.Attribute.VerticalAccuracy
    VerticalSpeed = PySide2.QtPositioning.QGeoPositionInfo.Attribute.VerticalSpeed
    __hash__ = None


class QGeoPositionInfoSource(__PySide2_QtCore.QObject):
    """ QGeoPositionInfoSource(self, parent: PySide2.QtCore.QObject) -> None """
    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> typing.List[str] """
        pass

    def backendProperty(self, name): # real signature unknown; restored from __doc__
        """ backendProperty(self, name: str) -> typing.Any """
        pass

    def createDefaultSource(self, parameters, p_str=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        createDefaultSource(parameters: typing.Dict[str, typing.Any], parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource
        createDefaultSource(parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource
        """
        pass

    def createSource(self, sourceName, parameters, p_str=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        createSource(sourceName: str, parameters: typing.Dict[str, typing.Any], parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource
        createSource(sourceName: str, parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource
        """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.Error """
        pass

    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly=False): # real signature unknown; restored from __doc__
        """ lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = False) -> PySide2.QtPositioning.QGeoPositionInfo """
        pass

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def positionUpdated(self, *args, **kwargs): # real signature unknown
        pass

    def preferredPositioningMethods(self): # real signature unknown; restored from __doc__
        """ preferredPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods """
        pass

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) -> None """
        pass

    def setBackendProperty(self, name, value): # real signature unknown; restored from __doc__
        """ setBackendProperty(self, name: str, value: typing.Any) -> bool """
        return False

    def setPreferredPositioningMethods(self, methods): # real signature unknown; restored from __doc__
        """ setPreferredPositioningMethods(self, methods: PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods) -> None """
        pass

    def setUpdateInterval(self, msec): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, msec: int) -> None """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) -> None """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) -> None """
        pass

    def supportedPositioningMethods(self): # real signature unknown; restored from __doc__
        """ supportedPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods """
        pass

    def supportedPositioningMethodsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def updateTimeout(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AccessError = PySide2.QtPositioning.QGeoPositionInfoSource.Error.AccessError
    AllPositioningMethods = PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethod.AllPositioningMethods
    ClosedError = PySide2.QtPositioning.QGeoPositionInfoSource.Error.ClosedError
    Error = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoPositionInfoSource.Error'>"
    NoError = PySide2.QtPositioning.QGeoPositionInfoSource.Error.NoError
    NonSatellitePositioningMethods = PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethod.NonSatellitePositioningMethods
    NoPositioningMethods = PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethod.NoPositioningMethods
    PositioningMethod = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethod'>"
    PositioningMethods = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods'>"
    SatellitePositioningMethods = PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethod.SatellitePositioningMethods
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000142721A75C0>'
    UnknownSourceError = PySide2.QtPositioning.QGeoPositionInfoSource.Error.UnknownSourceError


class QGeoPositionInfoSourceFactory(__Shiboken.Object):
    """ QGeoPositionInfoSourceFactory(self) -> None """
    def areaMonitor(self, parent): # real signature unknown; restored from __doc__
        """ areaMonitor(self, parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoAreaMonitorSource """
        pass

    def positionInfoSource(self, parent): # real signature unknown; restored from __doc__
        """ positionInfoSource(self, parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoPositionInfoSource """
        pass

    def satelliteInfoSource(self, parent): # real signature unknown; restored from __doc__
        """ satelliteInfoSource(self, parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QGeoRectangle(QGeoShape):
    """
    QGeoRectangle(self) -> None
    QGeoRectangle(self, center: PySide2.QtPositioning.QGeoCoordinate, degreesWidth: float, degreesHeight: float) -> None
    QGeoRectangle(self, coordinates: typing.Sequence[PySide2.QtPositioning.QGeoCoordinate]) -> None
    QGeoRectangle(self, other: PySide2.QtPositioning.QGeoRectangle) -> None
    QGeoRectangle(self, other: PySide2.QtPositioning.QGeoShape) -> None
    QGeoRectangle(self, topLeft: PySide2.QtPositioning.QGeoCoordinate, bottomRight: PySide2.QtPositioning.QGeoCoordinate) -> None
    """
    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def contains(self, coordinate): # real signature unknown; restored from __doc__
        """
        contains(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> bool
        contains(self, rectangle: PySide2.QtPositioning.QGeoRectangle) -> bool
        """
        return False

    def extendRectangle(self, coordinate): # real signature unknown; restored from __doc__
        """ extendRectangle(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def intersects(self, rectangle): # real signature unknown; restored from __doc__
        """ intersects(self, rectangle: PySide2.QtPositioning.QGeoRectangle) -> bool """
        return False

    def setBottomLeft(self, bottomLeft): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, bottomLeft: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setBottomRight(self, bottomRight): # real signature unknown; restored from __doc__
        """ setBottomRight(self, bottomRight: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setCenter(self, center): # real signature unknown; restored from __doc__
        """ setCenter(self, center: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setHeight(self, degreesHeight): # real signature unknown; restored from __doc__
        """ setHeight(self, degreesHeight: float) -> None """
        pass

    def setTopLeft(self, topLeft): # real signature unknown; restored from __doc__
        """ setTopLeft(self, topLeft: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setTopRight(self, topRight): # real signature unknown; restored from __doc__
        """ setTopRight(self, topRight: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setWidth(self, degreesWidth): # real signature unknown; restored from __doc__
        """ setWidth(self, degreesWidth: float) -> None """
        pass

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def translate(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translate(self, degreesLatitude: float, degreesLongitude: float) -> None """
        pass

    def translated(self, degreesLatitude, degreesLongitude): # real signature unknown; restored from __doc__
        """ translated(self, degreesLatitude: float, degreesLongitude: float) -> PySide2.QtPositioning.QGeoRectangle """
        pass

    def united(self, rectangle): # real signature unknown; restored from __doc__
        """ united(self, rectangle: PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

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

    def __ior__(self, rectangle): # real signature unknown; restored from __doc__
        """
        __ior__(self, rectangle: PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle
        
        Return self|=value.
        """
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

    def __or__(self, rectangle): # real signature unknown; restored from __doc__
        """
        __or__(self, rectangle: PySide2.QtPositioning.QGeoRectangle) -> PySide2.QtPositioning.QGeoRectangle
        
        Return self|value.
        """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    __hash__ = None


class QGeoSatelliteInfo(__Shiboken.Object):
    """
    QGeoSatelliteInfo(self) -> None
    QGeoSatelliteInfo(self, other: PySide2.QtPositioning.QGeoSatelliteInfo) -> None
    """
    def attribute(self, attribute): # real signature unknown; restored from __doc__
        """ attribute(self, attribute: PySide2.QtPositioning.QGeoSatelliteInfo.Attribute) -> float """
        return 0.0

    def hasAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ hasAttribute(self, attribute: PySide2.QtPositioning.QGeoSatelliteInfo.Attribute) -> bool """
        return False

    def removeAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ removeAttribute(self, attribute: PySide2.QtPositioning.QGeoSatelliteInfo.Attribute) -> None """
        pass

    def satelliteIdentifier(self): # real signature unknown; restored from __doc__
        """ satelliteIdentifier(self) -> int """
        return 0

    def satelliteSystem(self): # real signature unknown; restored from __doc__
        """ satelliteSystem(self) -> PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem """
        pass

    def setAttribute(self, attribute, value): # real signature unknown; restored from __doc__
        """ setAttribute(self, attribute: PySide2.QtPositioning.QGeoSatelliteInfo.Attribute, value: float) -> None """
        pass

    def setSatelliteIdentifier(self, satId): # real signature unknown; restored from __doc__
        """ setSatelliteIdentifier(self, satId: int) -> None """
        pass

    def setSatelliteSystem(self, system): # real signature unknown; restored from __doc__
        """ setSatelliteSystem(self, system: PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem) -> None """
        pass

    def setSignalStrength(self, signalStrength): # real signature unknown; restored from __doc__
        """ setSignalStrength(self, signalStrength: int) -> None """
        pass

    def signalStrength(self): # real signature unknown; restored from __doc__
        """ signalStrength(self) -> int """
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

    def __lshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __lshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __rshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    Attribute = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoSatelliteInfo.Attribute'>"
    Azimuth = PySide2.QtPositioning.QGeoSatelliteInfo.Attribute.Azimuth
    Elevation = PySide2.QtPositioning.QGeoSatelliteInfo.Attribute.Elevation
    GLONASS = PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem.GLONASS
    GPS = PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem.GPS
    SatelliteSystem = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem'>"
    Undefined = PySide2.QtPositioning.QGeoSatelliteInfo.SatelliteSystem.Undefined
    __hash__ = None


class QGeoSatelliteInfoSource(__PySide2_QtCore.QObject):
    """ QGeoSatelliteInfoSource(self, parent: PySide2.QtCore.QObject) -> None """
    def availableSources(self): # real signature unknown; restored from __doc__
        """ availableSources() -> typing.List[str] """
        pass

    def createDefaultSource(self, parameters, p_str=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        createDefaultSource(parameters: typing.Dict[str, typing.Any], parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource
        createDefaultSource(parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource
        """
        pass

    def createSource(self, sourceName, parameters, p_str=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        createSource(sourceName: str, parameters: typing.Dict[str, typing.Any], parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource
        createSource(sourceName: str, parent: PySide2.QtCore.QObject) -> PySide2.QtPositioning.QGeoSatelliteInfoSource
        """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtPositioning.QGeoSatelliteInfoSource.Error """
        pass

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def requestTimeout(self, *args, **kwargs): # real signature unknown
        pass

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) -> None """
        pass

    def satellitesInUseUpdated(self, *args, **kwargs): # real signature unknown
        pass

    def satellitesInViewUpdated(self, *args, **kwargs): # real signature unknown
        pass

    def setUpdateInterval(self, msec): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, msec: int) -> None """
        pass

    def sourceName(self): # real signature unknown; restored from __doc__
        """ sourceName(self) -> str """
        return ""

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) -> None """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) -> None """
        pass

    def updateInterval(self): # real signature unknown; restored from __doc__
        """ updateInterval(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AccessError = PySide2.QtPositioning.QGeoSatelliteInfoSource.Error.AccessError
    ClosedError = PySide2.QtPositioning.QGeoSatelliteInfoSource.Error.ClosedError
    Error = None # (!) real value is "<class 'PySide2.QtPositioning.QGeoSatelliteInfoSource.Error'>"
    NoError = PySide2.QtPositioning.QGeoSatelliteInfoSource.Error.NoError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000142721A7000>'
    UnknownSourceError = PySide2.QtPositioning.QGeoSatelliteInfoSource.Error.UnknownSourceError


class QNmeaPositionInfoSource(QGeoPositionInfoSource):
    """ QNmeaPositionInfoSource(self, updateMode: PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.Error """
        pass

    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly=False): # real signature unknown; restored from __doc__
        """ lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = False) -> PySide2.QtPositioning.QGeoPositionInfo """
        pass

    def minimumUpdateInterval(self): # real signature unknown; restored from __doc__
        """ minimumUpdateInterval(self) -> int """
        return 0

    def parsePosInfoFromNmeaData(self, data, size, posInfo): # real signature unknown; restored from __doc__
        """ parsePosInfoFromNmeaData(self, data: bytes, size: int, posInfo: PySide2.QtPositioning.QGeoPositionInfo) -> typing.Tuple[bool, bool] """
        pass

    def requestUpdate(self, timeout=0): # real signature unknown; restored from __doc__
        """ requestUpdate(self, timeout: int = 0) -> None """
        pass

    def setDevice(self, source): # real signature unknown; restored from __doc__
        """ setDevice(self, source: PySide2.QtCore.QIODevice) -> None """
        pass

    def setUpdateInterval(self, msec): # real signature unknown; restored from __doc__
        """ setUpdateInterval(self, msec: int) -> None """
        pass

    def setUserEquivalentRangeError(self, uere): # real signature unknown; restored from __doc__
        """ setUserEquivalentRangeError(self, uere: float) -> None """
        pass

    def startUpdates(self): # real signature unknown; restored from __doc__
        """ startUpdates(self) -> None """
        pass

    def stopUpdates(self): # real signature unknown; restored from __doc__
        """ stopUpdates(self) -> None """
        pass

    def supportedPositioningMethods(self): # real signature unknown; restored from __doc__
        """ supportedPositioningMethods(self) -> PySide2.QtPositioning.QGeoPositionInfoSource.PositioningMethods """
        pass

    def updateMode(self): # real signature unknown; restored from __doc__
        """ updateMode(self) -> PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode """
        pass

    def userEquivalentRangeError(self): # real signature unknown; restored from __doc__
        """ userEquivalentRangeError(self) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, updateMode, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    RealTimeMode = PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode.RealTimeMode
    SimulationMode = PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode.SimulationMode
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000142721A7900>'
    UpdateMode = None # (!) real value is "<class 'PySide2.QtPositioning.QNmeaPositionInfoSource.UpdateMode'>"


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000142715D17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtPositioning', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000142715D17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtPositioning.cp310-win_amd64.pyd')"

