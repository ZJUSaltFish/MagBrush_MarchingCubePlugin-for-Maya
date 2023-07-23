# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QXmlStreamWriter(__sip.simplewrapper):
    """
    QXmlStreamWriter()
    QXmlStreamWriter(device: QIODevice)
    QXmlStreamWriter(array: Union[QByteArray, bytes, bytearray])
    """
    def autoFormatting(self): # real signature unknown; restored from __doc__
        """ autoFormatting(self) -> bool """
        return False

    def autoFormattingIndent(self): # real signature unknown; restored from __doc__
        """ autoFormattingIndent(self) -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> QTextCodec """
        return QTextCodec

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        return QIODevice

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def setAutoFormatting(self, a0): # real signature unknown; restored from __doc__
        """ setAutoFormatting(self, a0: bool) """
        pass

    def setAutoFormattingIndent(self, spaces): # real signature unknown; restored from __doc__
        """ setAutoFormattingIndent(self, spaces: int) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCodec(self, codec: QTextCodec)
        setCodec(self, codecName: str)
        """
        pass

    def setDevice(self, device): # real signature unknown; restored from __doc__
        """ setDevice(self, device: QIODevice) """
        pass

    def writeAttribute(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeAttribute(self, qualifiedName: str, value: str)
        writeAttribute(self, namespaceUri: str, name: str, value: str)
        writeAttribute(self, attribute: QXmlStreamAttribute)
        """
        pass

    def writeAttributes(self, attributes): # real signature unknown; restored from __doc__
        """ writeAttributes(self, attributes: QXmlStreamAttributes) """
        pass

    def writeCDATA(self, text): # real signature unknown; restored from __doc__
        """ writeCDATA(self, text: str) """
        pass

    def writeCharacters(self, text): # real signature unknown; restored from __doc__
        """ writeCharacters(self, text: str) """
        pass

    def writeComment(self, text): # real signature unknown; restored from __doc__
        """ writeComment(self, text: str) """
        pass

    def writeCurrentToken(self, reader): # real signature unknown; restored from __doc__
        """ writeCurrentToken(self, reader: QXmlStreamReader) """
        pass

    def writeDefaultNamespace(self, namespaceUri): # real signature unknown; restored from __doc__
        """ writeDefaultNamespace(self, namespaceUri: str) """
        pass

    def writeDTD(self, dtd): # real signature unknown; restored from __doc__
        """ writeDTD(self, dtd: str) """
        pass

    def writeEmptyElement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeEmptyElement(self, qualifiedName: str)
        writeEmptyElement(self, namespaceUri: str, name: str)
        """
        pass

    def writeEndDocument(self): # real signature unknown; restored from __doc__
        """ writeEndDocument(self) """
        pass

    def writeEndElement(self): # real signature unknown; restored from __doc__
        """ writeEndElement(self) """
        pass

    def writeEntityReference(self, name): # real signature unknown; restored from __doc__
        """ writeEntityReference(self, name: str) """
        pass

    def writeNamespace(self, namespaceUri, prefix=''): # real signature unknown; restored from __doc__
        """ writeNamespace(self, namespaceUri: str, prefix: str = '') """
        pass

    def writeProcessingInstruction(self, target, data=''): # real signature unknown; restored from __doc__
        """ writeProcessingInstruction(self, target: str, data: str = '') """
        pass

    def writeStartDocument(self, version=None, standalone=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeStartDocument(self)
        writeStartDocument(self, version: str)
        writeStartDocument(self, version: str, standalone: bool)
        """
        pass

    def writeStartElement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeStartElement(self, qualifiedName: str)
        writeStartElement(self, namespaceUri: str, name: str)
        """
        pass

    def writeTextElement(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writeTextElement(self, qualifiedName: str, text: str)
        writeTextElement(self, namespaceUri: str, name: str, text: str)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



