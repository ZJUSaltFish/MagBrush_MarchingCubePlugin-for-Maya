# encoding: utf-8
# module PyQt5.pylupdate
# from D:\Maya2024\Python\lib\site-packages\PyQt5\pylupdate.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


# functions

def fetchtr_py(fileName, tor, defaultContext, mustExist, codecForSource, tr_func, translate_func): # real signature unknown; restored from __doc__
    """ fetchtr_py(fileName: bytes, tor: MetaTranslator, defaultContext: str, mustExist: bool, codecForSource: str, tr_func: str, translate_func: str) """
    pass

def fetchtr_ui(fileName, tor, defaultContext, mustExist): # real signature unknown; restored from __doc__
    """ fetchtr_ui(fileName: bytes, tor: MetaTranslator, defaultContext: str, mustExist: bool) """
    pass

def merge(tor, virginTor, out, noObsolete, verbose, filename): # real signature unknown; restored from __doc__
    """ merge(tor: MetaTranslator, virginTor: MetaTranslator, out: MetaTranslator, noObsolete: bool, verbose: bool, filename: str) """
    pass

def proFileTagMap(text): # real signature unknown; restored from __doc__
    """ proFileTagMap(text: str) -> Dict[str, str] """
    return {}

# classes

class MetaTranslator(__sip.simplewrapper):
    """
    MetaTranslator()
    MetaTranslator(tor: MetaTranslator)
    """
    def load(self, filename): # real signature unknown; restored from __doc__
        """ load(self, filename: str) -> bool """
        return False

    def save(self, filename): # real signature unknown; restored from __doc__
        """ save(self, filename: str) -> bool """
        return False

    def setCodec(self, name): # real signature unknown; restored from __doc__
        """ setCodec(self, name: str) """
        pass

    def stripEmptyContexts(self): # real signature unknown; restored from __doc__
        """ stripEmptyContexts(self) """
        pass

    def stripObsoleteMessages(self): # real signature unknown; restored from __doc__
        """ stripObsoleteMessages(self) """
        pass

    def __init__(self, tor=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values



