# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QUrl(__Shiboken.Object):
    """
    QUrl(self) -> None
    QUrl(self, copy: PySide2.QtCore.QUrl) -> None
    QUrl(self, url: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode) -> None
    """
    def adjusted(self, options): # real signature unknown; restored from __doc__
        """ adjusted(self, options: PySide2.QtCore.QUrl.FormattingOptions) -> PySide2.QtCore.QUrl """
        pass

    def authority(self, options=None): # real signature unknown; restored from __doc__
        """ authority(self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> str """
        return ""

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self, options=None): # real signature unknown; restored from __doc__
        """ fileName(self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyDecoded) -> str """
        return ""

    def fragment(self, options=None): # real signature unknown; restored from __doc__
        """ fragment(self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> str """
        return ""

    def fromAce(self, arg__1): # real signature unknown; restored from __doc__
        """ fromAce(arg__1: PySide2.QtCore.QByteArray) -> str """
        return ""

    def fromEncoded(self, url, mode=None): # real signature unknown; restored from __doc__
        """ fromEncoded(url: PySide2.QtCore.QByteArray, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode) -> PySide2.QtCore.QUrl """
        pass

    def fromLocalFile(self, localfile): # real signature unknown; restored from __doc__
        """ fromLocalFile(localfile: str) -> PySide2.QtCore.QUrl """
        pass

    def fromPercentEncoding(self, arg__1): # real signature unknown; restored from __doc__
        """ fromPercentEncoding(arg__1: PySide2.QtCore.QByteArray) -> str """
        return ""

    def fromStringList(self, uris, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromStringList(uris: typing.Sequence[str], mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode) -> typing.List[PySide2.QtCore.QUrl] """
        pass

    def fromUserInput(self, userInput): # real signature unknown; restored from __doc__
        """
        fromUserInput(userInput: str) -> PySide2.QtCore.QUrl
        fromUserInput(userInput: str, workingDirectory: str, options: PySide2.QtCore.QUrl.UserInputResolutionOptions = PySide2.QtCore.QUrl.UserInputResolutionOption.DefaultResolution) -> PySide2.QtCore.QUrl
        """
        pass

    def hasFragment(self): # real signature unknown; restored from __doc__
        """ hasFragment(self) -> bool """
        return False

    def hasQuery(self): # real signature unknown; restored from __doc__
        """ hasQuery(self) -> bool """
        return False

    def host(self, arg__1=None): # real signature unknown; restored from __doc__
        """ host(self, arg__1: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyDecoded) -> str """
        return ""

    def idnWhitelist(self): # real signature unknown; restored from __doc__
        """ idnWhitelist() -> typing.List[str] """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isLocalFile(self): # real signature unknown; restored from __doc__
        """ isLocalFile(self) -> bool """
        return False

    def isParentOf(self, url): # real signature unknown; restored from __doc__
        """ isParentOf(self, url: PySide2.QtCore.QUrl) -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ isRelative(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def matches(self, url, options): # real signature unknown; restored from __doc__
        """ matches(self, url: PySide2.QtCore.QUrl, options: PySide2.QtCore.QUrl.FormattingOptions) -> bool """
        return False

    def password(self, arg__1=None): # real signature unknown; restored from __doc__
        """ password(self, arg__1: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyDecoded) -> str """
        return ""

    def path(self, options=None): # real signature unknown; restored from __doc__
        """ path(self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyDecoded) -> str """
        return ""

    def port(self, defaultPort=-1): # real signature unknown; restored from __doc__
        """ port(self, defaultPort: int = -1) -> int """
        return 0

    def query(self, arg__1=None): # real signature unknown; restored from __doc__
        """ query(self, arg__1: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> str """
        return ""

    def resolved(self, relative): # real signature unknown; restored from __doc__
        """ resolved(self, relative: PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl """
        pass

    def scheme(self): # real signature unknown; restored from __doc__
        """ scheme(self) -> str """
        return ""

    def setAuthority(self, authority, mode=None): # real signature unknown; restored from __doc__
        """ setAuthority(self, authority: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode) -> None """
        pass

    def setFragment(self, fragment, mode=None): # real signature unknown; restored from __doc__
        """ setFragment(self, fragment: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode) -> None """
        pass

    def setHost(self, host, mode=None): # real signature unknown; restored from __doc__
        """ setHost(self, host: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.DecodedMode) -> None """
        pass

    def setIdnWhitelist(self, arg__1, p_str=None): # real signature unknown; restored from __doc__
        """ setIdnWhitelist(arg__1: typing.Sequence[str]) -> None """
        pass

    def setPassword(self, password, mode=None): # real signature unknown; restored from __doc__
        """ setPassword(self, password: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.DecodedMode) -> None """
        pass

    def setPath(self, path, mode=None): # real signature unknown; restored from __doc__
        """ setPath(self, path: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.DecodedMode) -> None """
        pass

    def setPort(self, port): # real signature unknown; restored from __doc__
        """ setPort(self, port: int) -> None """
        pass

    def setQuery(self, query): # real signature unknown; restored from __doc__
        """
        setQuery(self, query: PySide2.QtCore.QUrlQuery) -> None
        setQuery(self, query: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode) -> None
        """
        pass

    def setScheme(self, scheme): # real signature unknown; restored from __doc__
        """ setScheme(self, scheme: str) -> None """
        pass

    def setUrl(self, url, mode=None): # real signature unknown; restored from __doc__
        """ setUrl(self, url: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode) -> None """
        pass

    def setUserInfo(self, userInfo, mode=None): # real signature unknown; restored from __doc__
        """ setUserInfo(self, userInfo: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode) -> None """
        pass

    def setUserName(self, userName, mode=None): # real signature unknown; restored from __doc__
        """ setUserName(self, userName: str, mode: PySide2.QtCore.QUrl.ParsingMode = PySide2.QtCore.QUrl.ParsingMode.DecodedMode) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QUrl) -> None """
        pass

    def toAce(self, arg__1): # real signature unknown; restored from __doc__
        """ toAce(arg__1: str) -> PySide2.QtCore.QByteArray """
        pass

    def toDisplayString(self, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toDisplayString(self, options: PySide2.QtCore.QUrl.FormattingOptions = Instance(QUrl.FormattingOptions(QUrl.PrettyDecoded))) -> str """
        pass

    def toEncoded(self, options=None): # real signature unknown; restored from __doc__
        """ toEncoded(self, options: PySide2.QtCore.QUrl.FormattingOptions = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyEncoded) -> PySide2.QtCore.QByteArray """
        pass

    def toLocalFile(self): # real signature unknown; restored from __doc__
        """ toLocalFile(self) -> str """
        return ""

    def toPercentEncoding(self, arg__1, exclude=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toPercentEncoding(arg__1: str, exclude: PySide2.QtCore.QByteArray = Default(QByteArray), include: PySide2.QtCore.QByteArray = Default(QByteArray)) -> PySide2.QtCore.QByteArray """
        pass

    def topLevelDomain(self, options=None): # real signature unknown; restored from __doc__
        """ topLevelDomain(self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyDecoded) -> str """
        return ""

    def toString(self, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toString(self, options: PySide2.QtCore.QUrl.FormattingOptions = Instance(QUrl.FormattingOptions(QUrl.PrettyDecoded))) -> str """
        pass

    def toStringList(self, uris, PySide2_QtCore_QUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ toStringList(uris: typing.Sequence[PySide2.QtCore.QUrl], options: PySide2.QtCore.QUrl.FormattingOptions = Instance(QUrl.FormattingOptions(QUrl.PrettyDecoded))) -> typing.List[str] """
        pass

    def url(self, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ url(self, options: PySide2.QtCore.QUrl.FormattingOptions = Instance(QUrl.FormattingOptions(QUrl.PrettyDecoded))) -> str """
        pass

    def userInfo(self, options=None): # real signature unknown; restored from __doc__
        """ userInfo(self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded) -> str """
        return ""

    def userName(self, options=None): # real signature unknown; restored from __doc__
        """ userName(self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyDecoded) -> str """
        return ""

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__(self) -> object """
        return object()

    def __repr__(self): # real signature unknown; restored from __doc__
        """
        __repr__(self) -> object
        
        Return repr(self).
        """
        return object()

    AssumeLocalFile = PySide2.QtCore.QUrl.UserInputResolutionOption.AssumeLocalFile
    ComponentFormattingOption = None # (!) real value is "<class 'PySide2.QtCore.QUrl.ComponentFormattingOption'>"
    DecodedMode = PySide2.QtCore.QUrl.ParsingMode.DecodedMode
    DecodeReserved = PySide2.QtCore.QUrl.ComponentFormattingOption.DecodeReserved
    DefaultResolution = PySide2.QtCore.QUrl.UserInputResolutionOption.DefaultResolution
    EncodeDelimiters = PySide2.QtCore.QUrl.ComponentFormattingOption.EncodeDelimiters
    EncodeReserved = PySide2.QtCore.QUrl.ComponentFormattingOption.EncodeReserved
    EncodeSpaces = PySide2.QtCore.QUrl.ComponentFormattingOption.EncodeSpaces
    EncodeUnicode = PySide2.QtCore.QUrl.ComponentFormattingOption.EncodeUnicode
    FormattingOptions = None # (!) real value is "<class 'PySide2.QtCore.QUrl.FormattingOptions'>"
    FullyDecoded = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyDecoded
    FullyEncoded = PySide2.QtCore.QUrl.ComponentFormattingOption.FullyEncoded
    None_ = PySide2.QtCore.QUrl.UrlFormattingOption.None_
    NormalizePathSegments = PySide2.QtCore.QUrl.UrlFormattingOption.NormalizePathSegments
    ParsingMode = None # (!) real value is "<class 'PySide2.QtCore.QUrl.ParsingMode'>"
    PreferLocalFile = PySide2.QtCore.QUrl.UrlFormattingOption.PreferLocalFile
    PrettyDecoded = PySide2.QtCore.QUrl.ComponentFormattingOption.PrettyDecoded
    RemoveAuthority = PySide2.QtCore.QUrl.UrlFormattingOption.RemoveAuthority
    RemoveFilename = PySide2.QtCore.QUrl.UrlFormattingOption.RemoveFilename
    RemoveFragment = PySide2.QtCore.QUrl.UrlFormattingOption.RemoveFragment
    RemovePassword = PySide2.QtCore.QUrl.UrlFormattingOption.RemovePassword
    RemovePath = PySide2.QtCore.QUrl.UrlFormattingOption.RemovePath
    RemovePort = PySide2.QtCore.QUrl.UrlFormattingOption.RemovePort
    RemoveQuery = PySide2.QtCore.QUrl.UrlFormattingOption.RemoveQuery
    RemoveScheme = PySide2.QtCore.QUrl.UrlFormattingOption.RemoveScheme
    RemoveUserInfo = PySide2.QtCore.QUrl.UrlFormattingOption.RemoveUserInfo
    StrictMode = PySide2.QtCore.QUrl.ParsingMode.StrictMode
    StripTrailingSlash = PySide2.QtCore.QUrl.UrlFormattingOption.StripTrailingSlash
    TolerantMode = PySide2.QtCore.QUrl.ParsingMode.TolerantMode
    UrlFormattingOption = None # (!) real value is "<class 'PySide2.QtCore.QUrl.UrlFormattingOption'>"
    UserInputResolutionOption = None # (!) real value is "<class 'PySide2.QtCore.QUrl.UserInputResolutionOption'>"
    UserInputResolutionOptions = None # (!) real value is "<class 'PySide2.QtCore.QUrl.UserInputResolutionOptions'>"


