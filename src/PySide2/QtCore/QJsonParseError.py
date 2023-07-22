# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QJsonParseError(__Shiboken.Object):
    """
    QJsonParseError(self) -> None
    QJsonParseError(self, QJsonParseError: PySide2.QtCore.QJsonParseError) -> None
    """
    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
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

    error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DeepNesting = PySide2.QtCore.QJsonParseError.ParseError.DeepNesting
    DocumentTooLarge = PySide2.QtCore.QJsonParseError.ParseError.DocumentTooLarge
    GarbageAtEnd = PySide2.QtCore.QJsonParseError.ParseError.GarbageAtEnd
    IllegalEscapeSequence = PySide2.QtCore.QJsonParseError.ParseError.IllegalEscapeSequence
    IllegalNumber = PySide2.QtCore.QJsonParseError.ParseError.IllegalNumber
    IllegalUTF8String = PySide2.QtCore.QJsonParseError.ParseError.IllegalUTF8String
    IllegalValue = PySide2.QtCore.QJsonParseError.ParseError.IllegalValue
    MissingNameSeparator = PySide2.QtCore.QJsonParseError.ParseError.MissingNameSeparator
    MissingObject = PySide2.QtCore.QJsonParseError.ParseError.MissingObject
    MissingValueSeparator = PySide2.QtCore.QJsonParseError.ParseError.MissingValueSeparator
    NoError = PySide2.QtCore.QJsonParseError.ParseError.NoError
    ParseError = None # (!) real value is "<class 'PySide2.QtCore.QJsonParseError.ParseError'>"
    TerminationByNumber = PySide2.QtCore.QJsonParseError.ParseError.TerminationByNumber
    UnterminatedArray = PySide2.QtCore.QJsonParseError.ParseError.UnterminatedArray
    UnterminatedObject = PySide2.QtCore.QJsonParseError.ParseError.UnterminatedObject
    UnterminatedString = PySide2.QtCore.QJsonParseError.ParseError.UnterminatedString


