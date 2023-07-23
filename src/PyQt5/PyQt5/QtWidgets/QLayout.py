# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QLayoutItem import QLayoutItem

class QLayout(__PyQt5_QtCore.QObject, QLayoutItem):
    """
    QLayout(parent: QWidget)
    QLayout()
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def addChildLayout(self, l): # real signature unknown; restored from __doc__
        """ addChildLayout(self, l: QLayout) """
        pass

    def addChildWidget(self, w): # real signature unknown; restored from __doc__
        """ addChildWidget(self, w: QWidget) """
        pass

    def addItem(self, a0): # real signature unknown; restored from __doc__
        """ addItem(self, a0: QLayoutItem) """
        pass

    def addWidget(self, w): # real signature unknown; restored from __doc__
        """ addWidget(self, w: QWidget) """
        pass

    def alignmentRect(self, a0): # real signature unknown; restored from __doc__
        """ alignmentRect(self, a0: QRect) -> QRect """
        pass

    def childEvent(self, e): # real signature unknown; restored from __doc__
        """ childEvent(self, e: QChildEvent) """
        pass

    def closestAcceptableSize(self, w, s): # real signature unknown; restored from __doc__
        """ closestAcceptableSize(w: QWidget, s: QSize) -> QSize """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentsMargins(self): # real signature unknown; restored from __doc__
        """ contentsMargins(self) -> QMargins """
        pass

    def contentsRect(self): # real signature unknown; restored from __doc__
        """ contentsRect(self) -> QRect """
        pass

    def controlTypes(self): # real signature unknown; restored from __doc__
        """ controlTypes(self) -> QSizePolicy.ControlTypes """
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

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> Tuple[int, int, int, int] """
        pass

    def indexOf(self, a0): # real signature unknown; restored from __doc__ with multiple overloads
        """
        indexOf(self, a0: QWidget) -> int
        indexOf(self, a0: QLayoutItem) -> int
        """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, index): # real signature unknown; restored from __doc__
        """ itemAt(self, index: int) -> QLayoutItem """
        return QLayoutItem

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> QLayout """
        return QLayout

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def menuBar(self): # real signature unknown; restored from __doc__
        """ menuBar(self) -> QWidget """
        return QWidget

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> QWidget """
        return QWidget

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeItem(self, a0): # real signature unknown; restored from __doc__
        """ removeItem(self, a0: QLayoutItem) """
        pass

    def removeWidget(self, w): # real signature unknown; restored from __doc__
        """ removeWidget(self, w: QWidget) """
        pass

    def replaceWidget(self, from_, to, options, Qt_FindChildOptions=None, Qt_FindChildOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ replaceWidget(self, from_: QWidget, to: QWidget, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QLayoutItem """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAlignment(self, w: QWidget, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) -> bool
        setAlignment(self, l: QLayout, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) -> bool
        setAlignment(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag])
        """
        return False

    def setContentsMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContentsMargins(self, left: int, top: int, right: int, bottom: int)
        setContentsMargins(self, margins: QMargins)
        """
        pass

    def setEnabled(self, a0): # real signature unknown; restored from __doc__
        """ setEnabled(self, a0: bool) """
        pass

    def setGeometry(self, a0): # real signature unknown; restored from __doc__
        """ setGeometry(self, a0: QRect) """
        pass

    def setMenuBar(self, w): # real signature unknown; restored from __doc__
        """ setMenuBar(self, w: QWidget) """
        pass

    def setSizeConstraint(self, a0): # real signature unknown; restored from __doc__
        """ setSizeConstraint(self, a0: QLayout.SizeConstraint) """
        pass

    def setSpacing(self, a0): # real signature unknown; restored from __doc__
        """ setSpacing(self, a0: int) """
        pass

    def sizeConstraint(self): # real signature unknown; restored from __doc__
        """ sizeConstraint(self) -> QLayout.SizeConstraint """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, index): # real signature unknown; restored from __doc__
        """ takeAt(self, index: int) -> QLayoutItem """
        return QLayoutItem

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def totalHeightForWidth(self, w): # real signature unknown; restored from __doc__
        """ totalHeightForWidth(self, w: int) -> int """
        return 0

    def totalMaximumSize(self): # real signature unknown; restored from __doc__
        """ totalMaximumSize(self) -> QSize """
        pass

    def totalMinimumSize(self): # real signature unknown; restored from __doc__
        """ totalMinimumSize(self) -> QSize """
        pass

    def totalSizeHint(self): # real signature unknown; restored from __doc__
        """ totalSizeHint(self) -> QSize """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) """
        pass

    def widgetEvent(self, a0): # real signature unknown; restored from __doc__
        """ widgetEvent(self, a0: QEvent) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    SetDefaultConstraint = 0
    SetFixedSize = 3
    SetMaximumSize = 4
    SetMinAndMaxSize = 5
    SetMinimumSize = 2
    SetNoConstraint = 1


