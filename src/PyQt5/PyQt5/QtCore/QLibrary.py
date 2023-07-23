# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QLibrary(QObject):
    """
    QLibrary(parent: typing.Optional[QObject] = None)
    QLibrary(fileName: str, parent: typing.Optional[QObject] = None)
    QLibrary(fileName: str, verNum: int, parent: typing.Optional[QObject] = None)
    QLibrary(fileName: str, version: str, parent: typing.Optional[QObject] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isLibrary(self, fileName): # real signature unknown; restored from __doc__
        """ isLibrary(fileName: str) -> bool """
        return False

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ isLoaded(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) -> bool """
        return False

    def loadHints(self): # real signature unknown; restored from __doc__
        """ loadHints(self) -> QLibrary.LoadHints """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resolve(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resolve(self, symbol: str) -> PyQt5.sip.voidptr
        resolve(fileName: str, symbol: str) -> PyQt5.sip.voidptr
        resolve(fileName: str, verNum: int, symbol: str) -> PyQt5.sip.voidptr
        resolve(fileName: str, version: str, symbol: str) -> PyQt5.sip.voidptr
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, fileName): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: str) """
        pass

    def setFileNameAndVersion(self, fileName, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFileNameAndVersion(self, fileName: str, verNum: int)
        setFileNameAndVersion(self, fileName: str, version: str)
        """
        pass

    def setLoadHints(self, hints, QLibrary_LoadHints=None, QLibrary_LoadHint=None): # real signature unknown; restored from __doc__
        """ setLoadHints(self, hints: Union[QLibrary.LoadHints, QLibrary.LoadHint]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ unload(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DeepBindHint = 16
    ExportExternalSymbolsHint = 2
    LoadArchiveMemberHint = 4
    PreventUnloadHint = 8
    ResolveAllSymbolsHint = 1


