# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QEasingCurve(__Shiboken.Object):
    """
    QEasingCurve(self, other: PySide2.QtCore.QEasingCurve) -> None
    QEasingCurve(self, type: PySide2.QtCore.QEasingCurve.Type = PySide2.QtCore.QEasingCurve.Type.Linear) -> None
    """
    def addCubicBezierSegment(self, c1, c2, endPoint): # real signature unknown; restored from __doc__
        """ addCubicBezierSegment(self, c1: PySide2.QtCore.QPointF, c2: PySide2.QtCore.QPointF, endPoint: PySide2.QtCore.QPointF) -> None """
        pass

    def addTCBSegment(self, nextPoint, t, c, b): # real signature unknown; restored from __doc__
        """ addTCBSegment(self, nextPoint: PySide2.QtCore.QPointF, t: float, c: float, b: float) -> None """
        pass

    def amplitude(self): # real signature unknown; restored from __doc__
        """ amplitude(self) -> float """
        return 0.0

    def customType(self): # real signature unknown; restored from __doc__
        """ customType(self) -> object """
        return object()

    def overshoot(self): # real signature unknown; restored from __doc__
        """ overshoot(self) -> float """
        return 0.0

    def period(self): # real signature unknown; restored from __doc__
        """ period(self) -> float """
        return 0.0

    def setAmplitude(self, amplitude): # real signature unknown; restored from __doc__
        """ setAmplitude(self, amplitude: float) -> None """
        pass

    def setCustomType(self, arg__1): # real signature unknown; restored from __doc__
        """ setCustomType(self, arg__1: object) -> None """
        pass

    def setOvershoot(self, overshoot): # real signature unknown; restored from __doc__
        """ setOvershoot(self, overshoot: float) -> None """
        pass

    def setPeriod(self, period): # real signature unknown; restored from __doc__
        """ setPeriod(self, period: float) -> None """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: PySide2.QtCore.QEasingCurve.Type) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QEasingCurve) -> None """
        pass

    def toCubicSpline(self): # real signature unknown; restored from __doc__
        """ toCubicSpline(self) -> typing.List[PySide2.QtCore.QPointF] """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.QEasingCurve.Type """
        pass

    def valueForProgress(self, progress): # real signature unknown; restored from __doc__
        """ valueForProgress(self, progress: float) -> float """
        return 0.0

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

    def __init__(self, other): # real signature unknown; restored from __doc__
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

    BezierSpline = PySide2.QtCore.QEasingCurve.Type.BezierSpline
    CosineCurve = PySide2.QtCore.QEasingCurve.Type.CosineCurve
    Custom = PySide2.QtCore.QEasingCurve.Type.Custom
    InBack = PySide2.QtCore.QEasingCurve.Type.InBack
    InBounce = PySide2.QtCore.QEasingCurve.Type.InBounce
    InCirc = PySide2.QtCore.QEasingCurve.Type.InCirc
    InCubic = PySide2.QtCore.QEasingCurve.Type.InCubic
    InCurve = PySide2.QtCore.QEasingCurve.Type.InCurve
    InElastic = PySide2.QtCore.QEasingCurve.Type.InElastic
    InExpo = PySide2.QtCore.QEasingCurve.Type.InExpo
    InOutBack = PySide2.QtCore.QEasingCurve.Type.InOutBack
    InOutBounce = PySide2.QtCore.QEasingCurve.Type.InOutBounce
    InOutCirc = PySide2.QtCore.QEasingCurve.Type.InOutCirc
    InOutCubic = PySide2.QtCore.QEasingCurve.Type.InOutCubic
    InOutElastic = PySide2.QtCore.QEasingCurve.Type.InOutElastic
    InOutExpo = PySide2.QtCore.QEasingCurve.Type.InOutExpo
    InOutQuad = PySide2.QtCore.QEasingCurve.Type.InOutQuad
    InOutQuart = PySide2.QtCore.QEasingCurve.Type.InOutQuart
    InOutQuint = PySide2.QtCore.QEasingCurve.Type.InOutQuint
    InOutSine = PySide2.QtCore.QEasingCurve.Type.InOutSine
    InQuad = PySide2.QtCore.QEasingCurve.Type.InQuad
    InQuart = PySide2.QtCore.QEasingCurve.Type.InQuart
    InQuint = PySide2.QtCore.QEasingCurve.Type.InQuint
    InSine = PySide2.QtCore.QEasingCurve.Type.InSine
    Linear = PySide2.QtCore.QEasingCurve.Type.Linear
    NCurveTypes = PySide2.QtCore.QEasingCurve.Type.NCurveTypes
    OutBack = PySide2.QtCore.QEasingCurve.Type.OutBack
    OutBounce = PySide2.QtCore.QEasingCurve.Type.OutBounce
    OutCirc = PySide2.QtCore.QEasingCurve.Type.OutCirc
    OutCubic = PySide2.QtCore.QEasingCurve.Type.OutCubic
    OutCurve = PySide2.QtCore.QEasingCurve.Type.OutCurve
    OutElastic = PySide2.QtCore.QEasingCurve.Type.OutElastic
    OutExpo = PySide2.QtCore.QEasingCurve.Type.OutExpo
    OutInBack = PySide2.QtCore.QEasingCurve.Type.OutInBack
    OutInBounce = PySide2.QtCore.QEasingCurve.Type.OutInBounce
    OutInCirc = PySide2.QtCore.QEasingCurve.Type.OutInCirc
    OutInCubic = PySide2.QtCore.QEasingCurve.Type.OutInCubic
    OutInElastic = PySide2.QtCore.QEasingCurve.Type.OutInElastic
    OutInExpo = PySide2.QtCore.QEasingCurve.Type.OutInExpo
    OutInQuad = PySide2.QtCore.QEasingCurve.Type.OutInQuad
    OutInQuart = PySide2.QtCore.QEasingCurve.Type.OutInQuart
    OutInQuint = PySide2.QtCore.QEasingCurve.Type.OutInQuint
    OutInSine = PySide2.QtCore.QEasingCurve.Type.OutInSine
    OutQuad = PySide2.QtCore.QEasingCurve.Type.OutQuad
    OutQuart = PySide2.QtCore.QEasingCurve.Type.OutQuart
    OutQuint = PySide2.QtCore.QEasingCurve.Type.OutQuint
    OutSine = PySide2.QtCore.QEasingCurve.Type.OutSine
    SineCurve = PySide2.QtCore.QEasingCurve.Type.SineCurve
    TCBSpline = PySide2.QtCore.QEasingCurve.Type.TCBSpline
    Type = None # (!) real value is "<class 'PySide2.QtCore.QEasingCurve.Type'>"
    __hash__ = None


