# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QPaintDeviceWindow import QPaintDeviceWindow

class QOpenGLWindow(QPaintDeviceWindow):
    """
    QOpenGLWindow(self, shareContext: PySide2.QtGui.QOpenGLContext, updateBehavior: PySide2.QtGui.QOpenGLWindow.UpdateBehavior = PySide2.QtGui.QOpenGLWindow.UpdateBehavior.NoPartialUpdate, parent: typing.Optional[PySide2.QtGui.QWindow] = None) -> None
    QOpenGLWindow(self, updateBehavior: PySide2.QtGui.QOpenGLWindow.UpdateBehavior = PySide2.QtGui.QOpenGLWindow.UpdateBehavior.NoPartialUpdate, parent: typing.Optional[PySide2.QtGui.QWindow] = None) -> None
    """
    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> PySide2.QtGui.QOpenGLContext """
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) -> None """
        pass

    def frameSwapped(self, *args, **kwargs): # real signature unknown
        pass

    def grabFramebuffer(self): # real signature unknown; restored from __doc__
        """ grabFramebuffer(self) -> PySide2.QtGui.QImage """
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ initializeGL(self) -> None """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) -> None """
        pass

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) -> None """
        pass

    def paintOverGL(self): # real signature unknown; restored from __doc__
        """ paintOverGL(self) -> None """
        pass

    def paintUnderGL(self): # real signature unknown; restored from __doc__
        """ paintUnderGL(self) -> None """
        pass

    def redirected(self, arg__1): # real signature unknown; restored from __doc__
        """ redirected(self, arg__1: PySide2.QtCore.QPoint) -> PySide2.QtGui.QPaintDevice """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def resizeGL(self, w, h): # real signature unknown; restored from __doc__
        """ resizeGL(self, w: int, h: int) -> None """
        pass

    def shareContext(self): # real signature unknown; restored from __doc__
        """ shareContext(self) -> PySide2.QtGui.QOpenGLContext """
        pass

    def updateBehavior(self): # real signature unknown; restored from __doc__
        """ updateBehavior(self) -> PySide2.QtGui.QOpenGLWindow.UpdateBehavior """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, shareContext, updateBehavior=None, parent, PySide2_QtGui_QWindow=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    NoPartialUpdate = PySide2.QtGui.QOpenGLWindow.UpdateBehavior.NoPartialUpdate
    PartialUpdateBlend = PySide2.QtGui.QOpenGLWindow.UpdateBehavior.PartialUpdateBlend
    PartialUpdateBlit = PySide2.QtGui.QOpenGLWindow.UpdateBehavior.PartialUpdateBlit
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00844C40>'
    UpdateBehavior = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLWindow.UpdateBehavior'>"


