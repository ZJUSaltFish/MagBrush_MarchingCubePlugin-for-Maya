# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QTranslator(QObject):
    """ QTranslator(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def language(self): # real signature unknown; restored from __doc__
        """ language(self) -> str """
        return ""

    def load(self, data, len, directory=''): # real signature unknown; restored from __doc__
        """
        load(self, data: bytes, len: int, directory: str = '') -> bool
        load(self, filename: str, directory: str = '', search_delimiters: str = '', suffix: str = '') -> bool
        load(self, locale: PySide2.QtCore.QLocale, filename: str, prefix: str = '', directory: str = '', suffix: str = '') -> bool
        """
        return False

    def translate(self, context, sourceText, disambiguation, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ translate(self, context: bytes, sourceText: bytes, disambiguation: typing.Optional[bytes] = None, n: int = -1) -> str """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DDEB00>'


