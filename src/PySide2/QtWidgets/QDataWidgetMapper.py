# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QDataWidgetMapper(__PySide2_QtCore.QObject):
    """ QDataWidgetMapper(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addMapping(self, widget, section): # real signature unknown; restored from __doc__
        """
        addMapping(self, widget: PySide2.QtWidgets.QWidget, section: int) -> None
        addMapping(self, widget: PySide2.QtWidgets.QWidget, section: int, propertyName: PySide2.QtCore.QByteArray) -> None
        """
        pass

    def clearMapping(self): # real signature unknown; restored from __doc__
        """ clearMapping(self) -> None """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentIndexChanged(self, *args, **kwargs): # real signature unknown
        pass

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ itemDelegate(self) -> PySide2.QtWidgets.QAbstractItemDelegate """
        pass

    def mappedPropertyName(self, widget): # real signature unknown; restored from __doc__
        """ mappedPropertyName(self, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtCore.QByteArray """
        pass

    def mappedSection(self, widget): # real signature unknown; restored from __doc__
        """ mappedSection(self, widget: PySide2.QtWidgets.QWidget) -> int """
        return 0

    def mappedWidgetAt(self, section): # real signature unknown; restored from __doc__
        """ mappedWidgetAt(self, section: int) -> PySide2.QtWidgets.QWidget """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> PySide2.QtCore.QAbstractItemModel """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def removeMapping(self, widget): # real signature unknown; restored from __doc__
        """ removeMapping(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) -> None """
        pass

    def rootIndex(self): # real signature unknown; restored from __doc__
        """ rootIndex(self) -> PySide2.QtCore.QModelIndex """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) -> None """
        pass

    def setCurrentModelIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentModelIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setItemDelegate(self, delegate): # real signature unknown; restored from __doc__
        """ setItemDelegate(self, delegate: PySide2.QtWidgets.QAbstractItemDelegate) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setOrientation(self, aOrientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, aOrientation: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setSubmitPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setSubmitPolicy(self, policy: PySide2.QtWidgets.QDataWidgetMapper.SubmitPolicy) -> None """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def submitPolicy(self): # real signature unknown; restored from __doc__
        """ submitPolicy(self) -> PySide2.QtWidgets.QDataWidgetMapper.SubmitPolicy """
        pass

    def toFirst(self): # real signature unknown; restored from __doc__
        """ toFirst(self) -> None """
        pass

    def toLast(self): # real signature unknown; restored from __doc__
        """ toLast(self) -> None """
        pass

    def toNext(self): # real signature unknown; restored from __doc__
        """ toNext(self) -> None """
        pass

    def toPrevious(self): # real signature unknown; restored from __doc__
        """ toPrevious(self) -> None """
        pass

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

    AutoSubmit = PySide2.QtWidgets.QDataWidgetMapper.SubmitPolicy.AutoSubmit
    ManualSubmit = PySide2.QtWidgets.QDataWidgetMapper.SubmitPolicy.ManualSubmit
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50870E80>'
    SubmitPolicy = None # (!) real value is "<class 'PySide2.QtWidgets.QDataWidgetMapper.SubmitPolicy'>"


