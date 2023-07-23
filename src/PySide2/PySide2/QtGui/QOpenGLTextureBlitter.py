# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLTextureBlitter(__Shiboken.Object):
    """ QOpenGLTextureBlitter(self) -> None """
    def bind(self, target=3553): # real signature unknown; restored from __doc__
        """ bind(self, target: int = 3553) -> None """
        pass

    def blit(self, texture, targetTransform, sourceOrigin): # real signature unknown; restored from __doc__
        """
        blit(self, texture: int, targetTransform: PySide2.QtGui.QMatrix4x4, sourceOrigin: PySide2.QtGui.QOpenGLTextureBlitter.Origin) -> None
        blit(self, texture: int, targetTransform: PySide2.QtGui.QMatrix4x4, sourceTransform: PySide2.QtGui.QMatrix3x3) -> None
        """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) -> None """
        pass

    def isCreated(self): # real signature unknown; restored from __doc__
        """ isCreated(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> None """
        pass

    def setOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setOpacity(self, opacity: float) -> None """
        pass

    def setRedBlueSwizzle(self, swizzle): # real signature unknown; restored from __doc__
        """ setRedBlueSwizzle(self, swizzle: bool) -> None """
        pass

    def sourceTransform(self, subTexture, textureSize, origin): # real signature unknown; restored from __doc__
        """ sourceTransform(subTexture: PySide2.QtCore.QRectF, textureSize: PySide2.QtCore.QSize, origin: PySide2.QtGui.QOpenGLTextureBlitter.Origin) -> PySide2.QtGui.QMatrix3x3 """
        pass

    def supportsExternalOESTarget(self): # real signature unknown; restored from __doc__
        """ supportsExternalOESTarget(self) -> bool """
        return False

    def targetTransform(self, target, viewport): # real signature unknown; restored from __doc__
        """ targetTransform(target: PySide2.QtCore.QRectF, viewport: PySide2.QtCore.QRect) -> PySide2.QtGui.QMatrix4x4 """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Origin = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTextureBlitter.Origin'>"
    OriginBottomLeft = PySide2.QtGui.QOpenGLTextureBlitter.Origin.OriginBottomLeft
    OriginTopLeft = PySide2.QtGui.QOpenGLTextureBlitter.Origin.OriginTopLeft


