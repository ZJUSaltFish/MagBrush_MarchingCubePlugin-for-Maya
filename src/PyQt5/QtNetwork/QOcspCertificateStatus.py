# encoding: utf-8
# module PyQt5.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QOcspCertificateStatus(__enum.IntEnum):
    """ An enumeration. """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    Good = 0
    Revoked = 1
    Unknown = 2
    _member_map_ = {
        'Good': 0,
        'Revoked': 1,
        'Unknown': 2,
    }
    _member_names_ = [
        'Good',
        'Revoked',
        'Unknown',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


