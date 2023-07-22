# encoding: utf-8
# module PyQt5.QtXml
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QXmlReader import QXmlReader

class QXmlSimpleReader(QXmlReader):
    """ QXmlSimpleReader() """
    def contentHandler(self): # real signature unknown; restored from __doc__
        """ contentHandler(self) -> QXmlContentHandler """
        return QXmlContentHandler

    def declHandler(self): # real signature unknown; restored from __doc__
        """ declHandler(self) -> QXmlDeclHandler """
        return QXmlDeclHandler

    def DTDHandler(self): # real signature unknown; restored from __doc__
        """ DTDHandler(self) -> QXmlDTDHandler """
        return QXmlDTDHandler

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ entityResolver(self) -> QXmlEntityResolver """
        return QXmlEntityResolver

    def errorHandler(self): # real signature unknown; restored from __doc__
        """ errorHandler(self) -> QXmlErrorHandler """
        return QXmlErrorHandler

    def feature(self, name): # real signature unknown; restored from __doc__
        """ feature(self, name: str) -> Tuple[bool, bool] """
        pass

    def hasFeature(self, name): # real signature unknown; restored from __doc__
        """ hasFeature(self, name: str) -> bool """
        return False

    def hasProperty(self, name): # real signature unknown; restored from __doc__
        """ hasProperty(self, name: str) -> bool """
        return False

    def lexicalHandler(self): # real signature unknown; restored from __doc__
        """ lexicalHandler(self) -> QXmlLexicalHandler """
        return QXmlLexicalHandler

    def parse(self, input, incremental=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parse(self, input: QXmlInputSource) -> bool
        parse(self, input: QXmlInputSource, incremental: bool) -> bool
        """
        return False

    def parseContinue(self): # real signature unknown; restored from __doc__
        """ parseContinue(self) -> bool """
        return False

    def property(self, name): # real signature unknown; restored from __doc__
        """ property(self, name: str) -> Tuple[PyQt5.sip.voidptr, bool] """
        pass

    def setContentHandler(self, handler): # real signature unknown; restored from __doc__
        """ setContentHandler(self, handler: QXmlContentHandler) """
        pass

    def setDeclHandler(self, handler): # real signature unknown; restored from __doc__
        """ setDeclHandler(self, handler: QXmlDeclHandler) """
        pass

    def setDTDHandler(self, handler): # real signature unknown; restored from __doc__
        """ setDTDHandler(self, handler: QXmlDTDHandler) """
        pass

    def setEntityResolver(self, handler): # real signature unknown; restored from __doc__
        """ setEntityResolver(self, handler: QXmlEntityResolver) """
        pass

    def setErrorHandler(self, handler): # real signature unknown; restored from __doc__
        """ setErrorHandler(self, handler: QXmlErrorHandler) """
        pass

    def setFeature(self, name, value): # real signature unknown; restored from __doc__
        """ setFeature(self, name: str, value: bool) """
        pass

    def setLexicalHandler(self, handler): # real signature unknown; restored from __doc__
        """ setLexicalHandler(self, handler: QXmlLexicalHandler) """
        pass

    def setProperty(self, name, value): # real signature unknown; restored from __doc__
        """ setProperty(self, name: str, value: PyQt5.sip.voidptr) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


