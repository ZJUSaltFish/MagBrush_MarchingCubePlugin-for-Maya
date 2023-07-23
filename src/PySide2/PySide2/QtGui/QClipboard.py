# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QClipboard(__PySide2_QtCore.QObject):
    # no doc
    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, mode=None): # real signature unknown; restored from __doc__
        """ clear(self, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> None """
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def findBufferChanged(self, *args, **kwargs): # real signature unknown
        pass

    def image(self, mode=None): # real signature unknown; restored from __doc__
        """ image(self, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> PySide2.QtGui.QImage """
        pass

    def mimeData(self, mode=None): # real signature unknown; restored from __doc__
        """ mimeData(self, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> PySide2.QtCore.QMimeData """
        pass

    def ownsClipboard(self): # real signature unknown; restored from __doc__
        """ ownsClipboard(self) -> bool """
        return False

    def ownsFindBuffer(self): # real signature unknown; restored from __doc__
        """ ownsFindBuffer(self) -> bool """
        return False

    def ownsSelection(self): # real signature unknown; restored from __doc__
        """ ownsSelection(self) -> bool """
        return False

    def pixmap(self, mode=None): # real signature unknown; restored from __doc__
        """ pixmap(self, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> PySide2.QtGui.QPixmap """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setImage(self, arg__1, mode=None): # real signature unknown; restored from __doc__
        """ setImage(self, arg__1: PySide2.QtGui.QImage, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> None """
        pass

    def setMimeData(self, data, mode=None): # real signature unknown; restored from __doc__
        """ setMimeData(self, data: PySide2.QtCore.QMimeData, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> None """
        pass

    def setPixmap(self, arg__1, mode=None): # real signature unknown; restored from __doc__
        """ setPixmap(self, arg__1: PySide2.QtGui.QPixmap, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> None """
        pass

    def setText(self, arg__1, mode=None): # real signature unknown; restored from __doc__
        """ setText(self, arg__1: str, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> None """
        pass

    def supportsFindBuffer(self): # real signature unknown; restored from __doc__
        """ supportsFindBuffer(self) -> bool """
        return False

    def supportsSelection(self): # real signature unknown; restored from __doc__
        """ supportsSelection(self) -> bool """
        return False

    def text(self, mode=None): # real signature unknown; restored from __doc__
        """
        text(self, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> str
        text(self, subtype: str, mode: PySide2.QtGui.QClipboard.Mode = PySide2.QtGui.QClipboard.Mode.Clipboard) -> str
        """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Clipboard = PySide2.QtGui.QClipboard.Mode.Clipboard
    FindBuffer = PySide2.QtGui.QClipboard.Mode.FindBuffer
    LastMode = PySide2.QtGui.QClipboard.Mode.LastMode
    Mode = None # (!) real value is "<class 'PySide2.QtGui.QClipboard.Mode'>"
    Selection = PySide2.QtGui.QClipboard.Mode.Selection
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00854880>'


