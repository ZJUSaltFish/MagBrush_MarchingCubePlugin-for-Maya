# encoding: utf-8
# module PyQt5.QtHelp
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtHelp.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QCompressedHelpInfo(__sip.simplewrapper):
    """
    QCompressedHelpInfo()
    QCompressedHelpInfo(other: QCompressedHelpInfo)
    """
    def component(self): # real signature unknown; restored from __doc__
        """ component(self) -> str """
        return ""

    def fromCompressedHelpFile(self, documentationFileName): # real signature unknown; restored from __doc__
        """ fromCompressedHelpFile(documentationFileName: str) -> QCompressedHelpInfo """
        return QCompressedHelpInfo

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def namespaceName(self): # real signature unknown; restored from __doc__
        """ namespaceName(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QCompressedHelpInfo) """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> QVersionNumber """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpContentItem(__sip.simplewrapper):
    # no doc
    def child(self, row): # real signature unknown; restored from __doc__
        """ child(self, row: int) -> QHelpContentItem """
        return QHelpContentItem

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def childPosition(self, child): # real signature unknown; restored from __doc__
        """ childPosition(self, child: QHelpContentItem) -> int """
        return 0

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QHelpContentItem """
        return QHelpContentItem

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpContentModel(__PyQt5_QtCore.QAbstractItemModel):
    # no doc
    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def contentItemAt(self, index): # real signature unknown; restored from __doc__
        """ contentItemAt(self, index: QModelIndex) -> QHelpContentItem """
        return QHelpContentItem

    def contentsCreated(self, *args, **kwargs): # real signature unknown
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

    def contentsCreationStarted(self, *args, **kwargs): # real signature unknown
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

    def createContents(self, customFilterName): # real signature unknown; restored from __doc__
        """ createContents(self, customFilterName: str) """
        pass

    def data(self, index, role): # real signature unknown; restored from __doc__
        """ data(self, index: QModelIndex, role: int) -> Any """
        pass

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def isCreatingContents(self): # real signature unknown; restored from __doc__
        """ isCreatingContents(self) -> bool """
        return False

    def parent(self, index): # real signature unknown; restored from __doc__
        """ parent(self, index: QModelIndex) -> QModelIndex """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpContentWidget(__PyQt5_QtWidgets.QTreeView):
    # no doc
    def indexOf(self, link): # real signature unknown; restored from __doc__
        """ indexOf(self, link: QUrl) -> QModelIndex """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpEngineCore(__PyQt5_QtCore.QObject):
    """ QHelpEngineCore(collectionFile: str, parent: typing.Optional[QObject] = None) """
    def addCustomFilter(self, filterName, attributes, p_str=None): # real signature unknown; restored from __doc__
        """ addCustomFilter(self, filterName: str, attributes: Iterable[str]) -> bool """
        return False

    def autoSaveFilter(self): # real signature unknown; restored from __doc__
        """ autoSaveFilter(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collectionFile(self): # real signature unknown; restored from __doc__
        """ collectionFile(self) -> str """
        return ""

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def copyCollectionFile(self, fileName): # real signature unknown; restored from __doc__
        """ copyCollectionFile(self, fileName: str) -> bool """
        return False

    def currentFilter(self): # real signature unknown; restored from __doc__
        """ currentFilter(self) -> str """
        return ""

    def currentFilterChanged(self, *args, **kwargs): # real signature unknown
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

    def customFilters(self): # real signature unknown; restored from __doc__
        """ customFilters(self) -> List[str] """
        return []

    def customValue(self, key, defaultValue=None): # real signature unknown; restored from __doc__
        """ customValue(self, key: str, defaultValue: Any = None) -> Any """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentationFileName(self, namespaceName): # real signature unknown; restored from __doc__
        """ documentationFileName(self, namespaceName: str) -> str """
        return ""

    def documentsForIdentifier(self, id, filterName=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        documentsForIdentifier(self, id: str) -> List[QHelpLink]
        documentsForIdentifier(self, id: str, filterName: str) -> List[QHelpLink]
        """
        return []

    def documentsForKeyword(self, keyword, filterName=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        documentsForKeyword(self, keyword: str) -> List[QHelpLink]
        documentsForKeyword(self, keyword: str, filterName: str) -> List[QHelpLink]
        """
        return []

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> str """
        return ""

    def fileData(self, url): # real signature unknown; restored from __doc__
        """ fileData(self, url: QUrl) -> QByteArray """
        pass

    def files(self, namespaceName, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        files(self, namespaceName: str, filterAttributes: Iterable[str], extensionFilter: str = '') -> List[QUrl]
        files(self, namespaceName: str, filterName: str, extensionFilter: str = '') -> List[QUrl]
        """
        return []

    def filterAttributes(self, filterName=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        filterAttributes(self) -> List[str]
        filterAttributes(self, filterName: str) -> List[str]
        """
        return []

    def filterAttributeSets(self, namespaceName): # real signature unknown; restored from __doc__
        """ filterAttributeSets(self, namespaceName: str) -> List[List[str]] """
        return []

    def filterEngine(self): # real signature unknown; restored from __doc__
        """ filterEngine(self) -> QHelpFilterEngine """
        return QHelpFilterEngine

    def findFile(self, url): # real signature unknown; restored from __doc__
        """ findFile(self, url: QUrl) -> QUrl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def linksForIdentifier(self, id): # real signature unknown; restored from __doc__
        """ linksForIdentifier(self, id: str) -> Dict[str, QUrl] """
        return {}

    def linksForKeyword(self, keyword): # real signature unknown; restored from __doc__
        """ linksForKeyword(self, keyword: str) -> Dict[str, QUrl] """
        return {}

    def metaData(self, documentationFileName, name): # real signature unknown; restored from __doc__
        """ metaData(documentationFileName: str, name: str) -> Any """
        pass

    def namespaceName(self, documentationFileName): # real signature unknown; restored from __doc__
        """ namespaceName(documentationFileName: str) -> str """
        return ""

    def readersAboutToBeInvalidated(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerDocumentation(self, documentationFileName): # real signature unknown; restored from __doc__
        """ registerDocumentation(self, documentationFileName: str) -> bool """
        return False

    def registeredDocumentations(self): # real signature unknown; restored from __doc__
        """ registeredDocumentations(self) -> List[str] """
        return []

    def removeCustomFilter(self, filterName): # real signature unknown; restored from __doc__
        """ removeCustomFilter(self, filterName: str) -> bool """
        return False

    def removeCustomValue(self, key): # real signature unknown; restored from __doc__
        """ removeCustomValue(self, key: str) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoSaveFilter(self, save): # real signature unknown; restored from __doc__
        """ setAutoSaveFilter(self, save: bool) """
        pass

    def setCollectionFile(self, fileName): # real signature unknown; restored from __doc__
        """ setCollectionFile(self, fileName: str) """
        pass

    def setCurrentFilter(self, filterName): # real signature unknown; restored from __doc__
        """ setCurrentFilter(self, filterName: str) """
        pass

    def setCustomValue(self, key, value): # real signature unknown; restored from __doc__
        """ setCustomValue(self, key: str, value: Any) -> bool """
        return False

    def setupData(self): # real signature unknown; restored from __doc__
        """ setupData(self) -> bool """
        return False

    def setupFinished(self, *args, **kwargs): # real signature unknown
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

    def setupStarted(self, *args, **kwargs): # real signature unknown
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

    def setUsesFilterEngine(self, uses): # real signature unknown; restored from __doc__
        """ setUsesFilterEngine(self, uses: bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterDocumentation(self, namespaceName): # real signature unknown; restored from __doc__
        """ unregisterDocumentation(self, namespaceName: str) -> bool """
        return False

    def usesFilterEngine(self): # real signature unknown; restored from __doc__
        """ usesFilterEngine(self) -> bool """
        return False

    def warning(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, collectionFile, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpEngine(QHelpEngineCore):
    """ QHelpEngine(collectionFile: str, parent: typing.Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentModel(self): # real signature unknown; restored from __doc__
        """ contentModel(self) -> QHelpContentModel """
        return QHelpContentModel

    def contentWidget(self): # real signature unknown; restored from __doc__
        """ contentWidget(self) -> QHelpContentWidget """
        return QHelpContentWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def indexModel(self): # real signature unknown; restored from __doc__
        """ indexModel(self) -> QHelpIndexModel """
        return QHelpIndexModel

    def indexWidget(self): # real signature unknown; restored from __doc__
        """ indexWidget(self) -> QHelpIndexWidget """
        return QHelpIndexWidget

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def searchEngine(self): # real signature unknown; restored from __doc__
        """ searchEngine(self) -> QHelpSearchEngine """
        return QHelpSearchEngine

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, collectionFile, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpFilterData(__sip.simplewrapper):
    """
    QHelpFilterData()
    QHelpFilterData(other: QHelpFilterData)
    """
    def components(self): # real signature unknown; restored from __doc__
        """ components(self) -> List[str] """
        return []

    def setComponents(self, components, p_str=None): # real signature unknown; restored from __doc__
        """ setComponents(self, components: Iterable[str]) """
        pass

    def setVersions(self, versions, QVersionNumber=None): # real signature unknown; restored from __doc__
        """ setVersions(self, versions: Iterable[QVersionNumber]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QHelpFilterData) """
        pass

    def versions(self): # real signature unknown; restored from __doc__
        """ versions(self) -> List[QVersionNumber] """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QHelpFilterEngine(__PyQt5_QtCore.QObject):
    # no doc
    def activeFilter(self): # real signature unknown; restored from __doc__
        """ activeFilter(self) -> str """
        return ""

    def availableComponents(self): # real signature unknown; restored from __doc__
        """ availableComponents(self) -> List[str] """
        return []

    def availableVersions(self): # real signature unknown; restored from __doc__
        """ availableVersions(self) -> List[QVersionNumber] """
        return []

    def filterActivated(self, *args, **kwargs): # real signature unknown
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

    def filterData(self, filterName): # real signature unknown; restored from __doc__
        """ filterData(self, filterName: str) -> QHelpFilterData """
        return QHelpFilterData

    def filters(self): # real signature unknown; restored from __doc__
        """ filters(self) -> List[str] """
        return []

    def indices(self, filterName=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        indices(self) -> List[str]
        indices(self, filterName: str) -> List[str]
        """
        return []

    def namespacesForFilter(self, filterName): # real signature unknown; restored from __doc__
        """ namespacesForFilter(self, filterName: str) -> List[str] """
        return []

    def namespaceToComponent(self): # real signature unknown; restored from __doc__
        """ namespaceToComponent(self) -> Dict[str, str] """
        return {}

    def namespaceToVersion(self): # real signature unknown; restored from __doc__
        """ namespaceToVersion(self) -> Dict[str, QVersionNumber] """
        return {}

    def removeFilter(self, filterName): # real signature unknown; restored from __doc__
        """ removeFilter(self, filterName: str) -> bool """
        return False

    def setActiveFilter(self, filterName): # real signature unknown; restored from __doc__
        """ setActiveFilter(self, filterName: str) -> bool """
        return False

    def setFilterData(self, filterName, filterData): # real signature unknown; restored from __doc__
        """ setFilterData(self, filterName: str, filterData: QHelpFilterData) -> bool """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpFilterSettingsWidget(__PyQt5_QtWidgets.QWidget):
    """ QHelpFilterSettingsWidget(parent: typing.Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def applySettings(self, filterEngine): # real signature unknown; restored from __doc__
        """ applySettings(self, filterEngine: QHelpFilterEngine) -> bool """
        return False

    def changeEvent(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

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

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def readSettings(self, filterEngine): # real signature unknown; restored from __doc__
        """ readSettings(self, filterEngine: QHelpFilterEngine) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAvailableComponents(self, components, p_str=None): # real signature unknown; restored from __doc__
        """ setAvailableComponents(self, components: Iterable[str]) """
        pass

    def setAvailableVersions(self, versions, QVersionNumber=None): # real signature unknown; restored from __doc__
        """ setAvailableVersions(self, versions: Iterable[QVersionNumber]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpIndexModel(__PyQt5_QtCore.QStringListModel):
    # no doc
    def createIndex(self, customFilterName): # real signature unknown; restored from __doc__
        """ createIndex(self, customFilterName: str) """
        pass

    def filter(self, filter, wildcard=''): # real signature unknown; restored from __doc__
        """ filter(self, filter: str, wildcard: str = '') -> QModelIndex """
        pass

    def helpEngine(self): # real signature unknown; restored from __doc__
        """ helpEngine(self) -> QHelpEngineCore """
        return QHelpEngineCore

    def indexCreated(self, *args, **kwargs): # real signature unknown
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

    def indexCreationStarted(self, *args, **kwargs): # real signature unknown
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

    def isCreatingIndex(self): # real signature unknown; restored from __doc__
        """ isCreatingIndex(self) -> bool """
        return False

    def linksForKeyword(self, keyword): # real signature unknown; restored from __doc__
        """ linksForKeyword(self, keyword: str) -> Dict[str, QUrl] """
        return {}

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpIndexWidget(__PyQt5_QtWidgets.QListView):
    # no doc
    def activateCurrentItem(self): # real signature unknown; restored from __doc__
        """ activateCurrentItem(self) """
        pass

    def documentActivated(self, *args, **kwargs): # real signature unknown
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

    def documentsActivated(self, *args, **kwargs): # real signature unknown
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

    def filterIndices(self, filter, wildcard=''): # real signature unknown; restored from __doc__
        """ filterIndices(self, filter: str, wildcard: str = '') """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
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

    def linksActivated(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpLink(__sip.simplewrapper):
    """
    QHelpLink()
    QHelpLink(a0: QHelpLink)
    """
    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




class QHelpSearchEngine(__PyQt5_QtCore.QObject):
    """ QHelpSearchEngine(helpEngine: QHelpEngineCore, parent: typing.Optional[QObject] = None) """
    def cancelIndexing(self): # real signature unknown; restored from __doc__
        """ cancelIndexing(self) """
        pass

    def cancelSearching(self): # real signature unknown; restored from __doc__
        """ cancelSearching(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hitCount(self): # real signature unknown; restored from __doc__
        """ hitCount(self) -> int """
        return 0

    def hits(self, start, end): # real signature unknown; restored from __doc__
        """ hits(self, start: int, end: int) -> List[Tuple[str, str]] """
        return []

    def indexingFinished(self, *args, **kwargs): # real signature unknown
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

    def indexingStarted(self, *args, **kwargs): # real signature unknown
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> List[QHelpSearchQuery] """
        return []

    def queryWidget(self): # real signature unknown; restored from __doc__
        """ queryWidget(self) -> QHelpSearchQueryWidget """
        return QHelpSearchQueryWidget

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reindexDocumentation(self): # real signature unknown; restored from __doc__
        """ reindexDocumentation(self) """
        pass

    def resultWidget(self): # real signature unknown; restored from __doc__
        """ resultWidget(self) -> QHelpSearchResultWidget """
        return QHelpSearchResultWidget

    def search(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        search(self, queryList: Iterable[QHelpSearchQuery])
        search(self, searchInput: str)
        """
        pass

    def searchingFinished(self, *args, **kwargs): # real signature unknown
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

    def searchingStarted(self, *args, **kwargs): # real signature unknown
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

    def searchInput(self): # real signature unknown; restored from __doc__
        """ searchInput(self) -> str """
        return ""

    def searchResultCount(self): # real signature unknown; restored from __doc__
        """ searchResultCount(self) -> int """
        return 0

    def searchResults(self, start, end): # real signature unknown; restored from __doc__
        """ searchResults(self, start: int, end: int) -> List[QHelpSearchResult] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, helpEngine, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpSearchQuery(__sip.simplewrapper):
    """
    QHelpSearchQuery()
    QHelpSearchQuery(field: QHelpSearchQuery.FieldName, wordList: Iterable[str])
    QHelpSearchQuery(a0: QHelpSearchQuery)
    """
    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ALL = 4
    ATLEAST = 5
    DEFAULT = 0
    FUZZY = 1
    PHRASE = 3
    WITHOUT = 2


class QHelpSearchQueryWidget(__PyQt5_QtWidgets.QWidget):
    """ QHelpSearchQueryWidget(parent: typing.Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collapseExtendedSearch(self): # real signature unknown; restored from __doc__
        """ collapseExtendedSearch(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def expandExtendedSearch(self): # real signature unknown; restored from __doc__
        """ expandExtendedSearch(self) """
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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isCompactMode(self): # real signature unknown; restored from __doc__
        """ isCompactMode(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

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

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> List[QHelpSearchQuery] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def search(self, *args, **kwargs): # real signature unknown
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

    def searchInput(self): # real signature unknown; restored from __doc__
        """ searchInput(self) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCompactMode(self, on): # real signature unknown; restored from __doc__
        """ setCompactMode(self, on: bool) """
        pass

    def setQuery(self, queryList, QHelpSearchQuery=None): # real signature unknown; restored from __doc__
        """ setQuery(self, queryList: Iterable[QHelpSearchQuery]) """
        pass

    def setSearchInput(self, searchInput): # real signature unknown; restored from __doc__
        """ setSearchInput(self, searchInput: str) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpSearchResult(__sip.simplewrapper):
    """
    QHelpSearchResult()
    QHelpSearchResult(other: QHelpSearchResult)
    QHelpSearchResult(url: QUrl, title: str, snippet: str)
    """
    def snippet(self): # real signature unknown; restored from __doc__
        """ snippet(self) -> str """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpSearchResultWidget(__PyQt5_QtWidgets.QWidget):
    # no doc
    def linkAt(self, point): # real signature unknown; restored from __doc__
        """ linkAt(self, point: QPoint) -> QUrl """
        pass

    def requestShowLink(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values



