# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QDialog import QDialog

class QFileDialog(QDialog):
    """
    QFileDialog(parent: QWidget, f: Union[Qt.WindowFlags, Qt.WindowType])
    QFileDialog(parent: typing.Optional[QWidget] = None, caption: str = '', directory: str = '', filter: str = '')
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) """
        pass

    def acceptMode(self): # real signature unknown; restored from __doc__
        """ acceptMode(self) -> QFileDialog.AcceptMode """
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, e): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def currentUrlChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultSuffix(self): # real signature unknown; restored from __doc__
        """ defaultSuffix(self) -> str """
        return ""

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def directory(self): # real signature unknown; restored from __doc__
        """ directory(self) -> QDir """
        pass

    def directoryEntered(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def directoryUrl(self): # real signature unknown; restored from __doc__
        """ directoryUrl(self) -> QUrl """
        pass

    def directoryUrlEntered(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def fileMode(self): # real signature unknown; restored from __doc__
        """ fileMode(self) -> QFileDialog.FileMode """
        pass

    def fileSelected(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def filesSelected(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> QDir.Filters """
        pass

    def filterSelected(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def getExistingDirectory(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getExistingDirectory(parent: typing.Optional[QWidget] = None, caption: str = '', directory: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = QFileDialog.ShowDirsOnly) -> str """
        pass

    def getExistingDirectoryUrl(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getExistingDirectoryUrl(parent: typing.Optional[QWidget] = None, caption: str = '', directory: QUrl = QUrl(), options: Union[QFileDialog.Options, QFileDialog.Option] = QFileDialog.ShowDirsOnly, supportedSchemes: Iterable[str] = []) -> QUrl """
        pass

    def getOpenFileName(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileName(parent: typing.Optional[QWidget] = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[str, str] """
        pass

    def getOpenFileNames(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileNames(parent: typing.Optional[QWidget] = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[List[str], str] """
        pass

    def getOpenFileUrl(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileUrl(parent: typing.Optional[QWidget] = None, caption: str = '', directory: QUrl = QUrl(), filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str] """
        pass

    def getOpenFileUrls(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getOpenFileUrls(parent: typing.Optional[QWidget] = None, caption: str = '', directory: QUrl = QUrl(), filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[List[QUrl], str] """
        pass

    def getSaveFileName(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getSaveFileName(parent: typing.Optional[QWidget] = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[str, str] """
        pass

    def getSaveFileUrl(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getSaveFileUrl(parent: typing.Optional[QWidget] = None, caption: str = '', directory: QUrl = QUrl(), filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str] """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ history(self) -> List[str] """
        return []

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ iconProvider(self) -> QFileIconProvider """
        return QFileIconProvider

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self, label): # real signature unknown; restored from __doc__
        """ labelText(self, label: QFileDialog.DialogLabel) -> str """
        return ""

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mimeTypeFilters(self): # real signature unknown; restored from __doc__
        """ mimeTypeFilters(self) -> List[str] """
        return []

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> List[str] """
        return []

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, slot=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, slot: PYQT_SLOT)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QFileDialog.Options """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def proxyModel(self): # real signature unknown; restored from __doc__
        """ proxyModel(self) -> QAbstractProxyModel """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def restoreState(self, state, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ restoreState(self, state: Union[QByteArray, bytes, bytearray]) -> bool """
        return False

    def saveFileContent(self, fileContent, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ saveFileContent(fileContent: Union[QByteArray, bytes, bytearray], fileNameHint: str = '') """
        pass

    def saveState(self): # real signature unknown; restored from __doc__
        """ saveState(self) -> QByteArray """
        pass

    def selectedFiles(self): # real signature unknown; restored from __doc__
        """ selectedFiles(self) -> List[str] """
        return []

    def selectedMimeTypeFilter(self): # real signature unknown; restored from __doc__
        """ selectedMimeTypeFilter(self) -> str """
        return ""

    def selectedNameFilter(self): # real signature unknown; restored from __doc__
        """ selectedNameFilter(self) -> str """
        return ""

    def selectedUrls(self): # real signature unknown; restored from __doc__
        """ selectedUrls(self) -> List[QUrl] """
        return []

    def selectFile(self, filename): # real signature unknown; restored from __doc__
        """ selectFile(self, filename: str) """
        pass

    def selectMimeTypeFilter(self, filter): # real signature unknown; restored from __doc__
        """ selectMimeTypeFilter(self, filter: str) """
        pass

    def selectNameFilter(self, filter): # real signature unknown; restored from __doc__
        """ selectNameFilter(self, filter: str) """
        pass

    def selectUrl(self, url): # real signature unknown; restored from __doc__
        """ selectUrl(self, url: QUrl) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptMode(self, mode): # real signature unknown; restored from __doc__
        """ setAcceptMode(self, mode: QFileDialog.AcceptMode) """
        pass

    def setDefaultSuffix(self, suffix): # real signature unknown; restored from __doc__
        """ setDefaultSuffix(self, suffix: str) """
        pass

    def setDirectory(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setDirectory(self, directory: str)
        setDirectory(self, adirectory: QDir)
        """
        pass

    def setDirectoryUrl(self, directory): # real signature unknown; restored from __doc__
        """ setDirectoryUrl(self, directory: QUrl) """
        pass

    def setFileMode(self, mode): # real signature unknown; restored from __doc__
        """ setFileMode(self, mode: QFileDialog.FileMode) """
        pass

    def setFilter(self, filters, QDir_Filters=None, QDir_Filter=None): # real signature unknown; restored from __doc__
        """ setFilter(self, filters: Union[QDir.Filters, QDir.Filter]) """
        pass

    def setHistory(self, paths, p_str=None): # real signature unknown; restored from __doc__
        """ setHistory(self, paths: Iterable[str]) """
        pass

    def setIconProvider(self, provider): # real signature unknown; restored from __doc__
        """ setIconProvider(self, provider: QFileIconProvider) """
        pass

    def setItemDelegate(self, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, delegate: QAbstractItemDelegate) """
        pass

    def setLabelText(self, label, text): # real signature unknown; restored from __doc__
        """ setLabelText(self, label: QFileDialog.DialogLabel, text: str) """
        pass

    def setMimeTypeFilters(self, filters, p_str=None): # real signature unknown; restored from __doc__
        """ setMimeTypeFilters(self, filters: Iterable[str]) """
        pass

    def setNameFilter(self, filter): # real signature unknown; restored from __doc__
        """ setNameFilter(self, filter: str) """
        pass

    def setNameFilters(self, filters, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, filters: Iterable[str]) """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: QFileDialog.Option, on: bool = True) """
        pass

    def setOptions(self, options, QFileDialog_Options=None, QFileDialog_Option=None): # real signature unknown; restored from __doc__
        """ setOptions(self, options: Union[QFileDialog.Options, QFileDialog.Option]) """
        pass

    def setProxyModel(self, model): # real signature unknown; restored from __doc__
        """ setProxyModel(self, model: QAbstractProxyModel) """
        pass

    def setSidebarUrls(self, urls, QUrl=None): # real signature unknown; restored from __doc__
        """ setSidebarUrls(self, urls: Iterable[QUrl]) """
        pass

    def setSupportedSchemes(self, schemes, p_str=None): # real signature unknown; restored from __doc__
        """ setSupportedSchemes(self, schemes: Iterable[str]) """
        pass

    def setViewMode(self, mode): # real signature unknown; restored from __doc__
        """ setViewMode(self, mode: QFileDialog.ViewMode) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sidebarUrls(self): # real signature unknown; restored from __doc__
        """ sidebarUrls(self) -> List[QUrl] """
        return []

    def supportedSchemes(self): # real signature unknown; restored from __doc__
        """ supportedSchemes(self) -> List[str] """
        return []

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: QFileDialog.Option) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def urlSelected(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def urlsSelected(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> QFileDialog.ViewMode """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Accept = 3
    AcceptOpen = 0
    AcceptSave = 1
    AnyFile = 0
    Detail = 0
    Directory = 2
    DirectoryOnly = 4
    DontConfirmOverwrite = 4
    DontResolveSymlinks = 2
    DontUseCustomDirectoryIcons = 128
    DontUseNativeDialog = 16
    DontUseSheet = 8
    ExistingFile = 1
    ExistingFiles = 3
    FileName = 1
    FileType = 2
    HideNameFilterDetails = 64
    List = 1
    LookIn = 0
    ReadOnly = 32
    Reject = 4
    ShowDirsOnly = 1


