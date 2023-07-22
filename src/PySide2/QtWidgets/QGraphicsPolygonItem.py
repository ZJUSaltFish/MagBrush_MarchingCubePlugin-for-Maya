# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsPolygonItem(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None
    QGraphicsPolygonItem(self, polygon: PySide2.QtGui.QPolygonF, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None
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

    def fillRule(self): # real signature unknown; restored from __doc__
        """ fillRule(self) -> PySide2.QtCore.Qt.FillRule """
        pass

    def isObscuredBy(self, item): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, item: PySide2.QtWidgets.QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> PySide2.QtGui.QPainterPath """
        pass

    def paint(self, painter, option, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def polygon(self): # real signature unknown; restored from __doc__
        """ polygon(self) -> PySide2.QtGui.QPolygonF """
        pass

    def setFillRule(self, rule): # real signature unknown; restored from __doc__
        """ setFillRule(self, rule: PySide2.QtCore.Qt.FillRule) -> None """
        pass

    def setPolygon(self, polygon): # real signature unknown; restored from __doc__
        """ setPolygon(self, polygon: PySide2.QtGui.QPolygonF) -> None """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> PySide2.QtGui.QPainterPath """
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


