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

class QDialog(QWidget):
    """ QDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) -> None """
        pass

    def accepted(self, *args, **kwargs): # real signature unknown
        pass

    def adjustPosition(self, arg__1): # real signature unknown; restored from __doc__
        """ adjustPosition(self, arg__1: PySide2.QtWidgets.QWidget) -> None """
        pass

    def closeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ closeEvent(self, arg__1: PySide2.QtGui.QCloseEvent) -> None """
        pass

    def contextMenuEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, arg__1: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def done(self, arg__1): # real signature unknown; restored from __doc__
        """ done(self, arg__1: int) -> None """
        pass

    def eventFilter(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ eventFilter(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def extension(self): # real signature unknown; restored from __doc__
        """ extension(self) -> PySide2.QtWidgets.QWidget """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def isSizeGripEnabled(self): # real signature unknown; restored from __doc__
        """ isSizeGripEnabled(self) -> bool """
        return False

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """ open(self) -> None """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) -> None """
        pass

    def rejected(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> int """
        return 0

    def setExtension(self, extension): # real signature unknown; restored from __doc__
        """ setExtension(self, extension: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setModal(self, modal): # real signature unknown; restored from __doc__
        """ setModal(self, modal: bool) -> None """
        pass

    def setOrientation(self, orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, orientation: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def setResult(self, r): # real signature unknown; restored from __doc__
        """ setResult(self, r: int) -> None """
        pass

    def setSizeGripEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setSizeGripEnabled(self, arg__1: bool) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def showExtension(self, arg__1): # real signature unknown; restored from __doc__
        """ showExtension(self, arg__1: bool) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

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

    Accepted = PySide2.QtWidgets.QDialog.DialogCode.Accepted
    DialogCode = None # (!) real value is "<class 'PySide2.QtWidgets.QDialog.DialogCode'>"
    Rejected = PySide2.QtWidgets.QDialog.DialogCode.Rejected
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50833F40>'


