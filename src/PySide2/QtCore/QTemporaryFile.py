# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QFile import QFile

class QTemporaryFile(QFile):
    """
    QTemporaryFile(self) -> None
    QTemporaryFile(self, parent: PySide2.QtCore.QObject) -> None
    QTemporaryFile(self, templateName: str) -> None
    QTemporaryFile(self, templateName: str, parent: PySide2.QtCore.QObject) -> None
    """
    def autoRemove(self): # real signature unknown; restored from __doc__
        """ autoRemove(self) -> bool """
        return False

    def createLocalFile(self, file): # real signature unknown; restored from __doc__
        """
        createLocalFile(file: PySide2.QtCore.QFile) -> PySide2.QtCore.QTemporaryFile
        createLocalFile(fileName: str) -> PySide2.QtCore.QTemporaryFile
        """
        pass

    def createNativeFile(self, file): # real signature unknown; restored from __doc__
        """
        createNativeFile(file: PySide2.QtCore.QFile) -> PySide2.QtCore.QTemporaryFile
        createNativeFile(fileName: str) -> PySide2.QtCore.QTemporaryFile
        """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def fileTemplate(self): # real signature unknown; restored from __doc__
        """ fileTemplate(self) -> str """
        return ""

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> bool
        open(self, flags: PySide2.QtCore.QIODevice.OpenMode) -> bool
        """
        return False

    def rename(self, newName): # real signature unknown; restored from __doc__
        """ rename(self, newName: str) -> bool """
        return False

    def setAutoRemove(self, b): # real signature unknown; restored from __doc__
        """ setAutoRemove(self, b: bool) -> None """
        pass

    def setFileTemplate(self, name): # real signature unknown; restored from __doc__
        """ setFileTemplate(self, name: str) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DFC500>'


