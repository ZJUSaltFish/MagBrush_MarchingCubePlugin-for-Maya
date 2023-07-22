# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QIconEngine(__Shiboken.Object):
    """
    QIconEngine(self) -> None
    QIconEngine(self, other: PySide2.QtGui.QIconEngine) -> None
    """
    def actualSize(self, size, mode, state): # real signature unknown; restored from __doc__
        """ actualSize(self, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode, state: PySide2.QtGui.QIcon.State) -> PySide2.QtCore.QSize """
        pass

    def addFile(self, fileName, size, mode, state): # real signature unknown; restored from __doc__
        """ addFile(self, fileName: str, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode, state: PySide2.QtGui.QIcon.State) -> None """
        pass

    def addPixmap(self, pixmap, mode, state): # real signature unknown; restored from __doc__
        """ addPixmap(self, pixmap: PySide2.QtGui.QPixmap, mode: PySide2.QtGui.QIcon.Mode, state: PySide2.QtGui.QIcon.State) -> None """
        pass

    def availableSizes(self, mode=None, state=None): # real signature unknown; restored from __doc__
        """ availableSizes(self, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> typing.List[PySide2.QtCore.QSize] """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> PySide2.QtGui.QIconEngine """
        pass

    def iconName(self): # real signature unknown; restored from __doc__
        """ iconName(self) -> str """
        return ""

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def paint(self, painter, rect, mode, state): # real signature unknown; restored from __doc__
        """ paint(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, mode: PySide2.QtGui.QIcon.Mode, state: PySide2.QtGui.QIcon.State) -> None """
        pass

    def pixmap(self, size, mode, state): # real signature unknown; restored from __doc__
        """ pixmap(self, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode, state: PySide2.QtGui.QIcon.State) -> PySide2.QtGui.QPixmap """
        pass

    def read(self, in_): # real signature unknown; restored from __doc__
        """ read(self, in_: PySide2.QtCore.QDataStream) -> bool """
        return False

    def scaledPixmap(self, size, mode, state, scale): # real signature unknown; restored from __doc__
        """ scaledPixmap(self, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode, state: PySide2.QtGui.QIcon.State, scale: float) -> PySide2.QtGui.QPixmap """
        pass

    def write(self, out): # real signature unknown; restored from __doc__
        """ write(self, out: PySide2.QtCore.QDataStream) -> bool """
        return False

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    AvailableSizesArgument = None # (!) real value is "<class 'PySide2.QtGui.QIconEngine.AvailableSizesArgument'>"
    AvailableSizesHook = PySide2.QtGui.QIconEngine.IconEngineHook.AvailableSizesHook
    IconEngineHook = None # (!) real value is "<class 'PySide2.QtGui.QIconEngine.IconEngineHook'>"
    IconNameHook = PySide2.QtGui.QIconEngine.IconEngineHook.IconNameHook
    IsNullHook = PySide2.QtGui.QIconEngine.IconEngineHook.IsNullHook
    ScaledPixmapHook = PySide2.QtGui.QIconEngine.IconEngineHook.ScaledPixmapHook


