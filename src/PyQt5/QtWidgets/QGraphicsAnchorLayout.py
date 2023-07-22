# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsLayout import QGraphicsLayout

class QGraphicsAnchorLayout(QGraphicsLayout):
    """ QGraphicsAnchorLayout(parent: typing.Optional[QGraphicsLayoutItem] = None) """
    def addAnchor(self, firstItem, firstEdge, secondItem, secondEdge): # real signature unknown; restored from __doc__
        """ addAnchor(self, firstItem: QGraphicsLayoutItem, firstEdge: Qt.AnchorPoint, secondItem: QGraphicsLayoutItem, secondEdge: Qt.AnchorPoint) -> QGraphicsAnchor """
        return QGraphicsAnchor

    def addAnchors(self, firstItem, secondItem, orientations, Qt_Orientations=None, Qt_Orientation=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addAnchors(self, firstItem: QGraphicsLayoutItem, secondItem: QGraphicsLayoutItem, orientations: Union[Qt.Orientations, Qt.Orientation] = Qt.Horizontal|Qt.Vertical) """
        pass

    def addChildLayoutItem(self, *args, **kwargs): # real signature unknown
        pass

    def addCornerAnchors(self, firstItem, firstCorner, secondItem, secondCorner): # real signature unknown; restored from __doc__
        """ addCornerAnchors(self, firstItem: QGraphicsLayoutItem, firstCorner: Qt.Corner, secondItem: QGraphicsLayoutItem, secondCorner: Qt.Corner) """
        pass

    def anchor(self, firstItem, firstEdge, secondItem, secondEdge): # real signature unknown; restored from __doc__
        """ anchor(self, firstItem: QGraphicsLayoutItem, firstEdge: Qt.AnchorPoint, secondItem: QGraphicsLayoutItem, secondEdge: Qt.AnchorPoint) -> QGraphicsAnchor """
        return QGraphicsAnchor

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> float """
        return 0.0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def itemAt(self, index): # real signature unknown; restored from __doc__
        """ itemAt(self, index: int) -> QGraphicsLayoutItem """
        return QGraphicsLayoutItem

    def removeAt(self, index): # real signature unknown; restored from __doc__
        """ removeAt(self, index: int) """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: float) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: float) """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: float) """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> float """
        return 0.0

    def __init__(self, parent, QGraphicsLayoutItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


