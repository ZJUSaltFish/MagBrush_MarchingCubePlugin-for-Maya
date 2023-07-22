# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QGraphicsEffect(__PySide2_QtCore.QObject):
    """ QGraphicsEffect(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def boundingRectFor(self, sourceRect): # real signature unknown; restored from __doc__
        """ boundingRectFor(self, sourceRect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def draw(self, painter): # real signature unknown; restored from __doc__
        """ draw(self, painter: PySide2.QtGui.QPainter) -> None """
        pass

    def drawSource(self, painter): # real signature unknown; restored from __doc__
        """ drawSource(self, painter: PySide2.QtGui.QPainter) -> None """
        pass

    def enabledChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def setEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setEnabled(self, enable: bool) -> None """
        pass

    def sourceBoundingRect(self, system=None): # real signature unknown; restored from __doc__
        """ sourceBoundingRect(self, system: PySide2.QtCore.Qt.CoordinateSystem = PySide2.QtCore.Qt.CoordinateSystem.LogicalCoordinates) -> PySide2.QtCore.QRectF """
        pass

    def sourceChanged(self, flags): # real signature unknown; restored from __doc__
        """ sourceChanged(self, flags: PySide2.QtWidgets.QGraphicsEffect.ChangeFlags) -> None """
        pass

    def sourceIsPixmap(self): # real signature unknown; restored from __doc__
        """ sourceIsPixmap(self) -> bool """
        return False

    def sourcePixmap(self, system=None, offset, PySide2_QtCore_QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sourcePixmap(self, system: PySide2.QtCore.Qt.CoordinateSystem = PySide2.QtCore.Qt.CoordinateSystem.LogicalCoordinates, offset: typing.Optional[PySide2.QtCore.QPoint] = None, mode: PySide2.QtWidgets.QGraphicsEffect.PixmapPadMode = PySide2.QtWidgets.QGraphicsEffect.PixmapPadMode.PadToEffectiveBoundingRect) -> PySide2.QtGui.QPixmap """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) -> None """
        pass

    def updateBoundingRect(self): # real signature unknown; restored from __doc__
        """ updateBoundingRect(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ChangeFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsEffect.ChangeFlag'>"
    ChangeFlags = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsEffect.ChangeFlags'>"
    NoPad = PySide2.QtWidgets.QGraphicsEffect.PixmapPadMode.NoPad
    PadToEffectiveBoundingRect = PySide2.QtWidgets.QGraphicsEffect.PixmapPadMode.PadToEffectiveBoundingRect
    PadToTransparentBorder = PySide2.QtWidgets.QGraphicsEffect.PixmapPadMode.PadToTransparentBorder
    PixmapPadMode = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsEffect.PixmapPadMode'>"
    SourceAttached = PySide2.QtWidgets.QGraphicsEffect.ChangeFlag.SourceAttached
    SourceBoundingRectChanged = PySide2.QtWidgets.QGraphicsEffect.ChangeFlag.SourceBoundingRectChanged
    SourceDetached = PySide2.QtWidgets.QGraphicsEffect.ChangeFlag.SourceDetached
    SourceInvalidated = PySide2.QtWidgets.QGraphicsEffect.ChangeFlag.SourceInvalidated
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F5085A440>'


