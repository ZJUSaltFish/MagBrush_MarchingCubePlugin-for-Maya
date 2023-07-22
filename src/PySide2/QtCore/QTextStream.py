# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QTextStream(__Shiboken.Object):
    """
    QTextStream(self) -> None
    QTextStream(self, array: PySide2.QtCore.QByteArray, openMode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> None
    QTextStream(self, device: PySide2.QtCore.QIODevice) -> None
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def autoDetectUnicode(self): # real signature unknown; restored from __doc__
        """ autoDetectUnicode(self) -> bool """
        return False

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> PySide2.QtCore.QTextCodec """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def fieldAlignment(self): # real signature unknown; restored from __doc__
        """ fieldAlignment(self) -> PySide2.QtCore.QTextStream.FieldAlignment """
        pass

    def fieldWidth(self): # real signature unknown; restored from __doc__
        """ fieldWidth(self) -> int """
        return 0

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> None """
        pass

    def generateByteOrderMark(self): # real signature unknown; restored from __doc__
        """ generateByteOrderMark(self) -> bool """
        return False

    def integerBase(self): # real signature unknown; restored from __doc__
        """ integerBase(self) -> int """
        return 0

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> PySide2.QtCore.QLocale """
        pass

    def numberFlags(self): # real signature unknown; restored from __doc__
        """ numberFlags(self) -> PySide2.QtCore.QTextStream.NumberFlags """
        pass

    def padChar(self): # real signature unknown; restored from __doc__
        """ padChar(self) -> str """
        return ""

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> int """
        return 0

    def read(self, maxlen): # real signature unknown; restored from __doc__
        """ read(self, maxlen: int) -> str """
        return ""

    def readAll(self): # real signature unknown; restored from __doc__
        """ readAll(self) -> str """
        return ""

    def readLine(self, maxlen=0): # real signature unknown; restored from __doc__
        """ readLine(self, maxlen: int = 0) -> str """
        return ""

    def realNumberNotation(self): # real signature unknown; restored from __doc__
        """ realNumberNotation(self) -> PySide2.QtCore.QTextStream.RealNumberNotation """
        pass

    def realNumberPrecision(self): # real signature unknown; restored from __doc__
        """ realNumberPrecision(self) -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resetStatus(self): # real signature unknown; restored from __doc__
        """ resetStatus(self) -> None """
        pass

    def seek(self, pos): # real signature unknown; restored from __doc__
        """ seek(self, pos: int) -> bool """
        return False

    def setAutoDetectUnicode(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoDetectUnicode(self, enabled: bool) -> None """
        pass

    def setCodec(self, codec): # real signature unknown; restored from __doc__
        """
        setCodec(self, codec: PySide2.QtCore.QTextCodec) -> None
        setCodec(self, codecName: bytes) -> None
        """
        pass

    def setDevice(self, device): # real signature unknown; restored from __doc__
        """ setDevice(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def setFieldAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setFieldAlignment(self, alignment: PySide2.QtCore.QTextStream.FieldAlignment) -> None """
        pass

    def setFieldWidth(self, width): # real signature unknown; restored from __doc__
        """ setFieldWidth(self, width: int) -> None """
        pass

    def setGenerateByteOrderMark(self, generate): # real signature unknown; restored from __doc__
        """ setGenerateByteOrderMark(self, generate: bool) -> None """
        pass

    def setIntegerBase(self, base): # real signature unknown; restored from __doc__
        """ setIntegerBase(self, base: int) -> None """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: PySide2.QtCore.QLocale) -> None """
        pass

    def setNumberFlags(self, flags): # real signature unknown; restored from __doc__
        """ setNumberFlags(self, flags: PySide2.QtCore.QTextStream.NumberFlags) -> None """
        pass

    def setPadChar(self, ch): # real signature unknown; restored from __doc__
        """ setPadChar(self, ch: str) -> None """
        pass

    def setRealNumberNotation(self, notation): # real signature unknown; restored from __doc__
        """ setRealNumberNotation(self, notation: PySide2.QtCore.QTextStream.RealNumberNotation) -> None """
        pass

    def setRealNumberPrecision(self, precision): # real signature unknown; restored from __doc__
        """ setRealNumberPrecision(self, precision: int) -> None """
        pass

    def setStatus(self, status): # real signature unknown; restored from __doc__
        """ setStatus(self, status: PySide2.QtCore.QTextStream.Status) -> None """
        pass

    def skipWhiteSpace(self): # real signature unknown; restored from __doc__
        """ skipWhiteSpace(self) -> None """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtCore.QTextStream.Status """
        pass

    def string(self): # real signature unknown; restored from __doc__
        """ string(self) -> typing.List[str] """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __lshift__(self, array): # real signature unknown; restored from __doc__
        """
        __lshift__(self, array: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextStream
        __lshift__(self, ch: str) -> PySide2.QtCore.QTextStream
        __lshift__(self, ch: int) -> PySide2.QtCore.QTextStream
        __lshift__(self, f: float) -> PySide2.QtCore.QTextStream
        __lshift__(self, i: int) -> PySide2.QtCore.QTextStream
        __lshift__(self, i: int) -> PySide2.QtCore.QTextStream
        __lshift__(self, m: PySide2.QtCore.QTextStreamManipulator) -> PySide2.QtCore.QTextStream
        __lshift__(self, s: str) -> PySide2.QtCore.QTextStream
        __lshift__(self, s: str) -> PySide2.QtCore.QTextStream
        
        Return self<<value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, array): # real signature unknown; restored from __doc__
        """
        __rshift__(self, array: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextStream
        
        Return self>>value.
        """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AlignAccountingStyle = PySide2.QtCore.QTextStream.FieldAlignment.AlignAccountingStyle
    AlignCenter = PySide2.QtCore.QTextStream.FieldAlignment.AlignCenter
    AlignLeft = PySide2.QtCore.QTextStream.FieldAlignment.AlignLeft
    AlignRight = PySide2.QtCore.QTextStream.FieldAlignment.AlignRight
    FieldAlignment = None # (!) real value is "<class 'PySide2.QtCore.QTextStream.FieldAlignment'>"
    FixedNotation = PySide2.QtCore.QTextStream.RealNumberNotation.FixedNotation
    ForcePoint = PySide2.QtCore.QTextStream.NumberFlag.ForcePoint
    ForceSign = PySide2.QtCore.QTextStream.NumberFlag.ForceSign
    NumberFlag = None # (!) real value is "<class 'PySide2.QtCore.QTextStream.NumberFlag'>"
    NumberFlags = None # (!) real value is "<class 'PySide2.QtCore.QTextStream.NumberFlags'>"
    Ok = PySide2.QtCore.QTextStream.Status.Ok
    ReadCorruptData = PySide2.QtCore.QTextStream.Status.ReadCorruptData
    ReadPastEnd = PySide2.QtCore.QTextStream.Status.ReadPastEnd
    RealNumberNotation = None # (!) real value is "<class 'PySide2.QtCore.QTextStream.RealNumberNotation'>"
    ScientificNotation = PySide2.QtCore.QTextStream.RealNumberNotation.ScientificNotation
    ShowBase = PySide2.QtCore.QTextStream.NumberFlag.ShowBase
    SmartNotation = PySide2.QtCore.QTextStream.RealNumberNotation.SmartNotation
    Status = None # (!) real value is "<class 'PySide2.QtCore.QTextStream.Status'>"
    UppercaseBase = PySide2.QtCore.QTextStream.NumberFlag.UppercaseBase
    UppercaseDigits = PySide2.QtCore.QTextStream.NumberFlag.UppercaseDigits
    WriteFailed = PySide2.QtCore.QTextStream.Status.WriteFailed


