# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLContext(__PySide2_QtCore.QObject):
    """ QOpenGLContext(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def aboutToBeDestroyed(self, *args, **kwargs): # real signature unknown
        pass

    def areSharing(self, first, second): # real signature unknown; restored from __doc__
        """ areSharing(first: PySide2.QtGui.QOpenGLContext, second: PySide2.QtGui.QOpenGLContext) -> bool """
        return False

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def currentContext(self): # real signature unknown; restored from __doc__
        """ currentContext() -> PySide2.QtGui.QOpenGLContext """
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) -> None """
        pass

    def extensions(self): # real signature unknown; restored from __doc__
        """ extensions(self) -> typing.Set[PySide2.QtCore.QByteArray] """
        pass

    def extraFunctions(self): # real signature unknown; restored from __doc__
        """ extraFunctions(self) -> PySide2.QtGui.QOpenGLExtraFunctions """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QSurfaceFormat """
        pass

    def functions(self): # real signature unknown; restored from __doc__
        """ functions(self) -> PySide2.QtGui.QOpenGLFunctions """
        pass

    def globalShareContext(self): # real signature unknown; restored from __doc__
        """ globalShareContext() -> PySide2.QtGui.QOpenGLContext """
        pass

    def hasExtension(self, extension): # real signature unknown; restored from __doc__
        """ hasExtension(self, extension: PySide2.QtCore.QByteArray) -> bool """
        return False

    def isOpenGLES(self): # real signature unknown; restored from __doc__
        """ isOpenGLES(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self, surface): # real signature unknown; restored from __doc__
        """ makeCurrent(self, surface: PySide2.QtGui.QSurface) -> bool """
        return False

    def nativeHandle(self): # real signature unknown; restored from __doc__
        """ nativeHandle(self) -> typing.Any """
        pass

    def openGLModuleHandle(self): # real signature unknown; restored from __doc__
        """ openGLModuleHandle() -> int """
        return 0

    def openGLModuleType(self): # real signature unknown; restored from __doc__
        """ openGLModuleType() -> PySide2.QtGui.QOpenGLContext.OpenGLModuleType """
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> PySide2.QtGui.QScreen """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtGui.QSurfaceFormat) -> None """
        pass

    def setNativeHandle(self, handle): # real signature unknown; restored from __doc__
        """ setNativeHandle(self, handle: typing.Any) -> None """
        pass

    def setScreen(self, screen): # real signature unknown; restored from __doc__
        """ setScreen(self, screen: PySide2.QtGui.QScreen) -> None """
        pass

    def setShareContext(self, shareContext): # real signature unknown; restored from __doc__
        """ setShareContext(self, shareContext: PySide2.QtGui.QOpenGLContext) -> None """
        pass

    def shareContext(self): # real signature unknown; restored from __doc__
        """ shareContext(self) -> PySide2.QtGui.QOpenGLContext """
        pass

    def shareGroup(self): # real signature unknown; restored from __doc__
        """ shareGroup(self) -> PySide2.QtGui.QOpenGLContextGroup """
        pass

    def supportsThreadedOpenGL(self): # real signature unknown; restored from __doc__
        """ supportsThreadedOpenGL() -> bool """
        return False

    def surface(self): # real signature unknown; restored from __doc__
        """ surface(self) -> PySide2.QtGui.QSurface """
        pass

    def swapBuffers(self, surface): # real signature unknown; restored from __doc__
        """ swapBuffers(self, surface: PySide2.QtGui.QSurface) -> None """
        pass

    def versionFunctions(self, versionProfile=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ versionFunctions(self, versionProfile: PySide2.QtGui.QOpenGLVersionProfile = Default(QOpenGLVersionProfile)) -> PySide2.QtGui.QAbstractOpenGLFunctions """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    LibGL = PySide2.QtGui.QOpenGLContext.OpenGLModuleType.LibGL
    LibGLES = PySide2.QtGui.QOpenGLContext.OpenGLModuleType.LibGLES
    OpenGLModuleType = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLContext.OpenGLModuleType'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00855640>'


