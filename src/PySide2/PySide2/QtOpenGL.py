# encoding: utf-8
# module PySide2.QtOpenGL
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtOpenGL.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import PySide2.QtWidgets as __PySide2_QtWidgets
import Shiboken as __Shiboken


# no functions
# classes

class QGL(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AccumBuffer = PySide2.QtOpenGL.QGL.FormatOption.AccumBuffer
    AlphaChannel = PySide2.QtOpenGL.QGL.FormatOption.AlphaChannel
    ColorIndex = PySide2.QtOpenGL.QGL.FormatOption.ColorIndex
    DeprecatedFunctions = PySide2.QtOpenGL.QGL.FormatOption.DeprecatedFunctions
    DepthBuffer = PySide2.QtOpenGL.QGL.FormatOption.DepthBuffer
    DirectRendering = PySide2.QtOpenGL.QGL.FormatOption.DirectRendering
    DoubleBuffer = PySide2.QtOpenGL.QGL.FormatOption.DoubleBuffer
    FormatOption = None # (!) real value is "<class 'PySide2.QtOpenGL.QGL.FormatOption'>"
    FormatOptions = None # (!) real value is "<class 'PySide2.QtOpenGL.QGL.FormatOptions'>"
    HasOverlay = PySide2.QtOpenGL.QGL.FormatOption.HasOverlay
    IndirectRendering = PySide2.QtOpenGL.QGL.FormatOption.IndirectRendering
    NoAccumBuffer = PySide2.QtOpenGL.QGL.FormatOption.NoAccumBuffer
    NoAlphaChannel = PySide2.QtOpenGL.QGL.FormatOption.NoAlphaChannel
    NoDeprecatedFunctions = PySide2.QtOpenGL.QGL.FormatOption.NoDeprecatedFunctions
    NoDepthBuffer = PySide2.QtOpenGL.QGL.FormatOption.NoDepthBuffer
    NoOverlay = PySide2.QtOpenGL.QGL.FormatOption.NoOverlay
    NoSampleBuffers = PySide2.QtOpenGL.QGL.FormatOption.NoSampleBuffers
    NoStencilBuffer = PySide2.QtOpenGL.QGL.FormatOption.NoStencilBuffer
    NoStereoBuffers = PySide2.QtOpenGL.QGL.FormatOption.NoStereoBuffers
    Rgba = PySide2.QtOpenGL.QGL.FormatOption.Rgba
    SampleBuffers = PySide2.QtOpenGL.QGL.FormatOption.SampleBuffers
    SingleBuffer = PySide2.QtOpenGL.QGL.FormatOption.SingleBuffer
    StencilBuffer = PySide2.QtOpenGL.QGL.FormatOption.StencilBuffer
    StereoBuffers = PySide2.QtOpenGL.QGL.FormatOption.StereoBuffers


class QGLBuffer(__Shiboken.Object):
    """
    QGLBuffer(self) -> None
    QGLBuffer(self, other: PySide2.QtOpenGL.QGLBuffer) -> None
    QGLBuffer(self, type: PySide2.QtOpenGL.QGLBuffer.Type) -> None
    """
    def allocate(self, count): # real signature unknown; restored from __doc__
        """
        allocate(self, count: int) -> None
        allocate(self, data: int, count: int = -1) -> None
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
        """ map(self, access: PySide2.QtOpenGL.QGLBuffer.Access) -> int """
        return 0

    def read(self, offset, data, count): # real signature unknown; restored from __doc__
        """ read(self, offset: int, data: int, count: int) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """
        release(self) -> None
        release(type: PySide2.QtOpenGL.QGLBuffer.Type) -> None
        """
        pass

    def setUsagePattern(self, value): # real signature unknown; restored from __doc__
        """ setUsagePattern(self, value: PySide2.QtOpenGL.QGLBuffer.UsagePattern) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtOpenGL.QGLBuffer.Type """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) -> bool """
        return False

    def usagePattern(self): # real signature unknown; restored from __doc__
        """ usagePattern(self) -> PySide2.QtOpenGL.QGLBuffer.UsagePattern """
        pass

    def write(self, offset, data, count=-1): # real signature unknown; restored from __doc__
        """ write(self, offset: int, data: int, count: int = -1) -> None """
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

    Access = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLBuffer.Access'>"
    DynamicCopy = PySide2.QtOpenGL.QGLBuffer.UsagePattern.DynamicCopy
    DynamicDraw = PySide2.QtOpenGL.QGLBuffer.UsagePattern.DynamicDraw
    DynamicRead = PySide2.QtOpenGL.QGLBuffer.UsagePattern.DynamicRead
    IndexBuffer = PySide2.QtOpenGL.QGLBuffer.Type.IndexBuffer
    PixelPackBuffer = PySide2.QtOpenGL.QGLBuffer.Type.PixelPackBuffer
    PixelUnpackBuffer = PySide2.QtOpenGL.QGLBuffer.Type.PixelUnpackBuffer
    ReadOnly = PySide2.QtOpenGL.QGLBuffer.Access.ReadOnly
    ReadWrite = PySide2.QtOpenGL.QGLBuffer.Access.ReadWrite
    StaticCopy = PySide2.QtOpenGL.QGLBuffer.UsagePattern.StaticCopy
    StaticDraw = PySide2.QtOpenGL.QGLBuffer.UsagePattern.StaticDraw
    StaticRead = PySide2.QtOpenGL.QGLBuffer.UsagePattern.StaticRead
    StreamCopy = PySide2.QtOpenGL.QGLBuffer.UsagePattern.StreamCopy
    StreamDraw = PySide2.QtOpenGL.QGLBuffer.UsagePattern.StreamDraw
    StreamRead = PySide2.QtOpenGL.QGLBuffer.UsagePattern.StreamRead
    Type = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLBuffer.Type'>"
    UsagePattern = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLBuffer.UsagePattern'>"
    VertexBuffer = PySide2.QtOpenGL.QGLBuffer.Type.VertexBuffer
    WriteOnly = PySide2.QtOpenGL.QGLBuffer.Access.WriteOnly


class QGLColormap(__Shiboken.Object):
    """
    QGLColormap(self) -> None
    QGLColormap(self, arg__1: PySide2.QtOpenGL.QGLColormap) -> None
    """
    def entryColor(self, idx): # real signature unknown; restored from __doc__
        """ entryColor(self, idx: int) -> PySide2.QtGui.QColor """
        pass

    def entryRgb(self, idx): # real signature unknown; restored from __doc__
        """ entryRgb(self, idx: int) -> int """
        return 0

    def find(self, color): # real signature unknown; restored from __doc__
        """ find(self, color: int) -> int """
        return 0

    def findNearest(self, color): # real signature unknown; restored from __doc__
        """ findNearest(self, color: int) -> int """
        return 0

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def setEntry(self, idx, color): # real signature unknown; restored from __doc__
        """
        setEntry(self, idx: int, color: PySide2.QtGui.QColor) -> None
        setEntry(self, idx: int, color: int) -> None
        """
        pass

    def setHandle(self, ahandle): # real signature unknown; restored from __doc__
        """ setHandle(self, ahandle: int) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QGLContext(__Shiboken.Object):
    """ QGLContext(self, format: PySide2.QtOpenGL.QGLFormat) -> None """
    def areSharing(self, context1, context2): # real signature unknown; restored from __doc__
        """ areSharing(context1: PySide2.QtOpenGL.QGLContext, context2: PySide2.QtOpenGL.QGLContext) -> bool """
        return False

    def bindTexture(self, fileName): # real signature unknown; restored from __doc__
        """
        bindTexture(self, fileName: str) -> int
        bindTexture(self, image: PySide2.QtGui.QImage, target: int, format: int, options: PySide2.QtOpenGL.QGLContext.BindOptions) -> int
        bindTexture(self, image: PySide2.QtGui.QImage, target: int = 3553, format: int = 6408) -> int
        bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int, format: int, options: PySide2.QtOpenGL.QGLContext.BindOptions) -> int
        bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int = 3553, format: int = 6408) -> int
        """
        return 0

    def chooseContext(self, shareContext, PySide2_QtOpenGL_QGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ chooseContext(self, shareContext: typing.Optional[PySide2.QtOpenGL.QGLContext] = None) -> bool """
        pass

    def colorIndex(self, c): # real signature unknown; restored from __doc__
        """ colorIndex(self, c: PySide2.QtGui.QColor) -> int """
        return 0

    def contextHandle(self): # real signature unknown; restored from __doc__
        """ contextHandle(self) -> PySide2.QtGui.QOpenGLContext """
        pass

    def create(self, shareContext, PySide2_QtOpenGL_QGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ create(self, shareContext: typing.Optional[PySide2.QtOpenGL.QGLContext] = None) -> bool """
        pass

    def currentContext(self): # real signature unknown; restored from __doc__
        """ currentContext() -> PySide2.QtOpenGL.QGLContext """
        pass

    def deleteTexture(self, tx_id): # real signature unknown; restored from __doc__
        """ deleteTexture(self, tx_id: int) -> None """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtGui.QPaintDevice """
        pass

    def deviceIsPixmap(self): # real signature unknown; restored from __doc__
        """ deviceIsPixmap(self) -> bool """
        return False

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) -> None """
        pass

    def drawTexture(self, point, textureId, textureTarget=3553): # real signature unknown; restored from __doc__
        """
        drawTexture(self, point: PySide2.QtCore.QPointF, textureId: int, textureTarget: int = 3553) -> None
        drawTexture(self, target: PySide2.QtCore.QRectF, textureId: int, textureTarget: int = 3553) -> None
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtOpenGL.QGLFormat """
        pass

    def fromOpenGLContext(self, platformContext): # real signature unknown; restored from __doc__
        """ fromOpenGLContext(platformContext: PySide2.QtGui.QOpenGLContext) -> PySide2.QtOpenGL.QGLContext """
        pass

    def initialized(self): # real signature unknown; restored from __doc__
        """ initialized(self) -> bool """
        return False

    def isSharing(self): # real signature unknown; restored from __doc__
        """ isSharing(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) -> None """
        pass

    def moveToThread(self, thread): # real signature unknown; restored from __doc__
        """ moveToThread(self, thread: PySide2.QtCore.QThread) -> None """
        pass

    def overlayTransparentColor(self): # real signature unknown; restored from __doc__
        """ overlayTransparentColor(self) -> PySide2.QtGui.QColor """
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> PySide2.QtOpenGL.QGLFormat """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def setDevice(self, pDev): # real signature unknown; restored from __doc__
        """ setDevice(self, pDev: PySide2.QtGui.QPaintDevice) -> None """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtOpenGL.QGLFormat) -> None """
        pass

    def setInitialized(self, on): # real signature unknown; restored from __doc__
        """ setInitialized(self, on: bool) -> None """
        pass

    def setTextureCacheLimit(self, size): # real signature unknown; restored from __doc__
        """ setTextureCacheLimit(size: int) -> None """
        pass

    def setValid(self, valid): # real signature unknown; restored from __doc__
        """ setValid(self, valid: bool) -> None """
        pass

    def setWindowCreated(self, on): # real signature unknown; restored from __doc__
        """ setWindowCreated(self, on: bool) -> None """
        pass

    def swapBuffers(self): # real signature unknown; restored from __doc__
        """ swapBuffers(self) -> None """
        pass

    def textureCacheLimit(self): # real signature unknown; restored from __doc__
        """ textureCacheLimit() -> int """
        return 0

    def windowCreated(self): # real signature unknown; restored from __doc__
        """ windowCreated(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, format): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    BindOption = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLContext.BindOption'>"
    BindOptions = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLContext.BindOptions'>"
    CanFlipNativePixmapBindOption = PySide2.QtOpenGL.QGLContext.BindOption.CanFlipNativePixmapBindOption
    DefaultBindOption = PySide2.QtOpenGL.QGLContext.BindOption.DefaultBindOption
    InternalBindOption = PySide2.QtOpenGL.QGLContext.BindOption.InternalBindOption
    InvertedYBindOption = PySide2.QtOpenGL.QGLContext.BindOption.InvertedYBindOption
    LinearFilteringBindOption = PySide2.QtOpenGL.QGLContext.BindOption.LinearFilteringBindOption
    MemoryManagedBindOption = PySide2.QtOpenGL.QGLContext.BindOption.MemoryManagedBindOption
    MipmapBindOption = PySide2.QtOpenGL.QGLContext.BindOption.MipmapBindOption
    NoBindOption = PySide2.QtOpenGL.QGLContext.BindOption.NoBindOption
    PremultipliedAlphaBindOption = PySide2.QtOpenGL.QGLContext.BindOption.PremultipliedAlphaBindOption
    TemporarilyCachedBindOption = PySide2.QtOpenGL.QGLContext.BindOption.TemporarilyCachedBindOption


class QGLFormat(__Shiboken.Object):
    """
    QGLFormat(self) -> None
    QGLFormat(self, options: PySide2.QtOpenGL.QGL.FormatOptions, plane: int = 0) -> None
    QGLFormat(self, other: PySide2.QtOpenGL.QGLFormat) -> None
    """
    def accum(self): # real signature unknown; restored from __doc__
        """ accum(self) -> bool """
        return False

    def accumBufferSize(self): # real signature unknown; restored from __doc__
        """ accumBufferSize(self) -> int """
        return 0

    def alpha(self): # real signature unknown; restored from __doc__
        """ alpha(self) -> bool """
        return False

    def alphaBufferSize(self): # real signature unknown; restored from __doc__
        """ alphaBufferSize(self) -> int """
        return 0

    def blueBufferSize(self): # real signature unknown; restored from __doc__
        """ blueBufferSize(self) -> int """
        return 0

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ defaultFormat() -> PySide2.QtOpenGL.QGLFormat """
        pass

    def defaultOverlayFormat(self): # real signature unknown; restored from __doc__
        """ defaultOverlayFormat() -> PySide2.QtOpenGL.QGLFormat """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> bool """
        return False

    def depthBufferSize(self): # real signature unknown; restored from __doc__
        """ depthBufferSize(self) -> int """
        return 0

    def directRendering(self): # real signature unknown; restored from __doc__
        """ directRendering(self) -> bool """
        return False

    def doubleBuffer(self): # real signature unknown; restored from __doc__
        """ doubleBuffer(self) -> bool """
        return False

    def fromSurfaceFormat(self, format): # real signature unknown; restored from __doc__
        """ fromSurfaceFormat(format: PySide2.QtGui.QSurfaceFormat) -> PySide2.QtOpenGL.QGLFormat """
        pass

    def greenBufferSize(self): # real signature unknown; restored from __doc__
        """ greenBufferSize(self) -> int """
        return 0

    def hasOpenGL(self): # real signature unknown; restored from __doc__
        """ hasOpenGL() -> bool """
        return False

    def hasOpenGLOverlays(self): # real signature unknown; restored from __doc__
        """ hasOpenGLOverlays() -> bool """
        return False

    def hasOverlay(self): # real signature unknown; restored from __doc__
        """ hasOverlay(self) -> bool """
        return False

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ majorVersion(self) -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ minorVersion(self) -> int """
        return 0

    def openGLVersionFlags(self): # real signature unknown; restored from __doc__
        """ openGLVersionFlags() -> PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlags """
        pass

    def plane(self): # real signature unknown; restored from __doc__
        """ plane(self) -> int """
        return 0

    def profile(self): # real signature unknown; restored from __doc__
        """ profile(self) -> PySide2.QtOpenGL.QGLFormat.OpenGLContextProfile """
        pass

    def redBufferSize(self): # real signature unknown; restored from __doc__
        """ redBufferSize(self) -> int """
        return 0

    def rgba(self): # real signature unknown; restored from __doc__
        """ rgba(self) -> bool """
        return False

    def sampleBuffers(self): # real signature unknown; restored from __doc__
        """ sampleBuffers(self) -> bool """
        return False

    def samples(self): # real signature unknown; restored from __doc__
        """ samples(self) -> int """
        return 0

    def setAccum(self, enable): # real signature unknown; restored from __doc__
        """ setAccum(self, enable: bool) -> None """
        pass

    def setAccumBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setAccumBufferSize(self, size: int) -> None """
        pass

    def setAlpha(self, enable): # real signature unknown; restored from __doc__
        """ setAlpha(self, enable: bool) -> None """
        pass

    def setAlphaBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setAlphaBufferSize(self, size: int) -> None """
        pass

    def setBlueBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setBlueBufferSize(self, size: int) -> None """
        pass

    def setDefaultFormat(self, f): # real signature unknown; restored from __doc__
        """ setDefaultFormat(f: PySide2.QtOpenGL.QGLFormat) -> None """
        pass

    def setDefaultOverlayFormat(self, f): # real signature unknown; restored from __doc__
        """ setDefaultOverlayFormat(f: PySide2.QtOpenGL.QGLFormat) -> None """
        pass

    def setDepth(self, enable): # real signature unknown; restored from __doc__
        """ setDepth(self, enable: bool) -> None """
        pass

    def setDepthBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setDepthBufferSize(self, size: int) -> None """
        pass

    def setDirectRendering(self, enable): # real signature unknown; restored from __doc__
        """ setDirectRendering(self, enable: bool) -> None """
        pass

    def setDoubleBuffer(self, enable): # real signature unknown; restored from __doc__
        """ setDoubleBuffer(self, enable: bool) -> None """
        pass

    def setGreenBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setGreenBufferSize(self, size: int) -> None """
        pass

    def setOption(self, opt): # real signature unknown; restored from __doc__
        """ setOption(self, opt: PySide2.QtOpenGL.QGL.FormatOptions) -> None """
        pass

    def setOverlay(self, enable): # real signature unknown; restored from __doc__
        """ setOverlay(self, enable: bool) -> None """
        pass

    def setPlane(self, plane): # real signature unknown; restored from __doc__
        """ setPlane(self, plane: int) -> None """
        pass

    def setProfile(self, profile): # real signature unknown; restored from __doc__
        """ setProfile(self, profile: PySide2.QtOpenGL.QGLFormat.OpenGLContextProfile) -> None """
        pass

    def setRedBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setRedBufferSize(self, size: int) -> None """
        pass

    def setRgba(self, enable): # real signature unknown; restored from __doc__
        """ setRgba(self, enable: bool) -> None """
        pass

    def setSampleBuffers(self, enable): # real signature unknown; restored from __doc__
        """ setSampleBuffers(self, enable: bool) -> None """
        pass

    def setSamples(self, numSamples): # real signature unknown; restored from __doc__
        """ setSamples(self, numSamples: int) -> None """
        pass

    def setStencil(self, enable): # real signature unknown; restored from __doc__
        """ setStencil(self, enable: bool) -> None """
        pass

    def setStencilBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setStencilBufferSize(self, size: int) -> None """
        pass

    def setStereo(self, enable): # real signature unknown; restored from __doc__
        """ setStereo(self, enable: bool) -> None """
        pass

    def setSwapInterval(self, interval): # real signature unknown; restored from __doc__
        """ setSwapInterval(self, interval: int) -> None """
        pass

    def setVersion(self, major, minor): # real signature unknown; restored from __doc__
        """ setVersion(self, major: int, minor: int) -> None """
        pass

    def stencil(self): # real signature unknown; restored from __doc__
        """ stencil(self) -> bool """
        return False

    def stencilBufferSize(self): # real signature unknown; restored from __doc__
        """ stencilBufferSize(self) -> int """
        return 0

    def stereo(self): # real signature unknown; restored from __doc__
        """ stereo(self) -> bool """
        return False

    def swapInterval(self): # real signature unknown; restored from __doc__
        """ swapInterval(self) -> int """
        return 0

    def testOption(self, opt): # real signature unknown; restored from __doc__
        """ testOption(self, opt: PySide2.QtOpenGL.QGL.FormatOptions) -> bool """
        return False

    def toSurfaceFormat(self, format): # real signature unknown; restored from __doc__
        """ toSurfaceFormat(format: PySide2.QtOpenGL.QGLFormat) -> PySide2.QtGui.QSurfaceFormat """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    CompatibilityProfile = PySide2.QtOpenGL.QGLFormat.OpenGLContextProfile.CompatibilityProfile
    CoreProfile = PySide2.QtOpenGL.QGLFormat.OpenGLContextProfile.CoreProfile
    NoProfile = PySide2.QtOpenGL.QGLFormat.OpenGLContextProfile.NoProfile
    OpenGLContextProfile = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLFormat.OpenGLContextProfile'>"
    OpenGLVersionFlag = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag'>"
    OpenGLVersionFlags = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlags'>"
    OpenGL_ES_CommonLite_Version_1_0 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_CommonLite_Version_1_0
    OpenGL_ES_CommonLite_Version_1_1 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_CommonLite_Version_1_1
    OpenGL_ES_Common_Version_1_0 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_Common_Version_1_0
    OpenGL_ES_Common_Version_1_1 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_Common_Version_1_1
    OpenGL_ES_Version_2_0 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_Version_2_0
    OpenGL_Version_1_1 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_1
    OpenGL_Version_1_2 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_2
    OpenGL_Version_1_3 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_3
    OpenGL_Version_1_4 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_4
    OpenGL_Version_1_5 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_5
    OpenGL_Version_2_0 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_2_0
    OpenGL_Version_2_1 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_2_1
    OpenGL_Version_3_0 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_3_0
    OpenGL_Version_3_1 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_3_1
    OpenGL_Version_3_2 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_3_2
    OpenGL_Version_3_3 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_3_3
    OpenGL_Version_4_0 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_4_0
    OpenGL_Version_4_1 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_4_1
    OpenGL_Version_4_2 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_4_2
    OpenGL_Version_4_3 = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_4_3
    OpenGL_Version_None = PySide2.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_None
    __hash__ = None


class QGLFramebufferObject(__PySide2_QtGui.QPaintDevice):
    """
    QGLFramebufferObject(self, size: PySide2.QtCore.QSize, attachment: PySide2.QtOpenGL.QGLFramebufferObject.Attachment, target: int = 3553, internal_format: int = 0) -> None
    QGLFramebufferObject(self, size: PySide2.QtCore.QSize, format: PySide2.QtOpenGL.QGLFramebufferObjectFormat) -> None
    QGLFramebufferObject(self, size: PySide2.QtCore.QSize, target: int = 3553) -> None
    QGLFramebufferObject(self, width: int, height: int, attachment: PySide2.QtOpenGL.QGLFramebufferObject.Attachment, target: int = 3553, internal_format: int = 0) -> None
    QGLFramebufferObject(self, width: int, height: int, format: PySide2.QtOpenGL.QGLFramebufferObjectFormat) -> None
    QGLFramebufferObject(self, width: int, height: int, target: int = 3553) -> None
    """
    def attachment(self): # real signature unknown; restored from __doc__
        """ attachment(self) -> PySide2.QtOpenGL.QGLFramebufferObject.Attachment """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bindDefault(self): # real signature unknown; restored from __doc__
        """ bindDefault() -> bool """
        return False

    def blitFramebuffer(self, target, targetRect, source, sourceRect, buffers=16384, filter=9728): # real signature unknown; restored from __doc__
        """ blitFramebuffer(target: PySide2.QtOpenGL.QGLFramebufferObject, targetRect: PySide2.QtCore.QRect, source: PySide2.QtOpenGL.QGLFramebufferObject, sourceRect: PySide2.QtCore.QRect, buffers: int = 16384, filter: int = 9728) -> None """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def drawTexture(self, point, textureId, textureTarget=3553): # real signature unknown; restored from __doc__
        """
        drawTexture(self, point: PySide2.QtCore.QPointF, textureId: int, textureTarget: int = 3553) -> None
        drawTexture(self, target: PySide2.QtCore.QRectF, textureId: int, textureTarget: int = 3553) -> None
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtOpenGL.QGLFramebufferObjectFormat """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def hasOpenGLFramebufferBlit(self): # real signature unknown; restored from __doc__
        """ hasOpenGLFramebufferBlit() -> bool """
        return False

    def hasOpenGLFramebufferObjects(self): # real signature unknown; restored from __doc__
        """ hasOpenGLFramebufferObjects() -> bool """
        return False

    def isBound(self): # real signature unknown; restored from __doc__
        """ isBound(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> bool """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> int """
        return 0

    def toImage(self): # real signature unknown; restored from __doc__
        """ toImage(self) -> PySide2.QtGui.QImage """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, size, attachment, target=3553, internal_format=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Attachment = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLFramebufferObject.Attachment'>"
    CombinedDepthStencil = PySide2.QtOpenGL.QGLFramebufferObject.Attachment.CombinedDepthStencil
    Depth = PySide2.QtOpenGL.QGLFramebufferObject.Attachment.Depth
    NoAttachment = PySide2.QtOpenGL.QGLFramebufferObject.Attachment.NoAttachment


class QGLFramebufferObjectFormat(__Shiboken.Object):
    """
    QGLFramebufferObjectFormat(self) -> None
    QGLFramebufferObjectFormat(self, other: PySide2.QtOpenGL.QGLFramebufferObjectFormat) -> None
    """
    def attachment(self): # real signature unknown; restored from __doc__
        """ attachment(self) -> PySide2.QtOpenGL.QGLFramebufferObject.Attachment """
        pass

    def internalTextureFormat(self): # real signature unknown; restored from __doc__
        """ internalTextureFormat(self) -> int """
        return 0

    def mipmap(self): # real signature unknown; restored from __doc__
        """ mipmap(self) -> bool """
        return False

    def samples(self): # real signature unknown; restored from __doc__
        """ samples(self) -> int """
        return 0

    def setAttachment(self, attachment): # real signature unknown; restored from __doc__
        """ setAttachment(self, attachment: PySide2.QtOpenGL.QGLFramebufferObject.Attachment) -> None """
        pass

    def setInternalTextureFormat(self, internalTextureFormat): # real signature unknown; restored from __doc__
        """ setInternalTextureFormat(self, internalTextureFormat: int) -> None """
        pass

    def setMipmap(self, enabled): # real signature unknown; restored from __doc__
        """ setMipmap(self, enabled: bool) -> None """
        pass

    def setSamples(self, samples): # real signature unknown; restored from __doc__
        """ setSamples(self, samples: int) -> None """
        pass

    def setTextureTarget(self, target): # real signature unknown; restored from __doc__
        """ setTextureTarget(self, target: int) -> None """
        pass

    def textureTarget(self): # real signature unknown; restored from __doc__
        """ textureTarget(self) -> int """
        return 0

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

    __hash__ = None


class QGLPixelBuffer(__PySide2_QtGui.QPaintDevice):
    """
    QGLPixelBuffer(self, size: PySide2.QtCore.QSize, format: PySide2.QtOpenGL.QGLFormat = Default(QGLFormat.defaultFormat), shareWidget: typing.Optional[PySide2.QtOpenGL.QGLWidget] = None) -> None
    QGLPixelBuffer(self, width: int, height: int, format: PySide2.QtOpenGL.QGLFormat = Default(QGLFormat.defaultFormat), shareWidget: typing.Optional[PySide2.QtOpenGL.QGLWidget] = None) -> None
    """
    def bindTexture(self, fileName): # real signature unknown; restored from __doc__
        """
        bindTexture(self, fileName: str) -> int
        bindTexture(self, image: PySide2.QtGui.QImage, target: int = 3553) -> int
        bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int = 3553) -> int
        """
        return 0

    def bindToDynamicTexture(self, texture): # real signature unknown; restored from __doc__
        """ bindToDynamicTexture(self, texture: int) -> bool """
        return False

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> PySide2.QtOpenGL.QGLContext """
        pass

    def deleteTexture(self, texture_id): # real signature unknown; restored from __doc__
        """ deleteTexture(self, texture_id: int) -> None """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) -> bool """
        return False

    def drawTexture(self, point, textureId, textureTarget=3553): # real signature unknown; restored from __doc__
        """
        drawTexture(self, point: PySide2.QtCore.QPointF, textureId: int, textureTarget: int = 3553) -> None
        drawTexture(self, target: PySide2.QtCore.QRectF, textureId: int, textureTarget: int = 3553) -> None
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtOpenGL.QGLFormat """
        pass

    def generateDynamicTexture(self): # real signature unknown; restored from __doc__
        """ generateDynamicTexture(self) -> int """
        return 0

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def hasOpenGLPbuffers(self): # real signature unknown; restored from __doc__
        """ hasOpenGLPbuffers() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) -> bool """
        return False

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def releaseFromDynamicTexture(self): # real signature unknown; restored from __doc__
        """ releaseFromDynamicTexture(self) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def toImage(self): # real signature unknown; restored from __doc__
        """ toImage(self) -> PySide2.QtGui.QImage """
        pass

    def updateDynamicTexture(self, texture_id): # real signature unknown; restored from __doc__
        """ updateDynamicTexture(self, texture_id: int) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, size, format=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QGLShader(__PySide2_QtCore.QObject):
    """
    QGLShader(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, context: PySide2.QtOpenGL.QGLContext, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QGLShader(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def compileSourceCode(self, source): # real signature unknown; restored from __doc__
        """
        compileSourceCode(self, source: PySide2.QtCore.QByteArray) -> bool
        compileSourceCode(self, source: str) -> bool
        compileSourceCode(self, source: bytes) -> bool
        """
        return False

    def compileSourceFile(self, fileName): # real signature unknown; restored from __doc__
        """ compileSourceFile(self, fileName: str) -> bool """
        return False

    def hasOpenGLShaders(self, type, context, PySide2_QtOpenGL_QGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasOpenGLShaders(type: PySide2.QtOpenGL.QGLShader.ShaderType, context: typing.Optional[PySide2.QtOpenGL.QGLContext] = None) -> bool """
        pass

    def isCompiled(self): # real signature unknown; restored from __doc__
        """ isCompiled(self) -> bool """
        return False

    def log(self): # real signature unknown; restored from __doc__
        """ log(self) -> str """
        return ""

    def shaderId(self): # real signature unknown; restored from __doc__
        """ shaderId(self) -> int """
        return 0

    def shaderType(self): # real signature unknown; restored from __doc__
        """ shaderType(self) -> PySide2.QtOpenGL.QGLShader.ShaderType """
        pass

    def sourceCode(self): # real signature unknown; restored from __doc__
        """ sourceCode(self) -> PySide2.QtCore.QByteArray """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type, context, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Fragment = PySide2.QtOpenGL.QGLShader.ShaderTypeBit.Fragment
    Geometry = PySide2.QtOpenGL.QGLShader.ShaderTypeBit.Geometry
    ShaderType = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLShader.ShaderType'>"
    ShaderTypeBit = None # (!) real value is "<class 'PySide2.QtOpenGL.QGLShader.ShaderTypeBit'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001DF03B20780>'
    Vertex = PySide2.QtOpenGL.QGLShader.ShaderTypeBit.Vertex


class QGLShaderProgram(__PySide2_QtCore.QObject):
    """
    QGLShaderProgram(self, context: PySide2.QtOpenGL.QGLContext, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QGLShaderProgram(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def addShader(self, shader): # real signature unknown; restored from __doc__
        """ addShader(self, shader: PySide2.QtOpenGL.QGLShader) -> bool """
        return False

    def addShaderFromSourceCode(self, type, source): # real signature unknown; restored from __doc__
        """
        addShaderFromSourceCode(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, source: PySide2.QtCore.QByteArray) -> bool
        addShaderFromSourceCode(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, source: str) -> bool
        addShaderFromSourceCode(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, source: bytes) -> bool
        """
        return False

    def addShaderFromSourceFile(self, type, fileName): # real signature unknown; restored from __doc__
        """ addShaderFromSourceFile(self, type: PySide2.QtOpenGL.QGLShader.ShaderType, fileName: str) -> bool """
        return False

    def attributeLocation(self, name): # real signature unknown; restored from __doc__
        """
        attributeLocation(self, name: PySide2.QtCore.QByteArray) -> int
        attributeLocation(self, name: str) -> int
        attributeLocation(self, name: bytes) -> int
        """
        return 0

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bindAttributeLocation(self, name, location): # real signature unknown; restored from __doc__
        """
        bindAttributeLocation(self, name: PySide2.QtCore.QByteArray, location: int) -> None
        bindAttributeLocation(self, name: str, location: int) -> None
        bindAttributeLocation(self, name: bytes, location: int) -> None
        """
        pass

    def disableAttributeArray(self, location): # real signature unknown; restored from __doc__
        """
        disableAttributeArray(self, location: int) -> None
        disableAttributeArray(self, name: bytes) -> None
        """
        pass

    def enableAttributeArray(self, location): # real signature unknown; restored from __doc__
        """
        enableAttributeArray(self, location: int) -> None
        enableAttributeArray(self, name: bytes) -> None
        """
        pass

    def geometryInputType(self): # real signature unknown; restored from __doc__
        """ geometryInputType(self) -> int """
        return 0

    def geometryOutputType(self): # real signature unknown; restored from __doc__
        """ geometryOutputType(self) -> int """
        return 0

    def geometryOutputVertexCount(self): # real signature unknown; restored from __doc__
        """ geometryOutputVertexCount(self) -> int """
        return 0

    def hasOpenGLShaderPrograms(self, context, PySide2_QtOpenGL_QGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasOpenGLShaderPrograms(context: typing.Optional[PySide2.QtOpenGL.QGLContext] = None) -> bool """
        pass

    def isLinked(self): # real signature unknown; restored from __doc__
        """ isLinked(self) -> bool """
        return False

    def link(self): # real signature unknown; restored from __doc__
        """ link(self) -> bool """
        return False

    def log(self): # real signature unknown; restored from __doc__
        """ log(self) -> str """
        return ""

    def maxGeometryOutputVertices(self): # real signature unknown; restored from __doc__
        """ maxGeometryOutputVertices(self) -> int """
        return 0

    def programId(self): # real signature unknown; restored from __doc__
        """ programId(self) -> int """
        return 0

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> None """
        pass

    def removeAllShaders(self): # real signature unknown; restored from __doc__
        """ removeAllShaders(self) -> None """
        pass

    def removeShader(self, shader): # real signature unknown; restored from __doc__
        """ removeShader(self, shader: PySide2.QtOpenGL.QGLShader) -> None """
        pass

    def setAttributeArray2D(self, location, values, stride=0): # real signature unknown; restored from __doc__
        """
        setAttributeArray2D(self, location: int, values: PySide2.QtGui.QVector2D, stride: int = 0) -> None
        setAttributeArray2D(self, name: bytes, values: PySide2.QtGui.QVector2D, stride: int = 0) -> None
        """
        pass

    def setAttributeArray3D(self, location, values, stride=0): # real signature unknown; restored from __doc__
        """
        setAttributeArray3D(self, location: int, values: PySide2.QtGui.QVector3D, stride: int = 0) -> None
        setAttributeArray3D(self, name: bytes, values: PySide2.QtGui.QVector3D, stride: int = 0) -> None
        """
        pass

    def setAttributeArray4D(self, location, values, stride=0): # real signature unknown; restored from __doc__
        """
        setAttributeArray4D(self, location: int, values: PySide2.QtGui.QVector4D, stride: int = 0) -> None
        setAttributeArray4D(self, name: bytes, values: PySide2.QtGui.QVector4D, stride: int = 0) -> None
        """
        pass

    def setAttributeBuffer(self, location, type, offset, tupleSize, stride=0): # real signature unknown; restored from __doc__
        """
        setAttributeBuffer(self, location: int, type: int, offset: int, tupleSize: int, stride: int = 0) -> None
        setAttributeBuffer(self, name: bytes, type: int, offset: int, tupleSize: int, stride: int = 0) -> None
        """
        pass

    def setAttributeValue(self, location, value): # real signature unknown; restored from __doc__
        """
        setAttributeValue(self, location: int, value: float) -> None
        setAttributeValue(self, location: int, value: PySide2.QtGui.QColor) -> None
        setAttributeValue(self, location: int, value: PySide2.QtGui.QVector2D) -> None
        setAttributeValue(self, location: int, value: PySide2.QtGui.QVector3D) -> None
        setAttributeValue(self, location: int, value: PySide2.QtGui.QVector4D) -> None
        setAttributeValue(self, location: int, x: float, y: float) -> None
        setAttributeValue(self, location: int, x: float, y: float, z: float) -> None
        setAttributeValue(self, location: int, x: float, y: float, z: float, w: float) -> None
        setAttributeValue(self, name: bytes, value: float) -> None
        setAttributeValue(self, name: bytes, value: PySide2.QtGui.QColor) -> None
        setAttributeValue(self, name: bytes, value: PySide2.QtGui.QVector2D) -> None
        setAttributeValue(self, name: bytes, value: PySide2.QtGui.QVector3D) -> None
        setAttributeValue(self, name: bytes, value: PySide2.QtGui.QVector4D) -> None
        setAttributeValue(self, name: bytes, x: float, y: float) -> None
        setAttributeValue(self, name: bytes, x: float, y: float, z: float) -> None
        setAttributeValue(self, name: bytes, x: float, y: float, z: float, w: float) -> None
        """
        pass

    def setGeometryInputType(self, inputType): # real signature unknown; restored from __doc__
        """ setGeometryInputType(self, inputType: int) -> None """
        pass

    def setGeometryOutputType(self, outputType): # real signature unknown; restored from __doc__
        """ setGeometryOutputType(self, outputType: int) -> None """
        pass

    def setGeometryOutputVertexCount(self, count): # real signature unknown; restored from __doc__
        """ setGeometryOutputVertexCount(self, count: int) -> None """
        pass

    def setUniformValue(self, location, color): # real signature unknown; restored from __doc__
        """
        setUniformValue(self, location: int, color: PySide2.QtGui.QColor) -> None
        setUniformValue(self, location: int, point: PySide2.QtCore.QPoint) -> None
        setUniformValue(self, location: int, point: PySide2.QtCore.QPointF) -> None
        setUniformValue(self, location: int, size: PySide2.QtCore.QSize) -> None
        setUniformValue(self, location: int, size: PySide2.QtCore.QSizeF) -> None
        setUniformValue(self, location: int, value: float) -> None
        setUniformValue(self, location: int, value: int) -> None
        setUniformValue(self, location: int, value: int) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x2) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x3) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x4) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x2) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x3) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x4) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x2) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x3) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x4) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QTransform) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QVector2D) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QVector3D) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QVector4D) -> None
        setUniformValue(self, location: int, x: float, y: float) -> None
        setUniformValue(self, location: int, x: float, y: float, z: float) -> None
        setUniformValue(self, location: int, x: float, y: float, z: float, w: float) -> None
        setUniformValue(self, name: bytes, color: PySide2.QtGui.QColor) -> None
        setUniformValue(self, name: bytes, point: PySide2.QtCore.QPoint) -> None
        setUniformValue(self, name: bytes, point: PySide2.QtCore.QPointF) -> None
        setUniformValue(self, name: bytes, size: PySide2.QtCore.QSize) -> None
        setUniformValue(self, name: bytes, size: PySide2.QtCore.QSizeF) -> None
        setUniformValue(self, name: bytes, value: float) -> None
        setUniformValue(self, name: bytes, value: int) -> None
        setUniformValue(self, name: bytes, value: int) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix2x2) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix2x3) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix2x4) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix3x2) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix3x3) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix3x4) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix4x2) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix4x3) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix4x4) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QTransform) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QVector2D) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QVector3D) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QVector4D) -> None
        setUniformValue(self, name: bytes, x: float, y: float) -> None
        setUniformValue(self, name: bytes, x: float, y: float, z: float) -> None
        setUniformValue(self, name: bytes, x: float, y: float, z: float, w: float) -> None
        """
        pass

    def setUniformValueArray2D(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray2D(self, location: int, values: PySide2.QtGui.QVector2D, count: int) -> None
        setUniformValueArray2D(self, name: bytes, values: PySide2.QtGui.QVector2D, count: int) -> None
        """
        pass

    def setUniformValueArray2x2(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray2x2(self, location: int, values: PySide2.QtGui.QMatrix2x2, count: int) -> None
        setUniformValueArray2x2(self, name: bytes, values: PySide2.QtGui.QMatrix2x2, count: int) -> None
        """
        pass

    def setUniformValueArray2x3(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray2x3(self, location: int, values: PySide2.QtGui.QMatrix2x3, count: int) -> None
        setUniformValueArray2x3(self, name: bytes, values: PySide2.QtGui.QMatrix2x3, count: int) -> None
        """
        pass

    def setUniformValueArray2x4(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray2x4(self, location: int, values: PySide2.QtGui.QMatrix2x4, count: int) -> None
        setUniformValueArray2x4(self, name: bytes, values: PySide2.QtGui.QMatrix2x4, count: int) -> None
        """
        pass

    def setUniformValueArray3D(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray3D(self, location: int, values: PySide2.QtGui.QVector3D, count: int) -> None
        setUniformValueArray3D(self, name: bytes, values: PySide2.QtGui.QVector3D, count: int) -> None
        """
        pass

    def setUniformValueArray3x2(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray3x2(self, location: int, values: PySide2.QtGui.QMatrix3x2, count: int) -> None
        setUniformValueArray3x2(self, name: bytes, values: PySide2.QtGui.QMatrix3x2, count: int) -> None
        """
        pass

    def setUniformValueArray3x3(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray3x3(self, location: int, values: PySide2.QtGui.QMatrix3x3, count: int) -> None
        setUniformValueArray3x3(self, name: bytes, values: PySide2.QtGui.QMatrix3x3, count: int) -> None
        """
        pass

    def setUniformValueArray3x4(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray3x4(self, location: int, values: PySide2.QtGui.QMatrix3x4, count: int) -> None
        setUniformValueArray3x4(self, name: bytes, values: PySide2.QtGui.QMatrix3x4, count: int) -> None
        """
        pass

    def setUniformValueArray4D(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray4D(self, location: int, values: PySide2.QtGui.QVector4D, count: int) -> None
        setUniformValueArray4D(self, name: bytes, values: PySide2.QtGui.QVector4D, count: int) -> None
        """
        pass

    def setUniformValueArray4x2(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray4x2(self, location: int, values: PySide2.QtGui.QMatrix4x2, count: int) -> None
        setUniformValueArray4x2(self, name: bytes, values: PySide2.QtGui.QMatrix4x2, count: int) -> None
        """
        pass

    def setUniformValueArray4x3(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray4x3(self, location: int, values: PySide2.QtGui.QMatrix4x3, count: int) -> None
        setUniformValueArray4x3(self, name: bytes, values: PySide2.QtGui.QMatrix4x3, count: int) -> None
        """
        pass

    def setUniformValueArray4x4(self, location, values, count): # real signature unknown; restored from __doc__
        """
        setUniformValueArray4x4(self, location: int, values: PySide2.QtGui.QMatrix4x4, count: int) -> None
        setUniformValueArray4x4(self, name: bytes, values: PySide2.QtGui.QMatrix4x4, count: int) -> None
        """
        pass

    def setUniformValueArrayInt(self, location, values, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        setUniformValueArrayInt(self, location: int, values: typing.Sequence[int], count: int) -> None
        setUniformValueArrayInt(self, name: bytes, values: typing.Sequence[int], count: int) -> None
        """
        pass

    def setUniformValueArrayUint(self, location, values, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        setUniformValueArrayUint(self, location: int, values: typing.Sequence[int], count: int) -> None
        setUniformValueArrayUint(self, name: bytes, values: typing.Sequence[int], count: int) -> None
        """
        pass

    def shaders(self): # real signature unknown; restored from __doc__
        """ shaders(self) -> typing.List[PySide2.QtOpenGL.QGLShader] """
        pass

    def uniformLocation(self, name): # real signature unknown; restored from __doc__
        """
        uniformLocation(self, name: PySide2.QtCore.QByteArray) -> int
        uniformLocation(self, name: str) -> int
        uniformLocation(self, name: bytes) -> int
        """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, context, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001DF03B20400>'


class QGLWidget(__PySide2_QtWidgets.QWidget):
    """
    QGLWidget(self, context: PySide2.QtOpenGL.QGLContext, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, shareWidget: typing.Optional[PySide2.QtOpenGL.QGLWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QGLWidget(self, format: PySide2.QtOpenGL.QGLFormat, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, shareWidget: typing.Optional[PySide2.QtOpenGL.QGLWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QGLWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, shareWidget: typing.Optional[PySide2.QtOpenGL.QGLWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    """
    def autoBufferSwap(self): # real signature unknown; restored from __doc__
        """ autoBufferSwap(self) -> bool """
        return False

    def bindTexture(self, fileName): # real signature unknown; restored from __doc__
        """
        bindTexture(self, fileName: str) -> int
        bindTexture(self, image: PySide2.QtGui.QImage, target: int, format: int, options: PySide2.QtOpenGL.QGLContext.BindOptions) -> int
        bindTexture(self, image: PySide2.QtGui.QImage, target: int = 3553, format: int = 6408) -> int
        bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int, format: int, options: PySide2.QtOpenGL.QGLContext.BindOptions) -> int
        bindTexture(self, pixmap: PySide2.QtGui.QPixmap, target: int = 3553, format: int = 6408) -> int
        """
        return 0

    def colormap(self): # real signature unknown; restored from __doc__
        """ colormap(self) -> PySide2.QtOpenGL.QGLColormap """
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> PySide2.QtOpenGL.QGLContext """
        pass

    def convertToGLFormat(self, img): # real signature unknown; restored from __doc__
        """ convertToGLFormat(img: PySide2.QtGui.QImage) -> PySide2.QtGui.QImage """
        pass

    def deleteTexture(self, tx_id): # real signature unknown; restored from __doc__
        """ deleteTexture(self, tx_id: int) -> None """
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ doneCurrent(self) -> None """
        pass

    def doubleBuffer(self): # real signature unknown; restored from __doc__
        """ doubleBuffer(self) -> bool """
        return False

    def drawTexture(self, point, textureId, textureTarget=3553): # real signature unknown; restored from __doc__
        """
        drawTexture(self, point: PySide2.QtCore.QPointF, textureId: int, textureTarget: int = 3553) -> None
        drawTexture(self, target: PySide2.QtCore.QRectF, textureId: int, textureTarget: int = 3553) -> None
        """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtOpenGL.QGLFormat """
        pass

    def glDraw(self): # real signature unknown; restored from __doc__
        """ glDraw(self) -> None """
        pass

    def glInit(self): # real signature unknown; restored from __doc__
        """ glInit(self) -> None """
        pass

    def grabFrameBuffer(self, withAlpha=False): # real signature unknown; restored from __doc__
        """ grabFrameBuffer(self, withAlpha: bool = False) -> PySide2.QtGui.QImage """
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ initializeGL(self) -> None """
        pass

    def initializeOverlayGL(self): # real signature unknown; restored from __doc__
        """ initializeOverlayGL(self) -> None """
        pass

    def isSharing(self): # real signature unknown; restored from __doc__
        """ isSharing(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ makeCurrent(self) -> None """
        pass

    def makeOverlayCurrent(self): # real signature unknown; restored from __doc__
        """ makeOverlayCurrent(self) -> None """
        pass

    def overlayContext(self): # real signature unknown; restored from __doc__
        """ overlayContext(self) -> PySide2.QtOpenGL.QGLContext """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ paintGL(self) -> None """
        pass

    def paintOverlayGL(self): # real signature unknown; restored from __doc__
        """ paintOverlayGL(self) -> None """
        pass

    def qglClearColor(self, c): # real signature unknown; restored from __doc__
        """ qglClearColor(self, c: PySide2.QtGui.QColor) -> None """
        pass

    def qglColor(self, c): # real signature unknown; restored from __doc__
        """ qglColor(self, c: PySide2.QtGui.QColor) -> None """
        pass

    def renderPixmap(self, w=0, h=0, useContext=False): # real signature unknown; restored from __doc__
        """ renderPixmap(self, w: int = 0, h: int = 0, useContext: bool = False) -> PySide2.QtGui.QPixmap """
        pass

    def renderText(self, x, y, z, p_str, fnt=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        renderText(self, x: float, y: float, z: float, str: str, fnt: PySide2.QtGui.QFont = Default(QFont)) -> None
        renderText(self, x: int, y: int, str: str, fnt: PySide2.QtGui.QFont = Default(QFont)) -> None
        """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def resizeGL(self, w, h): # real signature unknown; restored from __doc__
        """ resizeGL(self, w: int, h: int) -> None """
        pass

    def resizeOverlayGL(self, w, h): # real signature unknown; restored from __doc__
        """ resizeOverlayGL(self, w: int, h: int) -> None """
        pass

    def setAutoBufferSwap(self, on): # real signature unknown; restored from __doc__
        """ setAutoBufferSwap(self, on: bool) -> None """
        pass

    def setColormap(self, map): # real signature unknown; restored from __doc__
        """ setColormap(self, map: PySide2.QtOpenGL.QGLColormap) -> None """
        pass

    def swapBuffers(self): # real signature unknown; restored from __doc__
        """ swapBuffers(self) -> None """
        pass

    def updateGL(self): # real signature unknown; restored from __doc__
        """ updateGL(self) -> None """
        pass

    def updateOverlayGL(self): # real signature unknown; restored from __doc__
        """ updateOverlayGL(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, context, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001DF03B20C80>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DF02B217B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtOpenGL', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DF02B217B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtOpenGL.cp310-win_amd64.pyd')"

