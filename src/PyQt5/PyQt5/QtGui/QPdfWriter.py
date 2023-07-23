# encoding: utf-8
# module PyQt5.QtGui
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPagedPaintDevice import QPagedPaintDevice

class QPdfWriter(__PyQt5_QtCore.QObject, QPagedPaintDevice):
    """
    QPdfWriter(filename: str)
    QPdfWriter(device: QIODevice)
    """
    def addFileAttachment(self, fileName, data, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addFileAttachment(self, fileName: str, data: Union[QByteArray, bytes, bytearray], mimeType: str = '') """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def creator(self): # real signature unknown; restored from __doc__
        """ creator(self) -> str """
        return ""

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentXmpMetadata(self): # real signature unknown; restored from __doc__
        """ documentXmpMetadata(self) -> QByteArray """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, id): # real signature unknown; restored from __doc__
        """ metric(self, id: QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ newPage(self) -> bool """
        return False

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        return QPaintEngine

    def pdfVersion(self): # real signature unknown; restored from __doc__
        """ pdfVersion(self) -> QPagedPaintDevice.PdfVersion """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCreator(self, creator): # real signature unknown; restored from __doc__
        """ setCreator(self, creator: str) """
        pass

    def setDocumentXmpMetadata(self, xmpMetadata, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setDocumentXmpMetadata(self, xmpMetadata: Union[QByteArray, bytes, bytearray]) """
        pass

    def setMargins(self, m): # real signature unknown; restored from __doc__
        """ setMargins(self, m: QPagedPaintDevice.Margins) """
        pass

    def setPageSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPageSize(self, size: QPagedPaintDevice.PageSize)
        setPageSize(self, pageSize: QPageSize) -> bool
        """
        return False

    def setPageSizeMM(self, size): # real signature unknown; restored from __doc__
        """ setPageSizeMM(self, size: QSizeF) """
        pass

    def setPdfVersion(self, version): # real signature unknown; restored from __doc__
        """ setPdfVersion(self, version: QPagedPaintDevice.PdfVersion) """
        pass

    def setResolution(self, resolution): # real signature unknown; restored from __doc__
        """ setResolution(self, resolution: int) """
        pass

    def setTitle(self, title): # real signature unknown; restored from __doc__
        """ setTitle(self, title: str) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


