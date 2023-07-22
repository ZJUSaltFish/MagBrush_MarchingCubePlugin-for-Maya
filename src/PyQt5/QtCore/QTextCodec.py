# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTextCodec(__sip.wrapper):
    """ QTextCodec() """
    def aliases(self): # real signature unknown; restored from __doc__
        """ aliases(self) -> List[QByteArray] """
        return []

    def availableCodecs(self): # real signature unknown; restored from __doc__
        """ availableCodecs() -> List[QByteArray] """
        return []

    def availableMibs(self): # real signature unknown; restored from __doc__
        """ availableMibs() -> List[int] """
        return []

    def canEncode(self, a0): # real signature unknown; restored from __doc__
        """ canEncode(self, a0: str) -> bool """
        return False

    def codecForHtml(self, ba, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForHtml(ba: Union[QByteArray, bytes, bytearray]) -> QTextCodec
        codecForHtml(ba: Union[QByteArray, bytes, bytearray], defaultCodec: QTextCodec) -> QTextCodec
        """
        return QTextCodec

    def codecForLocale(self): # real signature unknown; restored from __doc__
        """ codecForLocale() -> QTextCodec """
        return QTextCodec

    def codecForMib(self, mib): # real signature unknown; restored from __doc__
        """ codecForMib(mib: int) -> QTextCodec """
        return QTextCodec

    def codecForName(self, name, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForName(name: Union[QByteArray, bytes, bytearray]) -> QTextCodec
        codecForName(name: str) -> QTextCodec
        """
        return QTextCodec

    def codecForUtfText(self, ba, QByteArray=None, bytes=None, bytearray=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        codecForUtfText(ba: Union[QByteArray, bytes, bytearray]) -> QTextCodec
        codecForUtfText(ba: Union[QByteArray, bytes, bytearray], defaultCodec: QTextCodec) -> QTextCodec
        """
        return QTextCodec

    def convertFromUnicode(self, in_, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ convertFromUnicode(self, in_: PyQt5.sip.array[str], state: QTextCodec.ConverterState) -> QByteArray """
        pass

    def convertToUnicode(self, in_, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ convertToUnicode(self, in_: PyQt5.sip.array[bytes], state: QTextCodec.ConverterState) -> str """
        pass

    def fromUnicode(self, uc): # real signature unknown; restored from __doc__
        """ fromUnicode(self, uc: str) -> QByteArray """
        return QByteArray

    def makeDecoder(self, flags, QTextCodec_ConversionFlags=None, QTextCodec_ConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ makeDecoder(self, flags: Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag] = QTextCodec.DefaultConversion) -> QTextDecoder """
        pass

    def makeEncoder(self, flags, QTextCodec_ConversionFlags=None, QTextCodec_ConversionFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ makeEncoder(self, flags: Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag] = QTextCodec.DefaultConversion) -> QTextEncoder """
        pass

    def mibEnum(self): # real signature unknown; restored from __doc__
        """ mibEnum(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> QByteArray """
        return QByteArray

    def setCodecForLocale(self, c): # real signature unknown; restored from __doc__
        """ setCodecForLocale(c: QTextCodec) """
        pass

    def toUnicode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        toUnicode(self, a0: Union[QByteArray, bytes, bytearray]) -> str
        toUnicode(self, chars: bytes) -> str
        toUnicode(self, in_: PyQt5.sip.array[bytes], state: typing.Optional[QTextCodec.ConverterState] = None) -> str
        """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ConvertInvalidToNull = -2147483648
    DefaultConversion = 0
    IgnoreHeader = 1


