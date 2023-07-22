# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QFrame import QFrame

class QAbstractScrollArea(QFrame):
    """ QAbstractScrollArea(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def addScrollBarWidget(self, widget, alignment): # real signature unknown; restored from __doc__
        """ addScrollBarWidget(self, widget: PySide2.QtWidgets.QWidget, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def contextMenuEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, arg__1: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def cornerWidget(self): # real signature unknown; restored from __doc__
        """ cornerWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def dragEnterEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, arg__1: PySide2.QtGui.QDragEnterEvent) -> None """
        pass

    def dragLeaveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, arg__1: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMoveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, arg__1: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def dropEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dropEvent(self, arg__1: PySide2.QtGui.QDropEvent) -> None """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ eventFilter(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def horizontalScrollBar(self): # real signature unknown; restored from __doc__
        """ horizontalScrollBar(self) -> PySide2.QtWidgets.QScrollBar """
        pass

    def horizontalScrollBarPolicy(self): # real signature unknown; restored from __doc__
        """ horizontalScrollBarPolicy(self) -> PySide2.QtCore.Qt.ScrollBarPolicy """
        pass

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def maximumViewportSize(self): # real signature unknown; restored from __doc__
        """ maximumViewportSize(self) -> PySide2.QtCore.QSize """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def mouseDoubleClickEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseMoveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def scrollBarWidgets(self, alignment): # real signature unknown; restored from __doc__
        """ scrollBarWidgets(self, alignment: PySide2.QtCore.Qt.Alignment) -> typing.List[PySide2.QtWidgets.QWidget] """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) -> None """
        pass

    def setCornerWidget(self, widget): # real signature unknown; restored from __doc__
        """ setCornerWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setHorizontalScrollBar(self, scrollbar): # real signature unknown; restored from __doc__
        """ setHorizontalScrollBar(self, scrollbar: PySide2.QtWidgets.QScrollBar) -> None """
        pass

    def setHorizontalScrollBarPolicy(self, arg__1): # real signature unknown; restored from __doc__
        """ setHorizontalScrollBarPolicy(self, arg__1: PySide2.QtCore.Qt.ScrollBarPolicy) -> None """
        pass

    def setSizeAdjustPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setSizeAdjustPolicy(self, policy: PySide2.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy) -> None """
        pass

    def setupViewport(self, viewport): # real signature unknown; restored from __doc__
        """ setupViewport(self, viewport: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setVerticalScrollBar(self, scrollbar): # real signature unknown; restored from __doc__
        """ setVerticalScrollBar(self, scrollbar: PySide2.QtWidgets.QScrollBar) -> None """
        pass

    def setVerticalScrollBarPolicy(self, arg__1): # real signature unknown; restored from __doc__
        """ setVerticalScrollBarPolicy(self, arg__1: PySide2.QtCore.Qt.ScrollBarPolicy) -> None """
        pass

    def setViewport(self, widget): # real signature unknown; restored from __doc__
        """ setViewport(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setViewportMargins(self, left, top, right, bottom): # real signature unknown; restored from __doc__
        """
        setViewportMargins(self, left: int, top: int, right: int, bottom: int) -> None
        setViewportMargins(self, margins: PySide2.QtCore.QMargins) -> None
        """
        pass

    def sizeAdjustPolicy(self): # real signature unknown; restored from __doc__
        """ sizeAdjustPolicy(self) -> PySide2.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def verticalScrollBar(self): # real signature unknown; restored from __doc__
        """ verticalScrollBar(self) -> PySide2.QtWidgets.QScrollBar """
        pass

    def verticalScrollBarPolicy(self): # real signature unknown; restored from __doc__
        """ verticalScrollBarPolicy(self) -> PySide2.QtCore.Qt.ScrollBarPolicy """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> PySide2.QtWidgets.QWidget """
        pass

    def viewportEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ viewportEvent(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def viewportMargins(self): # real signature unknown; restored from __doc__
        """ viewportMargins(self) -> PySide2.QtCore.QMargins """
        pass

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def wheelEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ wheelEvent(self, arg__1: PySide2.QtGui.QWheelEvent) -> None """
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

    AdjustIgnored = PySide2.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored
    AdjustToContents = PySide2.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
    AdjustToContentsOnFirstShow = PySide2.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow
    SizeAdjustPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507E5040>'


