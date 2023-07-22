# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGraphicsItem import QGraphicsItem

class QGraphicsPixmapItem(QGraphicsItem):
    """
    QGraphicsPixmapItem(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None
    QGraphicsPixmapItem(self, pixmap: PySide2.QtGui.QPixmap, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def contains(self, point): # real signature unknown; restored from __doc__
        """ contains(self, point: PySide2.QtCore.QPointF) -> bool """
        return False

    def extension(self, variant): # real signature unknown; restored from __doc__
        """ extension(self, variant: typing.Any) -> typing.Any """
        pass

    def isObscuredBy(self, item): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, item: PySide2.QtWidgets.QGraphicsItem) -> bool """
        return False

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> PySide2.QtCore.QPointF """
        pass

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> PySide2.QtGui.QPainterPath """
        pass

    def paint(self, painter, option, widget): # real signature unknown; restored from __doc__
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> PySide2.QtGui.QPixmap """
        pass

    def setOffset(self, offset): # real signature unknown; restored from __doc__
        """
        setOffset(self, offset: PySide2.QtCore.QPointF) -> None
        setOffset(self, x: float, y: float) -> None
        """
        pass

    def setPixmap(self, pixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def setShapeMode(self, mode): # real signature unknown; restored from __doc__
        """ setShapeMode(self, mode: PySide2.QtWidgets.QGraphicsPixmapItem.ShapeMode) -> None """
        pass

    def setTransformationMode(self, mode): # real signature unknown; restored from __doc__
        """ setTransformationMode(self, mode: PySide2.QtCore.Qt.TransformationMode) -> None """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> PySide2.QtGui.QPainterPath """
        pass

    def shapeMode(self): # real signature unknown; restored from __doc__
        """ shapeMode(self) -> PySide2.QtWidgets.QGraphicsPixmapItem.ShapeMode """
        pass

    def transformationMode(self): # real signature unknown; restored from __doc__
        """ transformationMode(self) -> PySide2.QtCore.Qt.TransformationMode """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

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

    BoundingRectShape = PySide2.QtWidgets.QGraphicsPixmapItem.ShapeMode.BoundingRectShape
    HeuristicMaskShape = PySide2.QtWidgets.QGraphicsPixmapItem.ShapeMode.HeuristicMaskShape
    MaskShape = PySide2.QtWidgets.QGraphicsPixmapItem.ShapeMode.MaskShape
    ShapeMode = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsPixmapItem.ShapeMode'>"


