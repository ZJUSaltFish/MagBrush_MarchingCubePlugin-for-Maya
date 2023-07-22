# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QCoreApplication(QObject):
    """
    QCoreApplication(self) -> None
    QCoreApplication(self, arg__1: typing.Sequence[str]) -> None
    """
    def aboutToQuit(self, *args, **kwargs): # real signature unknown
        pass

    def addLibraryPath(self, arg__1): # real signature unknown; restored from __doc__
        """ addLibraryPath(arg__1: str) -> None """
        pass

    def applicationDirPath(self): # real signature unknown; restored from __doc__
        """ applicationDirPath() -> str """
        return ""

    def applicationFilePath(self): # real signature unknown; restored from __doc__
        """ applicationFilePath() -> str """
        return ""

    def applicationName(self): # real signature unknown; restored from __doc__
        """ applicationName() -> str """
        return ""

    def applicationNameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def applicationPid(self): # real signature unknown; restored from __doc__
        """ applicationPid() -> int """
        return 0

    def applicationVersion(self): # real signature unknown; restored from __doc__
        """ applicationVersion() -> str """
        return ""

    def applicationVersionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments() -> typing.List[str] """
        pass

    def closingDown(self): # real signature unknown; restored from __doc__
        """ closingDown() -> bool """
        return False

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventDispatcher(self): # real signature unknown; restored from __doc__
        """ eventDispatcher() -> PySide2.QtCore.QAbstractEventDispatcher """
        pass

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def exit(self, retcode=0): # real signature unknown; restored from __doc__
        """ exit(retcode: int = 0) -> None """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush() -> None """
        pass

    def hasPendingEvents(self): # real signature unknown; restored from __doc__
        """ hasPendingEvents() -> bool """
        return False

    def installNativeEventFilter(self, filterObj): # real signature unknown; restored from __doc__
        """ installNativeEventFilter(self, filterObj: PySide2.QtCore.QAbstractNativeEventFilter) -> None """
        pass

    def installTranslator(self, messageFile): # real signature unknown; restored from __doc__
        """ installTranslator(messageFile: PySide2.QtCore.QTranslator) -> bool """
        return False

    def instance(self): # real signature unknown; restored from __doc__
        """ instance() -> PySide2.QtCore.QCoreApplication """
        pass

    def isQuitLockEnabled(self): # real signature unknown; restored from __doc__
        """ isQuitLockEnabled() -> bool """
        return False

    def isSetuidAllowed(self): # real signature unknown; restored from __doc__
        """ isSetuidAllowed() -> bool """
        return False

    def libraryPaths(self): # real signature unknown; restored from __doc__
        """ libraryPaths() -> typing.List[str] """
        pass

    def notify(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ notify(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def organizationDomain(self): # real signature unknown; restored from __doc__
        """ organizationDomain() -> str """
        return ""

    def organizationDomainChanged(self, *args, **kwargs): # real signature unknown
        pass

    def organizationName(self): # real signature unknown; restored from __doc__
        """ organizationName() -> str """
        return ""

    def organizationNameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def postEvent(self, receiver, event, priority=None): # real signature unknown; restored from __doc__
        """ postEvent(receiver: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent, priority: int = PySide2.QtCore.Qt.EventPriority.NormalEventPriority) -> None """
        pass

    def processEvents(self, flags, maxtime): # real signature unknown; restored from __doc__
        """
        processEvents(flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags, maxtime: int) -> None
        processEvents(flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags = PySide2.QtCore.QEventLoop.ProcessEventsFlag.AllEvents) -> None
        """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit() -> None """
        pass

    def removeLibraryPath(self, arg__1): # real signature unknown; restored from __doc__
        """ removeLibraryPath(arg__1: str) -> None """
        pass

    def removeNativeEventFilter(self, filterObj): # real signature unknown; restored from __doc__
        """ removeNativeEventFilter(self, filterObj: PySide2.QtCore.QAbstractNativeEventFilter) -> None """
        pass

    def removePostedEvents(self, receiver, eventType=0): # real signature unknown; restored from __doc__
        """ removePostedEvents(receiver: PySide2.QtCore.QObject, eventType: int = 0) -> None """
        pass

    def removeTranslator(self, messageFile): # real signature unknown; restored from __doc__
        """ removeTranslator(messageFile: PySide2.QtCore.QTranslator) -> bool """
        return False

    def sendEvent(self, receiver, event): # real signature unknown; restored from __doc__
        """ sendEvent(receiver: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def sendPostedEvents(self, receiver, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sendPostedEvents(receiver: typing.Optional[PySide2.QtCore.QObject] = None, event_type: int = 0) -> None """
        pass

    def setApplicationName(self, application): # real signature unknown; restored from __doc__
        """ setApplicationName(application: str) -> None """
        pass

    def setApplicationVersion(self, version): # real signature unknown; restored from __doc__
        """ setApplicationVersion(version: str) -> None """
        pass

    def setAttribute(self, attribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(attribute: PySide2.QtCore.Qt.ApplicationAttribute, on: bool = True) -> None """
        pass

    def setEventDispatcher(self, eventDispatcher): # real signature unknown; restored from __doc__
        """ setEventDispatcher(eventDispatcher: PySide2.QtCore.QAbstractEventDispatcher) -> None """
        pass

    def setLibraryPaths(self, arg__1, p_str=None): # real signature unknown; restored from __doc__
        """ setLibraryPaths(arg__1: typing.Sequence[str]) -> None """
        pass

    def setOrganizationDomain(self, orgDomain): # real signature unknown; restored from __doc__
        """ setOrganizationDomain(orgDomain: str) -> None """
        pass

    def setOrganizationName(self, orgName): # real signature unknown; restored from __doc__
        """ setOrganizationName(orgName: str) -> None """
        pass

    def setQuitLockEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setQuitLockEnabled(enabled: bool) -> None """
        pass

    def setSetuidAllowed(self, allow): # real signature unknown; restored from __doc__
        """ setSetuidAllowed(allow: bool) -> None """
        pass

    def shutdown(self): # real signature unknown; restored from __doc__
        """ shutdown(self) -> None """
        pass

    def startingUp(self): # real signature unknown; restored from __doc__
        """ startingUp() -> bool """
        return False

    def testAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ testAttribute(attribute: PySide2.QtCore.Qt.ApplicationAttribute) -> bool """
        return False

    def translate(self, context, key, disambiguation, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ translate(context: bytes, key: bytes, disambiguation: typing.Optional[bytes] = None, n: int = -1) -> str """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E17940>'


