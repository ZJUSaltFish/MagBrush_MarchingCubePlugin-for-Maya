# encoding: utf-8
# module PySide2.QtSvg
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSvg.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import PySide2.QtWidgets as __PySide2_QtWidgets


# no functions
# classes

class QGraphicsSvgItem(__PySide2_QtWidgets.QGraphicsObject):
    """
    QGraphicsSvgItem(self, fileName: str, parentItem: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None
    QGraphicsSvgItem(self, parentItem: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def elementId(self): # real signature unknown; restored from __doc__
        """ elementId(self) -> str """
        return ""

    def isCachingEnabled(self): # real signature unknown; restored from __doc__
        """ isCachingEnabled(self) -> bool """
        return False

    def maximumCacheSize(self): # real signature unknown; restored from __doc__
        """ maximumCacheSize(self) -> PySide2.QtCore.QSize """
        pass

    def paint(self, painter, option, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ renderer(self) -> PySide2.QtSvg.QSvgRenderer """
        pass

    def setCachingEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setCachingEnabled(self, arg__1: bool) -> None """
        pass

    def setElementId(self, id): # real signature unknown; restored from __doc__
        """ setElementId(self, id: str) -> None """
        pass

    def setMaximumCacheSize(self, size): # real signature unknown; restored from __doc__
        """ setMaximumCacheSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setSharedRenderer(self, renderer): # real signature unknown; restored from __doc__
        """ setSharedRenderer(self, renderer: PySide2.QtSvg.QSvgRenderer) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, fileName, parentItem, PySide2_QtWidgets_QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000020196A5A180>'


class QSvgGenerator(__PySide2_QtGui.QPaintDevice):
    """ QSvgGenerator(self) -> None """
    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ outputDevice(self) -> PySide2.QtCore.QIODevice """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def setDescription(self, description): # real signature unknown; restored from __doc__
        """ setDescription(self, description: str) -> None """
        pass

    def setFileName(self, fileName): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: str) -> None """
        pass

    def setOutputDevice(self, outputDevice): # real signature unknown; restored from __doc__
        """ setOutputDevice(self, outputDevice: PySide2.QtCore.QIODevice) -> None """
        pass

    def setResolution(self, dpi): # real signature unknown; restored from __doc__
        """ setResolution(self, dpi: int) -> None """
        pass

    def setSize(self, size): # real signature unknown; restored from __doc__
        """ setSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setTitle(self, title): # real signature unknown; restored from __doc__
        """ setTitle(self, title: str) -> None """
        pass

    def setViewBox(self, viewBox): # real signature unknown; restored from __doc__
        """
        setViewBox(self, viewBox: PySide2.QtCore.QRect) -> None
        setViewBox(self, viewBox: PySide2.QtCore.QRectF) -> None
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def viewBox(self): # real signature unknown; restored from __doc__
        """ viewBox(self) -> PySide2.QtCore.QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ viewBoxF(self) -> PySide2.QtCore.QRectF """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QSvgRenderer(__PySide2_QtCore.QObject):
    """
    QSvgRenderer(self, contents: PySide2.QtCore.QByteArray, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSvgRenderer(self, contents: PySide2.QtCore.QXmlStreamReader, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSvgRenderer(self, filename: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSvgRenderer(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def animated(self): # real signature unknown; restored from __doc__
        """ animated(self) -> bool """
        return False

    def animationDuration(self): # real signature unknown; restored from __doc__
        """ animationDuration(self) -> int """
        return 0

    def aspectRatioMode(self): # real signature unknown; restored from __doc__
        """ aspectRatioMode(self) -> PySide2.QtCore.Qt.AspectRatioMode """
        pass

    def boundsOnElement(self, id): # real signature unknown; restored from __doc__
        """ boundsOnElement(self, id: str) -> PySide2.QtCore.QRectF """
        pass

    def currentFrame(self): # real signature unknown; restored from __doc__
        """ currentFrame(self) -> int """
        return 0

    def defaultSize(self): # real signature unknown; restored from __doc__
        """ defaultSize(self) -> PySide2.QtCore.QSize """
        pass

    def elementExists(self, id): # real signature unknown; restored from __doc__
        """ elementExists(self, id: str) -> bool """
        return False

    def framesPerSecond(self): # real signature unknown; restored from __doc__
        """ framesPerSecond(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def load(self, contents): # real signature unknown; restored from __doc__
        """
        load(self, contents: PySide2.QtCore.QByteArray) -> bool
        load(self, contents: PySide2.QtCore.QXmlStreamReader) -> bool
        load(self, filename: str) -> bool
        """
        return False

    def matrixForElement(self, id): # real signature unknown; restored from __doc__
        """ matrixForElement(self, id: str) -> PySide2.QtGui.QMatrix """
        pass

    def render(self, p): # real signature unknown; restored from __doc__
        """
        render(self, p: PySide2.QtGui.QPainter) -> None
        render(self, p: PySide2.QtGui.QPainter, bounds: PySide2.QtCore.QRectF) -> None
        render(self, p: PySide2.QtGui.QPainter, elementId: str, bounds: PySide2.QtCore.QRectF = Default(QRectF)) -> None
        """
        pass

    def repaintNeeded(self, *args, **kwargs): # real signature unknown
        pass

    def setAspectRatioMode(self, mode): # real signature unknown; restored from __doc__
        """ setAspectRatioMode(self, mode: PySide2.QtCore.Qt.AspectRatioMode) -> None """
        pass

    def setCurrentFrame(self, arg__1): # real signature unknown; restored from __doc__
        """ setCurrentFrame(self, arg__1: int) -> None """
        pass

    def setFramesPerSecond(self, num): # real signature unknown; restored from __doc__
        """ setFramesPerSecond(self, num: int) -> None """
        pass

    def setViewBox(self, viewbox): # real signature unknown; restored from __doc__
        """
        setViewBox(self, viewbox: PySide2.QtCore.QRect) -> None
        setViewBox(self, viewbox: PySide2.QtCore.QRectF) -> None
        """
        pass

    def transformForElement(self, id): # real signature unknown; restored from __doc__
        """ transformForElement(self, id: str) -> PySide2.QtGui.QTransform """
        pass

    def viewBox(self): # real signature unknown; restored from __doc__
        """ viewBox(self) -> PySide2.QtCore.QRect """
        pass

    def viewBoxF(self): # real signature unknown; restored from __doc__
        """ viewBoxF(self) -> PySide2.QtCore.QRectF """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, contents, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000020196A59E40>'


class QSvgWidget(__PySide2_QtWidgets.QWidget):
    """
    QSvgWidget(self, file: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QSvgWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def load(self, contents): # real signature unknown; restored from __doc__
        """
        load(self, contents: PySide2.QtCore.QByteArray) -> None
        load(self, file: str) -> None
        """
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def renderer(self): # real signature unknown; restored from __doc__
        """ renderer(self) -> PySide2.QtSvg.QSvgRenderer """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, file, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000020196A5A000>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020195A517B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtSvg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020195A517B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtSvg.cp310-win_amd64.pyd')"

