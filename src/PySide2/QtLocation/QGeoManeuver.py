# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QGeoManeuver(__Shiboken.Object):
    """
    QGeoManeuver(self) -> None
    QGeoManeuver(self, other: PySide2.QtLocation.QGeoManeuver) -> None
    """
    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> PySide2.QtLocation.QGeoManeuver.InstructionDirection """
        pass

    def distanceToNextInstruction(self): # real signature unknown; restored from __doc__
        """ distanceToNextInstruction(self) -> float """
        return 0.0

    def extendedAttributes(self): # real signature unknown; restored from __doc__
        """ extendedAttributes(self) -> typing.Dict[str, typing.Any] """
        pass

    def instructionText(self): # real signature unknown; restored from __doc__
        """ instructionText(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> PySide2.QtPositioning.QGeoCoordinate """
        pass

    def setDirection(self, direction): # real signature unknown; restored from __doc__
        """ setDirection(self, direction: PySide2.QtLocation.QGeoManeuver.InstructionDirection) -> None """
        pass

    def setDistanceToNextInstruction(self, distance): # real signature unknown; restored from __doc__
        """ setDistanceToNextInstruction(self, distance: float) -> None """
        pass

    def setExtendedAttributes(self, extendedAttributes, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setExtendedAttributes(self, extendedAttributes: typing.Dict[str, typing.Any]) -> None """
        pass

    def setInstructionText(self, instructionText): # real signature unknown; restored from __doc__
        """ setInstructionText(self, instructionText: str) -> None """
        pass

    def setPosition(self, position): # real signature unknown; restored from __doc__
        """ setPosition(self, position: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def setTimeToNextInstruction(self, secs): # real signature unknown; restored from __doc__
        """ setTimeToNextInstruction(self, secs: int) -> None """
        pass

    def setWaypoint(self, coordinate): # real signature unknown; restored from __doc__
        """ setWaypoint(self, coordinate: PySide2.QtPositioning.QGeoCoordinate) -> None """
        pass

    def timeToNextInstruction(self): # real signature unknown; restored from __doc__
        """ timeToNextInstruction(self) -> int """
        return 0

    def waypoint(self): # real signature unknown; restored from __doc__
        """ waypoint(self) -> PySide2.QtPositioning.QGeoCoordinate """
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

    DirectionBearLeft = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionBearLeft
    DirectionBearRight = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionBearRight
    DirectionForward = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionForward
    DirectionHardLeft = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionHardLeft
    DirectionHardRight = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionHardRight
    DirectionLeft = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionLeft
    DirectionLightLeft = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionLightLeft
    DirectionLightRight = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionLightRight
    DirectionRight = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionRight
    DirectionUTurnLeft = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionUTurnLeft
    DirectionUTurnRight = PySide2.QtLocation.QGeoManeuver.InstructionDirection.DirectionUTurnRight
    InstructionDirection = None # (!) real value is "<class 'PySide2.QtLocation.QGeoManeuver.InstructionDirection'>"
    NoDirection = PySide2.QtLocation.QGeoManeuver.InstructionDirection.NoDirection
    __hash__ = None


