# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPaintEngine(__Shiboken.Object):
    """ QPaintEngine(self, features: PySide2.QtGui.QPaintEngine.PaintEngineFeatures = Default(QPaintEngine.PaintEngineFeatures)) -> None """
    def begin(self, pdev): # real signature unknown; restored from __doc__
        """ begin(self, pdev: PySide2.QtGui.QPaintDevice) -> bool """
        return False

    def clearDirty(self, df): # real signature unknown; restored from __doc__
        """ clearDirty(self, df: PySide2.QtGui.QPaintEngine.DirtyFlags) -> None """
        pass

    def coordinateOffset(self): # real signature unknown; restored from __doc__
        """ coordinateOffset(self) -> PySide2.QtCore.QPoint """
        pass

    def drawEllipse(self, r): # real signature unknown; restored from __doc__
        """
        drawEllipse(self, r: PySide2.QtCore.QRect) -> None
        drawEllipse(self, r: PySide2.QtCore.QRectF) -> None
        """
        pass

    def drawImage(self, r, pm, sr, flags=None): # real signature unknown; restored from __doc__
        """ drawImage(self, r: PySide2.QtCore.QRectF, pm: PySide2.QtGui.QImage, sr: PySide2.QtCore.QRectF, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> None """
        pass

    def drawLines(self, lines, lineCount): # real signature unknown; restored from __doc__
        """
        drawLines(self, lines: PySide2.QtCore.QLine, lineCount: int) -> None
        drawLines(self, lines: PySide2.QtCore.QLineF, lineCount: int) -> None
        """
        pass

    def drawPath(self, path): # real signature unknown; restored from __doc__
        """ drawPath(self, path: PySide2.QtGui.QPainterPath) -> None """
        pass

    def drawPixmap(self, r, pm, sr): # real signature unknown; restored from __doc__
        """ drawPixmap(self, r: PySide2.QtCore.QRectF, pm: PySide2.QtGui.QPixmap, sr: PySide2.QtCore.QRectF) -> None """
        pass

    def drawPoints(self, points, pointCount): # real signature unknown; restored from __doc__
        """
        drawPoints(self, points: PySide2.QtCore.QPoint, pointCount: int) -> None
        drawPoints(self, points: PySide2.QtCore.QPointF, pointCount: int) -> None
        """
        pass

    def drawPolygon(self, points, pointCount, mode): # real signature unknown; restored from __doc__
        """
        drawPolygon(self, points: PySide2.QtCore.QPoint, pointCount: int, mode: PySide2.QtGui.QPaintEngine.PolygonDrawMode) -> None
        drawPolygon(self, points: PySide2.QtCore.QPointF, pointCount: int, mode: PySide2.QtGui.QPaintEngine.PolygonDrawMode) -> None
        """
        pass

    def drawRects(self, rects, rectCount): # real signature unknown; restored from __doc__
        """
        drawRects(self, rects: PySide2.QtCore.QRect, rectCount: int) -> None
        drawRects(self, rects: PySide2.QtCore.QRectF, rectCount: int) -> None
        """
        pass

    def drawTextItem(self, p, textItem): # real signature unknown; restored from __doc__
        """ drawTextItem(self, p: PySide2.QtCore.QPointF, textItem: PySide2.QtGui.QTextItem) -> None """
        pass

    def drawTiledPixmap(self, r, pixmap, s): # real signature unknown; restored from __doc__
        """ drawTiledPixmap(self, r: PySide2.QtCore.QRectF, pixmap: PySide2.QtGui.QPixmap, s: PySide2.QtCore.QPointF) -> None """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> bool """
        return False

    def hasFeature(self, feature): # real signature unknown; restored from __doc__
        """ hasFeature(self, feature: PySide2.QtGui.QPaintEngine.PaintEngineFeatures) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isExtended(self): # real signature unknown; restored from __doc__
        """ isExtended(self) -> bool """
        return False

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> PySide2.QtGui.QPaintDevice """
        pass

    def painter(self): # real signature unknown; restored from __doc__
        """ painter(self) -> PySide2.QtGui.QPainter """
        pass

    def setActive(self, newState): # real signature unknown; restored from __doc__
        """ setActive(self, newState: bool) -> None """
        pass

    def setDirty(self, df): # real signature unknown; restored from __doc__
        """ setDirty(self, df: PySide2.QtGui.QPaintEngine.DirtyFlags) -> None """
        pass

    def setSystemClip(self, baseClip): # real signature unknown; restored from __doc__
        """ setSystemClip(self, baseClip: PySide2.QtGui.QRegion) -> None """
        pass

    def setSystemRect(self, rect): # real signature unknown; restored from __doc__
        """ setSystemRect(self, rect: PySide2.QtCore.QRect) -> None """
        pass

    def syncState(self): # real signature unknown; restored from __doc__
        """ syncState(self) -> None """
        pass

    def systemClip(self): # real signature unknown; restored from __doc__
        """ systemClip(self) -> PySide2.QtGui.QRegion """
        pass

    def systemRect(self): # real signature unknown; restored from __doc__
        """ systemRect(self) -> PySide2.QtCore.QRect """
        pass

    def testDirty(self, df): # real signature unknown; restored from __doc__
        """ testDirty(self, df: PySide2.QtGui.QPaintEngine.DirtyFlags) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtGui.QPaintEngine.Type """
        pass

    def updateState(self, state): # real signature unknown; restored from __doc__
        """ updateState(self, state: PySide2.QtGui.QPaintEngineState) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, features=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gccaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selfDestruct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    AllDirty = PySide2.QtGui.QPaintEngine.DirtyFlag.AllDirty
    AllFeatures = PySide2.QtGui.QPaintEngine.PaintEngineFeature.AllFeatures
    AlphaBlend = PySide2.QtGui.QPaintEngine.PaintEngineFeature.AlphaBlend
    Antialiasing = PySide2.QtGui.QPaintEngine.PaintEngineFeature.Antialiasing
    BlendModes = PySide2.QtGui.QPaintEngine.PaintEngineFeature.BlendModes
    Blitter = PySide2.QtGui.QPaintEngine.Type.Blitter
    BrushStroke = PySide2.QtGui.QPaintEngine.PaintEngineFeature.BrushStroke
    ConicalGradientFill = PySide2.QtGui.QPaintEngine.PaintEngineFeature.ConicalGradientFill
    ConstantOpacity = PySide2.QtGui.QPaintEngine.PaintEngineFeature.ConstantOpacity
    ConvexMode = PySide2.QtGui.QPaintEngine.PolygonDrawMode.ConvexMode
    CoreGraphics = PySide2.QtGui.QPaintEngine.Type.CoreGraphics
    Direct2D = PySide2.QtGui.QPaintEngine.Type.Direct2D
    Direct3D = PySide2.QtGui.QPaintEngine.Type.Direct3D
    DirtyBackground = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyBackground
    DirtyBackgroundMode = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyBackgroundMode
    DirtyBrush = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyBrush
    DirtyBrushOrigin = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyBrushOrigin
    DirtyClipEnabled = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyClipEnabled
    DirtyClipPath = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyClipPath
    DirtyClipRegion = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyClipRegion
    DirtyCompositionMode = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyCompositionMode
    DirtyFlag = None # (!) real value is "<class 'PySide2.QtGui.QPaintEngine.DirtyFlag'>"
    DirtyFlags = None # (!) real value is "<class 'PySide2.QtGui.QPaintEngine.DirtyFlags'>"
    DirtyFont = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyFont
    DirtyHints = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyHints
    DirtyOpacity = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyOpacity
    DirtyPen = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyPen
    DirtyTransform = PySide2.QtGui.QPaintEngine.DirtyFlag.DirtyTransform
    LinearGradientFill = PySide2.QtGui.QPaintEngine.PaintEngineFeature.LinearGradientFill
    MacPrinter = PySide2.QtGui.QPaintEngine.Type.MacPrinter
    MaskedBrush = PySide2.QtGui.QPaintEngine.PaintEngineFeature.MaskedBrush
    MaxUser = PySide2.QtGui.QPaintEngine.Type.MaxUser
    ObjectBoundingModeGradients = PySide2.QtGui.QPaintEngine.PaintEngineFeature.ObjectBoundingModeGradients
    OddEvenMode = PySide2.QtGui.QPaintEngine.PolygonDrawMode.OddEvenMode
    OpenGL = PySide2.QtGui.QPaintEngine.Type.OpenGL
    OpenGL2 = PySide2.QtGui.QPaintEngine.Type.OpenGL2
    OpenVG = PySide2.QtGui.QPaintEngine.Type.OpenVG
    PaintBuffer = PySide2.QtGui.QPaintEngine.Type.PaintBuffer
    PaintEngineFeature = None # (!) real value is "<class 'PySide2.QtGui.QPaintEngine.PaintEngineFeature'>"
    PaintEngineFeatures = None # (!) real value is "<class 'PySide2.QtGui.QPaintEngine.PaintEngineFeatures'>"
    PainterPaths = PySide2.QtGui.QPaintEngine.PaintEngineFeature.PainterPaths
    PaintOutsidePaintEvent = PySide2.QtGui.QPaintEngine.PaintEngineFeature.PaintOutsidePaintEvent
    PatternBrush = PySide2.QtGui.QPaintEngine.PaintEngineFeature.PatternBrush
    PatternTransform = PySide2.QtGui.QPaintEngine.PaintEngineFeature.PatternTransform
    Pdf = PySide2.QtGui.QPaintEngine.Type.Pdf
    PerspectiveTransform = PySide2.QtGui.QPaintEngine.PaintEngineFeature.PerspectiveTransform
    Picture = PySide2.QtGui.QPaintEngine.Type.Picture
    PixmapTransform = PySide2.QtGui.QPaintEngine.PaintEngineFeature.PixmapTransform
    PolygonDrawMode = None # (!) real value is "<class 'PySide2.QtGui.QPaintEngine.PolygonDrawMode'>"
    PolylineMode = PySide2.QtGui.QPaintEngine.PolygonDrawMode.PolylineMode
    PorterDuff = PySide2.QtGui.QPaintEngine.PaintEngineFeature.PorterDuff
    PostScript = PySide2.QtGui.QPaintEngine.Type.PostScript
    PrimitiveTransform = PySide2.QtGui.QPaintEngine.PaintEngineFeature.PrimitiveTransform
    QuickDraw = PySide2.QtGui.QPaintEngine.Type.QuickDraw
    QWindowSystem = PySide2.QtGui.QPaintEngine.Type.QWindowSystem
    RadialGradientFill = PySide2.QtGui.QPaintEngine.PaintEngineFeature.RadialGradientFill
    Raster = PySide2.QtGui.QPaintEngine.Type.Raster
    RasterOpModes = PySide2.QtGui.QPaintEngine.PaintEngineFeature.RasterOpModes
    SVG = PySide2.QtGui.QPaintEngine.Type.SVG
    Type = None # (!) real value is "<class 'PySide2.QtGui.QPaintEngine.Type'>"
    User = PySide2.QtGui.QPaintEngine.Type.User
    WindingMode = PySide2.QtGui.QPaintEngine.PolygonDrawMode.WindingMode
    Windows = PySide2.QtGui.QPaintEngine.Type.Windows
    X11 = PySide2.QtGui.QPaintEngine.Type.X11


