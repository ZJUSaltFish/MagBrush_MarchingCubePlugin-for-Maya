# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QAccessibleEvent import QAccessibleEvent

class QAccessibleTableModelChangeEvent(QAccessibleEvent):
    """
    QAccessibleTableModelChangeEvent(self, iface: PySide2.QtGui.QAccessibleInterface, changeType: PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType) -> None
    QAccessibleTableModelChangeEvent(self, obj: PySide2.QtCore.QObject, changeType: PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType) -> None
    """
    def firstColumn(self): # real signature unknown; restored from __doc__
        """ firstColumn(self) -> int """
        return 0

    def firstRow(self): # real signature unknown; restored from __doc__
        """ firstRow(self) -> int """
        return 0

    def lastColumn(self): # real signature unknown; restored from __doc__
        """ lastColumn(self) -> int """
        return 0

    def lastRow(self): # real signature unknown; restored from __doc__
        """ lastRow(self) -> int """
        return 0

    def modelChangeType(self): # real signature unknown; restored from __doc__
        """ modelChangeType(self) -> PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType """
        pass

    def setFirstColumn(self, col): # real signature unknown; restored from __doc__
        """ setFirstColumn(self, col: int) -> None """
        pass

    def setFirstRow(self, row): # real signature unknown; restored from __doc__
        """ setFirstRow(self, row: int) -> None """
        pass

    def setLastColumn(self, col): # real signature unknown; restored from __doc__
        """ setLastColumn(self, col: int) -> None """
        pass

    def setLastRow(self, row): # real signature unknown; restored from __doc__
        """ setLastRow(self, row: int) -> None """
        pass

    def setModelChangeType(self, changeType): # real signature unknown; restored from __doc__
        """ setModelChangeType(self, changeType: PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, iface, changeType): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ColumnsInserted = PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType.ColumnsInserted
    ColumnsRemoved = PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType.ColumnsRemoved
    DataChanged = PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType.DataChanged
    ModelChangeType = None # (!) real value is "<class 'PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType'>"
    ModelReset = PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType.ModelReset
    RowsInserted = PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType.RowsInserted
    RowsRemoved = PySide2.QtGui.QAccessibleTableModelChangeEvent.ModelChangeType.RowsRemoved


