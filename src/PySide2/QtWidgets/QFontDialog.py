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

class QFontDialog(QDialog):
    """
    QFontDialog(self, initial: PySide2.QtGui.QFont, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QFontDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def currentFont(self): # real signature unknown; restored from __doc__
        """ currentFont(self) -> PySide2.QtGui.QFont """
        pass

    def currentFontChanged(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) -> None """
        pass

    def eventFilter(self, p_object, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, object: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def fontSelected(self, *args, **kwargs): # real signature unknown
        pass

    def getFont(self, initial, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        getFont(initial: PySide2.QtGui.QFont, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, title: str = '', options: PySide2.QtWidgets.QFontDialog.FontDialogOptions = Default(QFontDialog.FontDialogOptions)) -> typing.Tuple[PySide2.QtGui.QFont, bool]
        getFont(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> typing.Tuple[PySide2.QtGui.QFont, bool]
        """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> PySide2.QtWidgets.QFontDialog.FontDialogOptions """
        pass

    def selectedFont(self): # real signature unknown; restored from __doc__
        """ selectedFont(self) -> PySide2.QtGui.QFont """
        pass

    def setCurrentFont(self, font): # real signature unknown; restored from __doc__
        """ setCurrentFont(self, font: PySide2.QtGui.QFont) -> None """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtWidgets.QFontDialog.FontDialogOption, on: bool = True) -> None """
        pass

    def setOptions(self, options): # real signature unknown; restored from __doc__
        """ setOptions(self, options: PySide2.QtWidgets.QFontDialog.FontDialogOptions) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: PySide2.QtWidgets.QFontDialog.FontDialogOption) -> bool """
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

    DontUseNativeDialog = PySide2.QtWidgets.QFontDialog.FontDialogOption.DontUseNativeDialog
    FontDialogOption = None # (!) real value is "<class 'PySide2.QtWidgets.QFontDialog.FontDialogOption'>"
    FontDialogOptions = None # (!) real value is "<class 'PySide2.QtWidgets.QFontDialog.FontDialogOptions'>"
    MonospacedFonts = PySide2.QtWidgets.QFontDialog.FontDialogOption.MonospacedFonts
    NoButtons = PySide2.QtWidgets.QFontDialog.FontDialogOption.NoButtons
    NonScalableFonts = PySide2.QtWidgets.QFontDialog.FontDialogOption.NonScalableFonts
    ProportionalFonts = PySide2.QtWidgets.QFontDialog.FontDialogOption.ProportionalFonts
    ScalableFonts = PySide2.QtWidgets.QFontDialog.FontDialogOption.ScalableFonts
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50849100>'


