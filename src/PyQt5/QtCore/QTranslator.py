# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QTranslator(QObject):
    """ QTranslator(parent: typing.Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def language(self): # real signature unknown; restored from __doc__
        """ language(self) -> str """
        return ""

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, fileName: str, directory: str = '', searchDelimiters: str = '', suffix: str = '') -> bool
        load(self, locale: QLocale, fileName: str, prefix: str = '', directory: str = '', suffix: str = '') -> bool
        """
        return False

    def loadFromData(self, data, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ loadFromData(self, data: PyQt5.sip.array[bytes], directory: str = '') -> bool """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, context, sourceText, disambiguation, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ translate(self, context: str, sourceText: str, disambiguation: typing.Optional[str] = None, n: int = -1) -> str """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


