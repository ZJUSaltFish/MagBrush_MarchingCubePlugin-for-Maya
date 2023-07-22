# encoding: utf-8
# module PySide2.QtQuickWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtQuickWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtWidgets as __PySide2_QtWidgets


# no functions
# classes

class QQuickWidget(__PySide2_QtWidgets.QWidget):
    """
    QQuickWidget(self, engine: PySide2.QtQml.QQmlEngine, parent: PySide2.QtWidgets.QWidget) -> None
    QQuickWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QQuickWidget(self, source: PySide2.QtCore.QUrl, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
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

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> PySide2.QtQml.QQmlEngine """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> typing.List[PySide2.QtQml.QQmlError] """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QSurfaceFormat """
        pass

    def grabFramebuffer(self): # real signature unknown; restored from __doc__
        """ grabFramebuffer(self) -> PySide2.QtGui.QImage """
        pass

    def hideEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None """
        pass

    def initialSize(self): # real signature unknown; restored from __doc__
        """ initialSize(self) -> PySide2.QtCore.QSize """
        pass

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
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

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def quickWindow(self): # real signature unknown; restored from __doc__
        """ quickWindow(self) -> PySide2.QtQuick.QQuickWindow """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ resizeMode(self) -> PySide2.QtQuickWidgets.QQuickWidget.ResizeMode """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ rootContext(self) -> PySide2.QtQml.QQmlContext """
        pass

    def rootObject(self): # real signature unknown; restored from __doc__
        """ rootObject(self) -> PySide2.QtQuick.QQuickItem """
        pass

    def sceneGraphError(self, *args, **kwargs): # real signature unknown
        pass

    def setClearColor(self, color): # real signature unknown; restored from __doc__
        """ setClearColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setContent(self, url, component, item): # real signature unknown; restored from __doc__
        """ setContent(self, url: PySide2.QtCore.QUrl, component: PySide2.QtQml.QQmlComponent, item: PySide2.QtCore.QObject) -> None """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtGui.QSurfaceFormat) -> None """
        pass

    def setResizeMode(self, arg__1): # real signature unknown; restored from __doc__
        """ setResizeMode(self, arg__1: PySide2.QtQuickWidgets.QQuickWidget.ResizeMode) -> None """
        pass

    def setSource(self, arg__1): # real signature unknown; restored from __doc__
        """ setSource(self, arg__1: PySide2.QtCore.QUrl) -> None """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> PySide2.QtCore.QUrl """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtQuickWidgets.QQuickWidget.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def wheelEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ wheelEvent(self, arg__1: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, engine, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Error = PySide2.QtQuickWidgets.QQuickWidget.Status.Error
    Loading = PySide2.QtQuickWidgets.QQuickWidget.Status.Loading
    Null = PySide2.QtQuickWidgets.QQuickWidget.Status.Null
    Ready = PySide2.QtQuickWidgets.QQuickWidget.Status.Ready
    ResizeMode = None # (!) real value is "<class 'PySide2.QtQuickWidgets.QQuickWidget.ResizeMode'>"
    SizeRootObjectToView = PySide2.QtQuickWidgets.QQuickWidget.ResizeMode.SizeRootObjectToView
    SizeViewToRootObject = PySide2.QtQuickWidgets.QQuickWidget.ResizeMode.SizeViewToRootObject
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022BA1FF5A00>'
    Status = None # (!) real value is "<class 'PySide2.QtQuickWidgets.QQuickWidget.Status'>"


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022BA06A17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtQuickWidgets', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022BA06A17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtQuickWidgets.cp310-win_amd64.pyd')"

