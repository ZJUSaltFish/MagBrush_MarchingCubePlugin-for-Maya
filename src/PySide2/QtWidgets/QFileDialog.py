# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QDialog import QDialog

class QFileDialog(QDialog):
    """
    QFileDialog(self, parent: PySide2.QtWidgets.QWidget, f: PySide2.QtCore.Qt.WindowFlags) -> None
    QFileDialog(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', directory: str = '', filter: str = '') -> None
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) -> None """
        pass

    def acceptMode(self): # real signature unknown; restored from __doc__
        """ acceptMode(self) -> PySide2.QtWidgets.QFileDialog.AcceptMode """
        pass

    def changeEvent(self, e): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: PySide2.QtCore.QEvent) -> None """
        pass

    def confirmOverwrite(self): # real signature unknown; restored from __doc__
        """ confirmOverwrite(self) -> bool """
        return False

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentUrlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def defaultSuffix(self): # real signature unknown; restored from __doc__
        """ defaultSuffix(self) -> str """
        return ""

    def directory(self): # real signature unknown; restored from __doc__
        """ directory(self) -> PySide2.QtCore.QDir """
        pass

    def directoryEntered(self, *args, **kwargs): # real signature unknown
        pass

    def directoryUrl(self): # real signature unknown; restored from __doc__
        """ directoryUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def directoryUrlEntered(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) -> None """
        pass

    def fileMode(self): # real signature unknown; restored from __doc__
        """ fileMode(self) -> PySide2.QtWidgets.QFileDialog.FileMode """
        pass

    def fileSelected(self, *args, **kwargs): # real signature unknown
        pass

    def filesSelected(self, *args, **kwargs): # real signature unknown
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> PySide2.QtCore.QDir.Filters """
        pass

    def filterSelected(self, *args, **kwargs): # real signature unknown
        pass

    def getExistingDirectory(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getExistingDirectory(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', dir: str = '', options: PySide2.QtWidgets.QFileDialog.Options = PySide2.QtWidgets.QFileDialog.Option.ShowDirsOnly) -> str """
        pass

    def getExistingDirectoryUrl(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getExistingDirectoryUrl(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', dir: PySide2.QtCore.QUrl = Default(QUrl), options: PySide2.QtWidgets.QFileDialog.Options = PySide2.QtWidgets.QFileDialog.Option.ShowDirsOnly, supportedSchemes: typing.Sequence[str] = []) -> PySide2.QtCore.QUrl """
        pass

    def getOpenFileName(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileName(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', dir: str = '', filter: str = '', options: PySide2.QtWidgets.QFileDialog.Options = Default(QFileDialog.Options)) -> typing.Tuple[str, str] """
        pass

    def getOpenFileNames(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileNames(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', dir: str = '', filter: str = '', options: PySide2.QtWidgets.QFileDialog.Options = Default(QFileDialog.Options)) -> typing.Tuple[typing.List[str], str] """
        pass

    def getOpenFileUrl(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileUrl(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', dir: PySide2.QtCore.QUrl = Default(QUrl), filter: str = '', options: PySide2.QtWidgets.QFileDialog.Options = Default(QFileDialog.Options), supportedSchemes: typing.Sequence[str] = []) -> typing.Tuple[PySide2.QtCore.QUrl, str] """
        pass

    def getOpenFileUrls(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileUrls(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', dir: PySide2.QtCore.QUrl = Default(QUrl), filter: str = '', options: PySide2.QtWidgets.QFileDialog.Options = Default(QFileDialog.Options), supportedSchemes: typing.Sequence[str] = []) -> typing.Tuple[typing.List[PySide2.QtCore.QUrl], str] """
        pass

    def getSaveFileName(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getSaveFileName(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', dir: str = '', filter: str = '', options: PySide2.QtWidgets.QFileDialog.Options = Default(QFileDialog.Options)) -> typing.Tuple[str, str] """
        pass

    def getSaveFileUrl(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getSaveFileUrl(parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, caption: str = '', dir: PySide2.QtCore.QUrl = Default(QUrl), filter: str = '', options: PySide2.QtWidgets.QFileDialog.Options = Default(QFileDialog.Options), supportedSchemes: typing.Sequence[str] = []) -> typing.Tuple[PySide2.QtCore.QUrl, str] """
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> typing.List[str] """
        pass

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ iconProvider(self) -> PySide2.QtWidgets.QFileIconProvider """
        pass

    def isNameFilterDetailsVisible(self): # real signature unknown; restored from __doc__
        """ isNameFilterDetailsVisible(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> PySide2.QtWidgets.QAbstractItemDelegate """
        pass

    def labelText(self, label): # real signature unknown; restored from __doc__
        """ labelText(self, label: PySide2.QtWidgets.QFileDialog.DialogLabel) -> str """
        return ""

    def mimeTypeFilters(self): # real signature unknown; restored from __doc__
        """ mimeTypeFilters(self) -> typing.List[str] """
        pass

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> typing.List[str] """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> None
        open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> PySide2.QtWidgets.QFileDialog.Options """
        pass

    def proxyModel(self): # real signature unknown; restored from __doc__
        """ proxyModel(self) -> PySide2.QtCore.QAbstractProxyModel """
        pass

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ resolveSymlinks(self) -> bool """
        return False

    def restoreState(self, state): # real signature unknown; restored from __doc__
        """ restoreState(self, state: PySide2.QtCore.QByteArray) -> bool """
        return False

    def saveFileContent(self, fileContent, fileNameHint=''): # real signature unknown; restored from __doc__
        """ saveFileContent(fileContent: PySide2.QtCore.QByteArray, fileNameHint: str = '') -> None """
        pass

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> PySide2.QtCore.QByteArray """
        pass

    def selectedFiles(self): # real signature unknown; restored from __doc__
        """ selectedFiles(self) -> typing.List[str] """
        pass

    def selectedMimeTypeFilter(self): # real signature unknown; restored from __doc__
        """ selectedMimeTypeFilter(self) -> str """
        return ""

    def selectedNameFilter(self): # real signature unknown; restored from __doc__
        """ selectedNameFilter(self) -> str """
        return ""

    def selectedUrls(self): # real signature unknown; restored from __doc__
        """ selectedUrls(self) -> typing.List[PySide2.QtCore.QUrl] """
        pass

    def selectFile(self, filename): # real signature unknown; restored from __doc__
        """ selectFile(self, filename: str) -> None """
        pass

    def selectMimeTypeFilter(self, filter): # real signature unknown; restored from __doc__
        """ selectMimeTypeFilter(self, filter: str) -> None """
        pass

    def selectNameFilter(self, filter): # real signature unknown; restored from __doc__
        """ selectNameFilter(self, filter: str) -> None """
        pass

    def selectUrl(self, url): # real signature unknown; restored from __doc__
        """ selectUrl(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def setAcceptMode(self, mode): # real signature unknown; restored from __doc__
        """ setAcceptMode(self, mode: PySide2.QtWidgets.QFileDialog.AcceptMode) -> None """
        pass

    def setConfirmOverwrite(self, enabled): # real signature unknown; restored from __doc__
        """ setConfirmOverwrite(self, enabled: bool) -> None """
        pass

    def setDefaultSuffix(self, suffix): # real signature unknown; restored from __doc__
        """ setDefaultSuffix(self, suffix: str) -> None """
        pass

    def setDirectory(self, directory): # real signature unknown; restored from __doc__
        """
        setDirectory(self, directory: PySide2.QtCore.QDir) -> None
        setDirectory(self, directory: str) -> None
        """
        pass

    def setDirectoryUrl(self, directory): # real signature unknown; restored from __doc__
        """ setDirectoryUrl(self, directory: PySide2.QtCore.QUrl) -> None """
        pass

    def setFileMode(self, mode): # real signature unknown; restored from __doc__
        """ setFileMode(self, mode: PySide2.QtWidgets.QFileDialog.FileMode) -> None """
        pass

    def setFilter(self, filters): # real signature unknown; restored from __doc__
        """ setFilter(self, filters: PySide2.QtCore.QDir.Filters) -> None """
        pass

    def setHistory(self, paths, p_str=None): # real signature unknown; restored from __doc__
        """ setHistory(self, paths: typing.Sequence[str]) -> None """
        pass

    def setIconProvider(self, provider): # real signature unknown; restored from __doc__
        """ setIconProvider(self, provider: PySide2.QtWidgets.QFileIconProvider) -> None """
        pass

    def setItemDelegate(self, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, delegate: PySide2.QtWidgets.QAbstractItemDelegate) -> None """
        pass

    def setLabelText(self, label, text): # real signature unknown; restored from __doc__
        """ setLabelText(self, label: PySide2.QtWidgets.QFileDialog.DialogLabel, text: str) -> None """
        pass

    def setMimeTypeFilters(self, filters, p_str=None): # real signature unknown; restored from __doc__
        """ setMimeTypeFilters(self, filters: typing.Sequence[str]) -> None """
        pass

    def setNameFilter(self, filter): # real signature unknown; restored from __doc__
        """ setNameFilter(self, filter: str) -> None """
        pass

    def setNameFilterDetailsVisible(self, enabled): # real signature unknown; restored from __doc__
        """ setNameFilterDetailsVisible(self, enabled: bool) -> None """
        pass

    def setNameFilters(self, filters, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, filters: typing.Sequence[str]) -> None """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtWidgets.QFileDialog.Option, on: bool = True) -> None """
        pass

    def setOptions(self, options): # real signature unknown; restored from __doc__
        """ setOptions(self, options: PySide2.QtWidgets.QFileDialog.Options) -> None """
        pass

    def setProxyModel(self, model): # real signature unknown; restored from __doc__
        """ setProxyModel(self, model: PySide2.QtCore.QAbstractProxyModel) -> None """
        pass

    def setReadOnly(self, enabled): # real signature unknown; restored from __doc__
        """ setReadOnly(self, enabled: bool) -> None """
        pass

    def setResolveSymlinks(self, enabled): # real signature unknown; restored from __doc__
        """ setResolveSymlinks(self, enabled: bool) -> None """
        pass

    def setSidebarUrls(self, urls, PySide2_QtCore_QUrl=None): # real signature unknown; restored from __doc__
        """ setSidebarUrls(self, urls: typing.Sequence[PySide2.QtCore.QUrl]) -> None """
        pass

    def setSupportedSchemes(self, schemes, p_str=None): # real signature unknown; restored from __doc__
        """ setSupportedSchemes(self, schemes: typing.Sequence[str]) -> None """
        pass

    def setViewMode(self, mode): # real signature unknown; restored from __doc__
        """ setViewMode(self, mode: PySide2.QtWidgets.QFileDialog.ViewMode) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def sidebarUrls(self): # real signature unknown; restored from __doc__
        """ sidebarUrls(self) -> typing.List[PySide2.QtCore.QUrl] """
        pass

    def supportedSchemes(self): # real signature unknown; restored from __doc__
        """ supportedSchemes(self) -> typing.List[str] """
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: PySide2.QtWidgets.QFileDialog.Option) -> bool """
        return False

    def urlSelected(self, *args, **kwargs): # real signature unknown
        pass

    def urlsSelected(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> PySide2.QtWidgets.QFileDialog.ViewMode """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, f): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Accept = PySide2.QtWidgets.QFileDialog.DialogLabel.Accept
    AcceptMode = None # (!) real value is "<class 'PySide2.QtWidgets.QFileDialog.AcceptMode'>"
    AcceptOpen = PySide2.QtWidgets.QFileDialog.AcceptMode.AcceptOpen
    AcceptSave = PySide2.QtWidgets.QFileDialog.AcceptMode.AcceptSave
    AnyFile = PySide2.QtWidgets.QFileDialog.FileMode.AnyFile
    Detail = PySide2.QtWidgets.QFileDialog.ViewMode.Detail
    DialogLabel = None # (!) real value is "<class 'PySide2.QtWidgets.QFileDialog.DialogLabel'>"
    Directory = PySide2.QtWidgets.QFileDialog.FileMode.Directory
    DirectoryOnly = PySide2.QtWidgets.QFileDialog.FileMode.DirectoryOnly
    DontConfirmOverwrite = PySide2.QtWidgets.QFileDialog.Option.DontConfirmOverwrite
    DontResolveSymlinks = PySide2.QtWidgets.QFileDialog.Option.DontResolveSymlinks
    DontUseCustomDirectoryIcons = PySide2.QtWidgets.QFileDialog.Option.DontUseCustomDirectoryIcons
    DontUseNativeDialog = PySide2.QtWidgets.QFileDialog.Option.DontUseNativeDialog
    DontUseSheet = PySide2.QtWidgets.QFileDialog.Option.DontUseSheet
    ExistingFile = PySide2.QtWidgets.QFileDialog.FileMode.ExistingFile
    ExistingFiles = PySide2.QtWidgets.QFileDialog.FileMode.ExistingFiles
    FileMode = None # (!) real value is "<class 'PySide2.QtWidgets.QFileDialog.FileMode'>"
    FileName = PySide2.QtWidgets.QFileDialog.DialogLabel.FileName
    FileType = PySide2.QtWidgets.QFileDialog.DialogLabel.FileType
    HideNameFilterDetails = PySide2.QtWidgets.QFileDialog.Option.HideNameFilterDetails
    List = PySide2.QtWidgets.QFileDialog.ViewMode.List
    LookIn = PySide2.QtWidgets.QFileDialog.DialogLabel.LookIn
    Option = None # (!) real value is "<class 'PySide2.QtWidgets.QFileDialog.Option'>"
    Options = None # (!) real value is "<class 'PySide2.QtWidgets.QFileDialog.Options'>"
    ReadOnly = PySide2.QtWidgets.QFileDialog.Option.ReadOnly
    Reject = PySide2.QtWidgets.QFileDialog.DialogLabel.Reject
    ShowDirsOnly = PySide2.QtWidgets.QFileDialog.Option.ShowDirsOnly
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F508888C0>'
    ViewMode = None # (!) real value is "<class 'PySide2.QtWidgets.QFileDialog.ViewMode'>"


