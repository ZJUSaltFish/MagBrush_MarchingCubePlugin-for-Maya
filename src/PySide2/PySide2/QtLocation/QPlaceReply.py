# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPlaceReply(__PySide2_QtCore.QObject):
    """ QPlaceReply(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

    def aborted(self, *args, **kwargs): # real signature unknown
        pass

    def contentUpdated(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtLocation.QPlaceReply.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def setError(self, error, errorString): # real signature unknown; restored from __doc__
        """ setError(self, error: PySide2.QtLocation.QPlaceReply.Error, errorString: str) -> None """
        pass

    def setFinished(self, finished): # real signature unknown; restored from __doc__
        """ setFinished(self, finished: bool) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtLocation.QPlaceReply.Type """
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

    BadArgumentError = PySide2.QtLocation.QPlaceReply.Error.BadArgumentError
    CancelError = PySide2.QtLocation.QPlaceReply.Error.CancelError
    CategoryDoesNotExistError = PySide2.QtLocation.QPlaceReply.Error.CategoryDoesNotExistError
    CommunicationError = PySide2.QtLocation.QPlaceReply.Error.CommunicationError
    ContentReply = PySide2.QtLocation.QPlaceReply.Type.ContentReply
    DetailsReply = PySide2.QtLocation.QPlaceReply.Type.DetailsReply
    Error = None # (!) real value is "<class 'PySide2.QtLocation.QPlaceReply.Error'>"
    IdReply = PySide2.QtLocation.QPlaceReply.Type.IdReply
    MatchReply = PySide2.QtLocation.QPlaceReply.Type.MatchReply
    NoError = PySide2.QtLocation.QPlaceReply.Error.NoError
    ParseError = PySide2.QtLocation.QPlaceReply.Error.ParseError
    PermissionsError = PySide2.QtLocation.QPlaceReply.Error.PermissionsError
    PlaceDoesNotExistError = PySide2.QtLocation.QPlaceReply.Error.PlaceDoesNotExistError
    Reply = PySide2.QtLocation.QPlaceReply.Type.Reply
    SearchReply = PySide2.QtLocation.QPlaceReply.Type.SearchReply
    SearchSuggestionReply = PySide2.QtLocation.QPlaceReply.Type.SearchSuggestionReply
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000013BA752E880>'
    Type = None # (!) real value is "<class 'PySide2.QtLocation.QPlaceReply.Type'>"
    UnknownError = PySide2.QtLocation.QPlaceReply.Error.UnknownError
    UnsupportedError = PySide2.QtLocation.QPlaceReply.Error.UnsupportedError


