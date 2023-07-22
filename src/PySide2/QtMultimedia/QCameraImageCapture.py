# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaBindableInterface import QMediaBindableInterface

class QCameraImageCapture(__PySide2_QtCore.QObject, QMediaBindableInterface):
    """ QCameraImageCapture(self, mediaObject: PySide2.QtMultimedia.QMediaObject, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> PySide2.QtMultimedia.QMultimedia.AvailabilityStatus """
        pass

    def bufferFormat(self): # real signature unknown; restored from __doc__
        """ bufferFormat(self) -> PySide2.QtMultimedia.QVideoFrame.PixelFormat """
        pass

    def bufferFormatChanged(self, *args, **kwargs): # real signature unknown
        pass

    def cancelCapture(self): # real signature unknown; restored from __doc__
        """ cancelCapture(self) -> None """
        pass

    def capture(self, location=''): # real signature unknown; restored from __doc__
        """ capture(self, location: str = '') -> int """
        return 0

    def captureDestination(self): # real signature unknown; restored from __doc__
        """ captureDestination(self) -> PySide2.QtMultimedia.QCameraImageCapture.CaptureDestinations """
        pass

    def captureDestinationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def encodingSettings(self): # real signature unknown; restored from __doc__
        """ encodingSettings(self) -> PySide2.QtMultimedia.QImageEncoderSettings """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtMultimedia.QCameraImageCapture.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def imageAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def imageCaptured(self, *args, **kwargs): # real signature unknown
        pass

    def imageCodecDescription(self, codecName): # real signature unknown; restored from __doc__
        """ imageCodecDescription(self, codecName: str) -> str """
        return ""

    def imageExposed(self, *args, **kwargs): # real signature unknown
        pass

    def imageMetadataAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def imageSaved(self, *args, **kwargs): # real signature unknown
        pass

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isCaptureDestinationSupported(self, destination): # real signature unknown; restored from __doc__
        """ isCaptureDestinationSupported(self, destination: PySide2.QtMultimedia.QCameraImageCapture.CaptureDestinations) -> bool """
        return False

    def isReadyForCapture(self): # real signature unknown; restored from __doc__
        """ isReadyForCapture(self) -> bool """
        return False

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> PySide2.QtMultimedia.QMediaObject """
        pass

    def readyForCaptureChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferFormat(self, format): # real signature unknown; restored from __doc__
        """ setBufferFormat(self, format: PySide2.QtMultimedia.QVideoFrame.PixelFormat) -> None """
        pass

    def setCaptureDestination(self, destination): # real signature unknown; restored from __doc__
        """ setCaptureDestination(self, destination: PySide2.QtMultimedia.QCameraImageCapture.CaptureDestinations) -> None """
        pass

    def setEncodingSettings(self, settings): # real signature unknown; restored from __doc__
        """ setEncodingSettings(self, settings: PySide2.QtMultimedia.QImageEncoderSettings) -> None """
        pass

    def setMediaObject(self, arg__1): # real signature unknown; restored from __doc__
        """ setMediaObject(self, arg__1: PySide2.QtMultimedia.QMediaObject) -> bool """
        return False

    def supportedBufferFormats(self): # real signature unknown; restored from __doc__
        """ supportedBufferFormats(self) -> typing.List[PySide2.QtMultimedia.QVideoFrame.PixelFormat] """
        pass

    def supportedImageCodecs(self): # real signature unknown; restored from __doc__
        """ supportedImageCodecs(self) -> typing.List[str] """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, mediaObject, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    CaptureDestination = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraImageCapture.CaptureDestination'>"
    CaptureDestinations = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraImageCapture.CaptureDestinations'>"
    CaptureToBuffer = PySide2.QtMultimedia.QCameraImageCapture.CaptureDestination.CaptureToBuffer
    CaptureToFile = PySide2.QtMultimedia.QCameraImageCapture.CaptureDestination.CaptureToFile
    DriveMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraImageCapture.DriveMode'>"
    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraImageCapture.Error'>"
    FormatError = PySide2.QtMultimedia.QCameraImageCapture.Error.FormatError
    NoError = PySide2.QtMultimedia.QCameraImageCapture.Error.NoError
    NotReadyError = PySide2.QtMultimedia.QCameraImageCapture.Error.NotReadyError
    NotSupportedFeatureError = PySide2.QtMultimedia.QCameraImageCapture.Error.NotSupportedFeatureError
    OutOfSpaceError = PySide2.QtMultimedia.QCameraImageCapture.Error.OutOfSpaceError
    ResourceError = PySide2.QtMultimedia.QCameraImageCapture.Error.ResourceError
    SingleImageCapture = PySide2.QtMultimedia.QCameraImageCapture.DriveMode.SingleImageCapture
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000188746A6700>'


