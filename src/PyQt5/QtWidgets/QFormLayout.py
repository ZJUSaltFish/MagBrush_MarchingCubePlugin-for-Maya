# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QLayout import QLayout

class QFormLayout(QLayout):
    """ QFormLayout(parent: typing.Optional[QWidget] = None) """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, item): # real signature unknown; restored from __doc__
        """ addItem(self, item: QLayoutItem) """
        pass

    def addRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRow(self, label: QWidget, field: QWidget)
        addRow(self, label: QWidget, field: QLayout)
        addRow(self, labelText: str, field: QWidget)
        addRow(self, labelText: str, field: QLayout)
        addRow(self, widget: QWidget)
        addRow(self, layout: QLayout)
        """
        pass

    def alignmentRect(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def fieldGrowthPolicy(self): # real signature unknown; restored from __doc__
        """ fieldGrowthPolicy(self) -> QFormLayout.FieldGrowthPolicy """
        pass

    def formAlignment(self): # real signature unknown; restored from __doc__
        """ formAlignment(self) -> Qt.Alignment """
        pass

    def getItemPosition(self, index): # real signature unknown; restored from __doc__
        """ getItemPosition(self, index: int) -> Tuple[int, QFormLayout.ItemRole] """
        pass

    def getLayoutPosition(self, layout): # real signature unknown; restored from __doc__
        """ getLayoutPosition(self, layout: QLayout) -> Tuple[int, QFormLayout.ItemRole] """
        pass

    def getWidgetPosition(self, widget): # real signature unknown; restored from __doc__
        """ getWidgetPosition(self, widget: QWidget) -> Tuple[int, QFormLayout.ItemRole] """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, width): # real signature unknown; restored from __doc__
        """ heightForWidth(self, width: int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> int """
        return 0

    def insertRow(self, row, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRow(self, row: int, label: QWidget, field: QWidget)
        insertRow(self, row: int, label: QWidget, field: QLayout)
        insertRow(self, row: int, labelText: str, field: QWidget)
        insertRow(self, row: int, labelText: str, field: QLayout)
        insertRow(self, row: int, widget: QWidget)
        insertRow(self, row: int, layout: QLayout)
        """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, row: int, role: QFormLayout.ItemRole) -> QLayoutItem
        itemAt(self, index: int) -> QLayoutItem
        """
        return QLayoutItem

    def labelAlignment(self): # real signature unknown; restored from __doc__
        """ labelAlignment(self) -> Qt.Alignment """
        pass

    def labelForField(self, field): # real signature unknown; restored from __doc__ with multiple overloads
        """
        labelForField(self, field: QWidget) -> QWidget
        labelForField(self, field: QLayout) -> QWidget
        """
        return QWidget

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeRow(self, row: int)
        removeRow(self, widget: QWidget)
        removeRow(self, layout: QLayout)
        """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowWrapPolicy(self): # real signature unknown; restored from __doc__
        """ rowWrapPolicy(self) -> QFormLayout.RowWrapPolicy """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFieldGrowthPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setFieldGrowthPolicy(self, policy: QFormLayout.FieldGrowthPolicy) """
        pass

    def setFormAlignment(self, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setFormAlignment(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: QRect) """
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: int) """
        pass

    def setItem(self, row, role, item): # real signature unknown; restored from __doc__
        """ setItem(self, row: int, role: QFormLayout.ItemRole, item: QLayoutItem) """
        pass

    def setLabelAlignment(self, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setLabelAlignment(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setLayout(self, row, role, layout): # real signature unknown; restored from __doc__
        """ setLayout(self, row: int, role: QFormLayout.ItemRole, layout: QLayout) """
        pass

    def setRowWrapPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setRowWrapPolicy(self, policy: QFormLayout.RowWrapPolicy) """
        pass

    def setSpacing(self, a0): # real signature unknown; restored from __doc__
        """ setSpacing(self, a0: int) """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: int) """
        pass

    def setWidget(self, row, role, widget): # real signature unknown; restored from __doc__
        """ setWidget(self, row: int, role: QFormLayout.ItemRole, widget: QWidget) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, index): # real signature unknown; restored from __doc__
        """ takeAt(self, index: int) -> QLayoutItem """
        return QLayoutItem

    def takeRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        takeRow(self, row: int) -> QFormLayout.TakeRowResult
        takeRow(self, widget: QWidget) -> QFormLayout.TakeRowResult
        takeRow(self, layout: QLayout) -> QFormLayout.TakeRowResult
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> int """
        return 0

    def widgetEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AllNonFixedFieldsGrow = 2
    DontWrapRows = 0
    ExpandingFieldsGrow = 1
    FieldRole = 1
    FieldsStayAtSizeHint = 0
    LabelRole = 0
    SpanningRole = 2
    WrapAllRows = 2
    WrapLongRows = 1


