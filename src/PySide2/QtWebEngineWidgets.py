# encoding: utf-8
# module PySide2.QtWebEngineWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWebEngineWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtWidgets as __PySide2_QtWidgets
import Shiboken as __Shiboken


# no functions
# classes

class QWebEngineCertificateError(__Shiboken.Object):
    """
    QWebEngineCertificateError(self, error: int, url: PySide2.QtCore.QUrl, overridable: bool, errorDescription: str) -> None
    QWebEngineCertificateError(self, other: PySide2.QtWebEngineWidgets.QWebEngineCertificateError) -> None
    """
    def answered(self): # real signature unknown; restored from __doc__
        """ answered(self) -> bool """
        return False

    def certificateChain(self): # real signature unknown; restored from __doc__
        """ certificateChain(self) -> typing.List[PySide2.QtNetwork.QSslCertificate] """
        pass

    def defer(self): # real signature unknown; restored from __doc__
        """ defer(self) -> None """
        pass

    def deferred(self): # real signature unknown; restored from __doc__
        """ deferred(self) -> bool """
        return False

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error """
        pass

    def errorDescription(self): # real signature unknown; restored from __doc__
        """ errorDescription(self) -> str """
        return ""

    def ignoreCertificateError(self): # real signature unknown; restored from __doc__
        """ ignoreCertificateError(self) -> None """
        pass

    def isOverridable(self): # real signature unknown; restored from __doc__
        """ isOverridable(self) -> bool """
        return False

    def rejectCertificate(self): # real signature unknown; restored from __doc__
        """ rejectCertificate(self) -> None """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def __init__(self, error, url, overridable, errorDescription): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CertificateAuthorityInvalid = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateAuthorityInvalid
    CertificateCommonNameInvalid = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateCommonNameInvalid
    CertificateContainsErrors = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateContainsErrors
    CertificateDateInvalid = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateDateInvalid
    CertificateInvalid = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateInvalid
    CertificateKnownInterceptionBlocked = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateKnownInterceptionBlocked
    CertificateNameConstraintViolation = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateNameConstraintViolation
    CertificateNonUniqueName = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateNonUniqueName
    CertificateNoRevocationMechanism = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateNoRevocationMechanism
    CertificateRevoked = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateRevoked
    CertificateTransparencyRequired = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateTransparencyRequired
    CertificateUnableToCheckRevocation = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateUnableToCheckRevocation
    CertificateValidityTooLong = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateValidityTooLong
    CertificateWeakKey = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateWeakKey
    CertificateWeakSignatureAlgorithm = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.CertificateWeakSignatureAlgorithm
    Error = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error'>"
    SslPinnedKeyNotInCertificateChain = PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error.SslPinnedKeyNotInCertificateChain


class QWebEngineContextMenuData(__Shiboken.Object):
    """
    QWebEngineContextMenuData(self) -> None
    QWebEngineContextMenuData(self, other: PySide2.QtWebEngineWidgets.QWebEngineContextMenuData) -> None
    """
    def editFlags(self): # real signature unknown; restored from __doc__
        """ editFlags(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlags """
        pass

    def isContentEditable(self): # real signature unknown; restored from __doc__
        """ isContentEditable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def linkText(self): # real signature unknown; restored from __doc__
        """ linkText(self) -> str """
        return ""

    def linkUrl(self): # real signature unknown; restored from __doc__
        """ linkUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def mediaFlags(self): # real signature unknown; restored from __doc__
        """ mediaFlags(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlags """
        pass

    def mediaType(self): # real signature unknown; restored from __doc__
        """ mediaType(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType """
        pass

    def mediaUrl(self): # real signature unknown; restored from __doc__
        """ mediaUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def misspelledWord(self): # real signature unknown; restored from __doc__
        """ misspelledWord(self) -> str """
        return ""

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> PySide2.QtCore.QPoint """
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def spellCheckerSuggestions(self): # real signature unknown; restored from __doc__
        """ spellCheckerSuggestions(self) -> typing.List[str] """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CanCopy = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanCopy
    CanCut = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanCut
    CanDelete = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanDelete
    CanEditRichly = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanEditRichly
    CanPaste = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanPaste
    CanRedo = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanRedo
    CanSelectAll = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanSelectAll
    CanTranslate = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanTranslate
    CanUndo = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag.CanUndo
    EditFlag = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlag'>"
    EditFlags = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlags'>"
    MediaCanPrint = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaCanPrint
    MediaCanRotate = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaCanRotate
    MediaCanSave = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaCanSave
    MediaCanToggleControls = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaCanToggleControls
    MediaControls = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaControls
    MediaFlag = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag'>"
    MediaFlags = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlags'>"
    MediaHasAudio = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaHasAudio
    MediaInError = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaInError
    MediaLoop = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaLoop
    MediaMuted = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaMuted
    MediaPaused = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlag.MediaPaused
    MediaType = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType'>"
    MediaTypeAudio = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType.MediaTypeAudio
    MediaTypeCanvas = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType.MediaTypeCanvas
    MediaTypeFile = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType.MediaTypeFile
    MediaTypeImage = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType.MediaTypeImage
    MediaTypeNone = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType.MediaTypeNone
    MediaTypePlugin = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType.MediaTypePlugin
    MediaTypeVideo = PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType.MediaTypeVideo


class QWebEngineDownloadItem(__PySide2_QtCore.QObject):
    # no doc
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) -> None """
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) -> None """
        pass

    def downloadDirectory(self): # real signature unknown; restored from __doc__
        """ downloadDirectory(self) -> str """
        return ""

    def downloadFileName(self): # real signature unknown; restored from __doc__
        """ downloadFileName(self) -> str """
        return ""

    def downloadProgress(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def interruptReason(self): # real signature unknown; restored from __doc__
        """ interruptReason(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason """
        pass

    def interruptReasonString(self): # real signature unknown; restored from __doc__
        """ interruptReasonString(self) -> str """
        return ""

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isPaused(self): # real signature unknown; restored from __doc__
        """ isPaused(self) -> bool """
        return False

    def isPausedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isSavePageDownload(self): # real signature unknown; restored from __doc__
        """ isSavePageDownload(self) -> bool """
        return False

    def mimeType(self): # real signature unknown; restored from __doc__
        """ mimeType(self) -> str """
        return ""

    def page(self): # real signature unknown; restored from __doc__
        """ page(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) -> None """
        pass

    def receivedBytes(self): # real signature unknown; restored from __doc__
        """ receivedBytes(self) -> int """
        return 0

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def savePageFormat(self): # real signature unknown; restored from __doc__
        """ savePageFormat(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat """
        pass

    def setDownloadDirectory(self, directory): # real signature unknown; restored from __doc__
        """ setDownloadDirectory(self, directory: str) -> None """
        pass

    def setDownloadFileName(self, fileName): # real signature unknown; restored from __doc__
        """ setDownloadFileName(self, fileName: str) -> None """
        pass

    def setPath(self, path): # real signature unknown; restored from __doc__
        """ setPath(self, path: str) -> None """
        pass

    def setSavePageFormat(self, format): # real signature unknown; restored from __doc__
        """ setSavePageFormat(self, format: PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def suggestedFileName(self): # real signature unknown; restored from __doc__
        """ suggestedFileName(self) -> str """
        return ""

    def totalBytes(self): # real signature unknown; restored from __doc__
        """ totalBytes(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Attachment = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType.Attachment
    CompleteHtmlSaveFormat = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat.CompleteHtmlSaveFormat
    DownloadAttribute = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType.DownloadAttribute
    DownloadCancelled = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState.DownloadCancelled
    DownloadCompleted = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState.DownloadCompleted
    DownloadInProgress = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState.DownloadInProgress
    DownloadInterrupted = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState.DownloadInterrupted
    DownloadInterruptReason = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason'>"
    DownloadRequested = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState.DownloadRequested
    DownloadState = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState'>"
    DownloadType = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType'>"
    FileAccessDenied = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileAccessDenied
    FileBlocked = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileBlocked
    FileFailed = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileFailed
    FileHashMismatch = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileHashMismatch
    FileNameTooLong = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileNameTooLong
    FileNoSpace = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileNoSpace
    FileSecurityCheckFailed = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileSecurityCheckFailed
    FileTooLarge = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileTooLarge
    FileTooShort = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileTooShort
    FileTransientError = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileTransientError
    FileVirusInfected = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.FileVirusInfected
    MimeHtmlSaveFormat = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat.MimeHtmlSaveFormat
    NetworkDisconnected = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.NetworkDisconnected
    NetworkFailed = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.NetworkFailed
    NetworkInvalidRequest = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.NetworkInvalidRequest
    NetworkServerDown = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.NetworkServerDown
    NetworkTimeout = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.NetworkTimeout
    NoReason = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.NoReason
    SavePage = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType.SavePage
    SavePageFormat = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat'>"
    ServerBadContent = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.ServerBadContent
    ServerCertProblem = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.ServerCertProblem
    ServerFailed = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.ServerFailed
    ServerForbidden = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.ServerForbidden
    ServerUnauthorized = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.ServerUnauthorized
    ServerUnreachable = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.ServerUnreachable
    SingleHtmlSaveFormat = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat.SingleHtmlSaveFormat
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000020A95464740>'
    UnknownSaveFormat = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat.UnknownSaveFormat
    UserCanceled = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason.UserCanceled
    UserRequested = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType.UserRequested


class QWebEngineFullScreenRequest(__Shiboken.Object):
    # no doc
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) -> None """
        pass

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> PySide2.QtCore.QUrl """
        pass

    def reject(self): # real signature unknown; restored from __doc__
        """ reject(self) -> None """
        pass

    def toggleOn(self): # real signature unknown; restored from __doc__
        """ toggleOn(self) -> bool """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWebEngineHistory(__Shiboken.Object):
    # no doc
    def back(self): # real signature unknown; restored from __doc__
        """ back(self) -> None """
        pass

    def backItem(self): # real signature unknown; restored from __doc__
        """ backItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem """
        pass

    def backItems(self, maxItems): # real signature unknown; restored from __doc__
        """ backItems(self, maxItems: int) -> typing.List[PySide2.QtWebEngineWidgets.QWebEngineHistoryItem] """
        pass

    def canGoBack(self): # real signature unknown; restored from __doc__
        """ canGoBack(self) -> bool """
        return False

    def canGoForward(self): # real signature unknown; restored from __doc__
        """ canGoForward(self) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem """
        pass

    def currentItemIndex(self): # real signature unknown; restored from __doc__
        """ currentItemIndex(self) -> int """
        return 0

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) -> None """
        pass

    def forwardItem(self): # real signature unknown; restored from __doc__
        """ forwardItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem """
        pass

    def forwardItems(self, maxItems): # real signature unknown; restored from __doc__
        """ forwardItems(self, maxItems: int) -> typing.List[PySide2.QtWebEngineWidgets.QWebEngineHistoryItem] """
        pass

    def goToItem(self, item): # real signature unknown; restored from __doc__
        """ goToItem(self, item: PySide2.QtWebEngineWidgets.QWebEngineHistoryItem) -> None """
        pass

    def itemAt(self, i): # real signature unknown; restored from __doc__
        """ itemAt(self, i: int) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem """
        pass

    def items(self): # real signature unknown; restored from __doc__
        """ items(self) -> typing.List[PySide2.QtWebEngineWidgets.QWebEngineHistoryItem] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __lshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __lshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __rshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass


class QWebEngineHistoryItem(__Shiboken.Object):
    """ QWebEngineHistoryItem(self, other: PySide2.QtWebEngineWidgets.QWebEngineHistoryItem) -> None """
    def iconUrl(self): # real signature unknown; restored from __doc__
        """ iconUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastVisited(self): # real signature unknown; restored from __doc__
        """ lastVisited(self) -> PySide2.QtCore.QDateTime """
        pass

    def originalUrl(self): # real signature unknown; restored from __doc__
        """ originalUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtWebEngineWidgets.QWebEngineHistoryItem) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self, other): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWebEnginePage(__PySide2_QtCore.QObject):
    """
    QWebEnginePage(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QWebEnginePage(self, profile: PySide2.QtWebEngineWidgets.QWebEngineProfile, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def acceptNavigationRequest(self, url, type, isMainFrame): # real signature unknown; restored from __doc__
        """ acceptNavigationRequest(self, url: PySide2.QtCore.QUrl, type: PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType, isMainFrame: bool) -> bool """
        return False

    def action(self, action): # real signature unknown; restored from __doc__
        """ action(self, action: PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction) -> PySide2.QtWidgets.QAction """
        pass

    def audioMutedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> PySide2.QtGui.QColor """
        pass

    def certificateError(self, certificateError): # real signature unknown; restored from __doc__
        """ certificateError(self, certificateError: PySide2.QtWebEngineWidgets.QWebEngineCertificateError) -> bool """
        return False

    def chooseFiles(self, mode, oldFiles, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ chooseFiles(self, mode: PySide2.QtWebEngineWidgets.QWebEnginePage.FileSelectionMode, oldFiles: typing.Sequence[str], acceptedMimeTypes: typing.Sequence[str]) -> typing.List[str] """
        pass

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ contentsSize(self) -> PySide2.QtCore.QSizeF """
        pass

    def contentsSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuData(self): # real signature unknown; restored from __doc__
        """ contextMenuData(self) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData """
        pass

    def createStandardContextMenu(self): # real signature unknown; restored from __doc__
        """ createStandardContextMenu(self) -> PySide2.QtWidgets.QMenu """
        pass

    def createWindow(self, type): # real signature unknown; restored from __doc__
        """ createWindow(self, type: PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType) -> PySide2.QtWebEngineWidgets.QWebEnginePage """
        pass

    def devToolsPage(self): # real signature unknown; restored from __doc__
        """ devToolsPage(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage """
        pass

    def download(self, url, filename=''): # real signature unknown; restored from __doc__
        """ download(self, url: PySide2.QtCore.QUrl, filename: str = '') -> None """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def featurePermissionRequestCanceled(self, *args, **kwargs): # real signature unknown
        pass

    def featurePermissionRequested(self, *args, **kwargs): # real signature unknown
        pass

    def findText(self, arg__1, arg__2, arg__3): # real signature unknown; restored from __doc__
        """
        findText(self, arg__1: str, arg__2: PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags, arg__3: object) -> None
        findText(self, subString: str, options: PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags = Default(QWebEnginePage.FindFlags)) -> None
        """
        pass

    def findTextFinished(self, *args, **kwargs): # real signature unknown
        pass

    def fullScreenRequested(self, *args, **kwargs): # real signature unknown
        pass

    def geometryChangeRequested(self, *args, **kwargs): # real signature unknown
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistory """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def iconChanged(self, *args, **kwargs): # real signature unknown
        pass

    def iconUrl(self): # real signature unknown; restored from __doc__
        """ iconUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def iconUrlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def inspectedPage(self): # real signature unknown; restored from __doc__
        """ inspectedPage(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage """
        pass

    def isAudioMuted(self): # real signature unknown; restored from __doc__
        """ isAudioMuted(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def javaScriptAlert(self, securityOrigin, msg): # real signature unknown; restored from __doc__
        """ javaScriptAlert(self, securityOrigin: PySide2.QtCore.QUrl, msg: str) -> None """
        pass

    def javaScriptConfirm(self, securityOrigin, msg): # real signature unknown; restored from __doc__
        """ javaScriptConfirm(self, securityOrigin: PySide2.QtCore.QUrl, msg: str) -> bool """
        return False

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID): # real signature unknown; restored from __doc__
        """ javaScriptConsoleMessage(self, level: PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel, message: str, lineNumber: int, sourceID: str) -> None """
        pass

    def javaScriptPrompt(self, securityOrigin, msg, defaultValue): # real signature unknown; restored from __doc__
        """ javaScriptPrompt(self, securityOrigin: PySide2.QtCore.QUrl, msg: str, defaultValue: str) -> typing.Tuple[bool, str] """
        pass

    def lifecycleState(self): # real signature unknown; restored from __doc__
        """ lifecycleState(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage.LifecycleState """
        pass

    def lifecycleStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def linkHovered(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, request): # real signature unknown; restored from __doc__
        """
        load(self, request: PySide2.QtWebEngineCore.QWebEngineHttpRequest) -> None
        load(self, url: PySide2.QtCore.QUrl) -> None
        """
        pass

    def loadFinished(self, *args, **kwargs): # real signature unknown
        pass

    def loadProgress(self, *args, **kwargs): # real signature unknown
        pass

    def loadStarted(self, *args, **kwargs): # real signature unknown
        pass

    def pdfPrintingFinished(self, *args, **kwargs): # real signature unknown
        pass

    def print(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ print(self, arg__1: PySide2.QtPrintSupport.QPrinter, arg__2: object) -> None """
        pass

    def printRequested(self, *args, **kwargs): # real signature unknown
        pass

    def printToPdf(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        printToPdf(self, arg__1: object, arg__2: PySide2.QtGui.QPageLayout) -> None
        printToPdf(self, filePath: str, layout: PySide2.QtGui.QPageLayout = Instance(QPageLayout(QPageSize(QPageSize.A4), QPageLayout.Portrait, QMarginsF()))) -> None
        """
        pass

    def profile(self): # real signature unknown; restored from __doc__
        """ profile(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile """
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def quotaRequested(self, *args, **kwargs): # real signature unknown
        pass

    def recentlyAudible(self): # real signature unknown; restored from __doc__
        """ recentlyAudible(self) -> bool """
        return False

    def recentlyAudibleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def recommendedState(self): # real signature unknown; restored from __doc__
        """ recommendedState(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage.LifecycleState """
        pass

    def recommendedStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def registerProtocolHandlerRequested(self, *args, **kwargs): # real signature unknown
        pass

    def renderProcessPid(self): # real signature unknown; restored from __doc__
        """ renderProcessPid(self) -> int """
        return 0

    def renderProcessPidChanged(self, *args, **kwargs): # real signature unknown
        pass

    def renderProcessTerminated(self, *args, **kwargs): # real signature unknown
        pass

    def replaceMisspelledWord(self, replacement): # real signature unknown; restored from __doc__
        """ replaceMisspelledWord(self, replacement: str) -> None """
        pass

    def requestedUrl(self): # real signature unknown; restored from __doc__
        """ requestedUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def runJavaScript(self, arg__1, arg__2, arg__3): # real signature unknown; restored from __doc__
        """
        runJavaScript(self, arg__1: str, arg__2: int, arg__3: object) -> None
        runJavaScript(self, scriptSource: str) -> None
        runJavaScript(self, scriptSource: str, worldId: int) -> None
        """
        pass

    def save(self, filePath, format=None): # real signature unknown; restored from __doc__
        """ save(self, filePath: str, format: PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat = PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat.MimeHtmlSaveFormat) -> None """
        pass

    def scripts(self): # real signature unknown; restored from __doc__
        """ scripts(self) -> PySide2.QtWebEngineWidgets.QWebEngineScriptCollection """
        pass

    def scrollPosition(self): # real signature unknown; restored from __doc__
        """ scrollPosition(self) -> PySide2.QtCore.QPointF """
        pass

    def scrollPositionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectClientCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setAudioMuted(self, muted): # real signature unknown; restored from __doc__
        """ setAudioMuted(self, muted: bool) -> None """
        pass

    def setBackgroundColor(self, color): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setContent(self, data, mimeType='', baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContent(self, data: PySide2.QtCore.QByteArray, mimeType: str = '', baseUrl: PySide2.QtCore.QUrl = Default(QUrl)) -> None """
        pass

    def setDevToolsPage(self, page): # real signature unknown; restored from __doc__
        """ setDevToolsPage(self, page: PySide2.QtWebEngineWidgets.QWebEnginePage) -> None """
        pass

    def setFeaturePermission(self, securityOrigin, feature, policy): # real signature unknown; restored from __doc__
        """ setFeaturePermission(self, securityOrigin: PySide2.QtCore.QUrl, feature: PySide2.QtWebEngineWidgets.QWebEnginePage.Feature, policy: PySide2.QtWebEngineWidgets.QWebEnginePage.PermissionPolicy) -> None """
        pass

    def setHtml(self, html, baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHtml(self, html: str, baseUrl: PySide2.QtCore.QUrl = Default(QUrl)) -> None """
        pass

    def setInspectedPage(self, page): # real signature unknown; restored from __doc__
        """ setInspectedPage(self, page: PySide2.QtWebEngineWidgets.QWebEnginePage) -> None """
        pass

    def setLifecycleState(self, state): # real signature unknown; restored from __doc__
        """ setLifecycleState(self, state: PySide2.QtWebEngineWidgets.QWebEnginePage.LifecycleState) -> None """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def setUrlRequestInterceptor(self, interceptor): # real signature unknown; restored from __doc__
        """ setUrlRequestInterceptor(self, interceptor: PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor) -> None """
        pass

    def setView(self, view): # real signature unknown; restored from __doc__
        """ setView(self, view: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def setWebChannel(self, arg__1): # real signature unknown; restored from __doc__
        """
        setWebChannel(self, arg__1: PySide2.QtWebChannel.QWebChannel) -> None
        setWebChannel(self, arg__1: PySide2.QtWebChannel.QWebChannel, worldId: int) -> None
        """
        pass

    def setZoomFactor(self, factor): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, factor: float) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def titleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def toHtml(self, arg__1): # real signature unknown; restored from __doc__
        """ toHtml(self, arg__1: object) -> None """
        pass

    def toPlainText(self, arg__1): # real signature unknown; restored from __doc__
        """ toPlainText(self, arg__1: object) -> None """
        pass

    def triggerAction(self, action, checked=False): # real signature unknown; restored from __doc__
        """ triggerAction(self, action: PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction, checked: bool = False) -> None """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def urlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def view(self): # real signature unknown; restored from __doc__
        """ view(self) -> PySide2.QtWidgets.QWidget """
        pass

    def visibleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def webChannel(self): # real signature unknown; restored from __doc__
        """ webChannel(self) -> PySide2.QtWebChannel.QWebChannel """
        pass

    def windowCloseRequested(self, *args, **kwargs): # real signature unknown
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

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

    AbnormalTerminationStatus = PySide2.QtWebEngineWidgets.QWebEnginePage.RenderProcessTerminationStatus.AbnormalTerminationStatus
    AlignCenter = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.AlignCenter
    AlignJustified = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.AlignJustified
    AlignLeft = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.AlignLeft
    AlignRight = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.AlignRight
    Back = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Back
    Copy = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Copy
    CopyImageToClipboard = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.CopyImageToClipboard
    CopyImageUrlToClipboard = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.CopyImageUrlToClipboard
    CopyLinkToClipboard = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.CopyLinkToClipboard
    CopyMediaUrlToClipboard = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.CopyMediaUrlToClipboard
    CrashedTerminationStatus = PySide2.QtWebEngineWidgets.QWebEnginePage.RenderProcessTerminationStatus.CrashedTerminationStatus
    Cut = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Cut
    DesktopAudioVideoCapture = PySide2.QtWebEngineWidgets.QWebEnginePage.Feature.DesktopAudioVideoCapture
    DesktopVideoCapture = PySide2.QtWebEngineWidgets.QWebEnginePage.Feature.DesktopVideoCapture
    DownloadImageToDisk = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.DownloadImageToDisk
    DownloadLinkToDisk = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.DownloadLinkToDisk
    DownloadMediaToDisk = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.DownloadMediaToDisk
    ErrorMessageLevel = PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel.ErrorMessageLevel
    ExitFullScreen = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ExitFullScreen
    Feature = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.Feature'>"
    FileSelectionMode = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.FileSelectionMode'>"
    FileSelectOpen = PySide2.QtWebEngineWidgets.QWebEnginePage.FileSelectionMode.FileSelectOpen
    FileSelectOpenMultiple = PySide2.QtWebEngineWidgets.QWebEnginePage.FileSelectionMode.FileSelectOpenMultiple
    FindBackward = PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlag.FindBackward
    FindCaseSensitively = PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlag.FindCaseSensitively
    FindFlag = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlag'>"
    FindFlags = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags'>"
    Forward = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Forward
    Geolocation = PySide2.QtWebEngineWidgets.QWebEnginePage.Feature.Geolocation
    Indent = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Indent
    InfoMessageLevel = PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel.InfoMessageLevel
    InsertOrderedList = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.InsertOrderedList
    InsertUnorderedList = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.InsertUnorderedList
    InspectElement = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.InspectElement
    JavaScriptConsoleMessageLevel = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel'>"
    KilledTerminationStatus = PySide2.QtWebEngineWidgets.QWebEnginePage.RenderProcessTerminationStatus.KilledTerminationStatus
    LifecycleState = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.LifecycleState'>"
    MediaAudioCapture = PySide2.QtWebEngineWidgets.QWebEnginePage.Feature.MediaAudioCapture
    MediaAudioVideoCapture = PySide2.QtWebEngineWidgets.QWebEnginePage.Feature.MediaAudioVideoCapture
    MediaVideoCapture = PySide2.QtWebEngineWidgets.QWebEnginePage.Feature.MediaVideoCapture
    MouseLock = PySide2.QtWebEngineWidgets.QWebEnginePage.Feature.MouseLock
    NavigationType = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType'>"
    NavigationTypeBackForward = PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType.NavigationTypeBackForward
    NavigationTypeFormSubmitted = PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType.NavigationTypeFormSubmitted
    NavigationTypeLinkClicked = PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType.NavigationTypeLinkClicked
    NavigationTypeOther = PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType.NavigationTypeOther
    NavigationTypeRedirect = PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType.NavigationTypeRedirect
    NavigationTypeReload = PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType.NavigationTypeReload
    NavigationTypeTyped = PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType.NavigationTypeTyped
    NormalTerminationStatus = PySide2.QtWebEngineWidgets.QWebEnginePage.RenderProcessTerminationStatus.NormalTerminationStatus
    Notifications = PySide2.QtWebEngineWidgets.QWebEnginePage.Feature.Notifications
    NoWebAction = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.NoWebAction
    OpenLinkInNewBackgroundTab = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.OpenLinkInNewBackgroundTab
    OpenLinkInNewTab = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.OpenLinkInNewTab
    OpenLinkInNewWindow = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.OpenLinkInNewWindow
    OpenLinkInThisWindow = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.OpenLinkInThisWindow
    Outdent = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Outdent
    Paste = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Paste
    PasteAndMatchStyle = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.PasteAndMatchStyle
    PermissionDeniedByUser = PySide2.QtWebEngineWidgets.QWebEnginePage.PermissionPolicy.PermissionDeniedByUser
    PermissionGrantedByUser = PySide2.QtWebEngineWidgets.QWebEnginePage.PermissionPolicy.PermissionGrantedByUser
    PermissionPolicy = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.PermissionPolicy'>"
    PermissionUnknown = PySide2.QtWebEngineWidgets.QWebEnginePage.PermissionPolicy.PermissionUnknown
    Redo = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Redo
    Reload = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Reload
    ReloadAndBypassCache = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ReloadAndBypassCache
    RenderProcessTerminationStatus = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.RenderProcessTerminationStatus'>"
    RequestClose = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.RequestClose
    SavePage = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.SavePage
    SelectAll = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.SelectAll
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000020A95466F80>'
    Stop = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Stop
    ToggleBold = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ToggleBold
    ToggleItalic = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ToggleItalic
    ToggleMediaControls = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ToggleMediaControls
    ToggleMediaLoop = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ToggleMediaLoop
    ToggleMediaMute = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ToggleMediaMute
    ToggleMediaPlayPause = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ToggleMediaPlayPause
    ToggleStrikethrough = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ToggleStrikethrough
    ToggleUnderline = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ToggleUnderline
    Undo = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Undo
    Unselect = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.Unselect
    ViewSource = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.ViewSource
    WarningMessageLevel = PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel.WarningMessageLevel
    WebAction = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction'>"
    WebActionCount = PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction.WebActionCount
    WebBrowserBackgroundTab = PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType.WebBrowserBackgroundTab
    WebBrowserTab = PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType.WebBrowserTab
    WebBrowserWindow = PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType.WebBrowserWindow
    WebDialog = PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType.WebDialog
    WebWindowType = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType'>"


class QWebEngineProfile(__PySide2_QtCore.QObject):
    """
    QWebEngineProfile(self, name: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QWebEngineProfile(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def cachePath(self): # real signature unknown; restored from __doc__
        """ cachePath(self) -> str """
        return ""

    def clearAllVisitedLinks(self): # real signature unknown; restored from __doc__
        """ clearAllVisitedLinks(self) -> None """
        pass

    def clearHttpCache(self): # real signature unknown; restored from __doc__
        """ clearHttpCache(self) -> None """
        pass

    def clearVisitedLinks(self, urls, PySide2_QtCore_QUrl=None): # real signature unknown; restored from __doc__
        """ clearVisitedLinks(self, urls: typing.Sequence[PySide2.QtCore.QUrl]) -> None """
        pass

    def cookieStore(self): # real signature unknown; restored from __doc__
        """ cookieStore(self) -> PySide2.QtWebEngineCore.QWebEngineCookieStore """
        pass

    def defaultProfile(self): # real signature unknown; restored from __doc__
        """ defaultProfile() -> PySide2.QtWebEngineWidgets.QWebEngineProfile """
        pass

    def downloadPath(self): # real signature unknown; restored from __doc__
        """ downloadPath(self) -> str """
        return ""

    def downloadRequested(self, *args, **kwargs): # real signature unknown
        pass

    def httpAcceptLanguage(self): # real signature unknown; restored from __doc__
        """ httpAcceptLanguage(self) -> str """
        return ""

    def httpCacheMaximumSize(self): # real signature unknown; restored from __doc__
        """ httpCacheMaximumSize(self) -> int """
        return 0

    def httpCacheType(self): # real signature unknown; restored from __doc__
        """ httpCacheType(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType """
        pass

    def httpUserAgent(self): # real signature unknown; restored from __doc__
        """ httpUserAgent(self) -> str """
        return ""

    def installUrlSchemeHandler(self, scheme, arg__2): # real signature unknown; restored from __doc__
        """ installUrlSchemeHandler(self, scheme: PySide2.QtCore.QByteArray, arg__2: PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler) -> None """
        pass

    def isOffTheRecord(self): # real signature unknown; restored from __doc__
        """ isOffTheRecord(self) -> bool """
        return False

    def isSpellCheckEnabled(self): # real signature unknown; restored from __doc__
        """ isSpellCheckEnabled(self) -> bool """
        return False

    def isUsedForGlobalCertificateVerification(self): # real signature unknown; restored from __doc__
        """ isUsedForGlobalCertificateVerification(self) -> bool """
        return False

    def persistentCookiesPolicy(self): # real signature unknown; restored from __doc__
        """ persistentCookiesPolicy(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy """
        pass

    def persistentStoragePath(self): # real signature unknown; restored from __doc__
        """ persistentStoragePath(self) -> str """
        return ""

    def removeAllUrlSchemeHandlers(self): # real signature unknown; restored from __doc__
        """ removeAllUrlSchemeHandlers(self) -> None """
        pass

    def removeUrlScheme(self, scheme): # real signature unknown; restored from __doc__
        """ removeUrlScheme(self, scheme: PySide2.QtCore.QByteArray) -> None """
        pass

    def removeUrlSchemeHandler(self, arg__1): # real signature unknown; restored from __doc__
        """ removeUrlSchemeHandler(self, arg__1: PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler) -> None """
        pass

    def scripts(self): # real signature unknown; restored from __doc__
        """ scripts(self) -> PySide2.QtWebEngineWidgets.QWebEngineScriptCollection """
        pass

    def setCachePath(self, path): # real signature unknown; restored from __doc__
        """ setCachePath(self, path: str) -> None """
        pass

    def setDownloadPath(self, path): # real signature unknown; restored from __doc__
        """ setDownloadPath(self, path: str) -> None """
        pass

    def setHttpAcceptLanguage(self, httpAcceptLanguage): # real signature unknown; restored from __doc__
        """ setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None """
        pass

    def setHttpCacheMaximumSize(self, maxSize): # real signature unknown; restored from __doc__
        """ setHttpCacheMaximumSize(self, maxSize: int) -> None """
        pass

    def setHttpCacheType(self, arg__1): # real signature unknown; restored from __doc__
        """ setHttpCacheType(self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType) -> None """
        pass

    def setHttpUserAgent(self, userAgent): # real signature unknown; restored from __doc__
        """ setHttpUserAgent(self, userAgent: str) -> None """
        pass

    def setPersistentCookiesPolicy(self, arg__1): # real signature unknown; restored from __doc__
        """ setPersistentCookiesPolicy(self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy) -> None """
        pass

    def setPersistentStoragePath(self, path): # real signature unknown; restored from __doc__
        """ setPersistentStoragePath(self, path: str) -> None """
        pass

    def setRequestInterceptor(self, interceptor): # real signature unknown; restored from __doc__
        """ setRequestInterceptor(self, interceptor: PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor) -> None """
        pass

    def setSpellCheckEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setSpellCheckEnabled(self, enabled: bool) -> None """
        pass

    def setSpellCheckLanguages(self, languages, p_str=None): # real signature unknown; restored from __doc__
        """ setSpellCheckLanguages(self, languages: typing.Sequence[str]) -> None """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings """
        pass

    def setUrlRequestInterceptor(self, interceptor): # real signature unknown; restored from __doc__
        """ setUrlRequestInterceptor(self, interceptor: PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor) -> None """
        pass

    def setUseForGlobalCertificateVerification(self, enabled=True): # real signature unknown; restored from __doc__
        """ setUseForGlobalCertificateVerification(self, enabled: bool = True) -> None """
        pass

    def spellCheckLanguages(self): # real signature unknown; restored from __doc__
        """ spellCheckLanguages(self) -> typing.List[str] """
        pass

    def storageName(self): # real signature unknown; restored from __doc__
        """ storageName(self) -> str """
        return ""

    def urlSchemeHandler(self, arg__1): # real signature unknown; restored from __doc__
        """ urlSchemeHandler(self, arg__1: PySide2.QtCore.QByteArray) -> PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler """
        pass

    def visitedLinksContainsUrl(self, url): # real signature unknown; restored from __doc__
        """ visitedLinksContainsUrl(self, url: PySide2.QtCore.QUrl) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, name, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AllowPersistentCookies = PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies
    DiskHttpCache = PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType.DiskHttpCache
    ForcePersistentCookies = PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
    HttpCacheType = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType'>"
    MemoryHttpCache = PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType.MemoryHttpCache
    NoCache = PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType.NoCache
    NoPersistentCookies = PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy.NoPersistentCookies
    PersistentCookiesPolicy = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000020A95457640>'


class QWebEngineScript(__Shiboken.Object):
    """
    QWebEngineScript(self) -> None
    QWebEngineScript(self, other: PySide2.QtWebEngineWidgets.QWebEngineScript) -> None
    """
    def injectionPoint(self): # real signature unknown; restored from __doc__
        """ injectionPoint(self) -> PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def runsOnSubFrames(self): # real signature unknown; restored from __doc__
        """ runsOnSubFrames(self) -> bool """
        return False

    def setInjectionPoint(self, arg__1): # real signature unknown; restored from __doc__
        """ setInjectionPoint(self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint) -> None """
        pass

    def setName(self, arg__1): # real signature unknown; restored from __doc__
        """ setName(self, arg__1: str) -> None """
        pass

    def setRunsOnSubFrames(self, on): # real signature unknown; restored from __doc__
        """ setRunsOnSubFrames(self, on: bool) -> None """
        pass

    def setSourceCode(self, arg__1): # real signature unknown; restored from __doc__
        """ setSourceCode(self, arg__1: str) -> None """
        pass

    def setWorldId(self, arg__1): # real signature unknown; restored from __doc__
        """ setWorldId(self, arg__1: int) -> None """
        pass

    def sourceCode(self): # real signature unknown; restored from __doc__
        """ sourceCode(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtWebEngineWidgets.QWebEngineScript) -> None """
        pass

    def worldId(self): # real signature unknown; restored from __doc__
        """ worldId(self) -> int """
        return 0

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    ApplicationWorld = PySide2.QtWebEngineWidgets.QWebEngineScript.ScriptWorldId.ApplicationWorld
    Deferred = PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint.Deferred
    DocumentCreation = PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint.DocumentCreation
    DocumentReady = PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint.DocumentReady
    InjectionPoint = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint'>"
    MainWorld = PySide2.QtWebEngineWidgets.QWebEngineScript.ScriptWorldId.MainWorld
    ScriptWorldId = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineScript.ScriptWorldId'>"
    UserWorld = PySide2.QtWebEngineWidgets.QWebEngineScript.ScriptWorldId.UserWorld
    __hash__ = None


class QWebEngineScriptCollection(__Shiboken.Object):
    # no doc
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def contains(self, value): # real signature unknown; restored from __doc__
        """ contains(self, value: PySide2.QtWebEngineWidgets.QWebEngineScript) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def findScript(self, name): # real signature unknown; restored from __doc__
        """ findScript(self, name: str) -> PySide2.QtWebEngineWidgets.QWebEngineScript """
        pass

    def findScripts(self, name): # real signature unknown; restored from __doc__
        """ findScripts(self, name: str) -> typing.List[PySide2.QtWebEngineWidgets.QWebEngineScript] """
        pass

    def insert(self, arg__1): # real signature unknown; restored from __doc__
        """
        insert(self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineScript) -> None
        insert(self, list: typing.Sequence[PySide2.QtWebEngineWidgets.QWebEngineScript]) -> None
        """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def remove(self, arg__1): # real signature unknown; restored from __doc__
        """ remove(self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineScript) -> bool """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def toList(self): # real signature unknown; restored from __doc__
        """ toList(self) -> typing.List[PySide2.QtWebEngineWidgets.QWebEngineScript] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWebEngineSettings(__Shiboken.Object):
    # no doc
    def defaultSettings(self): # real signature unknown; restored from __doc__
        """ defaultSettings() -> PySide2.QtWebEngineWidgets.QWebEngineSettings """
        pass

    def defaultTextEncoding(self): # real signature unknown; restored from __doc__
        """ defaultTextEncoding(self) -> str """
        return ""

    def fontFamily(self, which): # real signature unknown; restored from __doc__
        """ fontFamily(self, which: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily) -> str """
        return ""

    def fontSize(self, type): # real signature unknown; restored from __doc__
        """ fontSize(self, type: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize) -> int """
        return 0

    def globalSettings(self): # real signature unknown; restored from __doc__
        """ globalSettings() -> PySide2.QtWebEngineWidgets.QWebEngineSettings """
        pass

    def resetAttribute(self, attr): # real signature unknown; restored from __doc__
        """ resetAttribute(self, attr: PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute) -> None """
        pass

    def resetFontFamily(self, which): # real signature unknown; restored from __doc__
        """ resetFontFamily(self, which: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily) -> None """
        pass

    def resetFontSize(self, type): # real signature unknown; restored from __doc__
        """ resetFontSize(self, type: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize) -> None """
        pass

    def resetUnknownUrlSchemePolicy(self): # real signature unknown; restored from __doc__
        """ resetUnknownUrlSchemePolicy(self) -> None """
        pass

    def setAttribute(self, attr, on): # real signature unknown; restored from __doc__
        """ setAttribute(self, attr: PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute, on: bool) -> None """
        pass

    def setDefaultTextEncoding(self, encoding): # real signature unknown; restored from __doc__
        """ setDefaultTextEncoding(self, encoding: str) -> None """
        pass

    def setFontFamily(self, which, family): # real signature unknown; restored from __doc__
        """ setFontFamily(self, which: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily, family: str) -> None """
        pass

    def setFontSize(self, type, size): # real signature unknown; restored from __doc__
        """ setFontSize(self, type: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize, size: int) -> None """
        pass

    def setUnknownUrlSchemePolicy(self, policy): # real signature unknown; restored from __doc__
        """ setUnknownUrlSchemePolicy(self, policy: PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy) -> None """
        pass

    def testAttribute(self, attr): # real signature unknown; restored from __doc__
        """ testAttribute(self, attr: PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute) -> bool """
        return False

    def unknownUrlSchemePolicy(self): # real signature unknown; restored from __doc__
        """ unknownUrlSchemePolicy(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Accelerated2dCanvasEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.Accelerated2dCanvasEnabled
    AllowAllUnknownUrlSchemes = PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy.AllowAllUnknownUrlSchemes
    AllowGeolocationOnInsecureOrigins = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.AllowGeolocationOnInsecureOrigins
    AllowRunningInsecureContent = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.AllowRunningInsecureContent
    AllowUnknownUrlSchemesFromUserInteraction = PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy.AllowUnknownUrlSchemesFromUserInteraction
    AllowWindowActivationFromJavaScript = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.AllowWindowActivationFromJavaScript
    AutoLoadIconsForPage = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.AutoLoadIconsForPage
    AutoLoadImages = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.AutoLoadImages
    CursiveFont = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily.CursiveFont
    DefaultFixedFontSize = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize.DefaultFixedFontSize
    DefaultFontSize = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize.DefaultFontSize
    DisallowUnknownUrlSchemes = PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy.DisallowUnknownUrlSchemes
    DnsPrefetchEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.DnsPrefetchEnabled
    ErrorPageEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.ErrorPageEnabled
    FantasyFont = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily.FantasyFont
    FixedFont = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily.FixedFont
    FocusOnNavigationEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.FocusOnNavigationEnabled
    FontFamily = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily'>"
    FontSize = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize'>"
    FullScreenSupportEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.FullScreenSupportEnabled
    HyperlinkAuditingEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.HyperlinkAuditingEnabled
    JavascriptCanAccessClipboard = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.JavascriptCanAccessClipboard
    JavascriptCanOpenWindows = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.JavascriptCanOpenWindows
    JavascriptCanPaste = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.JavascriptCanPaste
    JavascriptEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.JavascriptEnabled
    LinksIncludedInFocusChain = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.LinksIncludedInFocusChain
    LocalContentCanAccessFileUrls = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls
    LocalContentCanAccessRemoteUrls = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls
    LocalStorageEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.LocalStorageEnabled
    MinimumFontSize = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize.MinimumFontSize
    MinimumLogicalFontSize = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize.MinimumLogicalFontSize
    PdfViewerEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.PdfViewerEnabled
    PictographFont = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily.PictographFont
    PlaybackRequiresUserGesture = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.PlaybackRequiresUserGesture
    PluginsEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.PluginsEnabled
    PrintElementBackgrounds = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.PrintElementBackgrounds
    SansSerifFont = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily.SansSerifFont
    ScreenCaptureEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.ScreenCaptureEnabled
    ScrollAnimatorEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.ScrollAnimatorEnabled
    SerifFont = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily.SerifFont
    ShowScrollBars = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.ShowScrollBars
    SpatialNavigationEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.SpatialNavigationEnabled
    StandardFont = PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily.StandardFont
    TouchIconsEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.TouchIconsEnabled
    UnknownUrlSchemePolicy = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy'>"
    WebAttribute = None # (!) real value is "<class 'PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute'>"
    WebGLEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.WebGLEnabled
    WebRTCPublicInterfacesOnly = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.WebRTCPublicInterfacesOnly
    XSSAuditingEnabled = PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute.XSSAuditingEnabled


class QWebEngineView(__PySide2_QtWidgets.QWidget):
    """ QWebEngineView(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def back(self): # real signature unknown; restored from __doc__
        """ back(self) -> None """
        pass

    def closeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ closeEvent(self, arg__1: PySide2.QtGui.QCloseEvent) -> None """
        pass

    def contextMenuEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, arg__1: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def createWindow(self, type): # real signature unknown; restored from __doc__
        """ createWindow(self, type: PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType) -> PySide2.QtWebEngineWidgets.QWebEngineView """
        pass

    def dragEnterEvent(self, e): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, e: PySide2.QtGui.QDragEnterEvent) -> None """
        pass

    def dragLeaveEvent(self, e): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, e: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMoveEvent(self, e): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, e: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def dropEvent(self, e): # real signature unknown; restored from __doc__
        """ dropEvent(self, e: PySide2.QtGui.QDropEvent) -> None """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def findText(self, arg__1, arg__2, arg__3): # real signature unknown; restored from __doc__
        """
        findText(self, arg__1: str, arg__2: PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags, arg__3: object) -> None
        findText(self, subString: str, options: PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags = Default(QWebEnginePage.FindFlags)) -> None
        """
        pass

    def forward(self): # real signature unknown; restored from __doc__
        """ forward(self) -> None """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def hideEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None """
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistory """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def iconChanged(self, *args, **kwargs): # real signature unknown
        pass

    def iconUrl(self): # real signature unknown; restored from __doc__
        """ iconUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def iconUrlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, request): # real signature unknown; restored from __doc__
        """
        load(self, request: PySide2.QtWebEngineCore.QWebEngineHttpRequest) -> None
        load(self, url: PySide2.QtCore.QUrl) -> None
        """
        pass

    def loadFinished(self, *args, **kwargs): # real signature unknown
        pass

    def loadProgress(self, *args, **kwargs): # real signature unknown
        pass

    def loadStarted(self, *args, **kwargs): # real signature unknown
        pass

    def page(self): # real signature unknown; restored from __doc__
        """ page(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage """
        pass

    def pageAction(self, action): # real signature unknown; restored from __doc__
        """ pageAction(self, action: PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction) -> PySide2.QtWidgets.QAction """
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ reload(self) -> None """
        pass

    def renderProcessTerminated(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self): # real signature unknown; restored from __doc__
        """ selectedText(self) -> str """
        return ""

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setContent(self, data, mimeType='', baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setContent(self, data: PySide2.QtCore.QByteArray, mimeType: str = '', baseUrl: PySide2.QtCore.QUrl = Default(QUrl)) -> None """
        pass

    def setHtml(self, html, baseUrl=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setHtml(self, html: str, baseUrl: PySide2.QtCore.QUrl = Default(QUrl)) -> None """
        pass

    def setPage(self, page): # real signature unknown; restored from __doc__
        """ setPage(self, page: PySide2.QtWebEngineWidgets.QWebEnginePage) -> None """
        pass

    def settings(self): # real signature unknown; restored from __doc__
        """ settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings """
        pass

    def setUrl(self, url): # real signature unknown; restored from __doc__
        """ setUrl(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def setZoomFactor(self, factor): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, factor: float) -> None """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def titleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def triggerPageAction(self, action, checked=False): # real signature unknown; restored from __doc__
        """ triggerPageAction(self, action: PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction, checked: bool = False) -> None """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def urlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000020A95464B40>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020A938C17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtWebEngineWidgets', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020A938C17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtWebEngineWidgets.cp310-win_amd64.pyd')"

