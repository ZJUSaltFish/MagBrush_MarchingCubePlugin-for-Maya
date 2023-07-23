# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .object import object

class Property(object):
    """ Property(self, type: type, fget: typing.Optional[typing.Callable] = None, fset: typing.Optional[typing.Callable] = None, freset: typing.Optional[typing.Callable] = None, fdel: typing.Optional[typing.Callable] = None, doc: str = '', notify: typing.Optional[typing.Callable] = None, designable: bool = True, scriptable: bool = True, stored: bool = True, user: bool = False, constant: bool = False, final: bool = False) -> PySide2.QtCore.Property """
    def deleter(self, func): # real signature unknown; restored from __doc__
        """ deleter(self, func: typing.Callable) -> None """
        pass

    def getter(self, func): # real signature unknown; restored from __doc__
        """ getter(self, func: typing.Callable) -> None """
        pass

    def read(self, func): # real signature unknown; restored from __doc__
        """ read(self, func: typing.Callable) -> None """
        pass

    def resetter(self, *args, **kwargs): # real signature unknown
        pass

    def setter(self, func): # real signature unknown; restored from __doc__
        """ setter(self, func: typing.Callable) -> None """
        pass

    def write(self, func): # real signature unknown; restored from __doc__
        """ write(self, func: typing.Callable) -> None """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, type, fget, typing_Callable=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    fdel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



