# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QXmlStreamWriter(__Shiboken.Object):
    """
    QXmlStreamWriter(self) -> None
    QXmlStreamWriter(self, array: PySide2.QtCore.QByteArray) -> None
    QXmlStreamWriter(self, device: PySide2.QtCore.QIODevice) -> None
    """
    def autoFormatting(self): # real signature unknown; restored from __doc__
        """ autoFormatting(self) -> bool """
        return False

    def autoFormattingIndent(self): # real signature unknown; restored from __doc__
        """ autoFormattingIndent(self) -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> PySide2.QtCore.QTextCodec """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def setAutoFormatting(self, arg__1): # real signature unknown; restored from __doc__
        """ setAutoFormatting(self, arg__1: bool) -> None """
        pass

    def setAutoFormattingIndent(self, spacesOrTabs): # real signature unknown; restored from __doc__
        """ setAutoFormattingIndent(self, spacesOrTabs: int) -> None """
        pass

    def setCodec(self, codec): # real signature unknown; restored from __doc__
        """
        setCodec(self, codec: PySide2.QtCore.QTextCodec) -> None
        setCodec(self, codecName: bytes) -> None
        """
        pass

    def setDevice(self, device): # real signature unknown; restored from __doc__
        """ setDevice(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def writeAttribute(self, attribute): # real signature unknown; restored from __doc__
        """
        writeAttribute(self, attribute: PySide2.QtCore.QXmlStreamAttribute) -> None
        writeAttribute(self, namespaceUri: str, name: str, value: str) -> None
        writeAttribute(self, qualifiedName: str, value: str) -> None
        """
        pass

    def writeAttributes(self, attributes): # real signature unknown; restored from __doc__
        """ writeAttributes(self, attributes: PySide2.QtCore.QXmlStreamAttributes) -> None """
        pass

    def writeCDATA(self, text): # real signature unknown; restored from __doc__
        """ writeCDATA(self, text: str) -> None """
        pass

    def writeCharacters(self, text): # real signature unknown; restored from __doc__
        """ writeCharacters(self, text: str) -> None """
        pass

    def writeComment(self, text): # real signature unknown; restored from __doc__
        """ writeComment(self, text: str) -> None """
        pass

    def writeCurrentToken(self, reader): # real signature unknown; restored from __doc__
        """ writeCurrentToken(self, reader: PySide2.QtCore.QXmlStreamReader) -> None """
        pass

    def writeDefaultNamespace(self, namespaceUri): # real signature unknown; restored from __doc__
        """ writeDefaultNamespace(self, namespaceUri: str) -> None """
        pass

    def writeDTD(self, dtd): # real signature unknown; restored from __doc__
        """ writeDTD(self, dtd: str) -> None """
        pass

    def writeEmptyElement(self, namespaceUri, name): # real signature unknown; restored from __doc__
        """
        writeEmptyElement(self, namespaceUri: str, name: str) -> None
        writeEmptyElement(self, qualifiedName: str) -> None
        """
        pass

    def writeEndDocument(self): # real signature unknown; restored from __doc__
        """ writeEndDocument(self) -> None """
        pass

    def writeEndElement(self): # real signature unknown; restored from __doc__
        """ writeEndElement(self) -> None """
        pass

    def writeEntityReference(self, name): # real signature unknown; restored from __doc__
        """ writeEntityReference(self, name: str) -> None """
        pass

    def writeNamespace(self, namespaceUri, prefix=''): # real signature unknown; restored from __doc__
        """ writeNamespace(self, namespaceUri: str, prefix: str = '') -> None """
        pass

    def writeProcessingInstruction(self, target, data=''): # real signature unknown; restored from __doc__
        """ writeProcessingInstruction(self, target: str, data: str = '') -> None """
        pass

    def writeStartDocument(self): # real signature unknown; restored from __doc__
        """
        writeStartDocument(self) -> None
        writeStartDocument(self, version: str) -> None
        writeStartDocument(self, version: str, standalone: bool) -> None
        """
        pass

    def writeStartElement(self, namespaceUri, name): # real signature unknown; restored from __doc__
        """
        writeStartElement(self, namespaceUri: str, name: str) -> None
        writeStartElement(self, qualifiedName: str) -> None
        """
        pass

    def writeTextElement(self, namespaceUri, name, text): # real signature unknown; restored from __doc__
        """
        writeTextElement(self, namespaceUri: str, name: str, text: str) -> None
        writeTextElement(self, qualifiedName: str, text: str) -> None
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


