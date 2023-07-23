# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QFileSystemWatcher(QObject):
    """
    QFileSystemWatcher(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QFileSystemWatcher(self, paths: typing.Sequence[str], parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def addPath(self, file): # real signature unknown; restored from __doc__
        """ addPath(self, file: str) -> bool """
        return False

    def addPaths(self, files, p_str=None): # real signature unknown; restored from __doc__
        """ addPaths(self, files: typing.Sequence[str]) -> typing.List[str] """
        pass

    def directories(self): # real signature unknown; restored from __doc__
        """ directories(self) -> typing.List[str] """
        pass

    def directoryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def fileChanged(self, *args, **kwargs): # real signature unknown
        pass

    def files(self): # real signature unknown; restored from __doc__
        """ files(self) -> typing.List[str] """
        pass

    def removePath(self, file): # real signature unknown; restored from __doc__
        """ removePath(self, file: str) -> bool """
        return False

    def removePaths(self, files, p_str=None): # real signature unknown; restored from __doc__
        """ removePaths(self, files: typing.Sequence[str]) -> typing.List[str] """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DED940>'


