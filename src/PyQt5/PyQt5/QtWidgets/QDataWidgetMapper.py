# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QDataWidgetMapper(__PyQt5_QtCore.QObject):
    """ QDataWidgetMapper(parent: typing.Optional[QObject] = None) """
    def addMapping(self, widget, section, propertyName=None, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMapping(self, widget: QWidget, section: int)
        addMapping(self, widget: QWidget, section: int, propertyName: Union[QByteArray, bytes, bytearray])
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearMapping(self): # real signature unknown; restored from __doc__
        """ clearMapping(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentIndexChanged(self, *args, **kwargs): # real signature unknown
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

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def mappedPropertyName(self, widget): # real signature unknown; restored from __doc__
        """ mappedPropertyName(self, widget: QWidget) -> QByteArray """
        pass

    def mappedSection(self, widget): # real signature unknown; restored from __doc__
        """ mappedSection(self, widget: QWidget) -> int """
        return 0

    def mappedWidgetAt(self, section): # real signature unknown; restored from __doc__
        """ mappedWidgetAt(self, section: int) -> QWidget """
        return QWidget

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.Orientation """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeMapping(self, widget): # real signature unknown; restored from __doc__
        """ removeMapping(self, widget: QWidget) """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def rootIndex(self): # real signature unknown; restored from __doc__
        """ rootIndex(self) -> QModelIndex """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) """
        pass

    def setCurrentModelIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentModelIndex(self, index: QModelIndex) """
        pass

    def setItemDelegate(self, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, delegate: QAbstractItemDelegate) """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: QAbstractItemModel) """
        pass

    def setOrientation(self, aOrientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, aOrientation: Qt.Orientation) """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: QModelIndex) """
        pass

    def setSubmitPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setSubmitPolicy(self, policy: QDataWidgetMapper.SubmitPolicy) """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def submitPolicy(self): # real signature unknown; restored from __doc__
        """ submitPolicy(self) -> QDataWidgetMapper.SubmitPolicy """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toFirst(self): # real signature unknown; restored from __doc__
        """ toFirst(self) """
        pass

    def toLast(self): # real signature unknown; restored from __doc__
        """ toLast(self) """
        pass

    def toNext(self): # real signature unknown; restored from __doc__
        """ toNext(self) """
        pass

    def toPrevious(self): # real signature unknown; restored from __doc__
        """ toPrevious(self) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AutoSubmit = 0
    ManualSubmit = 1


