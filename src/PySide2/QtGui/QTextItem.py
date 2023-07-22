# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTextItem(__Shiboken.Object):
    """ QTextItem(self) -> None """
    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def renderFlags(self): # real signature unknown; restored from __doc__
        """ renderFlags(self) -> PySide2.QtGui.QTextItem.RenderFlags """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Dummy = PySide2.QtGui.QTextItem.RenderFlag.Dummy
    Overline = PySide2.QtGui.QTextItem.RenderFlag.Overline
    RenderFlag = None # (!) real value is "<class 'PySide2.QtGui.QTextItem.RenderFlag'>"
    RenderFlags = None # (!) real value is "<class 'PySide2.QtGui.QTextItem.RenderFlags'>"
    RightToLeft = PySide2.QtGui.QTextItem.RenderFlag.RightToLeft
    StrikeOut = PySide2.QtGui.QTextItem.RenderFlag.StrikeOut
    Underline = PySide2.QtGui.QTextItem.RenderFlag.Underline


