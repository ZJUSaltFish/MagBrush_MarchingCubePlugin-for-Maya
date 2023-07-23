# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLFramebufferObject(__Shiboken.Object):
    """
    QOpenGLFramebufferObject(self, size: PySide2.QtCore.QSize, attachment: PySide2.QtGui.QOpenGLFramebufferObject.Attachment, target: int = 3553, internalFormat: int = 0) -> None
    QOpenGLFramebufferObject(self, size: PySide2.QtCore.QSize, format: PySide2.QtGui.QOpenGLFramebufferObjectFormat) -> None
    QOpenGLFramebufferObject(self, size: PySide2.QtCore.QSize, target: int = 3553) -> None
    QOpenGLFramebufferObject(self, width: int, height: int, attachment: PySide2.QtGui.QOpenGLFramebufferObject.Attachment, target: int = 3553, internalFormat: int = 0) -> None
    QOpenGLFramebufferObject(self, width: int, height: int, format: PySide2.QtGui.QOpenGLFramebufferObjectFormat) -> None
    QOpenGLFramebufferObject(self, width: int, height: int, target: int = 3553) -> None
    """
    def addColorAttachment(self, size, internalFormat=0): # real signature unknown; restored from __doc__
        """
        addColorAttachment(self, size: PySide2.QtCore.QSize, internalFormat: int = 0) -> None
        addColorAttachment(self, width: int, height: int, internalFormat: int = 0) -> None
        """
        pass

    def attachment(self): # real signature unknown; restored from __doc__
        """ attachment(self) -> PySide2.QtGui.QOpenGLFramebufferObject.Attachment """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bindDefault(self): # real signature unknown; restored from __doc__
        """ bindDefault() -> bool """
        return False

    def blitFramebuffer(self, target, source, buffers=16384, filter=9728): # real signature unknown; restored from __doc__
        """
        blitFramebuffer(target: PySide2.QtGui.QOpenGLFramebufferObject, source: PySide2.QtGui.QOpenGLFramebufferObject, buffers: int = 16384, filter: int = 9728) -> None
        blitFramebuffer(target: PySide2.QtGui.QOpenGLFramebufferObject, targetRect: PySide2.QtCore.QRect, source: PySide2.QtGui.QOpenGLFramebufferObject, sourceRect: PySide2.QtCore.QRect, buffers: int, filter: int, readColorAttachmentIndex: int, drawColorAttachmentIndex: int) -> None
        blitFramebuffer(target: PySide2.QtGui.QOpenGLFramebufferObject, targetRect: PySide2.QtCore.QRect, source: PySide2.QtGui.QOpenGLFramebufferObject, sourceRect: PySide2.QtCore.QRect, buffers: int, filter: int, readColorAttachmentIndex: int, drawColorAttachmentIndex: int, restorePolicy: PySide2.QtGui.QOpenGLFramebufferObject.FramebufferRestorePolicy) -> None
        blitFramebuffer(target: PySide2.QtGui.QOpenGLFramebufferObject, targetRect: PySide2.QtCore.QRect, source: PySide2.QtGui.QOpenGLFramebufferObject, sourceRect: PySide2.QtCore.QRect, buffers: int = 16384, filter: int = 9728) -> None
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QOpenGLFramebufferObjectFormat """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def hasOpenGLFramebufferBlit(self): # real signature unknown; restored from __doc__
        """ hasOpenGLFramebufferBlit() -> bool """
        return False

    def hasOpenGLFramebufferObjects(self): # real signature unknown; restored from __doc__
        """ hasOpenGLFramebufferObjects() -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isBound(self): # real signature unknown; restored from __doc__
        """ isBound(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> bool """
        return False

    def setAttachment(self, attachment): # real signature unknown; restored from __doc__
        """ setAttachment(self, attachment: PySide2.QtGui.QOpenGLFramebufferObject.Attachment) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ sizes(self) -> typing.List[PySide2.QtCore.QSize] """
        pass

    def takeTexture(self): # real signature unknown; restored from __doc__
        """
        takeTexture(self) -> int
        takeTexture(self, colorAttachmentIndex: int) -> int
        """
        return 0

    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> int """
        return 0

    def textures(self): # real signature unknown; restored from __doc__
        """ textures(self) -> typing.List[int] """
        pass

    def toImage(self): # real signature unknown; restored from __doc__
        """
        toImage(self) -> PySide2.QtGui.QImage
        toImage(self, flipped: bool) -> PySide2.QtGui.QImage
        toImage(self, flipped: bool, colorAttachmentIndex: int) -> PySide2.QtGui.QImage
        """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, size, attachment, target=3553, internalFormat=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Attachment = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLFramebufferObject.Attachment'>"
    CombinedDepthStencil = PySide2.QtGui.QOpenGLFramebufferObject.Attachment.CombinedDepthStencil
    Depth = PySide2.QtGui.QOpenGLFramebufferObject.Attachment.Depth
    DontRestoreFramebufferBinding = PySide2.QtGui.QOpenGLFramebufferObject.FramebufferRestorePolicy.DontRestoreFramebufferBinding
    FramebufferRestorePolicy = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLFramebufferObject.FramebufferRestorePolicy'>"
    NoAttachment = PySide2.QtGui.QOpenGLFramebufferObject.Attachment.NoAttachment
    RestoreFrameBufferBinding = PySide2.QtGui.QOpenGLFramebufferObject.FramebufferRestorePolicy.RestoreFrameBufferBinding
    RestoreFramebufferBindingToDefault = PySide2.QtGui.QOpenGLFramebufferObject.FramebufferRestorePolicy.RestoreFramebufferBindingToDefault


