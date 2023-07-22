# encoding: utf-8
# module PySide2.QtSensors
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSensors.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSensor(__PySide2_QtCore.QObject):
    """ QSensor(self, type: PySide2.QtCore.QByteArray, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def activeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def addFilter(self, filter): # real signature unknown; restored from __doc__
        """ addFilter(self, filter: PySide2.QtSensors.QSensorFilter) -> None """
        pass

    def alwaysOnChanged(self, *args, **kwargs): # real signature unknown
        pass

    def availableDataRates(self): # real signature unknown; restored from __doc__
        """ availableDataRates(self) -> typing.List[typing.Tuple[int, int]] """
        pass

    def availableSensorsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def axesOrientationMode(self): # real signature unknown; restored from __doc__
        """ axesOrientationMode(self) -> PySide2.QtSensors.QSensor.AxesOrientationMode """
        pass

    def axesOrientationModeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def backend(self): # real signature unknown; restored from __doc__
        """ backend(self) -> PySide2.QtSensors.QSensorBackend """
        pass

    def bufferSize(self): # real signature unknown; restored from __doc__
        """ bufferSize(self) -> int """
        return 0

    def bufferSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def busyChanged(self, *args, **kwargs): # real signature unknown
        pass

    def connectToBackend(self): # real signature unknown; restored from __doc__
        """ connectToBackend(self) -> bool """
        return False

    def currentOrientation(self): # real signature unknown; restored from __doc__
        """ currentOrientation(self) -> int """
        return 0

    def currentOrientationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dataRate(self): # real signature unknown; restored from __doc__
        """ dataRate(self) -> int """
        return 0

    def dataRateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def defaultSensorForType(self, type): # real signature unknown; restored from __doc__
        """ defaultSensorForType(type: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray """
        pass

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def efficientBufferSize(self): # real signature unknown; restored from __doc__
        """ efficientBufferSize(self) -> int """
        return 0

    def efficientBufferSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> int """
        return 0

    def filters(self): # real signature unknown; restored from __doc__
        """ filters(self) -> typing.List[PySide2.QtSensors.QSensorFilter] """
        pass

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> PySide2.QtCore.QByteArray """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAlwaysOn(self): # real signature unknown; restored from __doc__
        """ isAlwaysOn(self) -> bool """
        return False

    def isBusy(self): # real signature unknown; restored from __doc__
        """ isBusy(self) -> bool """
        return False

    def isConnectedToBackend(self): # real signature unknown; restored from __doc__
        """ isConnectedToBackend(self) -> bool """
        return False

    def isFeatureSupported(self, feature): # real signature unknown; restored from __doc__
        """ isFeatureSupported(self, feature: PySide2.QtSensors.QSensor.Feature) -> bool """
        return False

    def maxBufferSize(self): # real signature unknown; restored from __doc__
        """ maxBufferSize(self) -> int """
        return 0

    def maxBufferSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def outputRange(self): # real signature unknown; restored from __doc__
        """ outputRange(self) -> int """
        return 0

    def outputRanges(self): # real signature unknown; restored from __doc__
        """ outputRanges(self) -> typing.List[PySide2.QtSensors.qoutputrange] """
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> PySide2.QtSensors.QSensorReading """
        pass

    def readingChanged(self, *args, **kwargs): # real signature unknown
        pass

    def removeFilter(self, filter): # real signature unknown; restored from __doc__
        """ removeFilter(self, filter: PySide2.QtSensors.QSensorFilter) -> None """
        pass

    def sensorError(self, *args, **kwargs): # real signature unknown
        pass

    def sensorsForType(self, type): # real signature unknown; restored from __doc__
        """ sensorsForType(type: PySide2.QtCore.QByteArray) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def sensorTypes(self): # real signature unknown; restored from __doc__
        """ sensorTypes() -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def setActive(self, active): # real signature unknown; restored from __doc__
        """ setActive(self, active: bool) -> None """
        pass

    def setAlwaysOn(self, alwaysOn): # real signature unknown; restored from __doc__
        """ setAlwaysOn(self, alwaysOn: bool) -> None """
        pass

    def setAxesOrientationMode(self, axesOrientationMode): # real signature unknown; restored from __doc__
        """ setAxesOrientationMode(self, axesOrientationMode: PySide2.QtSensors.QSensor.AxesOrientationMode) -> None """
        pass

    def setBufferSize(self, bufferSize): # real signature unknown; restored from __doc__
        """ setBufferSize(self, bufferSize: int) -> None """
        pass

    def setCurrentOrientation(self, currentOrientation): # real signature unknown; restored from __doc__
        """ setCurrentOrientation(self, currentOrientation: int) -> None """
        pass

    def setDataRate(self, rate): # real signature unknown; restored from __doc__
        """ setDataRate(self, rate: int) -> None """
        pass

    def setEfficientBufferSize(self, efficientBufferSize): # real signature unknown; restored from __doc__
        """ setEfficientBufferSize(self, efficientBufferSize: int) -> None """
        pass

    def setIdentifier(self, identifier): # real signature unknown; restored from __doc__
        """ setIdentifier(self, identifier: PySide2.QtCore.QByteArray) -> None """
        pass

    def setMaxBufferSize(self, maxBufferSize): # real signature unknown; restored from __doc__
        """ setMaxBufferSize(self, maxBufferSize: int) -> None """
        pass

    def setOutputRange(self, index): # real signature unknown; restored from __doc__
        """ setOutputRange(self, index: int) -> None """
        pass

    def setSkipDuplicates(self, skipDuplicates): # real signature unknown; restored from __doc__
        """ setSkipDuplicates(self, skipDuplicates: bool) -> None """
        pass

    def setUserOrientation(self, userOrientation): # real signature unknown; restored from __doc__
        """ setUserOrientation(self, userOrientation: int) -> None """
        pass

    def skipDuplicates(self): # real signature unknown; restored from __doc__
        """ skipDuplicates(self) -> bool """
        return False

    def skipDuplicatesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> bool """
        return False

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.QByteArray """
        pass

    def userOrientation(self): # real signature unknown; restored from __doc__
        """ userOrientation(self) -> int """
        return 0

    def userOrientationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AccelerationMode = PySide2.QtSensors.QSensor.Feature.AccelerationMode
    AlwaysOn = PySide2.QtSensors.QSensor.Feature.AlwaysOn
    AutomaticOrientation = PySide2.QtSensors.QSensor.AxesOrientationMode.AutomaticOrientation
    AxesOrientation = PySide2.QtSensors.QSensor.Feature.AxesOrientation
    AxesOrientationMode = None # (!) real value is "<class 'PySide2.QtSensors.QSensor.AxesOrientationMode'>"
    Buffering = PySide2.QtSensors.QSensor.Feature.Buffering
    Feature = None # (!) real value is "<class 'PySide2.QtSensors.QSensor.Feature'>"
    FieldOfView = PySide2.QtSensors.QSensor.Feature.FieldOfView
    FixedOrientation = PySide2.QtSensors.QSensor.AxesOrientationMode.FixedOrientation
    GeoValues = PySide2.QtSensors.QSensor.Feature.GeoValues
    PressureSensorTemperature = PySide2.QtSensors.QSensor.Feature.PressureSensorTemperature
    Reserved = PySide2.QtSensors.QSensor.Feature.Reserved
    SkipDuplicates = PySide2.QtSensors.QSensor.Feature.SkipDuplicates
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000206286B3E40>'
    UserOrientation = PySide2.QtSensors.QSensor.AxesOrientationMode.UserOrientation


