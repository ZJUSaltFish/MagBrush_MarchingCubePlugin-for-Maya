# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QItemEditorFactory(__sip.wrapper):
    """
    QItemEditorFactory()
    QItemEditorFactory(a0: QItemEditorFactory)
    """
    def createEditor(self, userType, parent): # real signature unknown; restored from __doc__
        """ createEditor(self, userType: int, parent: QWidget) -> QWidget """
        return QWidget

    def defaultFactory(self): # real signature unknown; restored from __doc__
        """ defaultFactory() -> QItemEditorFactory """
        return QItemEditorFactory

    def registerEditor(self, userType, creator): # real signature unknown; restored from __doc__
        """ registerEditor(self, userType: int, creator: QItemEditorCreatorBase) """
        pass

    def setDefaultFactory(self, factory): # real signature unknown; restored from __doc__
        """ setDefaultFactory(factory: QItemEditorFactory) """
        pass

    def valuePropertyName(self, userType): # real signature unknown; restored from __doc__
        """ valuePropertyName(self, userType: int) -> QByteArray """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



