# encoding: utf-8
# module PyQt5.QtGui
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOpenGLContext(__PyQt5_QtCore.QObject):
    """ QOpenGLContext(parent: typing.Optional[QObject] = None) """
    def aboutToBeDestroyed(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def areSharing(self, first, second): # real signature unknown; restored from __doc__
        """ areSharing(first: QOpenGLContext, second: QOpenGLContext) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def currentContext(self): # real signature unknown; restored from __doc__
        """ currentContext() -> QOpenGLContext """
        return QOpenGLContext

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) """
        pass

    def extensions(self): # real signature unknown; restored from __doc__
        """ extensions(self) -> Set[QByteArray] """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QSurfaceFormat """
        return QSurfaceFormat

    def getProcAddress(self, procName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ getProcAddress(self, procName: Union[QByteArray, bytes, bytearray]) -> PyQt5.sip.voidptr """
        pass

    def globalShareContext(self): # real signature unknown; restored from __doc__
        """ globalShareContext() -> QOpenGLContext """
        return QOpenGLContext

    def hasExtension(self, extension, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ hasExtension(self, extension: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def isOpenGLES(self): # real signature unknown; restored from __doc__
        """ isOpenGLES(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self, surface): # real signature unknown; restored from __doc__
        """ makeCurrent(self, surface: QSurface) -> bool """
        return False

    def nativeHandle(self): # real signature unknown; restored from __doc__
        """ nativeHandle(self) -> Any """
        pass

    def openGLModuleHandle(self): # real signature unknown; restored from __doc__
        """ openGLModuleHandle() -> PyQt5.sip.voidptr """
        pass

    def openGLModuleType(self): # real signature unknown; restored from __doc__
        """ openGLModuleType() -> QOpenGLContext.OpenGLModuleType """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> QScreen """
        return QScreen

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: QSurfaceFormat) """
        pass

    def setNativeHandle(self, handle): # real signature unknown; restored from __doc__
        """ setNativeHandle(self, handle: Any) """
        pass

    def setScreen(self, screen): # real signature unknown; restored from __doc__
        """ setScreen(self, screen: QScreen) """
        pass

    def setShareContext(self, shareContext): # real signature unknown; restored from __doc__
        """ setShareContext(self, shareContext: QOpenGLContext) """
        pass

    def shareContext(self): # real signature unknown; restored from __doc__
        """ shareContext(self) -> QOpenGLContext """
        return QOpenGLContext

    def shareGroup(self): # real signature unknown; restored from __doc__
        """ shareGroup(self) -> QOpenGLContextGroup """
        return QOpenGLContextGroup

    def supportsThreadedOpenGL(self): # real signature unknown; restored from __doc__
        """ supportsThreadedOpenGL() -> bool """
        return False

    def surface(self): # real signature unknown; restored from __doc__
        """ surface(self) -> QSurface """
        return QSurface

    def swapBuffers(self, surface): # real signature unknown; restored from __doc__
        """ swapBuffers(self, surface: QSurface) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def versionFunctions(self, versionProfile, QOpenGLVersionProfile=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ versionFunctions(self, versionProfile: typing.Optional[QOpenGLVersionProfile] = None) -> object """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    LibGL = 0
    LibGLES = 1


