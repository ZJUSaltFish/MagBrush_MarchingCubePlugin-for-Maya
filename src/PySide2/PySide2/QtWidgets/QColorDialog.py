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

class QColorDialog(QDialog):
    """
    QColorDialog(self, initial: PySide2.QtGui.QColor, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QColorDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def colorSelected(self, *args, **kwargs): # real signature unknown
        pass

    def currentColor(self): # real signature unknown; restored from __doc__
        """ currentColor(self) -> PySide2.QtGui.QColor """
        pass

    def currentColorChanged(self, *args, **kwargs): # real signature unknown
        pass

    def customColor(self, index): # real signature unknown; restored from __doc__
        """ customColor(index: int) -> PySide2.QtGui.QColor """
        pass

    def customCount(self): # real signature unknown; restored from __doc__
        """ customCount() -> int """
        return 0

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) -> None """
        pass

    def getColor(self, initial=None, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getColor(initial: PySide2.QtGui.QColor = PySide2.QtCore.Qt.GlobalColor.white, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, title: str = '', options: PySide2.QtWidgets.QColorDialog.ColorDialogOptions = Default(QColorDialog.ColorDialogOptions)) -> PySide2.QtGui.QColor """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> PySide2.QtWidgets.QColorDialog.ColorDialogOptions """
        pass

    def selectedColor(self): # real signature unknown; restored from __doc__
        """ selectedColor(self) -> PySide2.QtGui.QColor """
        pass

    def setCurrentColor(self, color): # real signature unknown; restored from __doc__
        """ setCurrentColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setCustomColor(self, index, color): # real signature unknown; restored from __doc__
        """ setCustomColor(index: int, color: PySide2.QtGui.QColor) -> None """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtWidgets.QColorDialog.ColorDialogOption, on: bool = True) -> None """
        pass

    def setOptions(self, options): # real signature unknown; restored from __doc__
        """ setOptions(self, options: PySide2.QtWidgets.QColorDialog.ColorDialogOptions) -> None """
        pass

    def setStandardColor(self, index, color): # real signature unknown; restored from __doc__
        """ setStandardColor(index: int, color: PySide2.QtGui.QColor) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def standardColor(self, index): # real signature unknown; restored from __doc__
        """ standardColor(index: int) -> PySide2.QtGui.QColor """
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: PySide2.QtWidgets.QColorDialog.ColorDialogOption) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, initial, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ColorDialogOption = None # (!) real value is "<class 'PySide2.QtWidgets.QColorDialog.ColorDialogOption'>"
    ColorDialogOptions = None # (!) real value is "<class 'PySide2.QtWidgets.QColorDialog.ColorDialogOptions'>"
    DontUseNativeDialog = PySide2.QtWidgets.QColorDialog.ColorDialogOption.DontUseNativeDialog
    NoButtons = PySide2.QtWidgets.QColorDialog.ColorDialogOption.NoButtons
    ShowAlphaChannel = PySide2.QtWidgets.QColorDialog.ColorDialogOption.ShowAlphaChannel
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F5084A5C0>'


