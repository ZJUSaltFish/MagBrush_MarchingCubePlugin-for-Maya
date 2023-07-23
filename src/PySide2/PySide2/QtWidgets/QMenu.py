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

class QMenu(QWidget):
    """
    QMenu(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QMenu(self, title: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def aboutToHide(self, *args, **kwargs): # real signature unknown
        pass

    def aboutToShow(self, *args, **kwargs): # real signature unknown
        pass

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

    def addAction(self, arg__1, arg__2, arg__3, arg__4, PySide2_QtGui_QKeySequence=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addAction(self, arg__1: PySide2.QtGui.QIcon, arg__2: str, arg__3: object, arg__4: typing.Optional[PySide2.QtGui.QKeySequence] = None) -> None
        addAction(self, arg__1: PySide2.QtWidgets.QAction) -> None
        addAction(self, arg__1: str, arg__2: object, arg__3: typing.Optional[PySide2.QtGui.QKeySequence] = None) -> None
        addAction(self, icon: PySide2.QtGui.QIcon, text: str) -> PySide2.QtWidgets.QAction
        addAction(self, icon: PySide2.QtGui.QIcon, text: str, receiver: PySide2.QtCore.QObject, member: bytes, shortcut: typing.Optional[PySide2.QtGui.QKeySequence] = None) -> PySide2.QtWidgets.QAction
        addAction(self, text: str) -> PySide2.QtWidgets.QAction
        addAction(self, text: str, receiver: PySide2.QtCore.QObject, member: bytes, shortcut: typing.Optional[PySide2.QtGui.QKeySequence] = None) -> PySide2.QtWidgets.QAction
        """
        pass

    def addMenu(self, icon, title): # real signature unknown; restored from __doc__
        """
        addMenu(self, icon: PySide2.QtGui.QIcon, title: str) -> PySide2.QtWidgets.QMenu
        addMenu(self, menu: PySide2.QtWidgets.QMenu) -> PySide2.QtWidgets.QAction
        addMenu(self, title: str) -> PySide2.QtWidgets.QMenu
        """
        pass

    def addSection(self, icon, text): # real signature unknown; restored from __doc__
        """
        addSection(self, icon: PySide2.QtGui.QIcon, text: str) -> PySide2.QtWidgets.QAction
        addSection(self, text: str) -> PySide2.QtWidgets.QAction
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

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> PySide2.QtWidgets.QAction """
        pass

    def enterEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ enterEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def exec_(self, actions, PySide2_QtWidgets_QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        exec_(actions: typing.Sequence[PySide2.QtWidgets.QAction], pos: PySide2.QtCore.QPoint, at: typing.Optional[PySide2.QtWidgets.QAction] = None, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtWidgets.QAction
        exec_(self) -> PySide2.QtWidgets.QAction
        exec_(self, pos: PySide2.QtCore.QPoint, at: typing.Optional[PySide2.QtWidgets.QAction] = None) -> PySide2.QtWidgets.QAction
        """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def hideEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None """
        pass

    def hideTearOffMenu(self): # real signature unknown; restored from __doc__
        """ hideTearOffMenu(self) -> None """
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def initStyleOption(self, option, action): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionMenuItem, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def insertMenu(self, before, menu): # real signature unknown; restored from __doc__
        """ insertMenu(self, before: PySide2.QtWidgets.QAction, menu: PySide2.QtWidgets.QMenu) -> PySide2.QtWidgets.QAction """
        pass

    def insertSection(self, before, icon, text): # real signature unknown; restored from __doc__
        """
        insertSection(self, before: PySide2.QtWidgets.QAction, icon: PySide2.QtGui.QIcon, text: str) -> PySide2.QtWidgets.QAction
        insertSection(self, before: PySide2.QtWidgets.QAction, text: str) -> PySide2.QtWidgets.QAction
        """
        pass

    def insertSeparator(self, before): # real signature unknown; restored from __doc__
        """ insertSeparator(self, before: PySide2.QtWidgets.QAction) -> PySide2.QtWidgets.QAction """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isTearOffEnabled(self): # real signature unknown; restored from __doc__
        """ isTearOffEnabled(self) -> bool """
        return False

    def isTearOffMenuVisible(self): # real signature unknown; restored from __doc__
        """ isTearOffMenuVisible(self) -> bool """
        return False

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def leaveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ leaveEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def menuAction(self): # real signature unknown; restored from __doc__
        """ menuAction(self) -> PySide2.QtWidgets.QAction """
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

    def popup(self, pos, at, PySide2_QtWidgets_QAction=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ popup(self, pos: PySide2.QtCore.QPoint, at: typing.Optional[PySide2.QtWidgets.QAction] = None) -> None """
        pass

    def separatorsCollapsible(self): # real signature unknown; restored from __doc__
        """ separatorsCollapsible(self) -> bool """
        return False

    def setActiveAction(self, act): # real signature unknown; restored from __doc__
        """ setActiveAction(self, act: PySide2.QtWidgets.QAction) -> None """
        pass

    def setDefaultAction(self, arg__1): # real signature unknown; restored from __doc__
        """ setDefaultAction(self, arg__1: PySide2.QtWidgets.QAction) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setSeparatorsCollapsible(self, collapse): # real signature unknown; restored from __doc__
        """ setSeparatorsCollapsible(self, collapse: bool) -> None """
        pass

    def setTearOffEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setTearOffEnabled(self, arg__1: bool) -> None """
        pass

    def setTitle(self, title): # real signature unknown; restored from __doc__
        """ setTitle(self, title: str) -> None """
        pass

    def setToolTipsVisible(self, visible): # real signature unknown; restored from __doc__
        """ setToolTipsVisible(self, visible: bool) -> None """
        pass

    def showTearOffMenu(self): # real signature unknown; restored from __doc__
        """
        showTearOffMenu(self) -> None
        showTearOffMenu(self, pos: PySide2.QtCore.QPoint) -> None
        """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def timerEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def toolTipsVisible(self): # real signature unknown; restored from __doc__
        """ toolTipsVisible(self) -> bool """
        return False

    def triggered(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ wheelEvent(self, arg__1: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50831480>'


