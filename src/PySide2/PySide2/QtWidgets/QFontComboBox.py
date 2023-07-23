# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QComboBox import QComboBox

class QFontComboBox(QComboBox):
    """ QFontComboBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def currentFont(self): # real signature unknown; restored from __doc__
        """ currentFont(self) -> PySide2.QtGui.QFont """
        pass

    def currentFontChanged(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def fontFilters(self): # real signature unknown; restored from __doc__
        """ fontFilters(self) -> PySide2.QtWidgets.QFontComboBox.FontFilters """
        pass

    def setCurrentFont(self, f): # real signature unknown; restored from __doc__
        """ setCurrentFont(self, f: PySide2.QtGui.QFont) -> None """
        pass

    def setFontFilters(self, filters): # real signature unknown; restored from __doc__
        """ setFontFilters(self, filters: PySide2.QtWidgets.QFontComboBox.FontFilters) -> None """
        pass

    def setWritingSystem(self, arg__1): # real signature unknown; restored from __doc__
        """ setWritingSystem(self, arg__1: PySide2.QtGui.QFontDatabase.WritingSystem) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def writingSystem(self): # real signature unknown; restored from __doc__
        """ writingSystem(self) -> PySide2.QtGui.QFontDatabase.WritingSystem """
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

    AllFonts = PySide2.QtWidgets.QFontComboBox.FontFilter.AllFonts
    FontFilter = None # (!) real value is "<class 'PySide2.QtWidgets.QFontComboBox.FontFilter'>"
    FontFilters = None # (!) real value is "<class 'PySide2.QtWidgets.QFontComboBox.FontFilters'>"
    MonospacedFonts = PySide2.QtWidgets.QFontComboBox.FontFilter.MonospacedFonts
    NonScalableFonts = PySide2.QtWidgets.QFontComboBox.FontFilter.NonScalableFonts
    ProportionalFonts = PySide2.QtWidgets.QFontComboBox.FontFilter.ProportionalFonts
    ScalableFonts = PySide2.QtWidgets.QFontComboBox.FontFilter.ScalableFonts
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507BDB80>'


