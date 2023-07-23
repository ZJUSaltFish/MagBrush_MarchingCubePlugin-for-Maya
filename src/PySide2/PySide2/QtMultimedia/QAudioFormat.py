# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAudioFormat(__Shiboken.Object):
    """
    QAudioFormat(self) -> None
    QAudioFormat(self, other: PySide2.QtMultimedia.QAudioFormat) -> None
    """
    def byteOrder(self): # real signature unknown; restored from __doc__
        """ byteOrder(self) -> PySide2.QtMultimedia.QAudioFormat.Endian """
        pass

    def bytesForDuration(self, duration): # real signature unknown; restored from __doc__
        """ bytesForDuration(self, duration: int) -> int """
        return 0

    def bytesForFrames(self, frameCount): # real signature unknown; restored from __doc__
        """ bytesForFrames(self, frameCount: int) -> int """
        return 0

    def bytesPerFrame(self): # real signature unknown; restored from __doc__
        """ bytesPerFrame(self) -> int """
        return 0

    def channelCount(self): # real signature unknown; restored from __doc__
        """ channelCount(self) -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> str """
        return ""

    def durationForBytes(self, byteCount): # real signature unknown; restored from __doc__
        """ durationForBytes(self, byteCount: int) -> int """
        return 0

    def durationForFrames(self, frameCount): # real signature unknown; restored from __doc__
        """ durationForFrames(self, frameCount: int) -> int """
        return 0

    def framesForBytes(self, byteCount): # real signature unknown; restored from __doc__
        """ framesForBytes(self, byteCount: int) -> int """
        return 0

    def framesForDuration(self, duration): # real signature unknown; restored from __doc__
        """ framesForDuration(self, duration: int) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def sampleRate(self): # real signature unknown; restored from __doc__
        """ sampleRate(self) -> int """
        return 0

    def sampleSize(self): # real signature unknown; restored from __doc__
        """ sampleSize(self) -> int """
        return 0

    def sampleType(self): # real signature unknown; restored from __doc__
        """ sampleType(self) -> PySide2.QtMultimedia.QAudioFormat.SampleType """
        pass

    def setByteOrder(self, byteOrder): # real signature unknown; restored from __doc__
        """ setByteOrder(self, byteOrder: PySide2.QtMultimedia.QAudioFormat.Endian) -> None """
        pass

    def setChannelCount(self, channelCount): # real signature unknown; restored from __doc__
        """ setChannelCount(self, channelCount: int) -> None """
        pass

    def setCodec(self, codec): # real signature unknown; restored from __doc__
        """ setCodec(self, codec: str) -> None """
        pass

    def setSampleRate(self, sampleRate): # real signature unknown; restored from __doc__
        """ setSampleRate(self, sampleRate: int) -> None """
        pass

    def setSampleSize(self, sampleSize): # real signature unknown; restored from __doc__
        """ setSampleSize(self, sampleSize: int) -> None """
        pass

    def setSampleType(self, sampleType): # real signature unknown; restored from __doc__
        """ setSampleType(self, sampleType: PySide2.QtMultimedia.QAudioFormat.SampleType) -> None """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    BigEndian = PySide2.QtMultimedia.QAudioFormat.Endian.BigEndian
    Endian = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudioFormat.Endian'>"
    Float = PySide2.QtMultimedia.QAudioFormat.SampleType.Float
    LittleEndian = PySide2.QtMultimedia.QAudioFormat.Endian.LittleEndian
    SampleType = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudioFormat.SampleType'>"
    SignedInt = PySide2.QtMultimedia.QAudioFormat.SampleType.SignedInt
    Unknown = PySide2.QtMultimedia.QAudioFormat.SampleType.Unknown
    UnSignedInt = PySide2.QtMultimedia.QAudioFormat.SampleType.UnSignedInt
    __hash__ = None


