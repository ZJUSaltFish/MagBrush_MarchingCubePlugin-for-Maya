# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAudioDeviceInfo(__Shiboken.Object):
    """
    QAudioDeviceInfo(self) -> None
    QAudioDeviceInfo(self, other: PySide2.QtMultimedia.QAudioDeviceInfo) -> None
    """
    def availableDevices(self, mode): # real signature unknown; restored from __doc__
        """ availableDevices(mode: PySide2.QtMultimedia.QAudio.Mode) -> typing.List[PySide2.QtMultimedia.QAudioDeviceInfo] """
        pass

    def defaultInputDevice(self): # real signature unknown; restored from __doc__
        """ defaultInputDevice() -> PySide2.QtMultimedia.QAudioDeviceInfo """
        pass

    def defaultOutputDevice(self): # real signature unknown; restored from __doc__
        """ defaultOutputDevice() -> PySide2.QtMultimedia.QAudioDeviceInfo """
        pass

    def deviceName(self): # real signature unknown; restored from __doc__
        """ deviceName(self) -> str """
        return ""

    def isFormatSupported(self, format): # real signature unknown; restored from __doc__
        """ isFormatSupported(self, format: PySide2.QtMultimedia.QAudioFormat) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def nearestFormat(self, format): # real signature unknown; restored from __doc__
        """ nearestFormat(self, format: PySide2.QtMultimedia.QAudioFormat) -> PySide2.QtMultimedia.QAudioFormat """
        pass

    def preferredFormat(self): # real signature unknown; restored from __doc__
        """ preferredFormat(self) -> PySide2.QtMultimedia.QAudioFormat """
        pass

    def realm(self): # real signature unknown; restored from __doc__
        """ realm(self) -> str """
        return ""

    def supportedByteOrders(self): # real signature unknown; restored from __doc__
        """ supportedByteOrders(self) -> typing.List[PySide2.QtMultimedia.QAudioFormat.Endian] """
        pass

    def supportedChannelCounts(self): # real signature unknown; restored from __doc__
        """ supportedChannelCounts(self) -> typing.List[int] """
        pass

    def supportedCodecs(self): # real signature unknown; restored from __doc__
        """ supportedCodecs(self) -> typing.List[str] """
        pass

    def supportedSampleRates(self): # real signature unknown; restored from __doc__
        """ supportedSampleRates(self) -> typing.List[int] """
        pass

    def supportedSampleSizes(self): # real signature unknown; restored from __doc__
        """ supportedSampleSizes(self) -> typing.List[int] """
        pass

    def supportedSampleTypes(self): # real signature unknown; restored from __doc__
        """ supportedSampleTypes(self) -> typing.List[PySide2.QtMultimedia.QAudioFormat.SampleType] """
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

    __hash__ = None


