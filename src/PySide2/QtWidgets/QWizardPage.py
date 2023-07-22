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

class QWizardPage(QWidget):
    """ QWizardPage(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def buttonText(self, which): # real signature unknown; restored from __doc__
        """ buttonText(self, which: PySide2.QtWidgets.QWizard.WizardButton) -> str """
        return ""

    def cleanupPage(self): # real signature unknown; restored from __doc__
        """ cleanupPage(self) -> None """
        pass

    def completeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def field(self, name): # real signature unknown; restored from __doc__
        """ field(self, name: str) -> typing.Any """
        pass

    def initializePage(self): # real signature unknown; restored from __doc__
        """ initializePage(self) -> None """
        pass

    def isCommitPage(self): # real signature unknown; restored from __doc__
        """ isCommitPage(self) -> bool """
        return False

    def isComplete(self): # real signature unknown; restored from __doc__
        """ isComplete(self) -> bool """
        return False

    def isFinalPage(self): # real signature unknown; restored from __doc__
        """ isFinalPage(self) -> bool """
        return False

    def nextId(self): # real signature unknown; restored from __doc__
        """ nextId(self) -> int """
        return 0

    def pixmap(self, which): # real signature unknown; restored from __doc__
        """ pixmap(self, which: PySide2.QtWidgets.QWizard.WizardPixmap) -> PySide2.QtGui.QPixmap """
        pass

    def registerField(self, name, widget, property, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerField(self, name: str, widget: PySide2.QtWidgets.QWidget, property: typing.Optional[bytes] = None, changedSignal: typing.Optional[bytes] = None) -> None """
        pass

    def setButtonText(self, which, text): # real signature unknown; restored from __doc__
        """ setButtonText(self, which: PySide2.QtWidgets.QWizard.WizardButton, text: str) -> None """
        pass

    def setCommitPage(self, commitPage): # real signature unknown; restored from __doc__
        """ setCommitPage(self, commitPage: bool) -> None """
        pass

    def setField(self, name, value): # real signature unknown; restored from __doc__
        """ setField(self, name: str, value: typing.Any) -> None """
        pass

    def setFinalPage(self, finalPage): # real signature unknown; restored from __doc__
        """ setFinalPage(self, finalPage: bool) -> None """
        pass

    def setPixmap(self, which, pixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, which: PySide2.QtWidgets.QWizard.WizardPixmap, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def setSubTitle(self, subTitle): # real signature unknown; restored from __doc__
        """ setSubTitle(self, subTitle: str) -> None """
        pass

    def setTitle(self, title): # real signature unknown; restored from __doc__
        """ setTitle(self, title: str) -> None """
        pass

    def subTitle(self): # real signature unknown; restored from __doc__
        """ subTitle(self) -> str """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def validatePage(self): # real signature unknown; restored from __doc__
        """ validatePage(self) -> bool """
        return False

    def wizard(self): # real signature unknown; restored from __doc__
        """ wizard(self) -> PySide2.QtWidgets.QWizard """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507BEE40>'


