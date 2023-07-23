# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCommandLineParser(__Shiboken.Object):
    """ QCommandLineParser(self) -> None """
    def addHelpOption(self): # real signature unknown; restored from __doc__
        """ addHelpOption(self) -> PySide2.QtCore.QCommandLineOption """
        pass

    def addOption(self, commandLineOption): # real signature unknown; restored from __doc__
        """ addOption(self, commandLineOption: PySide2.QtCore.QCommandLineOption) -> bool """
        return False

    def addOptions(self, options, PySide2_QtCore_QCommandLineOption=None): # real signature unknown; restored from __doc__
        """ addOptions(self, options: typing.Sequence[PySide2.QtCore.QCommandLineOption]) -> bool """
        return False

    def addPositionalArgument(self, name, description, syntax=''): # real signature unknown; restored from __doc__
        """ addPositionalArgument(self, name: str, description: str, syntax: str = '') -> None """
        pass

    def addVersionOption(self): # real signature unknown; restored from __doc__
        """ addVersionOption(self) -> PySide2.QtCore.QCommandLineOption """
        pass

    def applicationDescription(self): # real signature unknown; restored from __doc__
        """ applicationDescription(self) -> str """
        return ""

    def clearPositionalArguments(self): # real signature unknown; restored from __doc__
        """ clearPositionalArguments(self) -> None """
        pass

    def errorText(self): # real signature unknown; restored from __doc__
        """ errorText(self) -> str """
        return ""

    def helpText(self): # real signature unknown; restored from __doc__
        """ helpText(self) -> str """
        return ""

    def isSet(self, name): # real signature unknown; restored from __doc__
        """
        isSet(self, name: str) -> bool
        isSet(self, option: PySide2.QtCore.QCommandLineOption) -> bool
        """
        return False

    def optionNames(self): # real signature unknown; restored from __doc__
        """ optionNames(self) -> typing.List[str] """
        pass

    def parse(self, arguments, p_str=None): # real signature unknown; restored from __doc__
        """ parse(self, arguments: typing.Sequence[str]) -> bool """
        return False

    def positionalArguments(self): # real signature unknown; restored from __doc__
        """ positionalArguments(self) -> typing.List[str] """
        pass

    def process(self, app): # real signature unknown; restored from __doc__
        """
        process(self, app: PySide2.QtCore.QCoreApplication) -> None
        process(self, arguments: typing.Sequence[str]) -> None
        """
        pass

    def setApplicationDescription(self, description): # real signature unknown; restored from __doc__
        """ setApplicationDescription(self, description: str) -> None """
        pass

    def setOptionsAfterPositionalArgumentsMode(self, mode): # real signature unknown; restored from __doc__
        """ setOptionsAfterPositionalArgumentsMode(self, mode: PySide2.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode) -> None """
        pass

    def setSingleDashWordOptionMode(self, parsingMode): # real signature unknown; restored from __doc__
        """ setSingleDashWordOptionMode(self, parsingMode: PySide2.QtCore.QCommandLineParser.SingleDashWordOptionMode) -> None """
        pass

    def showHelp(self, exitCode=0): # real signature unknown; restored from __doc__
        """ showHelp(self, exitCode: int = 0) -> None """
        pass

    def showVersion(self): # real signature unknown; restored from __doc__
        """ showVersion(self) -> None """
        pass

    def unknownOptionNames(self): # real signature unknown; restored from __doc__
        """ unknownOptionNames(self) -> typing.List[str] """
        pass

    def value(self, name): # real signature unknown; restored from __doc__
        """
        value(self, name: str) -> str
        value(self, option: PySide2.QtCore.QCommandLineOption) -> str
        """
        return ""

    def values(self, name): # real signature unknown; restored from __doc__
        """
        values(self, name: str) -> typing.List[str]
        values(self, option: PySide2.QtCore.QCommandLineOption) -> typing.List[str]
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    OptionsAfterPositionalArgumentsMode = None # (!) real value is "<class 'PySide2.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode'>"
    ParseAsCompactedShortOptions = PySide2.QtCore.QCommandLineParser.SingleDashWordOptionMode.ParseAsCompactedShortOptions
    ParseAsLongOptions = PySide2.QtCore.QCommandLineParser.SingleDashWordOptionMode.ParseAsLongOptions
    ParseAsOptions = PySide2.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode.ParseAsOptions
    ParseAsPositionalArguments = PySide2.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode.ParseAsPositionalArguments
    SingleDashWordOptionMode = None # (!) real value is "<class 'PySide2.QtCore.QCommandLineParser.SingleDashWordOptionMode'>"


