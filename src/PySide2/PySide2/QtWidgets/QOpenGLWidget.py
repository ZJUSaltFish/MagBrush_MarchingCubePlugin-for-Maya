# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QWidget import QWidget

class QOpenGLWidget(QWidget):
    """ QOpenGLWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def aboutToCompose(self, *args, **kwargs): # real signature unknown
        pass

    def aboutToResize(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> PySide2.QtGui.QOpenGLContext """
        pass

    def defaultFramebufferObject(self): # real signature unknown; restored from __doc__
        """ defaultFramebufferObject(self) -> int """
        return 0

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QSurfaceFormat """
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

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def paintEvent(self, e): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) -> None """
        pass

    def redirected(self, p): # real signature unknown; restored from __doc__
        """ redirected(self, p: PySide2.QtCore.QPoint) -> PySide2.QtGui.QPaintDevice """
        pass

    def resized(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, e): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def resizeGL(self, w, h): # real signature unknown; restored from __doc__
        """ resizeGL(self, w: int, h: int) -> None """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtGui.QSurfaceFormat) -> None """
        pass

    def setTextureFormat(self, texFormat): # real signature unknown; restored from __doc__
        """ setTextureFormat(self, texFormat: int) -> None """
        pass

    def setUpdateBehavior(self, updateBehavior): # real signature unknown; restored from __doc__
        """ setUpdateBehavior(self, updateBehavior: PySide2.QtWidgets.QOpenGLWidget.UpdateBehavior) -> None """
        pass

    def textureFormat(self): # real signature unknown; restored from __doc__
        """ textureFormat(self) -> int """
        return 0

    def updateBehavior(self): # real signature unknown; restored from __doc__
        """ updateBehavior(self) -> PySide2.QtWidgets.QOpenGLWidget.UpdateBehavior """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    NoPartialUpdate = PySide2.QtWidgets.QOpenGLWidget.UpdateBehavior.NoPartialUpdate
    PartialUpdate = PySide2.QtWidgets.QOpenGLWidget.UpdateBehavior.PartialUpdate
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F508308C0>'
    UpdateBehavior = None # (!) real value is "<class 'PySide2.QtWidgets.QOpenGLWidget.UpdateBehavior'>"


