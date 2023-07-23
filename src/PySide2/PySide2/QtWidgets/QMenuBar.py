# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QWidget import QWidget

class QMenuBar(QWidget):
    """ QMenuBar(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def actionAt(self, arg__1): # real signature unknown; restored from __doc__
        """ actionAt(self, arg__1: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QAction """
        pass

    def actionEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ actionEvent(self, arg__1: PySide2.QtGui.QActionEvent) -> None """
        pass

    def actionGeometry(self, arg__1): # real signature unknown; restored from __doc__
        """ actionGeometry(self, arg__1: PySide2.QtWidgets.QAction) -> PySide2.QtCore.QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ activeAction(self) -> PySide2.QtWidgets.QAction """
        pass

    def addAction(self, arg__1): # real signature unknown; restored from __doc__
        """
        addAction(self, arg__1: PySide2.QtWidgets.QAction) -> None
        addAction(self, arg__1: str, arg__2: object) -> None
        addAction(self, text: str) -> PySide2.QtWidgets.QAction
        addAction(self, text: str, receiver: PySide2.QtCore.QObject, member: bytes) -> PySide2.QtWidgets.QAction
        """
        pass

    def addMenu(self, icon, title): # real signature unknown; restored from __doc__
        """
        addMenu(self, icon: PySide2.QtGui.QIcon, title: str) -> PySide2.QtWidgets.QMenu
        addMenu(self, menu: PySide2.QtWidgets.QMenu) -> PySide2.QtWidgets.QAction
        addMenu(self, title: str) -> PySide2.QtWidgets.QMenu
        """
        pass

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> PySide2.QtWidgets.QAction """
        pass

    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def cornerWidget(self, corner=None): # real signature unknown; restored from __doc__
        """ cornerWidget(self, corner: PySide2.QtCore.Qt.Corner = PySide2.QtCore.Qt.Corner.TopRightCorner) -> PySide2.QtWidgets.QWidget """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ eventFilter(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def focusInEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusInEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusOutEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def heightForWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ heightForWidth(self, arg__1: int) -> int """
        return 0

    def hovered(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, action): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionMenuItem, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def insertMenu(self, before, menu): # real signature unknown; restored from __doc__
        """ insertMenu(self, before: PySide2.QtWidgets.QAction, menu: PySide2.QtWidgets.QMenu) -> PySide2.QtWidgets.QAction """
        pass

    def insertSeparator(self, before): # real signature unknown; restored from __doc__
        """ insertSeparator(self, before: PySide2.QtWidgets.QAction) -> PySide2.QtWidgets.QAction """
        pass

    def isDefaultUp(self): # real signature unknown; restored from __doc__
        """ isDefaultUp(self) -> bool """
        return False

    def isNativeMenuBar(self): # real signature unknown; restored from __doc__
        """ isNativeMenuBar(self) -> bool """
        return False

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def leaveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ leaveEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
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

    def setActiveAction(self, action): # real signature unknown; restored from __doc__
        """ setActiveAction(self, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def setCornerWidget(self, w, corner=None): # real signature unknown; restored from __doc__
        """ setCornerWidget(self, w: PySide2.QtWidgets.QWidget, corner: PySide2.QtCore.Qt.Corner = PySide2.QtCore.Qt.Corner.TopRightCorner) -> None """
        pass

    def setDefaultUp(self, arg__1): # real signature unknown; restored from __doc__
        """ setDefaultUp(self, arg__1: bool) -> None """
        pass

    def setNativeMenuBar(self, nativeMenuBar): # real signature unknown; restored from __doc__
        """ setNativeMenuBar(self, nativeMenuBar: bool) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def timerEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50831080>'


