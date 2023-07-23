# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QFrame import QFrame

class QSplitter(QFrame):
    """
    QSplitter(self, arg__1: PySide2.QtCore.Qt.Orientation, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QSplitter(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def addWidget(self, widget): # real signature unknown; restored from __doc__
        """ addWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def childEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ childEvent(self, arg__1: PySide2.QtCore.QChildEvent) -> None """
        pass

    def childrenCollapsible(self): # real signature unknown; restored from __doc__
        """ childrenCollapsible(self) -> bool """
        return False

    def closestLegalPosition(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ closestLegalPosition(self, arg__1: int, arg__2: int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def createHandle(self): # real signature unknown; restored from __doc__
        """ createHandle(self) -> PySide2.QtWidgets.QSplitterHandle """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def getRange(self, index): # real signature unknown; restored from __doc__
        """ getRange(self, index: int) -> typing.Tuple[int, int] """
        pass

    def handle(self, index): # real signature unknown; restored from __doc__
        """ handle(self, index: int) -> PySide2.QtWidgets.QSplitterHandle """
        pass

    def handleWidth(self): # real signature unknown; restored from __doc__
        """ handleWidth(self) -> int """
        return 0

    def indexOf(self, w): # real signature unknown; restored from __doc__
        """ indexOf(self, w: PySide2.QtWidgets.QWidget) -> int """
        return 0

    def insertWidget(self, index, widget): # real signature unknown; restored from __doc__
        """ insertWidget(self, index: int, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def isCollapsible(self, index): # real signature unknown; restored from __doc__
        """ isCollapsible(self, index: int) -> bool """
        return False

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def moveSplitter(self, pos, index): # real signature unknown; restored from __doc__
        """ moveSplitter(self, pos: int, index: int) -> None """
        pass

    def opaqueResize(self): # real signature unknown; restored from __doc__
        """ opaqueResize(self) -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) -> None """
        pass

    def replaceWidget(self, index, widget): # real signature unknown; restored from __doc__
        """ replaceWidget(self, index: int, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtWidgets.QWidget """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def restoreState(self, state): # real signature unknown; restored from __doc__
        """ restoreState(self, state: PySide2.QtCore.QByteArray) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> PySide2.QtCore.QByteArray """
        pass

    def setChildrenCollapsible(self, arg__1): # real signature unknown; restored from __doc__
        """ setChildrenCollapsible(self, arg__1: bool) -> None """
        pass

    def setCollapsible(self, index, arg__2): # real signature unknown; restored from __doc__
        """ setCollapsible(self, index: int, arg__2: bool) -> None """
        pass

    def setHandleWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ setHandleWidth(self, arg__1: int) -> None """
        pass

    def setOpaqueResize(self, opaque=True): # real signature unknown; restored from __doc__
        """ setOpaqueResize(self, opaque: bool = True) -> None """
        pass

    def setOrientation(self, arg__1): # real signature unknown; restored from __doc__
        """ setOrientation(self, arg__1: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def setRubberBand(self, position): # real signature unknown; restored from __doc__
        """ setRubberBand(self, position: int) -> None """
        pass

    def setSizes(self, p_list, p_int=None): # real signature unknown; restored from __doc__
        """ setSizes(self, list: typing.Sequence[int]) -> None """
        pass

    def setStretchFactor(self, index, stretch): # real signature unknown; restored from __doc__
        """ setStretchFactor(self, index: int, stretch: int) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def sizes(self): # real signature unknown; restored from __doc__
        """ sizes(self) -> typing.List[int] """
        pass

    def splitterMoved(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, index): # real signature unknown; restored from __doc__
        """ widget(self, index: int) -> PySide2.QtWidgets.QWidget """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream
        
        Return self<<value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__1: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream
        
        Return self>>value.
        """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50816E00>'


