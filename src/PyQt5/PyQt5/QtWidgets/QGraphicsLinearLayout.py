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

class QGraphicsLinearLayout(QGraphicsLayout):
    """
    QGraphicsLinearLayout(parent: typing.Optional[QGraphicsLayoutItem] = None)
    QGraphicsLinearLayout(orientation: Qt.Orientation, parent: typing.Optional[QGraphicsLayoutItem] = None)
    """
    def addChildLayoutItem(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, item): # real signature unknown; restored from __doc__
        """ addItem(self, item: QGraphicsLayoutItem) """
        pass

    def addStretch(self, stretch=1): # real signature unknown; restored from __doc__
        """ addStretch(self, stretch: int = 1) """
        pass

    def alignment(self, item): # real signature unknown; restored from __doc__
        """ alignment(self, item: QGraphicsLayoutItem) -> Qt.Alignment """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def insertItem(self, index, item): # real signature unknown; restored from __doc__
        """ insertItem(self, index: int, item: QGraphicsLayoutItem) """
        pass

    def insertStretch(self, index, stretch=1): # real signature unknown; restored from __doc__
        """ insertStretch(self, index: int, stretch: int = 1) """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def itemAt(self, index): # real signature unknown; restored from __doc__
        """ itemAt(self, index: int) -> QGraphicsLayoutItem """
        return QGraphicsLayoutItem

    def itemSpacing(self, index): # real signature unknown; restored from __doc__
        """ itemSpacing(self, index: int) -> float """
        return 0.0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def removeAt(self, index): # real signature unknown; restored from __doc__
        """ removeAt(self, index: int) """
        pass

    def removeItem(self, item): # real signature unknown; restored from __doc__
        """ removeItem(self, item: QGraphicsLayoutItem) """
        pass

    def setAlignment(self, item, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, item: QGraphicsLayoutItem, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setItemSpacing(self, index, spacing): # real signature unknown; restored from __doc__
        """ setItemSpacing(self, index: int, spacing: float) """
        pass

    def setOrientation(self, orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, orientation: Qt.Orientation) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: float) """
        pass

    def setStretchFactor(self, item, stretch): # real signature unknown; restored from __doc__
        """ setStretchFactor(self, item: QGraphicsLayoutItem, stretch: int) """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> float """
        return 0.0

    def stretchFactor(self, item): # real signature unknown; restored from __doc__
        """ stretchFactor(self, item: QGraphicsLayoutItem) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


