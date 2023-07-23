# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPainter(__Shiboken.Object):
    """
    QPainter(self) -> None
    QPainter(self, arg__1: PySide2.QtGui.QPaintDevice) -> None
    """
    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> PySide2.QtGui.QBrush """
        pass

    def backgroundMode(self): # real signature unknown; restored from __doc__
        """ backgroundMode(self) -> PySide2.QtCore.Qt.BGMode """
        pass

    def begin(self, arg__1): # real signature unknown; restored from __doc__
        """ begin(self, arg__1: PySide2.QtGui.QPaintDevice) -> bool """
        return False

    def beginNativePainting(self): # real signature unknown; restored from __doc__
        """ beginNativePainting(self) -> None """
        pass

    def boundingRect(self, rect, flags, text): # real signature unknown; restored from __doc__
        """
        boundingRect(self, rect: PySide2.QtCore.QRect, flags: int, text: str) -> PySide2.QtCore.QRect
        boundingRect(self, rect: PySide2.QtCore.QRectF, flags: int, text: str) -> PySide2.QtCore.QRectF
        boundingRect(self, rect: PySide2.QtCore.QRectF, text: str, o: PySide2.QtGui.QTextOption = Default(QTextOption)) -> PySide2.QtCore.QRectF
        boundingRect(self, x: int, y: int, w: int, h: int, flags: int, text: str) -> PySide2.QtCore.QRect
        """
        pass

    def brush(self): # real signature unknown; restored from __doc__
        """ brush(self) -> PySide2.QtGui.QBrush """
        pass

    def brushOrigin(self): # real signature unknown; restored from __doc__
        """ brushOrigin(self) -> PySide2.QtCore.QPoint """
        pass

    def clipBoundingRect(self): # real signature unknown; restored from __doc__
        """ clipBoundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ clipPath(self) -> PySide2.QtGui.QPainterPath """
        pass

    def clipRegion(self): # real signature unknown; restored from __doc__
        """ clipRegion(self) -> PySide2.QtGui.QRegion """
        pass

    def combinedMatrix(self): # real signature unknown; restored from __doc__
        """ combinedMatrix(self) -> PySide2.QtGui.QMatrix """
        pass

    def combinedTransform(self): # real signature unknown; restored from __doc__
        """ combinedTransform(self) -> PySide2.QtGui.QTransform """
        pass

    def compositionMode(self): # real signature unknown; restored from __doc__
        """ compositionMode(self) -> PySide2.QtGui.QPainter.CompositionMode """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtGui.QPaintDevice """
        pass

    def deviceMatrix(self): # real signature unknown; restored from __doc__
        """ deviceMatrix(self) -> PySide2.QtGui.QMatrix """
        pass

    def deviceTransform(self): # real signature unknown; restored from __doc__
        """ deviceTransform(self) -> PySide2.QtGui.QTransform """
        pass

    def drawArc(self, arg__1, a, alen): # real signature unknown; restored from __doc__
        """
        drawArc(self, arg__1: PySide2.QtCore.QRect, a: int, alen: int) -> None
        drawArc(self, rect: PySide2.QtCore.QRectF, a: int, alen: int) -> None
        drawArc(self, x: int, y: int, w: int, h: int, a: int, alen: int) -> None
        """
        pass

    def drawChord(self, arg__1, a, alen): # real signature unknown; restored from __doc__
        """
        drawChord(self, arg__1: PySide2.QtCore.QRect, a: int, alen: int) -> None
        drawChord(self, rect: PySide2.QtCore.QRectF, a: int, alen: int) -> None
        drawChord(self, x: int, y: int, w: int, h: int, a: int, alen: int) -> None
        """
        pass

    def drawConvexPolygon(self, arg__1, PySide2_QtCore_QPointF=None): # real signature unknown; restored from __doc__
        """
        drawConvexPolygon(self, arg__1: typing.List[PySide2.QtCore.QPointF]) -> None
        drawConvexPolygon(self, arg__1: typing.List[PySide2.QtCore.QPoint]) -> None
        drawConvexPolygon(self, polygon: PySide2.QtGui.QPolygon) -> None
        drawConvexPolygon(self, polygon: PySide2.QtGui.QPolygonF) -> None
        """
        pass

    def drawEllipse(self, center, rx, ry): # real signature unknown; restored from __doc__
        """
        drawEllipse(self, center: PySide2.QtCore.QPoint, rx: int, ry: int) -> None
        drawEllipse(self, center: PySide2.QtCore.QPointF, rx: float, ry: float) -> None
        drawEllipse(self, r: PySide2.QtCore.QRect) -> None
        drawEllipse(self, r: PySide2.QtCore.QRectF) -> None
        drawEllipse(self, x: int, y: int, w: int, h: int) -> None
        """
        pass

    def drawImage(self, p, image): # real signature unknown; restored from __doc__
        """
        drawImage(self, p: PySide2.QtCore.QPoint, image: PySide2.QtGui.QImage) -> None
        drawImage(self, p: PySide2.QtCore.QPoint, image: PySide2.QtGui.QImage, sr: PySide2.QtCore.QRect, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> None
        drawImage(self, p: PySide2.QtCore.QPointF, image: PySide2.QtGui.QImage) -> None
        drawImage(self, p: PySide2.QtCore.QPointF, image: PySide2.QtGui.QImage, sr: PySide2.QtCore.QRectF, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> None
        drawImage(self, r: PySide2.QtCore.QRect, image: PySide2.QtGui.QImage) -> None
        drawImage(self, r: PySide2.QtCore.QRectF, image: PySide2.QtGui.QImage) -> None
        drawImage(self, targetRect: PySide2.QtCore.QRect, image: PySide2.QtGui.QImage, sourceRect: PySide2.QtCore.QRect, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> None
        drawImage(self, targetRect: PySide2.QtCore.QRectF, image: PySide2.QtGui.QImage, sourceRect: PySide2.QtCore.QRectF, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> None
        drawImage(self, x: int, y: int, image: PySide2.QtGui.QImage, sx: int = 0, sy: int = 0, sw: int = -1, sh: int = -1, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> None
        """
        pass

    def drawLine(self, line): # real signature unknown; restored from __doc__
        """
        drawLine(self, line: PySide2.QtCore.QLine) -> None
        drawLine(self, line: PySide2.QtCore.QLineF) -> None
        drawLine(self, p1: PySide2.QtCore.QPoint, p2: PySide2.QtCore.QPoint) -> None
        drawLine(self, p1: PySide2.QtCore.QPointF, p2: PySide2.QtCore.QPointF) -> None
        drawLine(self, x1: int, y1: int, x2: int, y2: int) -> None
        """
        pass

    def drawLines(self, lines, PySide2_QtCore_QLineF=None): # real signature unknown; restored from __doc__
        """
        drawLines(self, lines: typing.List[PySide2.QtCore.QLineF]) -> None
        drawLines(self, lines: typing.List[PySide2.QtCore.QLine]) -> None
        drawLines(self, pointPairs: typing.List[PySide2.QtCore.QPointF]) -> None
        drawLines(self, pointPairs: typing.List[PySide2.QtCore.QPoint]) -> None
        """
        pass

    def drawPath(self, path): # real signature unknown; restored from __doc__
        """ drawPath(self, path: PySide2.QtGui.QPainterPath) -> None """
        pass

    def drawPicture(self, p, picture): # real signature unknown; restored from __doc__
        """
        drawPicture(self, p: PySide2.QtCore.QPoint, picture: PySide2.QtGui.QPicture) -> None
        drawPicture(self, p: PySide2.QtCore.QPointF, picture: PySide2.QtGui.QPicture) -> None
        drawPicture(self, x: int, y: int, picture: PySide2.QtGui.QPicture) -> None
        """
        pass

    def drawPie(self, arg__1, a, alen): # real signature unknown; restored from __doc__
        """
        drawPie(self, arg__1: PySide2.QtCore.QRect, a: int, alen: int) -> None
        drawPie(self, rect: PySide2.QtCore.QRectF, a: int, alen: int) -> None
        drawPie(self, x: int, y: int, w: int, h: int, a: int, alen: int) -> None
        """
        pass

    def drawPixmap(self, p, pm): # real signature unknown; restored from __doc__
        """
        drawPixmap(self, p: PySide2.QtCore.QPoint, pm: PySide2.QtGui.QPixmap) -> None
        drawPixmap(self, p: PySide2.QtCore.QPoint, pm: PySide2.QtGui.QPixmap, sr: PySide2.QtCore.QRect) -> None
        drawPixmap(self, p: PySide2.QtCore.QPointF, pm: PySide2.QtGui.QPixmap) -> None
        drawPixmap(self, p: PySide2.QtCore.QPointF, pm: PySide2.QtGui.QPixmap, sr: PySide2.QtCore.QRectF) -> None
        drawPixmap(self, r: PySide2.QtCore.QRect, pm: PySide2.QtGui.QPixmap) -> None
        drawPixmap(self, targetRect: PySide2.QtCore.QRect, pixmap: PySide2.QtGui.QPixmap, sourceRect: PySide2.QtCore.QRect) -> None
        drawPixmap(self, targetRect: PySide2.QtCore.QRectF, pixmap: PySide2.QtGui.QPixmap, sourceRect: PySide2.QtCore.QRectF) -> None
        drawPixmap(self, x: int, y: int, pm: PySide2.QtGui.QPixmap) -> None
        drawPixmap(self, x: int, y: int, pm: PySide2.QtGui.QPixmap, sx: int, sy: int, sw: int, sh: int) -> None
        drawPixmap(self, x: int, y: int, w: int, h: int, pm: PySide2.QtGui.QPixmap) -> None
        drawPixmap(self, x: int, y: int, w: int, h: int, pm: PySide2.QtGui.QPixmap, sx: int, sy: int, sw: int, sh: int) -> None
        """
        pass

    def drawPixmapFragments(self, fragments, fragmentCount, pixmap, hints=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPixmapFragments(self, fragments: PySide2.QtGui.QPainter.PixmapFragment, fragmentCount: int, pixmap: PySide2.QtGui.QPixmap, hints: PySide2.QtGui.QPainter.PixmapFragmentHints = Default(QPainter.PixmapFragmentHints)) -> None """
        pass

    def drawPoint(self, p): # real signature unknown; restored from __doc__
        """
        drawPoint(self, p: PySide2.QtCore.QPoint) -> None
        drawPoint(self, pt: PySide2.QtCore.QPointF) -> None
        drawPoint(self, x: int, y: int) -> None
        """
        pass

    def drawPoints(self, arg__1, PySide2_QtCore_QPointF=None): # real signature unknown; restored from __doc__
        """
        drawPoints(self, arg__1: typing.List[PySide2.QtCore.QPointF]) -> None
        drawPoints(self, arg__1: typing.List[PySide2.QtCore.QPoint]) -> None
        drawPoints(self, points: PySide2.QtGui.QPolygon) -> None
        drawPoints(self, points: PySide2.QtGui.QPolygonF) -> None
        """
        pass

    def drawPolygon(self, arg__1, PySide2_QtCore_QPointF=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        drawPolygon(self, arg__1: typing.List[PySide2.QtCore.QPointF], arg__2: PySide2.QtCore.Qt.FillRule) -> None
        drawPolygon(self, arg__1: typing.List[PySide2.QtCore.QPoint], arg__2: PySide2.QtCore.Qt.FillRule) -> None
        drawPolygon(self, polygon: PySide2.QtGui.QPolygon, fillRule: PySide2.QtCore.Qt.FillRule = PySide2.QtCore.Qt.FillRule.OddEvenFill) -> None
        drawPolygon(self, polygon: PySide2.QtGui.QPolygonF, fillRule: PySide2.QtCore.Qt.FillRule = PySide2.QtCore.Qt.FillRule.OddEvenFill) -> None
        """
        pass

    def drawPolyline(self, arg__1, PySide2_QtCore_QPointF=None): # real signature unknown; restored from __doc__
        """
        drawPolyline(self, arg__1: typing.List[PySide2.QtCore.QPointF]) -> None
        drawPolyline(self, arg__1: typing.List[PySide2.QtCore.QPoint]) -> None
        drawPolyline(self, polygon: PySide2.QtGui.QPolygon) -> None
        drawPolyline(self, polyline: PySide2.QtGui.QPolygonF) -> None
        """
        pass

    def drawRect(self, rect): # real signature unknown; restored from __doc__
        """
        drawRect(self, rect: PySide2.QtCore.QRect) -> None
        drawRect(self, rect: PySide2.QtCore.QRectF) -> None
        drawRect(self, x1: int, y1: int, w: int, h: int) -> None
        """
        pass

    def drawRects(self, rectangles, PySide2_QtCore_QRectF=None): # real signature unknown; restored from __doc__
        """
        drawRects(self, rectangles: typing.List[PySide2.QtCore.QRectF]) -> None
        drawRects(self, rectangles: typing.List[PySide2.QtCore.QRect]) -> None
        """
        pass

    def drawRoundedRect(self, rect, xRadius, yRadius, mode=None): # real signature unknown; restored from __doc__
        """
        drawRoundedRect(self, rect: PySide2.QtCore.QRect, xRadius: float, yRadius: float, mode: PySide2.QtCore.Qt.SizeMode = PySide2.QtCore.Qt.SizeMode.AbsoluteSize) -> None
        drawRoundedRect(self, rect: PySide2.QtCore.QRectF, xRadius: float, yRadius: float, mode: PySide2.QtCore.Qt.SizeMode = PySide2.QtCore.Qt.SizeMode.AbsoluteSize) -> None
        drawRoundedRect(self, x: int, y: int, w: int, h: int, xRadius: float, yRadius: float, mode: PySide2.QtCore.Qt.SizeMode = PySide2.QtCore.Qt.SizeMode.AbsoluteSize) -> None
        """
        pass

    def drawRoundRect(self, r, xround=25, yround=25): # real signature unknown; restored from __doc__
        """
        drawRoundRect(self, r: PySide2.QtCore.QRect, xround: int = 25, yround: int = 25) -> None
        drawRoundRect(self, r: PySide2.QtCore.QRectF, xround: int = 25, yround: int = 25) -> None
        drawRoundRect(self, x: int, y: int, w: int, h: int, xRound: int = 25, yRound: int = 25) -> None
        """
        pass

    def drawStaticText(self, left, top, staticText): # real signature unknown; restored from __doc__
        """
        drawStaticText(self, left: int, top: int, staticText: PySide2.QtGui.QStaticText) -> None
        drawStaticText(self, topLeftPosition: PySide2.QtCore.QPoint, staticText: PySide2.QtGui.QStaticText) -> None
        drawStaticText(self, topLeftPosition: PySide2.QtCore.QPointF, staticText: PySide2.QtGui.QStaticText) -> None
        """
        pass

    def drawText(self, p, s): # real signature unknown; restored from __doc__
        """
        drawText(self, p: PySide2.QtCore.QPoint, s: str) -> None
        drawText(self, p: PySide2.QtCore.QPointF, s: str) -> None
        drawText(self, r: PySide2.QtCore.QRect, flags: int, text: str, br: PySide2.QtCore.QRect) -> None
        drawText(self, r: PySide2.QtCore.QRectF, flags: int, text: str, br: PySide2.QtCore.QRectF) -> None
        drawText(self, r: PySide2.QtCore.QRectF, text: str, o: PySide2.QtGui.QTextOption = Default(QTextOption)) -> None
        drawText(self, x: int, y: int, s: str) -> None
        drawText(self, x: int, y: int, w: int, h: int, flags: int, text: str, br: PySide2.QtCore.QRect) -> None
        """
        pass

    def drawTextItem(self, p, ti): # real signature unknown; restored from __doc__
        """
        drawTextItem(self, p: PySide2.QtCore.QPoint, ti: PySide2.QtGui.QTextItem) -> None
        drawTextItem(self, p: PySide2.QtCore.QPointF, ti: PySide2.QtGui.QTextItem) -> None
        drawTextItem(self, x: int, y: int, ti: PySide2.QtGui.QTextItem) -> None
        """
        pass

    def drawTiledPixmap(self, arg__1, arg__2, pos=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        drawTiledPixmap(self, arg__1: PySide2.QtCore.QRect, arg__2: PySide2.QtGui.QPixmap, pos: PySide2.QtCore.QPoint = Default(QPoint)) -> None
        drawTiledPixmap(self, rect: PySide2.QtCore.QRectF, pm: PySide2.QtGui.QPixmap, offset: PySide2.QtCore.QPointF = Default(QPointF)) -> None
        drawTiledPixmap(self, x: int, y: int, w: int, h: int, arg__5: PySide2.QtGui.QPixmap, sx: int = 0, sy: int = 0) -> None
        """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> bool """
        return False

    def endNativePainting(self): # real signature unknown; restored from __doc__
        """ endNativePainting(self) -> None """
        pass

    def eraseRect(self, arg__1): # real signature unknown; restored from __doc__
        """
        eraseRect(self, arg__1: PySide2.QtCore.QRect) -> None
        eraseRect(self, arg__1: PySide2.QtCore.QRectF) -> None
        eraseRect(self, x: int, y: int, w: int, h: int) -> None
        """
        pass

    def fillPath(self, path, brush): # real signature unknown; restored from __doc__
        """ fillPath(self, path: PySide2.QtGui.QPainterPath, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def fillRect(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        fillRect(self, arg__1: PySide2.QtCore.QRect, arg__2: PySide2.QtGui.QBrush) -> None
        fillRect(self, arg__1: PySide2.QtCore.QRect, color: PySide2.QtGui.QColor) -> None
        fillRect(self, arg__1: PySide2.QtCore.QRectF, arg__2: PySide2.QtGui.QBrush) -> None
        fillRect(self, arg__1: PySide2.QtCore.QRectF, color: PySide2.QtGui.QColor) -> None
        fillRect(self, r: PySide2.QtCore.QRect, c: PySide2.QtCore.Qt.GlobalColor) -> None
        fillRect(self, r: PySide2.QtCore.QRect, preset: PySide2.QtGui.QGradient.Preset) -> None
        fillRect(self, r: PySide2.QtCore.QRect, style: PySide2.QtCore.Qt.BrushStyle) -> None
        fillRect(self, r: PySide2.QtCore.QRectF, c: PySide2.QtCore.Qt.GlobalColor) -> None
        fillRect(self, r: PySide2.QtCore.QRectF, preset: PySide2.QtGui.QGradient.Preset) -> None
        fillRect(self, r: PySide2.QtCore.QRectF, style: PySide2.QtCore.Qt.BrushStyle) -> None
        fillRect(self, x: int, y: int, w: int, h: int, arg__5: PySide2.QtGui.QBrush) -> None
        fillRect(self, x: int, y: int, w: int, h: int, c: PySide2.QtCore.Qt.GlobalColor) -> None
        fillRect(self, x: int, y: int, w: int, h: int, color: PySide2.QtGui.QColor) -> None
        fillRect(self, x: int, y: int, w: int, h: int, preset: PySide2.QtGui.QGradient.Preset) -> None
        fillRect(self, x: int, y: int, w: int, h: int, style: PySide2.QtCore.Qt.BrushStyle) -> None
        """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def fontInfo(self): # real signature unknown; restored from __doc__
        """ fontInfo(self) -> PySide2.QtGui.QFontInfo """
        pass

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics(self) -> PySide2.QtGui.QFontMetrics """
        pass

    def hasClipping(self): # real signature unknown; restored from __doc__
        """ hasClipping(self) -> bool """
        return False

    def initFrom(self, device): # real signature unknown; restored from __doc__
        """ initFrom(self, device: PySide2.QtGui.QPaintDevice) -> None """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> PySide2.QtCore.Qt.LayoutDirection """
        pass

    def matrix(self): # real signature unknown; restored from __doc__
        """ matrix(self) -> PySide2.QtGui.QMatrix """
        pass

    def matrixEnabled(self): # real signature unknown; restored from __doc__
        """ matrixEnabled(self) -> bool """
        return False

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def pen(self): # real signature unknown; restored from __doc__
        """ pen(self) -> PySide2.QtGui.QPen """
        pass

    def redirected(self, device, offset, PySide2_QtCore_QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ redirected(device: PySide2.QtGui.QPaintDevice, offset: typing.Optional[PySide2.QtCore.QPoint] = None) -> PySide2.QtGui.QPaintDevice """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> PySide2.QtGui.QPainter.RenderHints """
        pass

    def resetMatrix(self): # real signature unknown; restored from __doc__
        """ resetMatrix(self) -> None """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) -> None """
        pass

    def restore(self): # real signature unknown; restored from __doc__
        """ restore(self) -> None """
        pass

    def restoreRedirected(self, device): # real signature unknown; restored from __doc__
        """ restoreRedirected(device: PySide2.QtGui.QPaintDevice) -> None """
        pass

    def rotate(self, a): # real signature unknown; restored from __doc__
        """ rotate(self, a: float) -> None """
        pass

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) -> None """
        pass

    def scale(self, sx, sy): # real signature unknown; restored from __doc__
        """ scale(self, sx: float, sy: float) -> None """
        pass

    def setBackground(self, bg): # real signature unknown; restored from __doc__
        """ setBackground(self, bg: PySide2.QtGui.QBrush) -> None """
        pass

    def setBackgroundMode(self, mode): # real signature unknown; restored from __doc__
        """ setBackgroundMode(self, mode: PySide2.QtCore.Qt.BGMode) -> None """
        pass

    def setBrush(self, brush): # real signature unknown; restored from __doc__
        """
        setBrush(self, brush: PySide2.QtGui.QBrush) -> None
        setBrush(self, style: PySide2.QtCore.Qt.BrushStyle) -> None
        """
        pass

    def setBrushOrigin(self, arg__1): # real signature unknown; restored from __doc__
        """
        setBrushOrigin(self, arg__1: PySide2.QtCore.QPoint) -> None
        setBrushOrigin(self, arg__1: PySide2.QtCore.QPointF) -> None
        setBrushOrigin(self, x: int, y: int) -> None
        """
        pass

    def setClipPath(self, path, op=None): # real signature unknown; restored from __doc__
        """ setClipPath(self, path: PySide2.QtGui.QPainterPath, op: PySide2.QtCore.Qt.ClipOperation = PySide2.QtCore.Qt.ClipOperation.ReplaceClip) -> None """
        pass

    def setClipping(self, enable): # real signature unknown; restored from __doc__
        """ setClipping(self, enable: bool) -> None """
        pass

    def setClipRect(self, arg__1, op=None): # real signature unknown; restored from __doc__
        """
        setClipRect(self, arg__1: PySide2.QtCore.QRect, op: PySide2.QtCore.Qt.ClipOperation = PySide2.QtCore.Qt.ClipOperation.ReplaceClip) -> None
        setClipRect(self, arg__1: PySide2.QtCore.QRectF, op: PySide2.QtCore.Qt.ClipOperation = PySide2.QtCore.Qt.ClipOperation.ReplaceClip) -> None
        setClipRect(self, x: int, y: int, w: int, h: int, op: PySide2.QtCore.Qt.ClipOperation = PySide2.QtCore.Qt.ClipOperation.ReplaceClip) -> None
        """
        pass

    def setClipRegion(self, arg__1, op=None): # real signature unknown; restored from __doc__
        """ setClipRegion(self, arg__1: PySide2.QtGui.QRegion, op: PySide2.QtCore.Qt.ClipOperation = PySide2.QtCore.Qt.ClipOperation.ReplaceClip) -> None """
        pass

    def setCompositionMode(self, mode): # real signature unknown; restored from __doc__
        """ setCompositionMode(self, mode: PySide2.QtGui.QPainter.CompositionMode) -> None """
        pass

    def setFont(self, f): # real signature unknown; restored from __doc__
        """ setFont(self, f: PySide2.QtGui.QFont) -> None """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, direction: PySide2.QtCore.Qt.LayoutDirection) -> None """
        pass

    def setMatrix(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setMatrix(self, matrix: PySide2.QtGui.QMatrix, combine: bool = False) -> None """
        pass

    def setMatrixEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setMatrixEnabled(self, enabled: bool) -> None """
        pass

    def setOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setOpacity(self, opacity: float) -> None """
        pass

    def setPen(self, color): # real signature unknown; restored from __doc__
        """
        setPen(self, color: PySide2.QtGui.QColor) -> None
        setPen(self, pen: PySide2.QtGui.QPen) -> None
        setPen(self, style: PySide2.QtCore.Qt.PenStyle) -> None
        """
        pass

    def setRedirected(self, device, replacement, offset=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setRedirected(device: PySide2.QtGui.QPaintDevice, replacement: PySide2.QtGui.QPaintDevice, offset: PySide2.QtCore.QPoint = Default(QPoint)) -> None """
        pass

    def setRenderHint(self, hint, on=True): # real signature unknown; restored from __doc__
        """ setRenderHint(self, hint: PySide2.QtGui.QPainter.RenderHint, on: bool = True) -> None """
        pass

    def setRenderHints(self, hints, on=True): # real signature unknown; restored from __doc__
        """ setRenderHints(self, hints: PySide2.QtGui.QPainter.RenderHints, on: bool = True) -> None """
        pass

    def setTransform(self, transform, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, transform: PySide2.QtGui.QTransform, combine: bool = False) -> None """
        pass

    def setViewport(self, viewport): # real signature unknown; restored from __doc__
        """
        setViewport(self, viewport: PySide2.QtCore.QRect) -> None
        setViewport(self, x: int, y: int, w: int, h: int) -> None
        """
        pass

    def setViewTransformEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setViewTransformEnabled(self, enable: bool) -> None """
        pass

    def setWindow(self, window): # real signature unknown; restored from __doc__
        """
        setWindow(self, window: PySide2.QtCore.QRect) -> None
        setWindow(self, x: int, y: int, w: int, h: int) -> None
        """
        pass

    def setWorldMatrix(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setWorldMatrix(self, matrix: PySide2.QtGui.QMatrix, combine: bool = False) -> None """
        pass

    def setWorldMatrixEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setWorldMatrixEnabled(self, enabled: bool) -> None """
        pass

    def setWorldTransform(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setWorldTransform(self, matrix: PySide2.QtGui.QTransform, combine: bool = False) -> None """
        pass

    def shear(self, sh, sv): # real signature unknown; restored from __doc__
        """ shear(self, sh: float, sv: float) -> None """
        pass

    def strokePath(self, path, pen): # real signature unknown; restored from __doc__
        """ strokePath(self, path: PySide2.QtGui.QPainterPath, pen: PySide2.QtGui.QPen) -> None """
        pass

    def testRenderHint(self, hint): # real signature unknown; restored from __doc__
        """ testRenderHint(self, hint: PySide2.QtGui.QPainter.RenderHint) -> bool """
        return False

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> PySide2.QtGui.QTransform """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translate(self, dx: float, dy: float) -> None
        translate(self, offset: PySide2.QtCore.QPoint) -> None
        translate(self, offset: PySide2.QtCore.QPointF) -> None
        """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> PySide2.QtCore.QRect """
        pass

    def viewTransformEnabled(self): # real signature unknown; restored from __doc__
        """ viewTransformEnabled(self) -> bool """
        return False

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtCore.QRect """
        pass

    def worldMatrix(self): # real signature unknown; restored from __doc__
        """ worldMatrix(self) -> PySide2.QtGui.QMatrix """
        pass

    def worldMatrixEnabled(self): # real signature unknown; restored from __doc__
        """ worldMatrixEnabled(self) -> bool """
        return False

    def worldTransform(self): # real signature unknown; restored from __doc__
        """ worldTransform(self) -> PySide2.QtGui.QTransform """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Antialiasing = PySide2.QtGui.QPainter.RenderHint.Antialiasing
    CompositionMode = None # (!) real value is "<class 'PySide2.QtGui.QPainter.CompositionMode'>"
    CompositionMode_Clear = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Clear
    CompositionMode_ColorBurn = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_ColorBurn
    CompositionMode_ColorDodge = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_ColorDodge
    CompositionMode_Darken = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Darken
    CompositionMode_Destination = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Destination
    CompositionMode_DestinationAtop = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_DestinationAtop
    CompositionMode_DestinationIn = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_DestinationIn
    CompositionMode_DestinationOut = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_DestinationOut
    CompositionMode_DestinationOver = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_DestinationOver
    CompositionMode_Difference = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Difference
    CompositionMode_Exclusion = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Exclusion
    CompositionMode_HardLight = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_HardLight
    CompositionMode_Lighten = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Lighten
    CompositionMode_Multiply = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Multiply
    CompositionMode_Overlay = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Overlay
    CompositionMode_Plus = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Plus
    CompositionMode_Screen = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Screen
    CompositionMode_SoftLight = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_SoftLight
    CompositionMode_Source = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Source
    CompositionMode_SourceAtop = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_SourceAtop
    CompositionMode_SourceIn = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_SourceIn
    CompositionMode_SourceOut = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_SourceOut
    CompositionMode_SourceOver = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_SourceOver
    CompositionMode_Xor = PySide2.QtGui.QPainter.CompositionMode.CompositionMode_Xor
    HighQualityAntialiasing = PySide2.QtGui.QPainter.RenderHint.HighQualityAntialiasing
    LosslessImageRendering = PySide2.QtGui.QPainter.RenderHint.LosslessImageRendering
    NonCosmeticDefaultPen = PySide2.QtGui.QPainter.RenderHint.NonCosmeticDefaultPen
    OpaqueHint = PySide2.QtGui.QPainter.PixmapFragmentHint.OpaqueHint
    PixmapFragment = None # (!) real value is "<class 'PySide2.QtGui.QPainter.PixmapFragment'>"
    PixmapFragmentHint = None # (!) real value is "<class 'PySide2.QtGui.QPainter.PixmapFragmentHint'>"
    PixmapFragmentHints = None # (!) real value is "<class 'PySide2.QtGui.QPainter.PixmapFragmentHints'>"
    Qt4CompatiblePainting = PySide2.QtGui.QPainter.RenderHint.Qt4CompatiblePainting
    RasterOp_ClearDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_ClearDestination
    RasterOp_NotDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_NotDestination
    RasterOp_NotSource = PySide2.QtGui.QPainter.CompositionMode.RasterOp_NotSource
    RasterOp_NotSourceAndDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_NotSourceAndDestination
    RasterOp_NotSourceAndNotDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_NotSourceAndNotDestination
    RasterOp_NotSourceOrDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_NotSourceOrDestination
    RasterOp_NotSourceOrNotDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_NotSourceOrNotDestination
    RasterOp_NotSourceXorDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_NotSourceXorDestination
    RasterOp_SetDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_SetDestination
    RasterOp_SourceAndDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_SourceAndDestination
    RasterOp_SourceAndNotDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_SourceAndNotDestination
    RasterOp_SourceOrDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_SourceOrDestination
    RasterOp_SourceOrNotDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_SourceOrNotDestination
    RasterOp_SourceXorDestination = PySide2.QtGui.QPainter.CompositionMode.RasterOp_SourceXorDestination
    RenderHint = None # (!) real value is "<class 'PySide2.QtGui.QPainter.RenderHint'>"
    RenderHints = None # (!) real value is "<class 'PySide2.QtGui.QPainter.RenderHints'>"
    SmoothPixmapTransform = PySide2.QtGui.QPainter.RenderHint.SmoothPixmapTransform
    TextAntialiasing = PySide2.QtGui.QPainter.RenderHint.TextAntialiasing


