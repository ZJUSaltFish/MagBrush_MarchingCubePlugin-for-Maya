# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAbstractVideoBuffer(__Shiboken.Object):
    """ QAbstractVideoBuffer(self, type: PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType) -> None """
    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> typing.Any """
        pass

    def handleType(self): # real signature unknown; restored from __doc__
        """ handleType(self) -> PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType """
        pass

    def mapMode(self): # real signature unknown; restored from __doc__
        """ mapMode(self) -> PySide2.QtMultimedia.QAbstractVideoBuffer.MapMode """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> None """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) -> None """
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


    CoreImageHandle = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.CoreImageHandle
    EGLImageHandle = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.EGLImageHandle
    GLTextureHandle = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.GLTextureHandle
    HandleType = None # (!) real value is "<class 'PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType'>"
    MapMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QAbstractVideoBuffer.MapMode'>"
    NoHandle = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.NoHandle
    NotMapped = PySide2.QtMultimedia.QAbstractVideoBuffer.MapMode.NotMapped
    QPixmapHandle = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.QPixmapHandle
    ReadOnly = PySide2.QtMultimedia.QAbstractVideoBuffer.MapMode.ReadOnly
    ReadWrite = PySide2.QtMultimedia.QAbstractVideoBuffer.MapMode.ReadWrite
    UserHandle = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.UserHandle
    WriteOnly = PySide2.QtMultimedia.QAbstractVideoBuffer.MapMode.WriteOnly
    XvShmImageHandle = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.XvShmImageHandle


