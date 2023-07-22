# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QHttpMultiPart(__PySide2_QtCore.QObject):
    """
    QHttpMultiPart(self, contentType: PySide2.QtNetwork.QHttpMultiPart.ContentType, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QHttpMultiPart(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def append(self, httpPart): # real signature unknown; restored from __doc__
        """ append(self, httpPart: PySide2.QtNetwork.QHttpPart) -> None """
        pass

    def boundary(self): # real signature unknown; restored from __doc__
        """ boundary(self) -> PySide2.QtCore.QByteArray """
        pass

    def setBoundary(self, boundary): # real signature unknown; restored from __doc__
        """ setBoundary(self, boundary: PySide2.QtCore.QByteArray) -> None """
        pass

    def setContentType(self, contentType): # real signature unknown; restored from __doc__
        """ setContentType(self, contentType: PySide2.QtNetwork.QHttpMultiPart.ContentType) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, contentType, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AlternativeType = PySide2.QtNetwork.QHttpMultiPart.ContentType.AlternativeType
    ContentType = None # (!) real value is "<class 'PySide2.QtNetwork.QHttpMultiPart.ContentType'>"
    FormDataType = PySide2.QtNetwork.QHttpMultiPart.ContentType.FormDataType
    MixedType = PySide2.QtNetwork.QHttpMultiPart.ContentType.MixedType
    RelatedType = PySide2.QtNetwork.QHttpMultiPart.ContentType.RelatedType
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001795D88C680>'


