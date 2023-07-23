# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QCameraExposure(__PySide2_QtCore.QObject):
    # no doc
    def aperture(self): # real signature unknown; restored from __doc__
        """ aperture(self) -> float """
        return 0.0

    def apertureChanged(self, *args, **kwargs): # real signature unknown
        pass

    def apertureRangeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def exposureCompensation(self): # real signature unknown; restored from __doc__
        """ exposureCompensation(self) -> float """
        return 0.0

    def exposureCompensationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def exposureMode(self): # real signature unknown; restored from __doc__
        """ exposureMode(self) -> PySide2.QtMultimedia.QCameraExposure.ExposureMode """
        pass

    def flashMode(self): # real signature unknown; restored from __doc__
        """ flashMode(self) -> PySide2.QtMultimedia.QCameraExposure.FlashModes """
        pass

    def flashReady(self, *args, **kwargs): # real signature unknown
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isExposureModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isExposureModeSupported(self, mode: PySide2.QtMultimedia.QCameraExposure.ExposureMode) -> bool """
        return False

    def isFlashModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isFlashModeSupported(self, mode: PySide2.QtMultimedia.QCameraExposure.FlashModes) -> bool """
        return False

    def isFlashReady(self): # real signature unknown; restored from __doc__
        """ isFlashReady(self) -> bool """
        return False

    def isMeteringModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isMeteringModeSupported(self, mode: PySide2.QtMultimedia.QCameraExposure.MeteringMode) -> bool """
        return False

    def isoSensitivity(self): # real signature unknown; restored from __doc__
        """ isoSensitivity(self) -> int """
        return 0

    def isoSensitivityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def meteringMode(self): # real signature unknown; restored from __doc__
        """ meteringMode(self) -> PySide2.QtMultimedia.QCameraExposure.MeteringMode """
        pass

    def requestedAperture(self): # real signature unknown; restored from __doc__
        """ requestedAperture(self) -> float """
        return 0.0

    def requestedIsoSensitivity(self): # real signature unknown; restored from __doc__
        """ requestedIsoSensitivity(self) -> int """
        return 0

    def requestedShutterSpeed(self): # real signature unknown; restored from __doc__
        """ requestedShutterSpeed(self) -> float """
        return 0.0

    def setAutoAperture(self): # real signature unknown; restored from __doc__
        """ setAutoAperture(self) -> None """
        pass

    def setAutoIsoSensitivity(self): # real signature unknown; restored from __doc__
        """ setAutoIsoSensitivity(self) -> None """
        pass

    def setAutoShutterSpeed(self): # real signature unknown; restored from __doc__
        """ setAutoShutterSpeed(self) -> None """
        pass

    def setExposureCompensation(self, ev): # real signature unknown; restored from __doc__
        """ setExposureCompensation(self, ev: float) -> None """
        pass

    def setExposureMode(self, mode): # real signature unknown; restored from __doc__
        """ setExposureMode(self, mode: PySide2.QtMultimedia.QCameraExposure.ExposureMode) -> None """
        pass

    def setFlashMode(self, mode): # real signature unknown; restored from __doc__
        """ setFlashMode(self, mode: PySide2.QtMultimedia.QCameraExposure.FlashModes) -> None """
        pass

    def setManualAperture(self, aperture): # real signature unknown; restored from __doc__
        """ setManualAperture(self, aperture: float) -> None """
        pass

    def setManualIsoSensitivity(self, iso): # real signature unknown; restored from __doc__
        """ setManualIsoSensitivity(self, iso: int) -> None """
        pass

    def setManualShutterSpeed(self, seconds): # real signature unknown; restored from __doc__
        """ setManualShutterSpeed(self, seconds: float) -> None """
        pass

    def setMeteringMode(self, mode): # real signature unknown; restored from __doc__
        """ setMeteringMode(self, mode: PySide2.QtMultimedia.QCameraExposure.MeteringMode) -> None """
        pass

    def setSpotMeteringPoint(self, point): # real signature unknown; restored from __doc__
        """ setSpotMeteringPoint(self, point: PySide2.QtCore.QPointF) -> None """
        pass

    def shutterSpeed(self): # real signature unknown; restored from __doc__
        """ shutterSpeed(self) -> float """
        return 0.0

    def shutterSpeedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def shutterSpeedRangeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def spotMeteringPoint(self): # real signature unknown; restored from __doc__
        """ spotMeteringPoint(self) -> PySide2.QtCore.QPointF """
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

    ExposureAction = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureAction
    ExposureAuto = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureAuto
    ExposureBacklight = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureBacklight
    ExposureBarcode = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureBarcode
    ExposureBeach = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureBeach
    ExposureCandlelight = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureCandlelight
    ExposureFireworks = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureFireworks
    ExposureLandscape = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureLandscape
    ExposureLargeAperture = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureLargeAperture
    ExposureManual = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureManual
    ExposureMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraExposure.ExposureMode'>"
    ExposureModeVendor = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureModeVendor
    ExposureNight = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureNight
    ExposureNightPortrait = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureNightPortrait
    ExposureParty = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureParty
    ExposurePortrait = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposurePortrait
    ExposureSmallAperture = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureSmallAperture
    ExposureSnow = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureSnow
    ExposureSports = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureSports
    ExposureSpotlight = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureSpotlight
    ExposureSteadyPhoto = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureSteadyPhoto
    ExposureSunset = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureSunset
    ExposureTheatre = PySide2.QtMultimedia.QCameraExposure.ExposureMode.ExposureTheatre
    FlashAuto = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashAuto
    FlashFill = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashFill
    FlashManual = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashManual
    FlashMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraExposure.FlashMode'>"
    FlashModes = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraExposure.FlashModes'>"
    FlashOff = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashOff
    FlashOn = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashOn
    FlashRedEyeReduction = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashRedEyeReduction
    FlashSlowSyncFrontCurtain = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashSlowSyncFrontCurtain
    FlashSlowSyncRearCurtain = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashSlowSyncRearCurtain
    FlashTorch = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashTorch
    FlashVideoLight = PySide2.QtMultimedia.QCameraExposure.FlashMode.FlashVideoLight
    MeteringAverage = PySide2.QtMultimedia.QCameraExposure.MeteringMode.MeteringAverage
    MeteringMatrix = PySide2.QtMultimedia.QCameraExposure.MeteringMode.MeteringMatrix
    MeteringMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraExposure.MeteringMode'>"
    MeteringSpot = PySide2.QtMultimedia.QCameraExposure.MeteringMode.MeteringSpot
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000188746B8140>'


