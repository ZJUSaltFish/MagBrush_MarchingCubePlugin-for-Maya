# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QPagedPaintDevice import QPagedPaintDevice

class QPdfWriter(__PySide2_QtCore.QObject, QPagedPaintDevice):
    """
    QPdfWriter(self, device: PySide2.QtCore.QIODevice) -> None
    QPdfWriter(self, filename: str) -> None
    """
    def addFileAttachment(self, fileName, data, mimeType=''): # real signature unknown; restored from __doc__
        """ addFileAttachment(self, fileName: str, data: PySide2.QtCore.QByteArray, mimeType: str = '') -> None """
        pass

    def creator(self): # real signature unknown; restored from __doc__
        """ creator(self) -> str """
        return ""

    def documentXmpMetadata(self): # real signature unknown; restored from __doc__
        """ documentXmpMetadata(self) -> PySide2.QtCore.QByteArray """
        pass

    def metric(self, id): # real signature unknown; restored from __doc__
        """ metric(self, id: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ newPage(self) -> bool """
        return False

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def pdfVersion(self): # real signature unknown; restored from __doc__
        """ pdfVersion(self) -> PySide2.QtGui.QPagedPaintDevice.PdfVersion """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def setCreator(self, creator): # real signature unknown; restored from __doc__
        """ setCreator(self, creator: str) -> None """
        pass

    def setDocumentXmpMetadata(self, xmpMetadata): # real signature unknown; restored from __doc__
        """ setDocumentXmpMetadata(self, xmpMetadata: PySide2.QtCore.QByteArray) -> None """
        pass

    def setMargins(self, m): # real signature unknown; restored from __doc__
        """ setMargins(self, m: PySide2.QtGui.QPagedPaintDevice.Margins) -> None """
        pass

    def setPageSize(self, size): # real signature unknown; restored from __doc__
        """ setPageSize(self, size: PySide2.QtGui.QPagedPaintDevice.PageSize) -> None """
        pass

    def setPageSizeMM(self, size): # real signature unknown; restored from __doc__
        """ setPageSizeMM(self, size: PySide2.QtCore.QSizeF) -> None """
        pass

    def setPdfVersion(self, version): # real signature unknown; restored from __doc__
        """ setPdfVersion(self, version: PySide2.QtGui.QPagedPaintDevice.PdfVersion) -> None """
        pass

    def setResolution(self, resolution): # real signature unknown; restored from __doc__
        """ setResolution(self, resolution: int) -> None """
        pass

    def setTitle(self, title): # real signature unknown; restored from __doc__
        """ setTitle(self, title: str) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, device): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F008451C0>'


