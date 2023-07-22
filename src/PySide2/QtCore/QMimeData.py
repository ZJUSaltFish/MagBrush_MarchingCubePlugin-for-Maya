# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QMimeData(QObject):
    """ QMimeData(self) -> None """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def colorData(self): # real signature unknown; restored from __doc__
        """ colorData(self) -> typing.Any """
        pass

    def data(self, mimetype): # real signature unknown; restored from __doc__
        """ data(self, mimetype: str) -> PySide2.QtCore.QByteArray """
        pass

    def formats(self): # real signature unknown; restored from __doc__
        """ formats(self) -> typing.List[str] """
        pass

    def hasColor(self): # real signature unknown; restored from __doc__
        """ hasColor(self) -> bool """
        return False

    def hasFormat(self, mimetype): # real signature unknown; restored from __doc__
        """ hasFormat(self, mimetype: str) -> bool """
        return False

    def hasHtml(self): # real signature unknown; restored from __doc__
        """ hasHtml(self) -> bool """
        return False

    def hasImage(self): # real signature unknown; restored from __doc__
        """ hasImage(self) -> bool """
        return False

    def hasText(self): # real signature unknown; restored from __doc__
        """ hasText(self) -> bool """
        return False

    def hasUrls(self): # real signature unknown; restored from __doc__
        """ hasUrls(self) -> bool """
        return False

    def html(self): # real signature unknown; restored from __doc__
        """ html(self) -> str """
        return ""

    def imageData(self): # real signature unknown; restored from __doc__
        """ imageData(self) -> typing.Any """
        pass

    def removeFormat(self, mimetype): # real signature unknown; restored from __doc__
        """ removeFormat(self, mimetype: str) -> None """
        pass

    def retrieveData(self, mimetype, preferredType): # real signature unknown; restored from __doc__
        """ retrieveData(self, mimetype: str, preferredType: type) -> typing.Any """
        pass

    def setColorData(self, color): # real signature unknown; restored from __doc__
        """ setColorData(self, color: typing.Any) -> None """
        pass

    def setData(self, mimetype, data): # real signature unknown; restored from __doc__
        """ setData(self, mimetype: str, data: PySide2.QtCore.QByteArray) -> None """
        pass

    def setHtml(self, html): # real signature unknown; restored from __doc__
        """ setHtml(self, html: str) -> None """
        pass

    def setImageData(self, image): # real signature unknown; restored from __doc__
        """ setImageData(self, image: typing.Any) -> None """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) -> None """
        pass

    def setUrls(self, urls, PySide2_QtCore_QUrl=None): # real signature unknown; restored from __doc__
        """ setUrls(self, urls: typing.Sequence[PySide2.QtCore.QUrl]) -> None """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def urls(self): # real signature unknown; restored from __doc__
        """ urls(self) -> typing.List[PySide2.QtCore.QUrl] """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DDD340>'


