# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QFileIconProvider(__Shiboken.Object):
    """ QFileIconProvider(self) -> None """
    def icon(self, info): # real signature unknown; restored from __doc__
        """
        icon(self, info: PySide2.QtCore.QFileInfo) -> PySide2.QtGui.QIcon
        icon(self, type: PySide2.QtWidgets.QFileIconProvider.IconType) -> PySide2.QtGui.QIcon
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> PySide2.QtWidgets.QFileIconProvider.Options """
        pass

    def setOptions(self, options): # real signature unknown; restored from __doc__
        """ setOptions(self, options: PySide2.QtWidgets.QFileIconProvider.Options) -> None """
        pass

    def type(self, info): # real signature unknown; restored from __doc__
        """ type(self, info: PySide2.QtCore.QFileInfo) -> str """
        return ""

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

    Computer = PySide2.QtWidgets.QFileIconProvider.IconType.Computer
    Desktop = PySide2.QtWidgets.QFileIconProvider.IconType.Desktop
    DontUseCustomDirectoryIcons = PySide2.QtWidgets.QFileIconProvider.Option.DontUseCustomDirectoryIcons
    Drive = PySide2.QtWidgets.QFileIconProvider.IconType.Drive
    File = PySide2.QtWidgets.QFileIconProvider.IconType.File
    Folder = PySide2.QtWidgets.QFileIconProvider.IconType.Folder
    IconType = None # (!) real value is "<class 'PySide2.QtWidgets.QFileIconProvider.IconType'>"
    Network = PySide2.QtWidgets.QFileIconProvider.IconType.Network
    Option = None # (!) real value is "<class 'PySide2.QtWidgets.QFileIconProvider.Option'>"
    Options = None # (!) real value is "<class 'PySide2.QtWidgets.QFileIconProvider.Options'>"
    Trashcan = PySide2.QtWidgets.QFileIconProvider.IconType.Trashcan


