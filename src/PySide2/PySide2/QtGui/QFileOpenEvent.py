# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QFileOpenEvent(__PySide2_QtCore.QEvent):
    """
    QFileOpenEvent(self, file: str) -> None
    QFileOpenEvent(self, url: PySide2.QtCore.QUrl) -> None
    """
    def file(self): # real signature unknown; restored from __doc__
        """ file(self) -> str """
        return ""

    def openFile(self, file, flags): # real signature unknown; restored from __doc__
        """ openFile(self, file: PySide2.QtCore.QFile, flags: PySide2.QtCore.QIODevice.OpenMode) -> bool """
        return False

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, file): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


