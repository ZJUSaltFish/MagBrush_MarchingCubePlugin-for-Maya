# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QLayout import QLayout

class QFormLayout(QLayout):
    """ QFormLayout(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def addItem(self, item): # real signature unknown; restored from __doc__
        """ addItem(self, item: PySide2.QtWidgets.QLayoutItem) -> None """
        pass

    def addRow(self, label, field): # real signature unknown; restored from __doc__
        """
        addRow(self, label: PySide2.QtWidgets.QWidget, field: PySide2.QtWidgets.QLayout) -> None
        addRow(self, label: PySide2.QtWidgets.QWidget, field: PySide2.QtWidgets.QWidget) -> None
        addRow(self, labelText: str, field: PySide2.QtWidgets.QLayout) -> None
        addRow(self, labelText: str, field: PySide2.QtWidgets.QWidget) -> None
        addRow(self, layout: PySide2.QtWidgets.QLayout) -> None
        addRow(self, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> PySide2.QtCore.Qt.Orientations """
        pass

    def fieldGrowthPolicy(self): # real signature unknown; restored from __doc__
        """ fieldGrowthPolicy(self) -> PySide2.QtWidgets.QFormLayout.FieldGrowthPolicy """
        pass

    def formAlignment(self): # real signature unknown; restored from __doc__
        """ formAlignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def getItemPosition(self, index, rolePtr): # real signature unknown; restored from __doc__
        """ getItemPosition(self, index: int, rolePtr: PySide2.QtWidgets.QFormLayout.ItemRole) -> int """
        return 0

    def getLayoutPosition(self, layout, rolePtr): # real signature unknown; restored from __doc__
        """ getLayoutPosition(self, layout: PySide2.QtWidgets.QLayout, rolePtr: PySide2.QtWidgets.QFormLayout.ItemRole) -> int """
        return 0

    def getWidgetPosition(self, widget, rolePtr): # real signature unknown; restored from __doc__
        """ getWidgetPosition(self, widget: PySide2.QtWidgets.QWidget, rolePtr: PySide2.QtWidgets.QFormLayout.ItemRole) -> int """
        return 0

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, width): # real signature unknown; restored from __doc__
        """ heightForWidth(self, width: int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> int """
        return 0

    def insertRow(self, row, label, field): # real signature unknown; restored from __doc__
        """
        insertRow(self, row: int, label: PySide2.QtWidgets.QWidget, field: PySide2.QtWidgets.QLayout) -> None
        insertRow(self, row: int, label: PySide2.QtWidgets.QWidget, field: PySide2.QtWidgets.QWidget) -> None
        insertRow(self, row: int, labelText: str, field: PySide2.QtWidgets.QLayout) -> None
        insertRow(self, row: int, labelText: str, field: PySide2.QtWidgets.QWidget) -> None
        insertRow(self, row: int, layout: PySide2.QtWidgets.QLayout) -> None
        insertRow(self, row: int, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def itemAt(self, index): # real signature unknown; restored from __doc__
        """
        itemAt(self, index: int) -> PySide2.QtWidgets.QLayoutItem
        itemAt(self, row: int, role: PySide2.QtWidgets.QFormLayout.ItemRole) -> PySide2.QtWidgets.QLayoutItem
        """
        pass

    def labelAlignment(self): # real signature unknown; restored from __doc__
        """ labelAlignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def labelForField(self, field): # real signature unknown; restored from __doc__
        """
        labelForField(self, field: PySide2.QtWidgets.QLayout) -> PySide2.QtWidgets.QWidget
        labelForField(self, field: PySide2.QtWidgets.QWidget) -> PySide2.QtWidgets.QWidget
        """
        pass

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> PySide2.QtCore.QSize """
        pass

    def removeRow(self, layout): # real signature unknown; restored from __doc__
        """
        removeRow(self, layout: PySide2.QtWidgets.QLayout) -> None
        removeRow(self, row: int) -> None
        removeRow(self, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowWrapPolicy(self): # real signature unknown; restored from __doc__
        """ rowWrapPolicy(self) -> PySide2.QtWidgets.QFormLayout.RowWrapPolicy """
        pass

    def setFieldGrowthPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setFieldGrowthPolicy(self, policy: PySide2.QtWidgets.QFormLayout.FieldGrowthPolicy) -> None """
        pass

    def setFormAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setFormAlignment(self, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: PySide2.QtCore.QRect) -> None """
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: int) -> None """
        pass

    def setItem(self, row, role, item): # real signature unknown; restored from __doc__
        """ setItem(self, row: int, role: PySide2.QtWidgets.QFormLayout.ItemRole, item: PySide2.QtWidgets.QLayoutItem) -> None """
        pass

    def setLabelAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setLabelAlignment(self, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setLayout(self, row, role, layout): # real signature unknown; restored from __doc__
        """ setLayout(self, row: int, role: PySide2.QtWidgets.QFormLayout.ItemRole, layout: PySide2.QtWidgets.QLayout) -> None """
        pass

    def setRowWrapPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setRowWrapPolicy(self, policy: PySide2.QtWidgets.QFormLayout.RowWrapPolicy) -> None """
        pass

    def setSpacing(self, arg__1): # real signature unknown; restored from __doc__
        """ setSpacing(self, arg__1: int) -> None """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: int) -> None """
        pass

    def setWidget(self, row, role, widget): # real signature unknown; restored from __doc__
        """ setWidget(self, row: int, role: PySide2.QtWidgets.QFormLayout.ItemRole, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, index): # real signature unknown; restored from __doc__
        """ takeAt(self, index: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> int """
        return 0

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

    AllNonFixedFieldsGrow = PySide2.QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow
    DontWrapRows = PySide2.QtWidgets.QFormLayout.RowWrapPolicy.DontWrapRows
    ExpandingFieldsGrow = PySide2.QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow
    FieldGrowthPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QFormLayout.FieldGrowthPolicy'>"
    FieldRole = PySide2.QtWidgets.QFormLayout.ItemRole.FieldRole
    FieldsStayAtSizeHint = PySide2.QtWidgets.QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint
    ItemRole = None # (!) real value is "<class 'PySide2.QtWidgets.QFormLayout.ItemRole'>"
    LabelRole = PySide2.QtWidgets.QFormLayout.ItemRole.LabelRole
    RowWrapPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QFormLayout.RowWrapPolicy'>"
    SpanningRole = PySide2.QtWidgets.QFormLayout.ItemRole.SpanningRole
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507955C0>'
    WrapAllRows = PySide2.QtWidgets.QFormLayout.RowWrapPolicy.WrapAllRows
    WrapLongRows = PySide2.QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows


