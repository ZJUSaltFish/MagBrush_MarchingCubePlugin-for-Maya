# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QPlaceReply import QPlaceReply

class QPlaceIdReply(QPlaceReply):
    """ QPlaceIdReply(self, operationType: PySide2.QtLocation.QPlaceIdReply.OperationType, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> str """
        return ""

    def operationType(self): # real signature unknown; restored from __doc__
        """ operationType(self) -> PySide2.QtLocation.QPlaceIdReply.OperationType """
        pass

    def setId(self, identifier): # real signature unknown; restored from __doc__
        """ setId(self, identifier: str) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtLocation.QPlaceReply.Type """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, operationType, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    OperationType = None # (!) real value is "<class 'PySide2.QtLocation.QPlaceIdReply.OperationType'>"
    RemoveCategory = PySide2.QtLocation.QPlaceIdReply.OperationType.RemoveCategory
    RemovePlace = PySide2.QtLocation.QPlaceIdReply.OperationType.RemovePlace
    SaveCategory = PySide2.QtLocation.QPlaceIdReply.OperationType.SaveCategory
    SavePlace = PySide2.QtLocation.QPlaceIdReply.OperationType.SavePlace
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000013BA752ED40>'


