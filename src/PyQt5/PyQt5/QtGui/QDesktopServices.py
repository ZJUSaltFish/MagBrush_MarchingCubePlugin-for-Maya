# encoding: utf-8
# module PyQt5.QtGui
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QDesktopServices(__sip.simplewrapper):
    """
    QDesktopServices()
    QDesktopServices(a0: QDesktopServices)
    """
    def openUrl(self, url): # real signature unknown; restored from __doc__
        """ openUrl(url: QUrl) -> bool """
        return False

    def setUrlHandler(self, scheme, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUrlHandler(scheme: str, receiver: QObject, method: str)
        setUrlHandler(scheme: str, method: Callable[[QUrl], None])
        """
        pass

    def unsetUrlHandler(self, scheme): # real signature unknown; restored from __doc__
        """ unsetUrlHandler(scheme: str) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



