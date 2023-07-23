# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaObject import QMediaObject

class QCamera(QMediaObject):
    """
    QCamera(self, cameraInfo: PySide2.QtMultimedia.QCameraInfo, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QCamera(self, deviceName: PySide2.QtCore.QByteArray, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QCamera(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QCamera(self, position: PySide2.QtMultimedia.QCamera.Position, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> PySide2.QtMultimedia.QMultimedia.AvailabilityStatus """
        pass

    def availableDevices(self): # real signature unknown; restored from __doc__
        """ availableDevices() -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def captureMode(self): # real signature unknown; restored from __doc__
        """ captureMode(self) -> PySide2.QtMultimedia.QCamera.CaptureModes """
        pass

    def captureModeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def deviceDescription(self, device): # real signature unknown; restored from __doc__
        """ deviceDescription(device: PySide2.QtCore.QByteArray) -> str """
        return ""

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtMultimedia.QCamera.Error """
        pass

    def errorOccurred(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def exposure(self): # real signature unknown; restored from __doc__
        """ exposure(self) -> PySide2.QtMultimedia.QCameraExposure """
        pass

    def focus(self): # real signature unknown; restored from __doc__
        """ focus(self) -> PySide2.QtMultimedia.QCameraFocus """
        pass

    def imageProcessing(self): # real signature unknown; restored from __doc__
        """ imageProcessing(self) -> PySide2.QtMultimedia.QCameraImageProcessing """
        pass

    def isCaptureModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isCaptureModeSupported(self, mode: PySide2.QtMultimedia.QCamera.CaptureModes) -> bool """
        return False

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) -> None """
        pass

    def locked(self, *args, **kwargs): # real signature unknown
        pass

    def lockFailed(self, *args, **kwargs): # real signature unknown
        pass

    def lockStatus(self): # real signature unknown; restored from __doc__
        """
        lockStatus(self) -> PySide2.QtMultimedia.QCamera.LockStatus
        lockStatus(self, lock: PySide2.QtMultimedia.QCamera.LockType) -> PySide2.QtMultimedia.QCamera.LockStatus
        """
        pass

    def lockStatusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def requestedLocks(self): # real signature unknown; restored from __doc__
        """ requestedLocks(self) -> PySide2.QtMultimedia.QCamera.LockTypes """
        pass

    def searchAndLock(self): # real signature unknown; restored from __doc__
        """
        searchAndLock(self) -> None
        searchAndLock(self, locks: PySide2.QtMultimedia.QCamera.LockTypes) -> None
        """
        pass

    def setCaptureMode(self, mode): # real signature unknown; restored from __doc__
        """ setCaptureMode(self, mode: PySide2.QtMultimedia.QCamera.CaptureModes) -> None """
        pass

    def setViewfinder(self, surface): # real signature unknown; restored from __doc__
        """
        setViewfinder(self, surface: PySide2.QtMultimedia.QAbstractVideoSurface) -> None
        setViewfinder(self, viewfinder: PySide2.QtMultimediaWidgets.QGraphicsVideoItem) -> None
        setViewfinder(self, viewfinder: PySide2.QtMultimediaWidgets.QVideoWidget) -> None
        """
        pass

    def setViewfinderSettings(self, settings): # real signature unknown; restored from __doc__
        """ setViewfinderSettings(self, settings: PySide2.QtMultimedia.QCameraViewfinderSettings) -> None """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtMultimedia.QCamera.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtMultimedia.QCamera.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def supportedLocks(self): # real signature unknown; restored from __doc__
        """ supportedLocks(self) -> PySide2.QtMultimedia.QCamera.LockTypes """
        pass

    def supportedViewfinderFrameRateRanges(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderFrameRateRanges(self, settings: PySide2.QtMultimedia.QCameraViewfinderSettings = Default(QCameraViewfinderSettings)) -> typing.List[PySide2.QtMultimedia.QCamera.FrameRateRange] """
        pass

    def supportedViewfinderPixelFormats(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderPixelFormats(self, settings: PySide2.QtMultimedia.QCameraViewfinderSettings = Default(QCameraViewfinderSettings)) -> typing.List[PySide2.QtMultimedia.QVideoFrame.PixelFormat] """
        pass

    def supportedViewfinderResolutions(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderResolutions(self, settings: PySide2.QtMultimedia.QCameraViewfinderSettings = Default(QCameraViewfinderSettings)) -> typing.List[PySide2.QtCore.QSize] """
        pass

    def supportedViewfinderSettings(self, settings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedViewfinderSettings(self, settings: PySide2.QtMultimedia.QCameraViewfinderSettings = Default(QCameraViewfinderSettings)) -> typing.List[PySide2.QtMultimedia.QCameraViewfinderSettings] """
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ unload(self) -> None """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """
        unlock(self) -> None
        unlock(self, locks: PySide2.QtMultimedia.QCamera.LockTypes) -> None
        """
        pass

    def viewfinderSettings(self): # real signature unknown; restored from __doc__
        """ viewfinderSettings(self) -> PySide2.QtMultimedia.QCameraViewfinderSettings """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, cameraInfo, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ActiveState = PySide2.QtMultimedia.QCamera.State.ActiveState
    ActiveStatus = PySide2.QtMultimedia.QCamera.Status.ActiveStatus
    BackFace = PySide2.QtMultimedia.QCamera.Position.BackFace
    CameraError = PySide2.QtMultimedia.QCamera.Error.CameraError
    CaptureMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.CaptureMode'>"
    CaptureModes = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.CaptureModes'>"
    CaptureStillImage = PySide2.QtMultimedia.QCamera.CaptureMode.CaptureStillImage
    CaptureVideo = PySide2.QtMultimedia.QCamera.CaptureMode.CaptureVideo
    CaptureViewfinder = PySide2.QtMultimedia.QCamera.CaptureMode.CaptureViewfinder
    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.Error'>"
    FrameRateRange = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.FrameRateRange'>"
    FrontFace = PySide2.QtMultimedia.QCamera.Position.FrontFace
    InvalidRequestError = PySide2.QtMultimedia.QCamera.Error.InvalidRequestError
    LoadedState = PySide2.QtMultimedia.QCamera.State.LoadedState
    LoadedStatus = PySide2.QtMultimedia.QCamera.Status.LoadedStatus
    LoadingStatus = PySide2.QtMultimedia.QCamera.Status.LoadingStatus
    LockAcquired = PySide2.QtMultimedia.QCamera.LockChangeReason.LockAcquired
    LockChangeReason = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.LockChangeReason'>"
    Locked = PySide2.QtMultimedia.QCamera.LockStatus.Locked
    LockExposure = PySide2.QtMultimedia.QCamera.LockType.LockExposure
    LockFailed = PySide2.QtMultimedia.QCamera.LockChangeReason.LockFailed
    LockFocus = PySide2.QtMultimedia.QCamera.LockType.LockFocus
    LockLost = PySide2.QtMultimedia.QCamera.LockChangeReason.LockLost
    LockStatus = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.LockStatus'>"
    LockTemporaryLost = PySide2.QtMultimedia.QCamera.LockChangeReason.LockTemporaryLost
    LockType = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.LockType'>"
    LockTypes = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.LockTypes'>"
    LockWhiteBalance = PySide2.QtMultimedia.QCamera.LockType.LockWhiteBalance
    NoError = PySide2.QtMultimedia.QCamera.Error.NoError
    NoLock = PySide2.QtMultimedia.QCamera.LockType.NoLock
    NotSupportedFeatureError = PySide2.QtMultimedia.QCamera.Error.NotSupportedFeatureError
    Position = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.Position'>"
    Searching = PySide2.QtMultimedia.QCamera.LockStatus.Searching
    ServiceMissingError = PySide2.QtMultimedia.QCamera.Error.ServiceMissingError
    StandbyStatus = PySide2.QtMultimedia.QCamera.Status.StandbyStatus
    StartingStatus = PySide2.QtMultimedia.QCamera.Status.StartingStatus
    State = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000018874678500>'
    Status = None # (!) real value is "<class 'PySide2.QtMultimedia.QCamera.Status'>"
    StoppingStatus = PySide2.QtMultimedia.QCamera.Status.StoppingStatus
    UnavailableStatus = PySide2.QtMultimedia.QCamera.Status.UnavailableStatus
    UnloadedState = PySide2.QtMultimedia.QCamera.State.UnloadedState
    UnloadedStatus = PySide2.QtMultimedia.QCamera.Status.UnloadedStatus
    UnloadingStatus = PySide2.QtMultimedia.QCamera.Status.UnloadingStatus
    Unlocked = PySide2.QtMultimedia.QCamera.LockStatus.Unlocked
    UnspecifiedPosition = PySide2.QtMultimedia.QCamera.Position.UnspecifiedPosition
    UserRequest = PySide2.QtMultimedia.QCamera.LockChangeReason.UserRequest


