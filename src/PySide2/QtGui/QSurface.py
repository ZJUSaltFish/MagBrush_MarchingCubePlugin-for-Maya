# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSurface(__Shiboken.Object):
    """ QSurface(self, type: PySide2.QtGui.QSurface.SurfaceClass) -> None """
    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QSurfaceFormat """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def supportsOpenGL(self): # real signature unknown; restored from __doc__
        """ supportsOpenGL(self) -> bool """
        return False

    def surfaceClass(self): # real signature unknown; restored from __doc__
        """ surfaceClass(self) -> PySide2.QtGui.QSurface.SurfaceClass """
        pass

    def surfaceHandle(self): # real signature unknown; restored from __doc__
        """ surfaceHandle(self) -> int """
        return 0

    def surfaceType(self): # real signature unknown; restored from __doc__
        """ surfaceType(self) -> PySide2.QtGui.QSurface.SurfaceType """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    m_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MetalSurface = PySide2.QtGui.QSurface.SurfaceType.MetalSurface
    Offscreen = PySide2.QtGui.QSurface.SurfaceClass.Offscreen
    OpenGLSurface = PySide2.QtGui.QSurface.SurfaceType.OpenGLSurface
    OpenVGSurface = PySide2.QtGui.QSurface.SurfaceType.OpenVGSurface
    RasterGLSurface = PySide2.QtGui.QSurface.SurfaceType.RasterGLSurface
    RasterSurface = PySide2.QtGui.QSurface.SurfaceType.RasterSurface
    SurfaceClass = None # (!) real value is "<class 'PySide2.QtGui.QSurface.SurfaceClass'>"
    SurfaceType = None # (!) real value is "<class 'PySide2.QtGui.QSurface.SurfaceType'>"
    VulkanSurface = PySide2.QtGui.QSurface.SurfaceType.VulkanSurface
    Window = PySide2.QtGui.QSurface.SurfaceClass.Window


