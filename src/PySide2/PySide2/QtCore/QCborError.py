# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCborError(__Shiboken.Object):
    """
    QCborError(self) -> None
    QCborError(self, QCborError: PySide2.QtCore.QCborError) -> None
    """
    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    c = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    AdvancePastEnd = PySide2.QtCore.QCborError.Code.AdvancePastEnd
    Code = None # (!) real value is "<class 'PySide2.QtCore.QCborError.Code'>"
    DataTooLarge = PySide2.QtCore.QCborError.Code.DataTooLarge
    EndOfFile = PySide2.QtCore.QCborError.Code.EndOfFile
    GarbageAtEnd = PySide2.QtCore.QCborError.Code.GarbageAtEnd
    IllegalNumber = PySide2.QtCore.QCborError.Code.IllegalNumber
    IllegalSimpleType = PySide2.QtCore.QCborError.Code.IllegalSimpleType
    IllegalType = PySide2.QtCore.QCborError.Code.IllegalType
    InputOutputError = PySide2.QtCore.QCborError.Code.InputOutputError
    InvalidUtf8String = PySide2.QtCore.QCborError.Code.InvalidUtf8String
    NestingTooDeep = PySide2.QtCore.QCborError.Code.NestingTooDeep
    NoError = PySide2.QtCore.QCborError.Code.NoError
    UnexpectedBreak = PySide2.QtCore.QCborError.Code.UnexpectedBreak
    UnknownError = PySide2.QtCore.QCborError.Code.UnknownError
    UnknownType = PySide2.QtCore.QCborError.Code.UnknownType
    UnsupportedType = PySide2.QtCore.QCborError.Code.UnsupportedType


