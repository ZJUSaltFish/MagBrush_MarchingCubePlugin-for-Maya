# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QWidget import QWidget

class QDockWidget(QWidget):
    """
    QDockWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QDockWidget(self, title: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    """
    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ allowedAreas(self) -> PySide2.QtCore.Qt.DockWidgetAreas """
        pass

    def allowedAreasChanged(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def closeEvent(self, event): # real signature unknown; restored from __doc__
        """ closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None """
        pass

    def dockLocationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def features(self): # real signature unknown; restored from __doc__
        """ features(self) -> PySide2.QtWidgets.QDockWidget.DockWidgetFeatures """
        pass

    def featuresChanged(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionDockWidget) -> None """
        pass

    def isAreaAllowed(self, area): # real signature unknown; restored from __doc__
        """ isAreaAllowed(self, area: PySide2.QtCore.Qt.DockWidgetArea) -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ isFloating(self) -> bool """
        return False

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def setAllowedAreas(self, areas): # real signature unknown; restored from __doc__
        """ setAllowedAreas(self, areas: PySide2.QtCore.Qt.DockWidgetAreas) -> None """
        pass

    def setFeatures(self, features): # real signature unknown; restored from __doc__
        """ setFeatures(self, features: PySide2.QtWidgets.QDockWidget.DockWidgetFeatures) -> None """
        pass

    def setFloating(self, floating): # real signature unknown; restored from __doc__
        """ setFloating(self, floating: bool) -> None """
        pass

    def setTitleBarWidget(self, widget): # real signature unknown; restored from __doc__
        """ setTitleBarWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setWidget(self, widget): # real signature unknown; restored from __doc__
        """ setWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def titleBarWidget(self): # real signature unknown; restored from __doc__
        """ titleBarWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ toggleViewAction(self) -> PySide2.QtWidgets.QAction """
        pass

    def topLevelChanged(self, *args, **kwargs): # real signature unknown
        pass

    def visibilityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> PySide2.QtWidgets.QWidget """
        pass

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

    AllDockWidgetFeatures = PySide2.QtWidgets.QDockWidget.DockWidgetFeature.AllDockWidgetFeatures
    DockWidgetClosable = PySide2.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetClosable
    DockWidgetFeature = None # (!) real value is "<class 'PySide2.QtWidgets.QDockWidget.DockWidgetFeature'>"
    DockWidgetFeatureMask = PySide2.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFeatureMask
    DockWidgetFeatures = None # (!) real value is "<class 'PySide2.QtWidgets.QDockWidget.DockWidgetFeatures'>"
    DockWidgetFloatable = PySide2.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable
    DockWidgetMovable = PySide2.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable
    DockWidgetVerticalTitleBar = PySide2.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetVerticalTitleBar
    NoDockWidgetFeatures = PySide2.QtWidgets.QDockWidget.DockWidgetFeature.NoDockWidgetFeatures
    Reserved = PySide2.QtWidgets.QDockWidget.DockWidgetFeature.Reserved
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50831A40>'


