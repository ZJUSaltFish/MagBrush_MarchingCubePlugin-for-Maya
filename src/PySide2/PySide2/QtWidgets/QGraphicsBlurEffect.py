# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGraphicsEffect import QGraphicsEffect

class QGraphicsBlurEffect(QGraphicsEffect):
    """ QGraphicsBlurEffect(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def blurHints(self): # real signature unknown; restored from __doc__
        """ blurHints(self) -> PySide2.QtWidgets.QGraphicsBlurEffect.BlurHints """
        pass

    def blurHintsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def blurRadius(self): # real signature unknown; restored from __doc__
        """ blurRadius(self) -> float """
        return 0.0

    def blurRadiusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def boundingRectFor(self, rect): # real signature unknown; restored from __doc__
        """ boundingRectFor(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def draw(self, painter): # real signature unknown; restored from __doc__
        """ draw(self, painter: PySide2.QtGui.QPainter) -> None """
        pass

    def setBlurHints(self, hints): # real signature unknown; restored from __doc__
        """ setBlurHints(self, hints: PySide2.QtWidgets.QGraphicsBlurEffect.BlurHints) -> None """
        pass

    def setBlurRadius(self, blurRadius): # real signature unknown; restored from __doc__
        """ setBlurRadius(self, blurRadius: float) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AnimationHint = PySide2.QtWidgets.QGraphicsBlurEffect.BlurHint.AnimationHint
    BlurHint = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsBlurEffect.BlurHint'>"
    BlurHints = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsBlurEffect.BlurHints'>"
    PerformanceHint = PySide2.QtWidgets.QGraphicsBlurEffect.BlurHint.PerformanceHint
    QualityHint = PySide2.QtWidgets.QGraphicsBlurEffect.BlurHint.QualityHint
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F5085AD00>'


