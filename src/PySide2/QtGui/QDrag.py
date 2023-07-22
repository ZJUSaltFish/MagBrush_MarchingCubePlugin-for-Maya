# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QDrag(__PySide2_QtCore.QObject):
    """ QDrag(self, dragSource: PySide2.QtCore.QObject) -> None """
    def actionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel() -> None """
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> PySide2.QtCore.Qt.DropAction """
        pass

    def dragCursor(self, action): # real signature unknown; restored from __doc__
        """ dragCursor(self, action: PySide2.QtCore.Qt.DropAction) -> PySide2.QtGui.QPixmap """
        pass

    def exec_(self, supportedActions, defaultAction): # real signature unknown; restored from __doc__
        """
        exec_(self, supportedActions: PySide2.QtCore.Qt.DropActions, defaultAction: PySide2.QtCore.Qt.DropAction) -> PySide2.QtCore.Qt.DropAction
        exec_(self, supportedActions: PySide2.QtCore.Qt.DropActions = PySide2.QtCore.Qt.DropAction.MoveAction) -> PySide2.QtCore.Qt.DropAction
        """
        pass

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ hotSpot(self) -> PySide2.QtCore.QPoint """
        pass

    def mimeData(self): # real signature unknown; restored from __doc__
        """ mimeData(self) -> PySide2.QtCore.QMimeData """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> PySide2.QtGui.QPixmap """
        pass

    def setDragCursor(self, cursor, action): # real signature unknown; restored from __doc__
        """ setDragCursor(self, cursor: PySide2.QtGui.QPixmap, action: PySide2.QtCore.Qt.DropAction) -> None """
        pass

    def setHotSpot(self, hotspot): # real signature unknown; restored from __doc__
        """ setHotSpot(self, hotspot: PySide2.QtCore.QPoint) -> None """
        pass

    def setMimeData(self, data): # real signature unknown; restored from __doc__
        """ setMimeData(self, data: PySide2.QtCore.QMimeData) -> None """
        pass

    def setPixmap(self, arg__1): # real signature unknown; restored from __doc__
        """ setPixmap(self, arg__1: PySide2.QtGui.QPixmap) -> None """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> PySide2.QtCore.QObject """
        pass

    def start(self, supportedActions=None): # real signature unknown; restored from __doc__
        """ start(self, supportedActions: PySide2.QtCore.Qt.DropActions = PySide2.QtCore.Qt.DropAction.CopyAction) -> PySide2.QtCore.Qt.DropAction """
        pass

    def supportedActions(self): # real signature unknown; restored from __doc__
        """ supportedActions(self) -> PySide2.QtCore.Qt.DropActions """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> PySide2.QtCore.QObject """
        pass

    def targetChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, dragSource): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00847280>'


