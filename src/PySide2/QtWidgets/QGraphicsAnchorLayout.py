# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGraphicsLayout import QGraphicsLayout

class QGraphicsAnchorLayout(QGraphicsLayout):
    """ QGraphicsAnchorLayout(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsLayoutItem] = None) -> None """
    def addAnchor(self, firstItem, firstEdge, secondItem, secondEdge): # real signature unknown; restored from __doc__
        """ addAnchor(self, firstItem: PySide2.QtWidgets.QGraphicsLayoutItem, firstEdge: PySide2.QtCore.Qt.AnchorPoint, secondItem: PySide2.QtWidgets.QGraphicsLayoutItem, secondEdge: PySide2.QtCore.Qt.AnchorPoint) -> PySide2.QtWidgets.QGraphicsAnchor """
        pass

    def addAnchors(self, firstItem, secondItem, orientations=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addAnchors(self, firstItem: PySide2.QtWidgets.QGraphicsLayoutItem, secondItem: PySide2.QtWidgets.QGraphicsLayoutItem, orientations: PySide2.QtCore.Qt.Orientations = Instance(Qt.Horizontal | Qt.Vertical)) -> None """
        pass

    def addCornerAnchors(self, firstItem, firstCorner, secondItem, secondCorner): # real signature unknown; restored from __doc__
        """ addCornerAnchors(self, firstItem: PySide2.QtWidgets.QGraphicsLayoutItem, firstCorner: PySide2.QtCore.Qt.Corner, secondItem: PySide2.QtWidgets.QGraphicsLayoutItem, secondCorner: PySide2.QtCore.Qt.Corner) -> None """
        pass

    def anchor(self, firstItem, firstEdge, secondItem, secondEdge): # real signature unknown; restored from __doc__
        """ anchor(self, firstItem: PySide2.QtWidgets.QGraphicsLayoutItem, firstEdge: PySide2.QtCore.Qt.AnchorPoint, secondItem: PySide2.QtWidgets.QGraphicsLayoutItem, secondEdge: PySide2.QtCore.Qt.AnchorPoint) -> PySide2.QtWidgets.QGraphicsAnchor """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> float """
        return 0.0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def itemAt(self, index): # real signature unknown; restored from __doc__
        """ itemAt(self, index: int) -> PySide2.QtWidgets.QGraphicsLayoutItem """
        pass

    def removeAt(self, index): # real signature unknown; restored from __doc__
        """ removeAt(self, index: int) -> None """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: float) -> None """
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: float) -> None """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: float) -> None """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: PySide2.QtCore.Qt.SizeHint, constraint: PySide2.QtCore.QSizeF = Default(QSizeF)) -> PySide2.QtCore.QSizeF """
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QGraphicsLayoutItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


