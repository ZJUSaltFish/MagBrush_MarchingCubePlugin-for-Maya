# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLBuffer(__Shiboken.Object):
    """
    QOpenGLBuffer(self) -> None
    QOpenGLBuffer(self, other: PySide2.QtGui.QOpenGLBuffer) -> None
    QOpenGLBuffer(self, type: PySide2.QtGui.QOpenGLBuffer.Type) -> None
    """
    def allocate(self, count): # real signature unknown; restored from __doc__
        """
        allocate(self, count: int) -> None
        allocate(self, data: int, count: int) -> None
        """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bufferId(self): # real signature unknown; restored from __doc__
        """ bufferId(self) -> int """
        return 0

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) -> None """
        pass

    def isCreated(self): # real signature unknown; restored from __doc__
        """ isCreated(self) -> bool """
        return False

    def map(self, access): # real signature unknown; restored from __doc__
        """ map(self, access: PySide2.QtGui.QOpenGLBuffer.Access) -> int """
        return 0

    def mapRange(self, offset, count, access): # real signature unknown; restored from __doc__
        """ mapRange(self, offset: int, count: int, access: PySide2.QtGui.QOpenGLBuffer.RangeAccessFlags) -> int """
        return 0

    def read(self, offset, data, count): # real signature unknown; restored from __doc__
        """ read(self, offset: int, data: int, count: int) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """
        release(self) -> None
        release(type: PySide2.QtGui.QOpenGLBuffer.Type) -> None
        """
        pass

    def setUsagePattern(self, value): # real signature unknown; restored from __doc__
        """ setUsagePattern(self, value: PySide2.QtGui.QOpenGLBuffer.UsagePattern) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtGui.QOpenGLBuffer.Type """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) -> bool """
        return False

    def usagePattern(self): # real signature unknown; restored from __doc__
        """ usagePattern(self) -> PySide2.QtGui.QOpenGLBuffer.UsagePattern """
        pass

    def write(self, offset, data, count): # real signature unknown; restored from __doc__
        """ write(self, offset: int, data: int, count: int) -> None """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Access = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLBuffer.Access'>"
    DynamicCopy = PySide2.QtGui.QOpenGLBuffer.UsagePattern.DynamicCopy
    DynamicDraw = PySide2.QtGui.QOpenGLBuffer.UsagePattern.DynamicDraw
    DynamicRead = PySide2.QtGui.QOpenGLBuffer.UsagePattern.DynamicRead
    IndexBuffer = PySide2.QtGui.QOpenGLBuffer.Type.IndexBuffer
    PixelPackBuffer = PySide2.QtGui.QOpenGLBuffer.Type.PixelPackBuffer
    PixelUnpackBuffer = PySide2.QtGui.QOpenGLBuffer.Type.PixelUnpackBuffer
    RangeAccessFlag = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLBuffer.RangeAccessFlag'>"
    RangeAccessFlags = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLBuffer.RangeAccessFlags'>"
    RangeFlushExplicit = PySide2.QtGui.QOpenGLBuffer.RangeAccessFlag.RangeFlushExplicit
    RangeInvalidate = PySide2.QtGui.QOpenGLBuffer.RangeAccessFlag.RangeInvalidate
    RangeInvalidateBuffer = PySide2.QtGui.QOpenGLBuffer.RangeAccessFlag.RangeInvalidateBuffer
    RangeRead = PySide2.QtGui.QOpenGLBuffer.RangeAccessFlag.RangeRead
    RangeUnsynchronized = PySide2.QtGui.QOpenGLBuffer.RangeAccessFlag.RangeUnsynchronized
    RangeWrite = PySide2.QtGui.QOpenGLBuffer.RangeAccessFlag.RangeWrite
    ReadOnly = PySide2.QtGui.QOpenGLBuffer.Access.ReadOnly
    ReadWrite = PySide2.QtGui.QOpenGLBuffer.Access.ReadWrite
    StaticCopy = PySide2.QtGui.QOpenGLBuffer.UsagePattern.StaticCopy
    StaticDraw = PySide2.QtGui.QOpenGLBuffer.UsagePattern.StaticDraw
    StaticRead = PySide2.QtGui.QOpenGLBuffer.UsagePattern.StaticRead
    StreamCopy = PySide2.QtGui.QOpenGLBuffer.UsagePattern.StreamCopy
    StreamDraw = PySide2.QtGui.QOpenGLBuffer.UsagePattern.StreamDraw
    StreamRead = PySide2.QtGui.QOpenGLBuffer.UsagePattern.StreamRead
    Type = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLBuffer.Type'>"
    UsagePattern = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLBuffer.UsagePattern'>"
    VertexBuffer = PySide2.QtGui.QOpenGLBuffer.Type.VertexBuffer
    WriteOnly = PySide2.QtGui.QOpenGLBuffer.Access.WriteOnly


