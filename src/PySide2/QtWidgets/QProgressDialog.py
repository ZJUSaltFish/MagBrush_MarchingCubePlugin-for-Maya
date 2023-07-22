# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QDialog import QDialog

class QProgressDialog(QDialog):
    """
    QProgressDialog(self, labelText: str, cancelButtonText: str, minimum: int, maximum: int, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QProgressDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    """
    def autoClose(self): # real signature unknown; restored from __doc__
        """ autoClose(self) -> bool """
        return False

    def autoReset(self): # real signature unknown; restored from __doc__
        """ autoReset(self) -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) -> None """
        pass

    def canceled(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def closeEvent(self, event): # real signature unknown; restored from __doc__
        """ closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None """
        pass

    def forceShow(self): # real signature unknown; restored from __doc__
        """ forceShow(self) -> None """
        pass

    def labelText(self): # real signature unknown; restored from __doc__
        """ labelText(self) -> str """
        return ""

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def minimumDuration(self): # real signature unknown; restored from __doc__
        """ minimumDuration(self) -> int """
        return 0

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def setAutoClose(self, close): # real signature unknown; restored from __doc__
        """ setAutoClose(self, close: bool) -> None """
        pass

    def setAutoReset(self, reset): # real signature unknown; restored from __doc__
        """ setAutoReset(self, reset: bool) -> None """
        pass

    def setBar(self, bar): # real signature unknown; restored from __doc__
        """ setBar(self, bar: PySide2.QtWidgets.QProgressBar) -> None """
        pass

    def setCancelButton(self, button): # real signature unknown; restored from __doc__
        """ setCancelButton(self, button: PySide2.QtWidgets.QPushButton) -> None """
        pass

    def setCancelButtonText(self, text): # real signature unknown; restored from __doc__
        """ setCancelButtonText(self, text: str) -> None """
        pass

    def setLabel(self, label): # real signature unknown; restored from __doc__
        """ setLabel(self, label: PySide2.QtWidgets.QLabel) -> None """
        pass

    def setLabelText(self, text): # real signature unknown; restored from __doc__
        """ setLabelText(self, text: str) -> None """
        pass

    def setMaximum(self, maximum): # real signature unknown; restored from __doc__
        """ setMaximum(self, maximum: int) -> None """
        pass

    def setMinimum(self, minimum): # real signature unknown; restored from __doc__
        """ setMinimum(self, minimum: int) -> None """
        pass

    def setMinimumDuration(self, ms): # real signature unknown; restored from __doc__
        """ setMinimumDuration(self, ms: int) -> None """
        pass

    def setRange(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setRange(self, minimum: int, maximum: int) -> None """
        pass

    def setValue(self, progress): # real signature unknown; restored from __doc__
        """ setValue(self, progress: int) -> None """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def wasCanceled(self): # real signature unknown; restored from __doc__
        """ wasCanceled(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, labelText, cancelButtonText, minimum, maximum, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F5084AA00>'


