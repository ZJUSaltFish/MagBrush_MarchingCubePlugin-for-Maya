# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QTextCodec(__Shiboken.Object):
    """ QTextCodec(self) -> None """
    def aliases(self): # real signature unknown; restored from __doc__
        """ aliases(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def availableCodecs(self): # real signature unknown; restored from __doc__
        """ availableCodecs() -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def availableMibs(self): # real signature unknown; restored from __doc__
        """ availableMibs() -> typing.List[int] """
        pass

    def canEncode(self, arg__1): # real signature unknown; restored from __doc__
        """
        canEncode(self, arg__1: str) -> bool
        canEncode(self, arg__1: str) -> bool
        """
        return False

    def codecForHtml(self, ba): # real signature unknown; restored from __doc__
        """
        codecForHtml(ba: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextCodec
        codecForHtml(ba: PySide2.QtCore.QByteArray, defaultCodec: PySide2.QtCore.QTextCodec) -> PySide2.QtCore.QTextCodec
        """
        pass

    def codecForLocale(self): # real signature unknown; restored from __doc__
        """ codecForLocale() -> PySide2.QtCore.QTextCodec """
        pass

    def codecForMib(self, mib): # real signature unknown; restored from __doc__
        """ codecForMib(mib: int) -> PySide2.QtCore.QTextCodec """
        pass

    def codecForName(self, name): # real signature unknown; restored from __doc__
        """
        codecForName(name: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextCodec
        codecForName(name: bytes) -> PySide2.QtCore.QTextCodec
        """
        pass

    def codecForUtfText(self, ba): # real signature unknown; restored from __doc__
        """
        codecForUtfText(ba: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextCodec
        codecForUtfText(ba: PySide2.QtCore.QByteArray, defaultCodec: PySide2.QtCore.QTextCodec) -> PySide2.QtCore.QTextCodec
        """
        pass

    def convertToUnicode(self, in_, length, state): # real signature unknown; restored from __doc__
        """ convertToUnicode(self, in_: bytes, length: int, state: PySide2.QtCore.QTextCodec.ConverterState) -> str """
        return ""

    def fromUnicode(self, uc): # real signature unknown; restored from __doc__
        """ fromUnicode(self, uc: str) -> PySide2.QtCore.QByteArray """
        pass

    def makeDecoder(self, flags=None): # real signature unknown; restored from __doc__
        """ makeDecoder(self, flags: PySide2.QtCore.QTextCodec.ConversionFlags = PySide2.QtCore.QTextCodec.ConversionFlag.DefaultConversion) -> PySide2.QtCore.QTextDecoder """
        pass

    def makeEncoder(self, flags=None): # real signature unknown; restored from __doc__
        """ makeEncoder(self, flags: PySide2.QtCore.QTextCodec.ConversionFlags = PySide2.QtCore.QTextCodec.ConversionFlag.DefaultConversion) -> PySide2.QtCore.QTextEncoder """
        pass

    def mibEnum(self): # real signature unknown; restored from __doc__
        """ mibEnum(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> PySide2.QtCore.QByteArray """
        pass

    def setCodecForLocale(self, c): # real signature unknown; restored from __doc__
        """ setCodecForLocale(c: PySide2.QtCore.QTextCodec) -> None """
        pass

    def toUnicode(self, arg__1): # real signature unknown; restored from __doc__
        """
        toUnicode(self, arg__1: PySide2.QtCore.QByteArray) -> str
        toUnicode(self, chars: bytes) -> str
        toUnicode(self, in_: bytes, length: int, state: typing.Optional[PySide2.QtCore.QTextCodec.ConverterState] = None) -> str
        """
        return ""

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

    ConversionFlag = None # (!) real value is "<class 'PySide2.QtCore.QTextCodec.ConversionFlag'>"
    ConversionFlags = None # (!) real value is "<class 'PySide2.QtCore.QTextCodec.ConversionFlags'>"
    ConverterState = None # (!) real value is "<class 'PySide2.QtCore.QTextCodec.ConverterState'>"
    ConvertInvalidToNull = PySide2.QtCore.QTextCodec.ConversionFlag.ConvertInvalidToNull
    DefaultConversion = PySide2.QtCore.QTextCodec.ConversionFlag.DefaultConversion
    FreeFunction = PySide2.QtCore.QTextCodec.ConversionFlag.FreeFunction
    IgnoreHeader = PySide2.QtCore.QTextCodec.ConversionFlag.IgnoreHeader


