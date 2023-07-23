# encoding: utf-8
# module PySide2.QtMultimediaWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimediaWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtMultimedia as __PySide2_QtMultimedia
import PySide2.QtWidgets as __PySide2_QtWidgets


# no functions
# classes

class QVideoWidget(__PySide2_QtWidgets.QWidget, __PySide2_QtMultimedia.QMediaBindableInterface):
    """ QVideoWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def aspectRatioMode(self): # real signature unknown; restored from __doc__
        """ aspectRatioMode(self) -> PySide2.QtCore.Qt.AspectRatioMode """
        pass

    def brightness(self): # real signature unknown; restored from __doc__
        """ brightness(self) -> int """
        return 0

    def brightnessChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contrast(self): # real signature unknown; restored from __doc__
        """ contrast(self) -> int """
        return 0

    def contrastChanged(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def fullScreenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, event): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: PySide2.QtGui.QHideEvent) -> None """
        pass

    def hue(self): # real signature unknown; restored from __doc__
        """ hue(self) -> int """
        return 0

    def hueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> PySide2.QtMultimedia.QMediaObject """
        pass

    def moveEvent(self, event): # real signature unknown; restored from __doc__
        """ moveEvent(self, event: PySide2.QtGui.QMoveEvent) -> None """
        pass

    def nativeEvent(self, eventType, message): # real signature unknown; restored from __doc__
        """ nativeEvent(self, eventType: PySide2.QtCore.QByteArray, message: int) -> typing.Tuple[bool, int] """
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def saturation(self): # real signature unknown; restored from __doc__
        """ saturation(self) -> int """
        return 0

    def saturationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setAspectRatioMode(self, mode): # real signature unknown; restored from __doc__
        """ setAspectRatioMode(self, mode: PySide2.QtCore.Qt.AspectRatioMode) -> None """
        pass

    def setBrightness(self, brightness): # real signature unknown; restored from __doc__
        """ setBrightness(self, brightness: int) -> None """
        pass

    def setContrast(self, contrast): # real signature unknown; restored from __doc__
        """ setContrast(self, contrast: int) -> None """
        pass

    def setFullScreen(self, fullScreen): # real signature unknown; restored from __doc__
        """ setFullScreen(self, fullScreen: bool) -> None """
        pass

    def setHue(self, hue): # real signature unknown; restored from __doc__
        """ setHue(self, hue: int) -> None """
        pass

    def setMediaObject(self, p_object): # real signature unknown; restored from __doc__
        """ setMediaObject(self, object: PySide2.QtMultimedia.QMediaObject) -> bool """
        return False

    def setSaturation(self, saturation): # real signature unknown; restored from __doc__
        """ setSaturation(self, saturation: int) -> None """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def videoSurface(self): # real signature unknown; restored from __doc__
        """ videoSurface(self) -> PySide2.QtMultimedia.QAbstractVideoSurface """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000221BE8AE900>'


class QCameraViewfinder(QVideoWidget):
    """ QCameraViewfinder(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> PySide2.QtMultimedia.QMediaObject """
        pass

    def setMediaObject(self, p_object): # real signature unknown; restored from __doc__
        """ setMediaObject(self, object: PySide2.QtMultimedia.QMediaObject) -> bool """
        return False

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000221BE8AE9C0>'


class QGraphicsVideoItem(__PySide2_QtWidgets.QGraphicsObject, __PySide2_QtMultimedia.QMediaBindableInterface):
    """ QGraphicsVideoItem(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None """
    def aspectRatioMode(self): # real signature unknown; restored from __doc__
        """ aspectRatioMode(self) -> PySide2.QtCore.Qt.AspectRatioMode """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange, value: typing.Any) -> typing.Any """
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> PySide2.QtMultimedia.QMediaObject """
        pass

    def nativeSize(self): # real signature unknown; restored from __doc__
        """ nativeSize(self) -> PySide2.QtCore.QSizeF """
        pass

    def nativeSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> PySide2.QtCore.QPointF """
        pass

    def paint(self, painter, option, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def setAspectRatioMode(self, mode): # real signature unknown; restored from __doc__
        """ setAspectRatioMode(self, mode: PySide2.QtCore.Qt.AspectRatioMode) -> None """
        pass

    def setMediaObject(self, p_object): # real signature unknown; restored from __doc__
        """ setMediaObject(self, object: PySide2.QtMultimedia.QMediaObject) -> bool """
        return False

    def setOffset(self, offset): # real signature unknown; restored from __doc__
        """ setOffset(self, offset: PySide2.QtCore.QPointF) -> None """
        pass

    def setSize(self, size): # real signature unknown; restored from __doc__
        """ setSize(self, size: PySide2.QtCore.QSizeF) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSizeF """
        pass

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def videoSurface(self): # real signature unknown; restored from __doc__
        """ videoSurface(self) -> PySide2.QtMultimedia.QAbstractVideoSurface """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000221BE8AEAC0>'


class QVideoWidgetControl(__PySide2_QtMultimedia.QMediaControl):
    """ QVideoWidgetControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def aspectRatioMode(self): # real signature unknown; restored from __doc__
        """ aspectRatioMode(self) -> PySide2.QtCore.Qt.AspectRatioMode """
        pass

    def brightness(self): # real signature unknown; restored from __doc__
        """ brightness(self) -> int """
        return 0

    def brightnessChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contrast(self): # real signature unknown; restored from __doc__
        """ contrast(self) -> int """
        return 0

    def contrastChanged(self, *args, **kwargs): # real signature unknown
        pass

    def fullScreenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hue(self): # real signature unknown; restored from __doc__
        """ hue(self) -> int """
        return 0

    def hueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isFullScreen(self): # real signature unknown; restored from __doc__
        """ isFullScreen(self) -> bool """
        return False

    def saturation(self): # real signature unknown; restored from __doc__
        """ saturation(self) -> int """
        return 0

    def saturationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setAspectRatioMode(self, mode): # real signature unknown; restored from __doc__
        """ setAspectRatioMode(self, mode: PySide2.QtCore.Qt.AspectRatioMode) -> None """
        pass

    def setBrightness(self, brightness): # real signature unknown; restored from __doc__
        """ setBrightness(self, brightness: int) -> None """
        pass

    def setContrast(self, contrast): # real signature unknown; restored from __doc__
        """ setContrast(self, contrast: int) -> None """
        pass

    def setFullScreen(self, fullScreen): # real signature unknown; restored from __doc__
        """ setFullScreen(self, fullScreen: bool) -> None """
        pass

    def setHue(self, hue): # real signature unknown; restored from __doc__
        """ setHue(self, hue: int) -> None """
        pass

    def setSaturation(self, saturation): # real signature unknown; restored from __doc__
        """ setSaturation(self, saturation: int) -> None """
        pass

    def videoWidget(self): # real signature unknown; restored from __doc__
        """ videoWidget(self) -> PySide2.QtWidgets.QWidget """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000221BE8AEBC0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000221BCFE17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtMultimediaWidgets', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000221BCFE17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtMultimediaWidgets.cp310-win_amd64.pyd')"

