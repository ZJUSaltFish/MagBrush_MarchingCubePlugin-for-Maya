# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QMediaServiceProviderHint(__Shiboken.Object):
    """
    QMediaServiceProviderHint(self) -> None
    QMediaServiceProviderHint(self, device: PySide2.QtCore.QByteArray) -> None
    QMediaServiceProviderHint(self, features: PySide2.QtMultimedia.QMediaServiceProviderHint.Features) -> None
    QMediaServiceProviderHint(self, mimeType: str, codecs: typing.Sequence[str]) -> None
    QMediaServiceProviderHint(self, other: PySide2.QtMultimedia.QMediaServiceProviderHint) -> None
    QMediaServiceProviderHint(self, position: PySide2.QtMultimedia.QCamera.Position) -> None
    """
    def cameraPosition(self): # real signature unknown; restored from __doc__
        """ cameraPosition(self) -> PySide2.QtMultimedia.QCamera.Position """
        pass

    def codecs(self): # real signature unknown; restored from __doc__
        """ codecs(self) -> typing.List[str] """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QByteArray """
        pass

    def features(self): # real signature unknown; restored from __doc__
        """ features(self) -> PySide2.QtMultimedia.QMediaServiceProviderHint.Features """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def mimeType(self): # real signature unknown; restored from __doc__
        """ mimeType(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtMultimedia.QMediaServiceProviderHint.Type """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    CameraPosition = PySide2.QtMultimedia.QMediaServiceProviderHint.Type.CameraPosition
    ContentType = PySide2.QtMultimedia.QMediaServiceProviderHint.Type.ContentType
    Device = PySide2.QtMultimedia.QMediaServiceProviderHint.Type.Device
    Feature = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaServiceProviderHint.Feature'>"
    Features = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaServiceProviderHint.Features'>"
    LowLatencyPlayback = PySide2.QtMultimedia.QMediaServiceProviderHint.Feature.LowLatencyPlayback
    Null = PySide2.QtMultimedia.QMediaServiceProviderHint.Type.Null
    RecordingSupport = PySide2.QtMultimedia.QMediaServiceProviderHint.Feature.RecordingSupport
    StreamPlayback = PySide2.QtMultimedia.QMediaServiceProviderHint.Feature.StreamPlayback
    SupportedFeatures = PySide2.QtMultimedia.QMediaServiceProviderHint.Type.SupportedFeatures
    Type = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaServiceProviderHint.Type'>"
    VideoSurface = PySide2.QtMultimedia.QMediaServiceProviderHint.Feature.VideoSurface
    __hash__ = None


