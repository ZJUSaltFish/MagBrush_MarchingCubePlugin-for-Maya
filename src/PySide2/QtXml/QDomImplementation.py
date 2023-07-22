# encoding: utf-8
# module PySide2.QtXml
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtXml.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDomImplementation(__Shiboken.Object):
    """
    QDomImplementation(self) -> None
    QDomImplementation(self, arg__1: PySide2.QtXml.QDomImplementation) -> None
    """
    def createDocument(self, nsURI, qName, doctype): # real signature unknown; restored from __doc__
        """ createDocument(self, nsURI: str, qName: str, doctype: PySide2.QtXml.QDomDocumentType) -> PySide2.QtXml.QDomDocument """
        pass

    def createDocumentType(self, qName, publicId, systemId): # real signature unknown; restored from __doc__
        """ createDocumentType(self, qName: str, publicId: str, systemId: str) -> PySide2.QtXml.QDomDocumentType """
        pass

    def hasFeature(self, feature, version): # real signature unknown; restored from __doc__
        """ hasFeature(self, feature: str, version: str) -> bool """
        return False

    def invalidDataPolicy(self): # real signature unknown; restored from __doc__
        """ invalidDataPolicy() -> PySide2.QtXml.QDomImplementation.InvalidDataPolicy """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def setInvalidDataPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setInvalidDataPolicy(policy: PySide2.QtXml.QDomImplementation.InvalidDataPolicy) -> None """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    AcceptInvalidChars = PySide2.QtXml.QDomImplementation.InvalidDataPolicy.AcceptInvalidChars
    DropInvalidChars = PySide2.QtXml.QDomImplementation.InvalidDataPolicy.DropInvalidChars
    InvalidDataPolicy = None # (!) real value is "<class 'PySide2.QtXml.QDomImplementation.InvalidDataPolicy'>"
    ReturnNullNode = PySide2.QtXml.QDomImplementation.InvalidDataPolicy.ReturnNullNode
    __hash__ = None


