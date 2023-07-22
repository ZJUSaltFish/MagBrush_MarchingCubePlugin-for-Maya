# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QDialog import QDialog

class QWizard(QDialog):
    """ QWizard(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def addPage(self, page): # real signature unknown; restored from __doc__
        """ addPage(self, page: PySide2.QtWidgets.QWizardPage) -> int """
        return 0

    def back(self): # real signature unknown; restored from __doc__
        """ back(self) -> None """
        pass

    def button(self, which): # real signature unknown; restored from __doc__
        """ button(self, which: PySide2.QtWidgets.QWizard.WizardButton) -> PySide2.QtWidgets.QAbstractButton """
        pass

    def buttonText(self, which): # real signature unknown; restored from __doc__
        """ buttonText(self, which: PySide2.QtWidgets.QWizard.WizardButton) -> str """
        return ""

    def cleanupPage(self, id): # real signature unknown; restored from __doc__
        """ cleanupPage(self, id: int) -> None """
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ currentId(self) -> int """
        return 0

    def currentIdChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentPage(self): # real signature unknown; restored from __doc__
        """ currentPage(self) -> PySide2.QtWidgets.QWizardPage """
        pass

    def customButtonClicked(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) -> None """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def field(self, name): # real signature unknown; restored from __doc__
        """ field(self, name: str) -> typing.Any """
        pass

    def hasVisitedPage(self, id): # real signature unknown; restored from __doc__
        """ hasVisitedPage(self, id: int) -> bool """
        return False

    def helpRequested(self, *args, **kwargs): # real signature unknown
        pass

    def initializePage(self, id): # real signature unknown; restored from __doc__
        """ initializePage(self, id: int) -> None """
        pass

    def nativeEvent(self, eventType, message): # real signature unknown; restored from __doc__
        """ nativeEvent(self, eventType: PySide2.QtCore.QByteArray, message: int) -> typing.Tuple[bool, int] """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> None """
        pass

    def nextId(self): # real signature unknown; restored from __doc__
        """ nextId(self) -> int """
        return 0

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> PySide2.QtWidgets.QWizard.WizardOptions """
        pass

    def page(self, id): # real signature unknown; restored from __doc__
        """ page(self, id: int) -> PySide2.QtWidgets.QWizardPage """
        pass

    def pageAdded(self, *args, **kwargs): # real signature unknown
        pass

    def pageIds(self): # real signature unknown; restored from __doc__
        """ pageIds(self) -> typing.List[int] """
        pass

    def pageRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def pixmap(self, which): # real signature unknown; restored from __doc__
        """ pixmap(self, which: PySide2.QtWidgets.QWizard.WizardPixmap) -> PySide2.QtGui.QPixmap """
        pass

    def removePage(self, id): # real signature unknown; restored from __doc__
        """ removePage(self, id: int) -> None """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def restart(self): # real signature unknown; restored from __doc__
        """ restart(self) -> None """
        pass

    def setButton(self, which, button): # real signature unknown; restored from __doc__
        """ setButton(self, which: PySide2.QtWidgets.QWizard.WizardButton, button: PySide2.QtWidgets.QAbstractButton) -> None """
        pass

    def setButtonLayout(self, layout, PySide2_QtWidgets_QWizard_WizardButton=None): # real signature unknown; restored from __doc__
        """ setButtonLayout(self, layout: typing.Sequence[PySide2.QtWidgets.QWizard.WizardButton]) -> None """
        pass

    def setButtonText(self, which, text): # real signature unknown; restored from __doc__
        """ setButtonText(self, which: PySide2.QtWidgets.QWizard.WizardButton, text: str) -> None """
        pass

    def setDefaultProperty(self, className, property, changedSignal): # real signature unknown; restored from __doc__
        """ setDefaultProperty(self, className: bytes, property: bytes, changedSignal: bytes) -> None """
        pass

    def setField(self, name, value): # real signature unknown; restored from __doc__
        """ setField(self, name: str, value: typing.Any) -> None """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtWidgets.QWizard.WizardOption, on: bool = True) -> None """
        pass

    def setOptions(self, options): # real signature unknown; restored from __doc__
        """ setOptions(self, options: PySide2.QtWidgets.QWizard.WizardOptions) -> None """
        pass

    def setPage(self, id, page): # real signature unknown; restored from __doc__
        """ setPage(self, id: int, page: PySide2.QtWidgets.QWizardPage) -> None """
        pass

    def setPixmap(self, which, pixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, which: PySide2.QtWidgets.QWizard.WizardPixmap, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def setSideWidget(self, widget): # real signature unknown; restored from __doc__
        """ setSideWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setStartId(self, id): # real signature unknown; restored from __doc__
        """ setStartId(self, id: int) -> None """
        pass

    def setSubTitleFormat(self, format): # real signature unknown; restored from __doc__
        """ setSubTitleFormat(self, format: PySide2.QtCore.Qt.TextFormat) -> None """
        pass

    def setTitleFormat(self, format): # real signature unknown; restored from __doc__
        """ setTitleFormat(self, format: PySide2.QtCore.Qt.TextFormat) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def setWizardStyle(self, style): # real signature unknown; restored from __doc__
        """ setWizardStyle(self, style: PySide2.QtWidgets.QWizard.WizardStyle) -> None """
        pass

    def sideWidget(self): # real signature unknown; restored from __doc__
        """ sideWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def startId(self): # real signature unknown; restored from __doc__
        """ startId(self) -> int """
        return 0

    def subTitleFormat(self): # real signature unknown; restored from __doc__
        """ subTitleFormat(self) -> PySide2.QtCore.Qt.TextFormat """
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: PySide2.QtWidgets.QWizard.WizardOption) -> bool """
        return False

    def titleFormat(self): # real signature unknown; restored from __doc__
        """ titleFormat(self) -> PySide2.QtCore.Qt.TextFormat """
        pass

    def validateCurrentPage(self): # real signature unknown; restored from __doc__
        """ validateCurrentPage(self) -> bool """
        return False

    def visitedIds(self): # real signature unknown; restored from __doc__
        """ visitedIds(self) -> typing.List[int] """
        pass

    def visitedPages(self): # real signature unknown; restored from __doc__
        """ visitedPages(self) -> typing.List[int] """
        pass

    def wizardStyle(self): # real signature unknown; restored from __doc__
        """ wizardStyle(self) -> PySide2.QtWidgets.QWizard.WizardStyle """
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

    AeroStyle = PySide2.QtWidgets.QWizard.WizardStyle.AeroStyle
    BackButton = PySide2.QtWidgets.QWizard.WizardButton.BackButton
    BackgroundPixmap = PySide2.QtWidgets.QWizard.WizardPixmap.BackgroundPixmap
    BannerPixmap = PySide2.QtWidgets.QWizard.WizardPixmap.BannerPixmap
    CancelButton = PySide2.QtWidgets.QWizard.WizardButton.CancelButton
    CancelButtonOnLeft = PySide2.QtWidgets.QWizard.WizardOption.CancelButtonOnLeft
    ClassicStyle = PySide2.QtWidgets.QWizard.WizardStyle.ClassicStyle
    CommitButton = PySide2.QtWidgets.QWizard.WizardButton.CommitButton
    CustomButton1 = PySide2.QtWidgets.QWizard.WizardButton.CustomButton1
    CustomButton2 = PySide2.QtWidgets.QWizard.WizardButton.CustomButton2
    CustomButton3 = PySide2.QtWidgets.QWizard.WizardButton.CustomButton3
    DisabledBackButtonOnLastPage = PySide2.QtWidgets.QWizard.WizardOption.DisabledBackButtonOnLastPage
    ExtendedWatermarkPixmap = PySide2.QtWidgets.QWizard.WizardOption.ExtendedWatermarkPixmap
    FinishButton = PySide2.QtWidgets.QWizard.WizardButton.FinishButton
    HaveCustomButton1 = PySide2.QtWidgets.QWizard.WizardOption.HaveCustomButton1
    HaveCustomButton2 = PySide2.QtWidgets.QWizard.WizardOption.HaveCustomButton2
    HaveCustomButton3 = PySide2.QtWidgets.QWizard.WizardOption.HaveCustomButton3
    HaveFinishButtonOnEarlyPages = PySide2.QtWidgets.QWizard.WizardOption.HaveFinishButtonOnEarlyPages
    HaveHelpButton = PySide2.QtWidgets.QWizard.WizardOption.HaveHelpButton
    HaveNextButtonOnLastPage = PySide2.QtWidgets.QWizard.WizardOption.HaveNextButtonOnLastPage
    HelpButton = PySide2.QtWidgets.QWizard.WizardButton.HelpButton
    HelpButtonOnRight = PySide2.QtWidgets.QWizard.WizardOption.HelpButtonOnRight
    IgnoreSubTitles = PySide2.QtWidgets.QWizard.WizardOption.IgnoreSubTitles
    IndependentPages = PySide2.QtWidgets.QWizard.WizardOption.IndependentPages
    LogoPixmap = PySide2.QtWidgets.QWizard.WizardPixmap.LogoPixmap
    MacStyle = PySide2.QtWidgets.QWizard.WizardStyle.MacStyle
    ModernStyle = PySide2.QtWidgets.QWizard.WizardStyle.ModernStyle
    NButtons = PySide2.QtWidgets.QWizard.WizardButton.NButtons
    NextButton = PySide2.QtWidgets.QWizard.WizardButton.NextButton
    NoBackButtonOnLastPage = PySide2.QtWidgets.QWizard.WizardOption.NoBackButtonOnLastPage
    NoBackButtonOnStartPage = PySide2.QtWidgets.QWizard.WizardOption.NoBackButtonOnStartPage
    NoButton = PySide2.QtWidgets.QWizard.WizardButton.NoButton
    NoCancelButton = PySide2.QtWidgets.QWizard.WizardOption.NoCancelButton
    NoCancelButtonOnLastPage = PySide2.QtWidgets.QWizard.WizardOption.NoCancelButtonOnLastPage
    NoDefaultButton = PySide2.QtWidgets.QWizard.WizardOption.NoDefaultButton
    NPixmaps = PySide2.QtWidgets.QWizard.WizardPixmap.NPixmaps
    NStandardButtons = PySide2.QtWidgets.QWizard.WizardButton.NStandardButtons
    NStyles = PySide2.QtWidgets.QWizard.WizardStyle.NStyles
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F508581C0>'
    Stretch = PySide2.QtWidgets.QWizard.WizardButton.Stretch
    WatermarkPixmap = PySide2.QtWidgets.QWizard.WizardPixmap.WatermarkPixmap
    WizardButton = None # (!) real value is "<class 'PySide2.QtWidgets.QWizard.WizardButton'>"
    WizardOption = None # (!) real value is "<class 'PySide2.QtWidgets.QWizard.WizardOption'>"
    WizardOptions = None # (!) real value is "<class 'PySide2.QtWidgets.QWizard.WizardOptions'>"
    WizardPixmap = None # (!) real value is "<class 'PySide2.QtWidgets.QWizard.WizardPixmap'>"
    WizardStyle = None # (!) real value is "<class 'PySide2.QtWidgets.QWizard.WizardStyle'>"


