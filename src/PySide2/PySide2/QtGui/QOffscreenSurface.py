# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QSurface import QSurface

class QOffscreenSurface(__PySide2_QtCore.QObject, QSurface):
    """
    QOffscreenSurface(self, screen: PySide2.QtGui.QScreen, parent: PySide2.QtCore.QObject) -> None
    QOffscreenSurface(self, screen: typing.Optional[PySide2.QtGui.QScreen] = None) -> None
    """
    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> None """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) -> None """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QSurfaceFormat """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nativeHandle(self): # real signature unknown; restored from __doc__
        """ nativeHandle(self) -> int """
        return 0

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> PySide2.QtGui.QSurfaceFormat """
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> PySide2.QtGui.QScreen """
        pass

    def screenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtGui.QSurfaceFormat) -> None """
        pass

    def setNativeHandle(self, handle): # real signature unknown; restored from __doc__
        """ setNativeHandle(self, handle: int) -> None """
        pass

    def setScreen(self, screen): # real signature unknown; restored from __doc__
        """ setScreen(self, screen: PySide2.QtGui.QScreen) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
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

    def __init__(self, screen, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00855780>'


