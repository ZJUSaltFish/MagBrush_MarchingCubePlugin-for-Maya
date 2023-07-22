# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QLocale(__Shiboken.Object):
    """
    QLocale(self) -> None
    QLocale(self, language: PySide2.QtCore.QLocale.Language, country: PySide2.QtCore.QLocale.Country = PySide2.QtCore.QLocale.Country.AnyCountry) -> None
    QLocale(self, language: PySide2.QtCore.QLocale.Language, script: PySide2.QtCore.QLocale.Script, country: PySide2.QtCore.QLocale.Country) -> None
    QLocale(self, name: str) -> None
    QLocale(self, other: PySide2.QtCore.QLocale) -> None
    """
    def amText(self): # real signature unknown; restored from __doc__
        """ amText(self) -> str """
        return ""

    def bcp47Name(self): # real signature unknown; restored from __doc__
        """ bcp47Name(self) -> str """
        return ""

    def c(self): # real signature unknown; restored from __doc__
        """ c() -> PySide2.QtCore.QLocale """
        pass

    def collation(self): # real signature unknown; restored from __doc__
        """ collation(self) -> PySide2.QtCore.QLocale """
        pass

    def countriesForLanguage(self, lang): # real signature unknown; restored from __doc__
        """ countriesForLanguage(lang: PySide2.QtCore.QLocale.Language) -> typing.List[PySide2.QtCore.QLocale.Country] """
        pass

    def country(self): # real signature unknown; restored from __doc__
        """ country(self) -> PySide2.QtCore.QLocale.Country """
        pass

    def countryToString(self, country): # real signature unknown; restored from __doc__
        """ countryToString(country: PySide2.QtCore.QLocale.Country) -> str """
        return ""

    def createSeparatedList(self, strl, p_str=None): # real signature unknown; restored from __doc__
        """ createSeparatedList(self, strl: typing.Sequence[str]) -> str """
        return ""

    def currencySymbol(self, arg__1=None): # real signature unknown; restored from __doc__
        """ currencySymbol(self, arg__1: PySide2.QtCore.QLocale.CurrencySymbolFormat = PySide2.QtCore.QLocale.CurrencySymbolFormat.CurrencySymbol) -> str """
        return ""

    def dateFormat(self, format=None): # real signature unknown; restored from __doc__
        """ dateFormat(self, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def dateTimeFormat(self, format=None): # real signature unknown; restored from __doc__
        """ dateTimeFormat(self, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def dayName(self, arg__1, format=None): # real signature unknown; restored from __doc__
        """ dayName(self, arg__1: int, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def decimalPoint(self): # real signature unknown; restored from __doc__
        """ decimalPoint(self) -> str """
        return ""

    def exponential(self): # real signature unknown; restored from __doc__
        """ exponential(self) -> str """
        return ""

    def firstDayOfWeek(self): # real signature unknown; restored from __doc__
        """ firstDayOfWeek(self) -> PySide2.QtCore.Qt.DayOfWeek """
        pass

    def formattedDataSize(self, bytes, precision=2, format=None): # real signature unknown; restored from __doc__
        """ formattedDataSize(self, bytes: int, precision: int = 2, format: PySide2.QtCore.QLocale.DataSizeFormats = PySide2.QtCore.QLocale.DataSizeFormat.DataSizeIecFormat) -> str """
        return ""

    def groupSeparator(self): # real signature unknown; restored from __doc__
        """ groupSeparator(self) -> str """
        return ""

    def language(self): # real signature unknown; restored from __doc__
        """ language(self) -> PySide2.QtCore.QLocale.Language """
        pass

    def languageToString(self, language): # real signature unknown; restored from __doc__
        """ languageToString(language: PySide2.QtCore.QLocale.Language) -> str """
        return ""

    def matchingLocales(self, language, script, country): # real signature unknown; restored from __doc__
        """ matchingLocales(language: PySide2.QtCore.QLocale.Language, script: PySide2.QtCore.QLocale.Script, country: PySide2.QtCore.QLocale.Country) -> typing.List[PySide2.QtCore.QLocale] """
        pass

    def measurementSystem(self): # real signature unknown; restored from __doc__
        """ measurementSystem(self) -> PySide2.QtCore.QLocale.MeasurementSystem """
        pass

    def monthName(self, arg__1, format=None): # real signature unknown; restored from __doc__
        """ monthName(self, arg__1: int, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nativeCountryName(self): # real signature unknown; restored from __doc__
        """ nativeCountryName(self) -> str """
        return ""

    def nativeLanguageName(self): # real signature unknown; restored from __doc__
        """ nativeLanguageName(self) -> str """
        return ""

    def negativeSign(self): # real signature unknown; restored from __doc__
        """ negativeSign(self) -> str """
        return ""

    def numberOptions(self): # real signature unknown; restored from __doc__
        """ numberOptions(self) -> PySide2.QtCore.QLocale.NumberOptions """
        pass

    def percent(self): # real signature unknown; restored from __doc__
        """ percent(self) -> str """
        return ""

    def pmText(self): # real signature unknown; restored from __doc__
        """ pmText(self) -> str """
        return ""

    def positiveSign(self): # real signature unknown; restored from __doc__
        """ positiveSign(self) -> str """
        return ""

    def quoteString(self, p_str, style=None): # real signature unknown; restored from __doc__
        """
        quoteString(self, str: str, style: PySide2.QtCore.QLocale.QuotationStyle = PySide2.QtCore.QLocale.QuotationStyle.StandardQuotation) -> str
        quoteString(self, str: str, style: PySide2.QtCore.QLocale.QuotationStyle = PySide2.QtCore.QLocale.QuotationStyle.StandardQuotation) -> str
        """
        return ""

    def script(self): # real signature unknown; restored from __doc__
        """ script(self) -> PySide2.QtCore.QLocale.Script """
        pass

    def scriptToString(self, script): # real signature unknown; restored from __doc__
        """ scriptToString(script: PySide2.QtCore.QLocale.Script) -> str """
        return ""

    def setDefault(self, locale): # real signature unknown; restored from __doc__
        """ setDefault(locale: PySide2.QtCore.QLocale) -> None """
        pass

    def setNumberOptions(self, options): # real signature unknown; restored from __doc__
        """ setNumberOptions(self, options: PySide2.QtCore.QLocale.NumberOptions) -> None """
        pass

    def standaloneDayName(self, arg__1, format=None): # real signature unknown; restored from __doc__
        """ standaloneDayName(self, arg__1: int, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def standaloneMonthName(self, arg__1, format=None): # real signature unknown; restored from __doc__
        """ standaloneMonthName(self, arg__1: int, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QLocale) -> None """
        pass

    def system(self): # real signature unknown; restored from __doc__
        """ system() -> PySide2.QtCore.QLocale """
        pass

    def textDirection(self): # real signature unknown; restored from __doc__
        """ textDirection(self) -> PySide2.QtCore.Qt.LayoutDirection """
        pass

    def timeFormat(self, format=None): # real signature unknown; restored from __doc__
        """ timeFormat(self, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def toCurrencyString(self, arg__1, symbol, precision): # real signature unknown; restored from __doc__
        """
        toCurrencyString(self, arg__1: float, symbol: str, precision: int) -> str
        toCurrencyString(self, arg__1: float, symbol: str = '') -> str
        toCurrencyString(self, arg__1: int, symbol: str = '') -> str
        toCurrencyString(self, arg__1: int, symbol: str = '') -> str
        toCurrencyString(self, arg__1: int, symbol: str = '') -> str
        toCurrencyString(self, arg__1: int, symbol: str = '') -> str
        toCurrencyString(self, arg__1: int, symbol: str = '') -> str
        toCurrencyString(self, arg__1: int, symbol: str = '') -> str
        toCurrencyString(self, i: float, symbol: str, precision: int) -> str
        toCurrencyString(self, i: float, symbol: str = '') -> str
        """
        return ""

    def toDate(self, string, format, cal): # real signature unknown; restored from __doc__
        """
        toDate(self, string: str, format: PySide2.QtCore.QLocale.FormatType, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QDate
        toDate(self, string: str, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> PySide2.QtCore.QDate
        toDate(self, string: str, format: str) -> PySide2.QtCore.QDate
        toDate(self, string: str, format: str, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QDate
        """
        pass

    def toDateTime(self, string, format, cal): # real signature unknown; restored from __doc__
        """
        toDateTime(self, string: str, format: PySide2.QtCore.QLocale.FormatType, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QDateTime
        toDateTime(self, string: str, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> PySide2.QtCore.QDateTime
        toDateTime(self, string: str, format: str) -> PySide2.QtCore.QDateTime
        toDateTime(self, string: str, format: str, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QDateTime
        """
        pass

    def toDouble(self, s): # real signature unknown; restored from __doc__
        """ toDouble(self, s: str) -> typing.Tuple[float, bool] """
        pass

    def toFloat(self, s): # real signature unknown; restored from __doc__
        """ toFloat(self, s: str) -> typing.Tuple[float, bool] """
        pass

    def toInt(self, s): # real signature unknown; restored from __doc__
        """ toInt(self, s: str) -> typing.Tuple[int, bool] """
        pass

    def toLong(self, s): # real signature unknown; restored from __doc__
        """
        toLong(self, s: str) -> typing.Tuple[int, bool]
        toLong(self, s: str) -> typing.Tuple[int, bool]
        """
        pass

    def toLongLong(self, s): # real signature unknown; restored from __doc__
        """ toLongLong(self, s: str) -> typing.Tuple[int, bool] """
        pass

    def toLower(self, p_str): # real signature unknown; restored from __doc__
        """ toLower(self, str: str) -> str """
        return ""

    def toShort(self, s): # real signature unknown; restored from __doc__
        """ toShort(self, s: str) -> typing.Tuple[int, bool] """
        pass

    def toString(self, date, format, cal): # real signature unknown; restored from __doc__
        """
        toString(self, date: PySide2.QtCore.QDate, format: PySide2.QtCore.QLocale.FormatType, cal: PySide2.QtCore.QCalendar) -> str
        toString(self, date: PySide2.QtCore.QDate, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str
        toString(self, date: PySide2.QtCore.QDate, formatStr: str) -> str
        toString(self, dateTime: PySide2.QtCore.QDateTime, format: PySide2.QtCore.QLocale.FormatType, cal: PySide2.QtCore.QCalendar) -> str
        toString(self, dateTime: PySide2.QtCore.QDateTime, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str
        toString(self, dateTime: PySide2.QtCore.QDateTime, format: str) -> str
        toString(self, i: float, f: int = 'g', prec: int = 6) -> str
        toString(self, i: float, f: int = 'g', prec: int = 6) -> str
        toString(self, i: int) -> str
        toString(self, i: int) -> str
        toString(self, i: int) -> str
        toString(self, i: int) -> str
        toString(self, i: int) -> str
        toString(self, time: PySide2.QtCore.QTime, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str
        toString(self, time: PySide2.QtCore.QTime, formatStr: str) -> str
        """
        return ""

    def toTime(self, string, format, cal): # real signature unknown; restored from __doc__
        """
        toTime(self, string: str, format: PySide2.QtCore.QLocale.FormatType, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QTime
        toTime(self, string: str, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> PySide2.QtCore.QTime
        toTime(self, string: str, format: str) -> PySide2.QtCore.QTime
        toTime(self, string: str, format: str, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QTime
        """
        pass

    def toUInt(self, s): # real signature unknown; restored from __doc__
        """ toUInt(self, s: str) -> typing.Tuple[int, bool] """
        pass

    def toULong(self, s): # real signature unknown; restored from __doc__
        """
        toULong(self, s: str) -> typing.Tuple[int, bool]
        toULong(self, s: str) -> typing.Tuple[int, bool]
        """
        pass

    def toULongLong(self, s): # real signature unknown; restored from __doc__
        """ toULongLong(self, s: str) -> typing.Tuple[int, bool] """
        pass

    def toUpper(self, p_str): # real signature unknown; restored from __doc__
        """ toUpper(self, str: str) -> str """
        return ""

    def toUShort(self, s): # real signature unknown; restored from __doc__
        """ toUShort(self, s: str) -> typing.Tuple[int, bool] """
        pass

    def uiLanguages(self): # real signature unknown; restored from __doc__
        """ uiLanguages(self) -> typing.List[str] """
        pass

    def weekdays(self): # real signature unknown; restored from __doc__
        """ weekdays(self) -> typing.List[PySide2.QtCore.Qt.DayOfWeek] """
        pass

    def zeroDigit(self): # real signature unknown; restored from __doc__
        """ zeroDigit(self) -> str """
        return ""

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

    Abkhazian = PySide2.QtCore.QLocale.Language.Abkhazian
    AdlamScript = PySide2.QtCore.QLocale.Script.AdlamScript
    Afan = PySide2.QtCore.QLocale.Language.Afan
    Afar = PySide2.QtCore.QLocale.Language.Afar
    Afghanistan = PySide2.QtCore.QLocale.Country.Afghanistan
    Afrikaans = PySide2.QtCore.QLocale.Language.Afrikaans
    Aghem = PySide2.QtCore.QLocale.Language.Aghem
    Ahom = PySide2.QtCore.QLocale.Language.Ahom
    AhomScript = PySide2.QtCore.QLocale.Script.AhomScript
    Akan = PySide2.QtCore.QLocale.Language.Akan
    Akkadian = PySide2.QtCore.QLocale.Language.Akkadian
    Akoose = PySide2.QtCore.QLocale.Language.Akoose
    AlandIslands = PySide2.QtCore.QLocale.Country.AlandIslands
    Albania = PySide2.QtCore.QLocale.Country.Albania
    Albanian = PySide2.QtCore.QLocale.Language.Albanian
    Algeria = PySide2.QtCore.QLocale.Country.Algeria
    AlternateQuotation = PySide2.QtCore.QLocale.QuotationStyle.AlternateQuotation
    AmericanSamoa = PySide2.QtCore.QLocale.Country.AmericanSamoa
    AmericanSignLanguage = PySide2.QtCore.QLocale.Language.AmericanSignLanguage
    Amharic = PySide2.QtCore.QLocale.Language.Amharic
    AnatolianHieroglyphsScript = PySide2.QtCore.QLocale.Script.AnatolianHieroglyphsScript
    AncientEgyptian = PySide2.QtCore.QLocale.Language.AncientEgyptian
    AncientGreek = PySide2.QtCore.QLocale.Language.AncientGreek
    AncientNorthArabian = PySide2.QtCore.QLocale.Language.AncientNorthArabian
    Andorra = PySide2.QtCore.QLocale.Country.Andorra
    Angola = PySide2.QtCore.QLocale.Country.Angola
    Anguilla = PySide2.QtCore.QLocale.Country.Anguilla
    Antarctica = PySide2.QtCore.QLocale.Country.Antarctica
    AntiguaAndBarbuda = PySide2.QtCore.QLocale.Country.AntiguaAndBarbuda
    AnyCountry = PySide2.QtCore.QLocale.Country.AnyCountry
    AnyLanguage = PySide2.QtCore.QLocale.Language.AnyLanguage
    AnyScript = PySide2.QtCore.QLocale.Script.AnyScript
    Arabic = PySide2.QtCore.QLocale.Language.Arabic
    ArabicScript = PySide2.QtCore.QLocale.Script.ArabicScript
    Aragonese = PySide2.QtCore.QLocale.Language.Aragonese
    Aramaic = PySide2.QtCore.QLocale.Language.Aramaic
    ArdhamagadhiPrakrit = PySide2.QtCore.QLocale.Language.ArdhamagadhiPrakrit
    Argentina = PySide2.QtCore.QLocale.Country.Argentina
    Armenia = PySide2.QtCore.QLocale.Country.Armenia
    Armenian = PySide2.QtCore.QLocale.Language.Armenian
    ArmenianScript = PySide2.QtCore.QLocale.Script.ArmenianScript
    Aruba = PySide2.QtCore.QLocale.Country.Aruba
    AscensionIsland = PySide2.QtCore.QLocale.Country.AscensionIsland
    Assamese = PySide2.QtCore.QLocale.Language.Assamese
    Asturian = PySide2.QtCore.QLocale.Language.Asturian
    Asu = PySide2.QtCore.QLocale.Language.Asu
    Atsam = PySide2.QtCore.QLocale.Language.Atsam
    Australia = PySide2.QtCore.QLocale.Country.Australia
    Austria = PySide2.QtCore.QLocale.Country.Austria
    Avaric = PySide2.QtCore.QLocale.Language.Avaric
    Avestan = PySide2.QtCore.QLocale.Language.Avestan
    AvestanScript = PySide2.QtCore.QLocale.Script.AvestanScript
    Aymara = PySide2.QtCore.QLocale.Language.Aymara
    Azerbaijan = PySide2.QtCore.QLocale.Country.Azerbaijan
    Azerbaijani = PySide2.QtCore.QLocale.Language.Azerbaijani
    Bafia = PySide2.QtCore.QLocale.Language.Bafia
    Bahamas = PySide2.QtCore.QLocale.Country.Bahamas
    Bahrain = PySide2.QtCore.QLocale.Country.Bahrain
    Balinese = PySide2.QtCore.QLocale.Language.Balinese
    BalineseScript = PySide2.QtCore.QLocale.Script.BalineseScript
    Bambara = PySide2.QtCore.QLocale.Language.Bambara
    BamumScript = PySide2.QtCore.QLocale.Script.BamumScript
    Bamun = PySide2.QtCore.QLocale.Language.Bamun
    Bangladesh = PySide2.QtCore.QLocale.Country.Bangladesh
    Barbados = PySide2.QtCore.QLocale.Country.Barbados
    Basaa = PySide2.QtCore.QLocale.Language.Basaa
    Bashkir = PySide2.QtCore.QLocale.Language.Bashkir
    Basque = PySide2.QtCore.QLocale.Language.Basque
    Bassa = PySide2.QtCore.QLocale.Language.Bassa
    BassaVahScript = PySide2.QtCore.QLocale.Script.BassaVahScript
    BatakScript = PySide2.QtCore.QLocale.Script.BatakScript
    BatakToba = PySide2.QtCore.QLocale.Language.BatakToba
    Belarus = PySide2.QtCore.QLocale.Country.Belarus
    Belarusian = PySide2.QtCore.QLocale.Language.Belarusian
    Belgium = PySide2.QtCore.QLocale.Country.Belgium
    Belize = PySide2.QtCore.QLocale.Country.Belize
    Bemba = PySide2.QtCore.QLocale.Language.Bemba
    Bena = PySide2.QtCore.QLocale.Language.Bena
    Bengali = PySide2.QtCore.QLocale.Language.Bengali
    BengaliScript = PySide2.QtCore.QLocale.Script.BengaliScript
    Benin = PySide2.QtCore.QLocale.Country.Benin
    Bermuda = PySide2.QtCore.QLocale.Country.Bermuda
    BhaiksukiScript = PySide2.QtCore.QLocale.Script.BhaiksukiScript
    Bhojpuri = PySide2.QtCore.QLocale.Language.Bhojpuri
    Bhutan = PySide2.QtCore.QLocale.Country.Bhutan
    Bhutani = PySide2.QtCore.QLocale.Language.Bhutani
    Bihari = PySide2.QtCore.QLocale.Language.Bihari
    Bislama = PySide2.QtCore.QLocale.Language.Bislama
    Blin = PySide2.QtCore.QLocale.Language.Blin
    Bodo = PySide2.QtCore.QLocale.Language.Bodo
    Bolivia = PySide2.QtCore.QLocale.Country.Bolivia
    Bonaire = PySide2.QtCore.QLocale.Country.Bonaire
    BopomofoScript = PySide2.QtCore.QLocale.Script.BopomofoScript
    BosniaAndHerzegowina = PySide2.QtCore.QLocale.Country.BosniaAndHerzegowina
    Bosnian = PySide2.QtCore.QLocale.Language.Bosnian
    Botswana = PySide2.QtCore.QLocale.Country.Botswana
    BouvetIsland = PySide2.QtCore.QLocale.Country.BouvetIsland
    BrahmiScript = PySide2.QtCore.QLocale.Script.BrahmiScript
    BrailleScript = PySide2.QtCore.QLocale.Script.BrailleScript
    Brazil = PySide2.QtCore.QLocale.Country.Brazil
    Breton = PySide2.QtCore.QLocale.Language.Breton
    BritishIndianOceanTerritory = PySide2.QtCore.QLocale.Country.BritishIndianOceanTerritory
    BritishVirginIslands = PySide2.QtCore.QLocale.Country.BritishVirginIslands
    Brunei = PySide2.QtCore.QLocale.Country.Brunei
    Buginese = PySide2.QtCore.QLocale.Language.Buginese
    BugineseScript = PySide2.QtCore.QLocale.Script.BugineseScript
    Buhid = PySide2.QtCore.QLocale.Language.Buhid
    BuhidScript = PySide2.QtCore.QLocale.Script.BuhidScript
    Bulgaria = PySide2.QtCore.QLocale.Country.Bulgaria
    Bulgarian = PySide2.QtCore.QLocale.Language.Bulgarian
    BurkinaFaso = PySide2.QtCore.QLocale.Country.BurkinaFaso
    Burmese = PySide2.QtCore.QLocale.Language.Burmese
    Burundi = PySide2.QtCore.QLocale.Country.Burundi
    Byelorussian = PySide2.QtCore.QLocale.Language.Byelorussian
    C = PySide2.QtCore.QLocale.Language.C
    Cambodia = PySide2.QtCore.QLocale.Country.Cambodia
    Cambodian = PySide2.QtCore.QLocale.Language.Cambodian
    Cameroon = PySide2.QtCore.QLocale.Country.Cameroon
    Canada = PySide2.QtCore.QLocale.Country.Canada
    CanadianAboriginalScript = PySide2.QtCore.QLocale.Script.CanadianAboriginalScript
    CanaryIslands = PySide2.QtCore.QLocale.Country.CanaryIslands
    Cantonese = PySide2.QtCore.QLocale.Language.Cantonese
    CapeVerde = PySide2.QtCore.QLocale.Country.CapeVerde
    Carian = PySide2.QtCore.QLocale.Language.Carian
    CarianScript = PySide2.QtCore.QLocale.Script.CarianScript
    Catalan = PySide2.QtCore.QLocale.Language.Catalan
    CaucasianAlbanianScript = PySide2.QtCore.QLocale.Script.CaucasianAlbanianScript
    CaymanIslands = PySide2.QtCore.QLocale.Country.CaymanIslands
    Cebuano = PySide2.QtCore.QLocale.Language.Cebuano
    CentralAfricanRepublic = PySide2.QtCore.QLocale.Country.CentralAfricanRepublic
    CentralKurdish = PySide2.QtCore.QLocale.Language.CentralKurdish
    CentralMoroccoTamazight = PySide2.QtCore.QLocale.Language.CentralMoroccoTamazight
    CeutaAndMelilla = PySide2.QtCore.QLocale.Country.CeutaAndMelilla
    Chad = PySide2.QtCore.QLocale.Country.Chad
    Chakma = PySide2.QtCore.QLocale.Language.Chakma
    ChakmaScript = PySide2.QtCore.QLocale.Script.ChakmaScript
    Chamorro = PySide2.QtCore.QLocale.Language.Chamorro
    ChamScript = PySide2.QtCore.QLocale.Script.ChamScript
    Chechen = PySide2.QtCore.QLocale.Language.Chechen
    Cherokee = PySide2.QtCore.QLocale.Language.Cherokee
    CherokeeScript = PySide2.QtCore.QLocale.Script.CherokeeScript
    Chewa = PySide2.QtCore.QLocale.Language.Chewa
    Chickasaw = PySide2.QtCore.QLocale.Language.Chickasaw
    Chiga = PySide2.QtCore.QLocale.Language.Chiga
    Chile = PySide2.QtCore.QLocale.Country.Chile
    China = PySide2.QtCore.QLocale.Country.China
    Chinese = PySide2.QtCore.QLocale.Language.Chinese
    ChristmasIsland = PySide2.QtCore.QLocale.Country.ChristmasIsland
    Church = PySide2.QtCore.QLocale.Language.Church
    Chuvash = PySide2.QtCore.QLocale.Language.Chuvash
    ClassicalMandaic = PySide2.QtCore.QLocale.Language.ClassicalMandaic
    ClippertonIsland = PySide2.QtCore.QLocale.Country.ClippertonIsland
    CocosIslands = PySide2.QtCore.QLocale.Country.CocosIslands
    Colognian = PySide2.QtCore.QLocale.Language.Colognian
    Colombia = PySide2.QtCore.QLocale.Country.Colombia
    Comoros = PySide2.QtCore.QLocale.Country.Comoros
    CongoBrazzaville = PySide2.QtCore.QLocale.Country.CongoBrazzaville
    CongoKinshasa = PySide2.QtCore.QLocale.Country.CongoKinshasa
    CongoSwahili = PySide2.QtCore.QLocale.Language.CongoSwahili
    CookIslands = PySide2.QtCore.QLocale.Country.CookIslands
    Coptic = PySide2.QtCore.QLocale.Language.Coptic
    CopticScript = PySide2.QtCore.QLocale.Script.CopticScript
    Cornish = PySide2.QtCore.QLocale.Language.Cornish
    Corsican = PySide2.QtCore.QLocale.Language.Corsican
    CostaRica = PySide2.QtCore.QLocale.Country.CostaRica
    Country = None # (!) real value is "<class 'PySide2.QtCore.QLocale.Country'>"
    Cree = PySide2.QtCore.QLocale.Language.Cree
    Croatia = PySide2.QtCore.QLocale.Country.Croatia
    Croatian = PySide2.QtCore.QLocale.Language.Croatian
    Cuba = PySide2.QtCore.QLocale.Country.Cuba
    CuneiformScript = PySide2.QtCore.QLocale.Script.CuneiformScript
    CuraSao = PySide2.QtCore.QLocale.Country.CuraSao
    CurrencyDisplayName = PySide2.QtCore.QLocale.CurrencySymbolFormat.CurrencyDisplayName
    CurrencyIsoCode = PySide2.QtCore.QLocale.CurrencySymbolFormat.CurrencyIsoCode
    CurrencySymbol = PySide2.QtCore.QLocale.CurrencySymbolFormat.CurrencySymbol
    CurrencySymbolFormat = None # (!) real value is "<class 'PySide2.QtCore.QLocale.CurrencySymbolFormat'>"
    CypriotScript = PySide2.QtCore.QLocale.Script.CypriotScript
    Cyprus = PySide2.QtCore.QLocale.Country.Cyprus
    CyrillicScript = PySide2.QtCore.QLocale.Script.CyrillicScript
    Czech = PySide2.QtCore.QLocale.Language.Czech
    CzechRepublic = PySide2.QtCore.QLocale.Country.CzechRepublic
    Danish = PySide2.QtCore.QLocale.Language.Danish
    DataSizeBase1000 = PySide2.QtCore.QLocale.DataSizeFormat.DataSizeBase1000
    DataSizeFormat = None # (!) real value is "<class 'PySide2.QtCore.QLocale.DataSizeFormat'>"
    DataSizeFormats = None # (!) real value is "<class 'PySide2.QtCore.QLocale.DataSizeFormats'>"
    DataSizeIecFormat = PySide2.QtCore.QLocale.DataSizeFormat.DataSizeIecFormat
    DataSizeSIFormat = PySide2.QtCore.QLocale.DataSizeFormat.DataSizeSIFormat
    DataSizeSIQuantifiers = PySide2.QtCore.QLocale.DataSizeFormat.DataSizeSIQuantifiers
    DataSizeTraditionalFormat = PySide2.QtCore.QLocale.DataSizeFormat.DataSizeTraditionalFormat
    DefaultNumberOptions = PySide2.QtCore.QLocale.NumberOption.DefaultNumberOptions
    DemocraticRepublicOfCongo = PySide2.QtCore.QLocale.Country.DemocraticRepublicOfCongo
    DemocraticRepublicOfKorea = PySide2.QtCore.QLocale.Country.DemocraticRepublicOfKorea
    Denmark = PySide2.QtCore.QLocale.Country.Denmark
    DeseretScript = PySide2.QtCore.QLocale.Script.DeseretScript
    DevanagariScript = PySide2.QtCore.QLocale.Script.DevanagariScript
    DiegoGarcia = PySide2.QtCore.QLocale.Country.DiegoGarcia
    Divehi = PySide2.QtCore.QLocale.Language.Divehi
    Djibouti = PySide2.QtCore.QLocale.Country.Djibouti
    Dogri = PySide2.QtCore.QLocale.Language.Dogri
    Dominica = PySide2.QtCore.QLocale.Country.Dominica
    DominicanRepublic = PySide2.QtCore.QLocale.Country.DominicanRepublic
    Duala = PySide2.QtCore.QLocale.Language.Duala
    DuployanScript = PySide2.QtCore.QLocale.Script.DuployanScript
    Dutch = PySide2.QtCore.QLocale.Language.Dutch
    Dzongkha = PySide2.QtCore.QLocale.Language.Dzongkha
    EasternCham = PySide2.QtCore.QLocale.Language.EasternCham
    EasternKayah = PySide2.QtCore.QLocale.Language.EasternKayah
    EastTimor = PySide2.QtCore.QLocale.Country.EastTimor
    Ecuador = PySide2.QtCore.QLocale.Country.Ecuador
    Egypt = PySide2.QtCore.QLocale.Country.Egypt
    EgyptianHieroglyphsScript = PySide2.QtCore.QLocale.Script.EgyptianHieroglyphsScript
    ElbasanScript = PySide2.QtCore.QLocale.Script.ElbasanScript
    ElSalvador = PySide2.QtCore.QLocale.Country.ElSalvador
    Embu = PySide2.QtCore.QLocale.Language.Embu
    English = PySide2.QtCore.QLocale.Language.English
    EquatorialGuinea = PySide2.QtCore.QLocale.Country.EquatorialGuinea
    Eritrea = PySide2.QtCore.QLocale.Country.Eritrea
    Erzya = PySide2.QtCore.QLocale.Language.Erzya
    Esperanto = PySide2.QtCore.QLocale.Language.Esperanto
    Estonia = PySide2.QtCore.QLocale.Country.Estonia
    Estonian = PySide2.QtCore.QLocale.Language.Estonian
    Ethiopia = PySide2.QtCore.QLocale.Country.Ethiopia
    EthiopicScript = PySide2.QtCore.QLocale.Script.EthiopicScript
    Etruscan = PySide2.QtCore.QLocale.Language.Etruscan
    Europe = PySide2.QtCore.QLocale.Country.Europe
    EuropeanUnion = PySide2.QtCore.QLocale.Country.EuropeanUnion
    Ewe = PySide2.QtCore.QLocale.Language.Ewe
    Ewondo = PySide2.QtCore.QLocale.Language.Ewondo
    FalklandIslands = PySide2.QtCore.QLocale.Country.FalklandIslands
    FaroeIslands = PySide2.QtCore.QLocale.Country.FaroeIslands
    Faroese = PySide2.QtCore.QLocale.Language.Faroese
    Fiji = PySide2.QtCore.QLocale.Country.Fiji
    Fijian = PySide2.QtCore.QLocale.Language.Fijian
    Filipino = PySide2.QtCore.QLocale.Language.Filipino
    Finland = PySide2.QtCore.QLocale.Country.Finland
    Finnish = PySide2.QtCore.QLocale.Language.Finnish
    FloatingPointPrecisionOption = None # (!) real value is "<class 'PySide2.QtCore.QLocale.FloatingPointPrecisionOption'>"
    FloatingPointShortest = PySide2.QtCore.QLocale.FloatingPointPrecisionOption.FloatingPointShortest
    FormatType = None # (!) real value is "<class 'PySide2.QtCore.QLocale.FormatType'>"
    France = PySide2.QtCore.QLocale.Country.France
    FraserScript = PySide2.QtCore.QLocale.Script.FraserScript
    French = PySide2.QtCore.QLocale.Language.French
    FrenchGuiana = PySide2.QtCore.QLocale.Country.FrenchGuiana
    FrenchPolynesia = PySide2.QtCore.QLocale.Country.FrenchPolynesia
    FrenchSouthernTerritories = PySide2.QtCore.QLocale.Country.FrenchSouthernTerritories
    Frisian = PySide2.QtCore.QLocale.Language.Frisian
    Friulian = PySide2.QtCore.QLocale.Language.Friulian
    Fulah = PySide2.QtCore.QLocale.Language.Fulah
    Ga = PySide2.QtCore.QLocale.Language.Ga
    Gabon = PySide2.QtCore.QLocale.Country.Gabon
    Gaelic = PySide2.QtCore.QLocale.Language.Gaelic
    Galician = PySide2.QtCore.QLocale.Language.Galician
    Gambia = PySide2.QtCore.QLocale.Country.Gambia
    Ganda = PySide2.QtCore.QLocale.Language.Ganda
    Geez = PySide2.QtCore.QLocale.Language.Geez
    Georgia = PySide2.QtCore.QLocale.Country.Georgia
    Georgian = PySide2.QtCore.QLocale.Language.Georgian
    GeorgianScript = PySide2.QtCore.QLocale.Script.GeorgianScript
    German = PySide2.QtCore.QLocale.Language.German
    Germany = PySide2.QtCore.QLocale.Country.Germany
    Ghana = PySide2.QtCore.QLocale.Country.Ghana
    Gibraltar = PySide2.QtCore.QLocale.Country.Gibraltar
    GlagoliticScript = PySide2.QtCore.QLocale.Script.GlagoliticScript
    Gothic = PySide2.QtCore.QLocale.Language.Gothic
    GothicScript = PySide2.QtCore.QLocale.Script.GothicScript
    GranthaScript = PySide2.QtCore.QLocale.Script.GranthaScript
    Greece = PySide2.QtCore.QLocale.Country.Greece
    Greek = PySide2.QtCore.QLocale.Language.Greek
    GreekScript = PySide2.QtCore.QLocale.Script.GreekScript
    Greenland = PySide2.QtCore.QLocale.Country.Greenland
    Greenlandic = PySide2.QtCore.QLocale.Language.Greenlandic
    Grenada = PySide2.QtCore.QLocale.Country.Grenada
    Guadeloupe = PySide2.QtCore.QLocale.Country.Guadeloupe
    Guam = PySide2.QtCore.QLocale.Country.Guam
    Guarani = PySide2.QtCore.QLocale.Language.Guarani
    Guatemala = PySide2.QtCore.QLocale.Country.Guatemala
    Guernsey = PySide2.QtCore.QLocale.Country.Guernsey
    Guinea = PySide2.QtCore.QLocale.Country.Guinea
    GuineaBissau = PySide2.QtCore.QLocale.Country.GuineaBissau
    Gujarati = PySide2.QtCore.QLocale.Language.Gujarati
    GujaratiScript = PySide2.QtCore.QLocale.Script.GujaratiScript
    GurmukhiScript = PySide2.QtCore.QLocale.Script.GurmukhiScript
    Gusii = PySide2.QtCore.QLocale.Language.Gusii
    Guyana = PySide2.QtCore.QLocale.Country.Guyana
    Haiti = PySide2.QtCore.QLocale.Country.Haiti
    Haitian = PySide2.QtCore.QLocale.Language.Haitian
    HangulScript = PySide2.QtCore.QLocale.Script.HangulScript
    HanScript = PySide2.QtCore.QLocale.Script.HanScript
    Hanunoo = PySide2.QtCore.QLocale.Language.Hanunoo
    HanunooScript = PySide2.QtCore.QLocale.Script.HanunooScript
    HanWithBopomofoScript = PySide2.QtCore.QLocale.Script.HanWithBopomofoScript
    HatranScript = PySide2.QtCore.QLocale.Script.HatranScript
    Hausa = PySide2.QtCore.QLocale.Language.Hausa
    Hawaiian = PySide2.QtCore.QLocale.Language.Hawaiian
    HeardAndMcDonaldIslands = PySide2.QtCore.QLocale.Country.HeardAndMcDonaldIslands
    Hebrew = PySide2.QtCore.QLocale.Language.Hebrew
    HebrewScript = PySide2.QtCore.QLocale.Script.HebrewScript
    Herero = PySide2.QtCore.QLocale.Language.Herero
    HieroglyphicLuwian = PySide2.QtCore.QLocale.Language.HieroglyphicLuwian
    Hindi = PySide2.QtCore.QLocale.Language.Hindi
    HiraganaScript = PySide2.QtCore.QLocale.Script.HiraganaScript
    HiriMotu = PySide2.QtCore.QLocale.Language.HiriMotu
    HmongNjua = PySide2.QtCore.QLocale.Language.HmongNjua
    Ho = PySide2.QtCore.QLocale.Language.Ho
    Honduras = PySide2.QtCore.QLocale.Country.Honduras
    HongKong = PySide2.QtCore.QLocale.Country.HongKong
    Hungarian = PySide2.QtCore.QLocale.Language.Hungarian
    Hungary = PySide2.QtCore.QLocale.Country.Hungary
    Iceland = PySide2.QtCore.QLocale.Country.Iceland
    Icelandic = PySide2.QtCore.QLocale.Language.Icelandic
    Ido = PySide2.QtCore.QLocale.Language.Ido
    Igbo = PySide2.QtCore.QLocale.Language.Igbo
    ImperialAramaicScript = PySide2.QtCore.QLocale.Script.ImperialAramaicScript
    ImperialSystem = PySide2.QtCore.QLocale.MeasurementSystem.ImperialSystem
    ImperialUKSystem = PySide2.QtCore.QLocale.MeasurementSystem.ImperialUKSystem
    ImperialUSSystem = PySide2.QtCore.QLocale.MeasurementSystem.ImperialUSSystem
    InariSami = PySide2.QtCore.QLocale.Language.InariSami
    IncludeTrailingZeroesAfterDot = PySide2.QtCore.QLocale.NumberOption.IncludeTrailingZeroesAfterDot
    India = PySide2.QtCore.QLocale.Country.India
    Indonesia = PySide2.QtCore.QLocale.Country.Indonesia
    Indonesian = PySide2.QtCore.QLocale.Language.Indonesian
    Ingush = PySide2.QtCore.QLocale.Language.Ingush
    InscriptionalPahlaviScript = PySide2.QtCore.QLocale.Script.InscriptionalPahlaviScript
    InscriptionalParthianScript = PySide2.QtCore.QLocale.Script.InscriptionalParthianScript
    Interlingua = PySide2.QtCore.QLocale.Language.Interlingua
    Interlingue = PySide2.QtCore.QLocale.Language.Interlingue
    Inuktitut = PySide2.QtCore.QLocale.Language.Inuktitut
    Inupiak = PySide2.QtCore.QLocale.Language.Inupiak
    Iran = PySide2.QtCore.QLocale.Country.Iran
    Iraq = PySide2.QtCore.QLocale.Country.Iraq
    Ireland = PySide2.QtCore.QLocale.Country.Ireland
    Irish = PySide2.QtCore.QLocale.Language.Irish
    IsleOfMan = PySide2.QtCore.QLocale.Country.IsleOfMan
    Israel = PySide2.QtCore.QLocale.Country.Israel
    Italian = PySide2.QtCore.QLocale.Language.Italian
    Italy = PySide2.QtCore.QLocale.Country.Italy
    IvoryCoast = PySide2.QtCore.QLocale.Country.IvoryCoast
    Jamaica = PySide2.QtCore.QLocale.Country.Jamaica
    JamoScript = PySide2.QtCore.QLocale.Script.JamoScript
    Japan = PySide2.QtCore.QLocale.Country.Japan
    Japanese = PySide2.QtCore.QLocale.Language.Japanese
    JapaneseScript = PySide2.QtCore.QLocale.Script.JapaneseScript
    Javanese = PySide2.QtCore.QLocale.Language.Javanese
    JavaneseScript = PySide2.QtCore.QLocale.Script.JavaneseScript
    Jersey = PySide2.QtCore.QLocale.Country.Jersey
    Jju = PySide2.QtCore.QLocale.Language.Jju
    JolaFonyi = PySide2.QtCore.QLocale.Language.JolaFonyi
    Jordan = PySide2.QtCore.QLocale.Country.Jordan
    Kabuverdianu = PySide2.QtCore.QLocale.Language.Kabuverdianu
    Kabyle = PySide2.QtCore.QLocale.Language.Kabyle
    KaithiScript = PySide2.QtCore.QLocale.Script.KaithiScript
    Kako = PySide2.QtCore.QLocale.Language.Kako
    Kalenjin = PySide2.QtCore.QLocale.Language.Kalenjin
    Kamba = PySide2.QtCore.QLocale.Language.Kamba
    Kannada = PySide2.QtCore.QLocale.Language.Kannada
    KannadaScript = PySide2.QtCore.QLocale.Script.KannadaScript
    Kanuri = PySide2.QtCore.QLocale.Language.Kanuri
    Kashmiri = PySide2.QtCore.QLocale.Language.Kashmiri
    KatakanaScript = PySide2.QtCore.QLocale.Script.KatakanaScript
    KayahLiScript = PySide2.QtCore.QLocale.Script.KayahLiScript
    Kazakh = PySide2.QtCore.QLocale.Language.Kazakh
    Kazakhstan = PySide2.QtCore.QLocale.Country.Kazakhstan
    Kenya = PySide2.QtCore.QLocale.Country.Kenya
    Kenyang = PySide2.QtCore.QLocale.Language.Kenyang
    KharoshthiScript = PySide2.QtCore.QLocale.Script.KharoshthiScript
    Khmer = PySide2.QtCore.QLocale.Language.Khmer
    KhmerScript = PySide2.QtCore.QLocale.Script.KhmerScript
    KhojkiScript = PySide2.QtCore.QLocale.Script.KhojkiScript
    KhudawadiScript = PySide2.QtCore.QLocale.Script.KhudawadiScript
    Kiche = PySide2.QtCore.QLocale.Language.Kiche
    Kikuyu = PySide2.QtCore.QLocale.Language.Kikuyu
    Kinyarwanda = PySide2.QtCore.QLocale.Language.Kinyarwanda
    Kirghiz = PySide2.QtCore.QLocale.Language.Kirghiz
    Kiribati = PySide2.QtCore.QLocale.Country.Kiribati
    Komi = PySide2.QtCore.QLocale.Language.Komi
    Kongo = PySide2.QtCore.QLocale.Language.Kongo
    Konkani = PySide2.QtCore.QLocale.Language.Konkani
    Korean = PySide2.QtCore.QLocale.Language.Korean
    KoreanScript = PySide2.QtCore.QLocale.Script.KoreanScript
    Koro = PySide2.QtCore.QLocale.Language.Koro
    Kosovo = PySide2.QtCore.QLocale.Country.Kosovo
    KoyraboroSenni = PySide2.QtCore.QLocale.Language.KoyraboroSenni
    KoyraChiini = PySide2.QtCore.QLocale.Language.KoyraChiini
    Kpelle = PySide2.QtCore.QLocale.Language.Kpelle
    Kurdish = PySide2.QtCore.QLocale.Language.Kurdish
    Kurundi = PySide2.QtCore.QLocale.Language.Kurundi
    Kuwait = PySide2.QtCore.QLocale.Country.Kuwait
    Kwanyama = PySide2.QtCore.QLocale.Language.Kwanyama
    Kwasio = PySide2.QtCore.QLocale.Language.Kwasio
    Kyrgyzstan = PySide2.QtCore.QLocale.Country.Kyrgyzstan
    Lakota = PySide2.QtCore.QLocale.Language.Lakota
    Langi = PySide2.QtCore.QLocale.Language.Langi
    Language = None # (!) real value is "<class 'PySide2.QtCore.QLocale.Language'>"
    LannaScript = PySide2.QtCore.QLocale.Script.LannaScript
    Lao = PySide2.QtCore.QLocale.Language.Lao
    Laos = PySide2.QtCore.QLocale.Country.Laos
    LaoScript = PySide2.QtCore.QLocale.Script.LaoScript
    LargeFloweryMiao = PySide2.QtCore.QLocale.Language.LargeFloweryMiao
    LastCountry = PySide2.QtCore.QLocale.Country.LastCountry
    LastLanguage = PySide2.QtCore.QLocale.Language.LastLanguage
    LastScript = PySide2.QtCore.QLocale.Script.LastScript
    Latin = PySide2.QtCore.QLocale.Language.Latin
    LatinAmerica = PySide2.QtCore.QLocale.Country.LatinAmerica
    LatinAmericaAndTheCaribbean = PySide2.QtCore.QLocale.Country.LatinAmericaAndTheCaribbean
    LatinScript = PySide2.QtCore.QLocale.Script.LatinScript
    Latvia = PySide2.QtCore.QLocale.Country.Latvia
    Latvian = PySide2.QtCore.QLocale.Language.Latvian
    Lebanon = PySide2.QtCore.QLocale.Country.Lebanon
    Lepcha = PySide2.QtCore.QLocale.Language.Lepcha
    LepchaScript = PySide2.QtCore.QLocale.Script.LepchaScript
    Lesotho = PySide2.QtCore.QLocale.Country.Lesotho
    Lezghian = PySide2.QtCore.QLocale.Language.Lezghian
    Liberia = PySide2.QtCore.QLocale.Country.Liberia
    Libya = PySide2.QtCore.QLocale.Country.Libya
    Liechtenstein = PySide2.QtCore.QLocale.Country.Liechtenstein
    Limbu = PySide2.QtCore.QLocale.Language.Limbu
    Limburgish = PySide2.QtCore.QLocale.Language.Limburgish
    LimbuScript = PySide2.QtCore.QLocale.Script.LimbuScript
    LinearA = PySide2.QtCore.QLocale.Language.LinearA
    LinearAScript = PySide2.QtCore.QLocale.Script.LinearAScript
    LinearBScript = PySide2.QtCore.QLocale.Script.LinearBScript
    Lingala = PySide2.QtCore.QLocale.Language.Lingala
    Lisu = PySide2.QtCore.QLocale.Language.Lisu
    LiteraryChinese = PySide2.QtCore.QLocale.Language.LiteraryChinese
    Lithuania = PySide2.QtCore.QLocale.Country.Lithuania
    Lithuanian = PySide2.QtCore.QLocale.Language.Lithuanian
    Lojban = PySide2.QtCore.QLocale.Language.Lojban
    LongFormat = PySide2.QtCore.QLocale.FormatType.LongFormat
    LowerSorbian = PySide2.QtCore.QLocale.Language.LowerSorbian
    LowGerman = PySide2.QtCore.QLocale.Language.LowGerman
    Lu = PySide2.QtCore.QLocale.Language.Lu
    LubaKatanga = PySide2.QtCore.QLocale.Language.LubaKatanga
    LuleSami = PySide2.QtCore.QLocale.Language.LuleSami
    Luo = PySide2.QtCore.QLocale.Language.Luo
    Luxembourg = PySide2.QtCore.QLocale.Country.Luxembourg
    Luxembourgish = PySide2.QtCore.QLocale.Language.Luxembourgish
    Luyia = PySide2.QtCore.QLocale.Language.Luyia
    Lycian = PySide2.QtCore.QLocale.Language.Lycian
    LycianScript = PySide2.QtCore.QLocale.Script.LycianScript
    Lydian = PySide2.QtCore.QLocale.Language.Lydian
    LydianScript = PySide2.QtCore.QLocale.Script.LydianScript
    Macau = PySide2.QtCore.QLocale.Country.Macau
    Macedonia = PySide2.QtCore.QLocale.Country.Macedonia
    Macedonian = PySide2.QtCore.QLocale.Language.Macedonian
    Machame = PySide2.QtCore.QLocale.Language.Machame
    Madagascar = PySide2.QtCore.QLocale.Country.Madagascar
    MahajaniScript = PySide2.QtCore.QLocale.Script.MahajaniScript
    Maithili = PySide2.QtCore.QLocale.Language.Maithili
    MakhuwaMeetto = PySide2.QtCore.QLocale.Language.MakhuwaMeetto
    Makonde = PySide2.QtCore.QLocale.Language.Makonde
    Malagasy = PySide2.QtCore.QLocale.Language.Malagasy
    Malawi = PySide2.QtCore.QLocale.Country.Malawi
    Malay = PySide2.QtCore.QLocale.Language.Malay
    Malayalam = PySide2.QtCore.QLocale.Language.Malayalam
    MalayalamScript = PySide2.QtCore.QLocale.Script.MalayalamScript
    Malaysia = PySide2.QtCore.QLocale.Country.Malaysia
    Maldives = PySide2.QtCore.QLocale.Country.Maldives
    Mali = PySide2.QtCore.QLocale.Country.Mali
    Malta = PySide2.QtCore.QLocale.Country.Malta
    Maltese = PySide2.QtCore.QLocale.Language.Maltese
    MandaeanScript = PySide2.QtCore.QLocale.Script.MandaeanScript
    Mandingo = PySide2.QtCore.QLocale.Language.Mandingo
    ManichaeanMiddlePersian = PySide2.QtCore.QLocale.Language.ManichaeanMiddlePersian
    ManichaeanScript = PySide2.QtCore.QLocale.Script.ManichaeanScript
    Manipuri = PySide2.QtCore.QLocale.Language.Manipuri
    Manx = PySide2.QtCore.QLocale.Language.Manx
    Maori = PySide2.QtCore.QLocale.Language.Maori
    Mapuche = PySide2.QtCore.QLocale.Language.Mapuche
    Marathi = PySide2.QtCore.QLocale.Language.Marathi
    MarchenScript = PySide2.QtCore.QLocale.Script.MarchenScript
    Marshallese = PySide2.QtCore.QLocale.Language.Marshallese
    MarshallIslands = PySide2.QtCore.QLocale.Country.MarshallIslands
    Martinique = PySide2.QtCore.QLocale.Country.Martinique
    Masai = PySide2.QtCore.QLocale.Language.Masai
    Mauritania = PySide2.QtCore.QLocale.Country.Mauritania
    Mauritius = PySide2.QtCore.QLocale.Country.Mauritius
    Mayotte = PySide2.QtCore.QLocale.Country.Mayotte
    Mazanderani = PySide2.QtCore.QLocale.Language.Mazanderani
    MeasurementSystem = None # (!) real value is "<class 'PySide2.QtCore.QLocale.MeasurementSystem'>"
    MeiteiMayekScript = PySide2.QtCore.QLocale.Script.MeiteiMayekScript
    Mende = PySide2.QtCore.QLocale.Language.Mende
    MendeKikakuiScript = PySide2.QtCore.QLocale.Script.MendeKikakuiScript
    Meroitic = PySide2.QtCore.QLocale.Language.Meroitic
    MeroiticCursiveScript = PySide2.QtCore.QLocale.Script.MeroiticCursiveScript
    MeroiticScript = PySide2.QtCore.QLocale.Script.MeroiticScript
    Meru = PySide2.QtCore.QLocale.Language.Meru
    Meta = PySide2.QtCore.QLocale.Language.Meta
    MetricSystem = PySide2.QtCore.QLocale.MeasurementSystem.MetricSystem
    Mexico = PySide2.QtCore.QLocale.Country.Mexico
    Micronesia = PySide2.QtCore.QLocale.Country.Micronesia
    ModiScript = PySide2.QtCore.QLocale.Script.ModiScript
    Mohawk = PySide2.QtCore.QLocale.Language.Mohawk
    Moldavian = PySide2.QtCore.QLocale.Language.Moldavian
    Moldova = PySide2.QtCore.QLocale.Country.Moldova
    Monaco = PySide2.QtCore.QLocale.Country.Monaco
    Mongolia = PySide2.QtCore.QLocale.Country.Mongolia
    Mongolian = PySide2.QtCore.QLocale.Language.Mongolian
    MongolianScript = PySide2.QtCore.QLocale.Script.MongolianScript
    Mono = PySide2.QtCore.QLocale.Language.Mono
    Montenegro = PySide2.QtCore.QLocale.Country.Montenegro
    Montserrat = PySide2.QtCore.QLocale.Country.Montserrat
    Morisyen = PySide2.QtCore.QLocale.Language.Morisyen
    Morocco = PySide2.QtCore.QLocale.Country.Morocco
    Mozambique = PySide2.QtCore.QLocale.Country.Mozambique
    MroScript = PySide2.QtCore.QLocale.Script.MroScript
    Mru = PySide2.QtCore.QLocale.Language.Mru
    MultaniScript = PySide2.QtCore.QLocale.Script.MultaniScript
    Mundang = PySide2.QtCore.QLocale.Language.Mundang
    Muscogee = PySide2.QtCore.QLocale.Language.Muscogee
    Myanmar = PySide2.QtCore.QLocale.Country.Myanmar
    MyanmarScript = PySide2.QtCore.QLocale.Script.MyanmarScript
    NabataeanScript = PySide2.QtCore.QLocale.Script.NabataeanScript
    Nama = PySide2.QtCore.QLocale.Language.Nama
    Namibia = PySide2.QtCore.QLocale.Country.Namibia
    NarrowFormat = PySide2.QtCore.QLocale.FormatType.NarrowFormat
    NauruCountry = PySide2.QtCore.QLocale.Country.NauruCountry
    NauruLanguage = PySide2.QtCore.QLocale.Language.NauruLanguage
    Navaho = PySide2.QtCore.QLocale.Language.Navaho
    Ndonga = PySide2.QtCore.QLocale.Language.Ndonga
    Nepal = PySide2.QtCore.QLocale.Country.Nepal
    Nepali = PySide2.QtCore.QLocale.Language.Nepali
    Netherlands = PySide2.QtCore.QLocale.Country.Netherlands
    Newari = PySide2.QtCore.QLocale.Language.Newari
    NewaScript = PySide2.QtCore.QLocale.Script.NewaScript
    NewCaledonia = PySide2.QtCore.QLocale.Country.NewCaledonia
    NewTaiLueScript = PySide2.QtCore.QLocale.Script.NewTaiLueScript
    NewZealand = PySide2.QtCore.QLocale.Country.NewZealand
    Ngiemboon = PySide2.QtCore.QLocale.Language.Ngiemboon
    Ngomba = PySide2.QtCore.QLocale.Language.Ngomba
    Nicaragua = PySide2.QtCore.QLocale.Country.Nicaragua
    Niger = PySide2.QtCore.QLocale.Country.Niger
    Nigeria = PySide2.QtCore.QLocale.Country.Nigeria
    NigerianPidgin = PySide2.QtCore.QLocale.Language.NigerianPidgin
    Niue = PySide2.QtCore.QLocale.Country.Niue
    Nko = PySide2.QtCore.QLocale.Language.Nko
    NkoScript = PySide2.QtCore.QLocale.Script.NkoScript
    NorfolkIsland = PySide2.QtCore.QLocale.Country.NorfolkIsland
    NorthernLuri = PySide2.QtCore.QLocale.Language.NorthernLuri
    NorthernMarianaIslands = PySide2.QtCore.QLocale.Country.NorthernMarianaIslands
    NorthernSami = PySide2.QtCore.QLocale.Language.NorthernSami
    NorthernSotho = PySide2.QtCore.QLocale.Language.NorthernSotho
    NorthernThai = PySide2.QtCore.QLocale.Language.NorthernThai
    NorthKorea = PySide2.QtCore.QLocale.Country.NorthKorea
    NorthNdebele = PySide2.QtCore.QLocale.Language.NorthNdebele
    Norway = PySide2.QtCore.QLocale.Country.Norway
    Norwegian = PySide2.QtCore.QLocale.Language.Norwegian
    NorwegianBokmal = PySide2.QtCore.QLocale.Language.NorwegianBokmal
    NorwegianNynorsk = PySide2.QtCore.QLocale.Language.NorwegianNynorsk
    Nuer = PySide2.QtCore.QLocale.Language.Nuer
    NumberOption = None # (!) real value is "<class 'PySide2.QtCore.QLocale.NumberOption'>"
    NumberOptions = None # (!) real value is "<class 'PySide2.QtCore.QLocale.NumberOptions'>"
    Nyanja = PySide2.QtCore.QLocale.Language.Nyanja
    Nyankole = PySide2.QtCore.QLocale.Language.Nyankole
    Occitan = PySide2.QtCore.QLocale.Language.Occitan
    OghamScript = PySide2.QtCore.QLocale.Script.OghamScript
    Ojibwa = PySide2.QtCore.QLocale.Language.Ojibwa
    OlChikiScript = PySide2.QtCore.QLocale.Script.OlChikiScript
    OldHungarianScript = PySide2.QtCore.QLocale.Script.OldHungarianScript
    OldIrish = PySide2.QtCore.QLocale.Language.OldIrish
    OldItalicScript = PySide2.QtCore.QLocale.Script.OldItalicScript
    OldNorse = PySide2.QtCore.QLocale.Language.OldNorse
    OldNorthArabianScript = PySide2.QtCore.QLocale.Script.OldNorthArabianScript
    OldPermicScript = PySide2.QtCore.QLocale.Script.OldPermicScript
    OldPersian = PySide2.QtCore.QLocale.Language.OldPersian
    OldPersianScript = PySide2.QtCore.QLocale.Script.OldPersianScript
    OldSouthArabianScript = PySide2.QtCore.QLocale.Script.OldSouthArabianScript
    OldTurkish = PySide2.QtCore.QLocale.Language.OldTurkish
    Oman = PySide2.QtCore.QLocale.Country.Oman
    OmitGroupSeparator = PySide2.QtCore.QLocale.NumberOption.OmitGroupSeparator
    OmitLeadingZeroInExponent = PySide2.QtCore.QLocale.NumberOption.OmitLeadingZeroInExponent
    Oriya = PySide2.QtCore.QLocale.Language.Oriya
    OriyaScript = PySide2.QtCore.QLocale.Script.OriyaScript
    OrkhonScript = PySide2.QtCore.QLocale.Script.OrkhonScript
    Oromo = PySide2.QtCore.QLocale.Language.Oromo
    Osage = PySide2.QtCore.QLocale.Language.Osage
    OsageScript = PySide2.QtCore.QLocale.Script.OsageScript
    OsmanyaScript = PySide2.QtCore.QLocale.Script.OsmanyaScript
    Ossetic = PySide2.QtCore.QLocale.Language.Ossetic
    OutlyingOceania = PySide2.QtCore.QLocale.Country.OutlyingOceania
    PahawhHmongScript = PySide2.QtCore.QLocale.Script.PahawhHmongScript
    Pahlavi = PySide2.QtCore.QLocale.Language.Pahlavi
    Pakistan = PySide2.QtCore.QLocale.Country.Pakistan
    Palau = PySide2.QtCore.QLocale.Country.Palau
    Palauan = PySide2.QtCore.QLocale.Language.Palauan
    PalestinianTerritories = PySide2.QtCore.QLocale.Country.PalestinianTerritories
    Pali = PySide2.QtCore.QLocale.Language.Pali
    PalmyreneScript = PySide2.QtCore.QLocale.Script.PalmyreneScript
    Panama = PySide2.QtCore.QLocale.Country.Panama
    Papiamento = PySide2.QtCore.QLocale.Language.Papiamento
    PapuaNewGuinea = PySide2.QtCore.QLocale.Country.PapuaNewGuinea
    Paraguay = PySide2.QtCore.QLocale.Country.Paraguay
    Parthian = PySide2.QtCore.QLocale.Language.Parthian
    Pashto = PySide2.QtCore.QLocale.Language.Pashto
    PauCinHauScript = PySide2.QtCore.QLocale.Script.PauCinHauScript
    PeoplesRepublicOfCongo = PySide2.QtCore.QLocale.Country.PeoplesRepublicOfCongo
    Persian = PySide2.QtCore.QLocale.Language.Persian
    Peru = PySide2.QtCore.QLocale.Country.Peru
    PhagsPaScript = PySide2.QtCore.QLocale.Script.PhagsPaScript
    Philippines = PySide2.QtCore.QLocale.Country.Philippines
    Phoenician = PySide2.QtCore.QLocale.Language.Phoenician
    PhoenicianScript = PySide2.QtCore.QLocale.Script.PhoenicianScript
    Pitcairn = PySide2.QtCore.QLocale.Country.Pitcairn
    Poland = PySide2.QtCore.QLocale.Country.Poland
    Polish = PySide2.QtCore.QLocale.Language.Polish
    PollardPhoneticScript = PySide2.QtCore.QLocale.Script.PollardPhoneticScript
    Portugal = PySide2.QtCore.QLocale.Country.Portugal
    Portuguese = PySide2.QtCore.QLocale.Language.Portuguese
    PrakritLanguage = PySide2.QtCore.QLocale.Language.PrakritLanguage
    Prussian = PySide2.QtCore.QLocale.Language.Prussian
    PsalterPahlaviScript = PySide2.QtCore.QLocale.Script.PsalterPahlaviScript
    PuertoRico = PySide2.QtCore.QLocale.Country.PuertoRico
    Punjabi = PySide2.QtCore.QLocale.Language.Punjabi
    Qatar = PySide2.QtCore.QLocale.Country.Qatar
    Quechua = PySide2.QtCore.QLocale.Language.Quechua
    QuotationStyle = None # (!) real value is "<class 'PySide2.QtCore.QLocale.QuotationStyle'>"
    Rejang = PySide2.QtCore.QLocale.Language.Rejang
    RejangScript = PySide2.QtCore.QLocale.Script.RejangScript
    RejectGroupSeparator = PySide2.QtCore.QLocale.NumberOption.RejectGroupSeparator
    RejectLeadingZeroInExponent = PySide2.QtCore.QLocale.NumberOption.RejectLeadingZeroInExponent
    RejectTrailingZeroesAfterDot = PySide2.QtCore.QLocale.NumberOption.RejectTrailingZeroesAfterDot
    RepublicOfKorea = PySide2.QtCore.QLocale.Country.RepublicOfKorea
    Reunion = PySide2.QtCore.QLocale.Country.Reunion
    RhaetoRomance = PySide2.QtCore.QLocale.Language.RhaetoRomance
    Romania = PySide2.QtCore.QLocale.Country.Romania
    Romanian = PySide2.QtCore.QLocale.Language.Romanian
    Romansh = PySide2.QtCore.QLocale.Language.Romansh
    Rombo = PySide2.QtCore.QLocale.Language.Rombo
    Rundi = PySide2.QtCore.QLocale.Language.Rundi
    RunicScript = PySide2.QtCore.QLocale.Script.RunicScript
    Russia = PySide2.QtCore.QLocale.Country.Russia
    Russian = PySide2.QtCore.QLocale.Language.Russian
    RussianFederation = PySide2.QtCore.QLocale.Country.RussianFederation
    Rwa = PySide2.QtCore.QLocale.Language.Rwa
    Rwanda = PySide2.QtCore.QLocale.Country.Rwanda
    Sabaean = PySide2.QtCore.QLocale.Language.Sabaean
    Saho = PySide2.QtCore.QLocale.Language.Saho
    SaintBarthelemy = PySide2.QtCore.QLocale.Country.SaintBarthelemy
    SaintHelena = PySide2.QtCore.QLocale.Country.SaintHelena
    SaintKittsAndNevis = PySide2.QtCore.QLocale.Country.SaintKittsAndNevis
    SaintLucia = PySide2.QtCore.QLocale.Country.SaintLucia
    SaintMartin = PySide2.QtCore.QLocale.Country.SaintMartin
    SaintPierreAndMiquelon = PySide2.QtCore.QLocale.Country.SaintPierreAndMiquelon
    SaintVincentAndTheGrenadines = PySide2.QtCore.QLocale.Country.SaintVincentAndTheGrenadines
    Sakha = PySide2.QtCore.QLocale.Language.Sakha
    Samaritan = PySide2.QtCore.QLocale.Language.Samaritan
    SamaritanScript = PySide2.QtCore.QLocale.Script.SamaritanScript
    Samburu = PySide2.QtCore.QLocale.Language.Samburu
    Samoa = PySide2.QtCore.QLocale.Country.Samoa
    Samoan = PySide2.QtCore.QLocale.Language.Samoan
    Sango = PySide2.QtCore.QLocale.Language.Sango
    Sangu = PySide2.QtCore.QLocale.Language.Sangu
    SanMarino = PySide2.QtCore.QLocale.Country.SanMarino
    Sanskrit = PySide2.QtCore.QLocale.Language.Sanskrit
    Santali = PySide2.QtCore.QLocale.Language.Santali
    SaoTomeAndPrincipe = PySide2.QtCore.QLocale.Country.SaoTomeAndPrincipe
    Saraiki = PySide2.QtCore.QLocale.Language.Saraiki
    Sardinian = PySide2.QtCore.QLocale.Language.Sardinian
    SaudiArabia = PySide2.QtCore.QLocale.Country.SaudiArabia
    Saurashtra = PySide2.QtCore.QLocale.Language.Saurashtra
    SaurashtraScript = PySide2.QtCore.QLocale.Script.SaurashtraScript
    Script = None # (!) real value is "<class 'PySide2.QtCore.QLocale.Script'>"
    Sena = PySide2.QtCore.QLocale.Language.Sena
    Senegal = PySide2.QtCore.QLocale.Country.Senegal
    Serbia = PySide2.QtCore.QLocale.Country.Serbia
    Serbian = PySide2.QtCore.QLocale.Language.Serbian
    SerboCroatian = PySide2.QtCore.QLocale.Language.SerboCroatian
    Seychelles = PySide2.QtCore.QLocale.Country.Seychelles
    Shambala = PySide2.QtCore.QLocale.Language.Shambala
    SharadaScript = PySide2.QtCore.QLocale.Script.SharadaScript
    ShavianScript = PySide2.QtCore.QLocale.Script.ShavianScript
    Shona = PySide2.QtCore.QLocale.Language.Shona
    ShortFormat = PySide2.QtCore.QLocale.FormatType.ShortFormat
    SichuanYi = PySide2.QtCore.QLocale.Language.SichuanYi
    Sicilian = PySide2.QtCore.QLocale.Language.Sicilian
    Sidamo = PySide2.QtCore.QLocale.Language.Sidamo
    SiddhamScript = PySide2.QtCore.QLocale.Script.SiddhamScript
    SierraLeone = PySide2.QtCore.QLocale.Country.SierraLeone
    SignWritingScript = PySide2.QtCore.QLocale.Script.SignWritingScript
    Silesian = PySide2.QtCore.QLocale.Language.Silesian
    SimplifiedChineseScript = PySide2.QtCore.QLocale.Script.SimplifiedChineseScript
    SimplifiedHanScript = PySide2.QtCore.QLocale.Script.SimplifiedHanScript
    Sindhi = PySide2.QtCore.QLocale.Language.Sindhi
    Singapore = PySide2.QtCore.QLocale.Country.Singapore
    Sinhala = PySide2.QtCore.QLocale.Language.Sinhala
    SinhalaScript = PySide2.QtCore.QLocale.Script.SinhalaScript
    SintMaarten = PySide2.QtCore.QLocale.Country.SintMaarten
    SkoltSami = PySide2.QtCore.QLocale.Language.SkoltSami
    Slovak = PySide2.QtCore.QLocale.Language.Slovak
    Slovakia = PySide2.QtCore.QLocale.Country.Slovakia
    Slovenia = PySide2.QtCore.QLocale.Country.Slovenia
    Slovenian = PySide2.QtCore.QLocale.Language.Slovenian
    Soga = PySide2.QtCore.QLocale.Language.Soga
    SolomonIslands = PySide2.QtCore.QLocale.Country.SolomonIslands
    Somali = PySide2.QtCore.QLocale.Language.Somali
    Somalia = PySide2.QtCore.QLocale.Country.Somalia
    Sora = PySide2.QtCore.QLocale.Language.Sora
    SoraSompengScript = PySide2.QtCore.QLocale.Script.SoraSompengScript
    SouthAfrica = PySide2.QtCore.QLocale.Country.SouthAfrica
    SouthernKurdish = PySide2.QtCore.QLocale.Language.SouthernKurdish
    SouthernSami = PySide2.QtCore.QLocale.Language.SouthernSami
    SouthernSotho = PySide2.QtCore.QLocale.Language.SouthernSotho
    SouthGeorgiaAndTheSouthSandwichIslands = PySide2.QtCore.QLocale.Country.SouthGeorgiaAndTheSouthSandwichIslands
    SouthKorea = PySide2.QtCore.QLocale.Country.SouthKorea
    SouthNdebele = PySide2.QtCore.QLocale.Language.SouthNdebele
    SouthSudan = PySide2.QtCore.QLocale.Country.SouthSudan
    Spain = PySide2.QtCore.QLocale.Country.Spain
    Spanish = PySide2.QtCore.QLocale.Language.Spanish
    SriLanka = PySide2.QtCore.QLocale.Country.SriLanka
    StandardMoroccanTamazight = PySide2.QtCore.QLocale.Language.StandardMoroccanTamazight
    StandardQuotation = PySide2.QtCore.QLocale.QuotationStyle.StandardQuotation
    Sudan = PySide2.QtCore.QLocale.Country.Sudan
    Sundanese = PySide2.QtCore.QLocale.Language.Sundanese
    SundaneseScript = PySide2.QtCore.QLocale.Script.SundaneseScript
    Suriname = PySide2.QtCore.QLocale.Country.Suriname
    SvalbardAndJanMayenIslands = PySide2.QtCore.QLocale.Country.SvalbardAndJanMayenIslands
    Swahili = PySide2.QtCore.QLocale.Language.Swahili
    Swati = PySide2.QtCore.QLocale.Language.Swati
    Swaziland = PySide2.QtCore.QLocale.Country.Swaziland
    Sweden = PySide2.QtCore.QLocale.Country.Sweden
    Swedish = PySide2.QtCore.QLocale.Language.Swedish
    SwissGerman = PySide2.QtCore.QLocale.Language.SwissGerman
    Switzerland = PySide2.QtCore.QLocale.Country.Switzerland
    Sylheti = PySide2.QtCore.QLocale.Language.Sylheti
    SylotiNagriScript = PySide2.QtCore.QLocale.Script.SylotiNagriScript
    Syria = PySide2.QtCore.QLocale.Country.Syria
    Syriac = PySide2.QtCore.QLocale.Language.Syriac
    SyriacScript = PySide2.QtCore.QLocale.Script.SyriacScript
    SyrianArabRepublic = PySide2.QtCore.QLocale.Country.SyrianArabRepublic
    Tachelhit = PySide2.QtCore.QLocale.Language.Tachelhit
    Tagalog = PySide2.QtCore.QLocale.Language.Tagalog
    TagalogScript = PySide2.QtCore.QLocale.Script.TagalogScript
    Tagbanwa = PySide2.QtCore.QLocale.Language.Tagbanwa
    TagbanwaScript = PySide2.QtCore.QLocale.Script.TagbanwaScript
    Tahitian = PySide2.QtCore.QLocale.Language.Tahitian
    TaiDam = PySide2.QtCore.QLocale.Language.TaiDam
    TaiLeScript = PySide2.QtCore.QLocale.Script.TaiLeScript
    TaiNua = PySide2.QtCore.QLocale.Language.TaiNua
    Taita = PySide2.QtCore.QLocale.Language.Taita
    TaiVietScript = PySide2.QtCore.QLocale.Script.TaiVietScript
    Taiwan = PySide2.QtCore.QLocale.Country.Taiwan
    Tajik = PySide2.QtCore.QLocale.Language.Tajik
    Tajikistan = PySide2.QtCore.QLocale.Country.Tajikistan
    TakriScript = PySide2.QtCore.QLocale.Script.TakriScript
    Tamil = PySide2.QtCore.QLocale.Language.Tamil
    TamilScript = PySide2.QtCore.QLocale.Script.TamilScript
    Tangut = PySide2.QtCore.QLocale.Language.Tangut
    TangutScript = PySide2.QtCore.QLocale.Script.TangutScript
    Tanzania = PySide2.QtCore.QLocale.Country.Tanzania
    Taroko = PySide2.QtCore.QLocale.Language.Taroko
    Tasawaq = PySide2.QtCore.QLocale.Language.Tasawaq
    Tatar = PySide2.QtCore.QLocale.Language.Tatar
    TedimChin = PySide2.QtCore.QLocale.Language.TedimChin
    Telugu = PySide2.QtCore.QLocale.Language.Telugu
    TeluguScript = PySide2.QtCore.QLocale.Script.TeluguScript
    Teso = PySide2.QtCore.QLocale.Language.Teso
    ThaanaScript = PySide2.QtCore.QLocale.Script.ThaanaScript
    Thai = PySide2.QtCore.QLocale.Language.Thai
    Thailand = PySide2.QtCore.QLocale.Country.Thailand
    ThaiScript = PySide2.QtCore.QLocale.Script.ThaiScript
    Tibetan = PySide2.QtCore.QLocale.Language.Tibetan
    TibetanScript = PySide2.QtCore.QLocale.Script.TibetanScript
    TifinaghScript = PySide2.QtCore.QLocale.Script.TifinaghScript
    Tigre = PySide2.QtCore.QLocale.Language.Tigre
    Tigrinya = PySide2.QtCore.QLocale.Language.Tigrinya
    TirhutaScript = PySide2.QtCore.QLocale.Script.TirhutaScript
    Togo = PySide2.QtCore.QLocale.Country.Togo
    Tokelau = PySide2.QtCore.QLocale.Country.Tokelau
    TokelauCountry = PySide2.QtCore.QLocale.Country.TokelauCountry
    TokelauLanguage = PySide2.QtCore.QLocale.Language.TokelauLanguage
    TokPisin = PySide2.QtCore.QLocale.Language.TokPisin
    Tonga = PySide2.QtCore.QLocale.Country.Tonga
    Tongan = PySide2.QtCore.QLocale.Language.Tongan
    TraditionalChineseScript = PySide2.QtCore.QLocale.Script.TraditionalChineseScript
    TraditionalHanScript = PySide2.QtCore.QLocale.Script.TraditionalHanScript
    TrinidadAndTobago = PySide2.QtCore.QLocale.Country.TrinidadAndTobago
    TristanDaCunha = PySide2.QtCore.QLocale.Country.TristanDaCunha
    Tsonga = PySide2.QtCore.QLocale.Language.Tsonga
    Tswana = PySide2.QtCore.QLocale.Language.Tswana
    Tunisia = PySide2.QtCore.QLocale.Country.Tunisia
    Turkey = PySide2.QtCore.QLocale.Country.Turkey
    Turkish = PySide2.QtCore.QLocale.Language.Turkish
    Turkmen = PySide2.QtCore.QLocale.Language.Turkmen
    Turkmenistan = PySide2.QtCore.QLocale.Country.Turkmenistan
    TurksAndCaicosIslands = PySide2.QtCore.QLocale.Country.TurksAndCaicosIslands
    Tuvalu = PySide2.QtCore.QLocale.Country.Tuvalu
    TuvaluCountry = PySide2.QtCore.QLocale.Country.TuvaluCountry
    TuvaluLanguage = PySide2.QtCore.QLocale.Language.TuvaluLanguage
    Twi = PySide2.QtCore.QLocale.Language.Twi
    Tyap = PySide2.QtCore.QLocale.Language.Tyap
    Uganda = PySide2.QtCore.QLocale.Country.Uganda
    Ugaritic = PySide2.QtCore.QLocale.Language.Ugaritic
    UgariticScript = PySide2.QtCore.QLocale.Script.UgariticScript
    Uighur = PySide2.QtCore.QLocale.Language.Uighur
    Uigur = PySide2.QtCore.QLocale.Language.Uigur
    Ukraine = PySide2.QtCore.QLocale.Country.Ukraine
    Ukrainian = PySide2.QtCore.QLocale.Language.Ukrainian
    UncodedLanguages = PySide2.QtCore.QLocale.Language.UncodedLanguages
    UnitedArabEmirates = PySide2.QtCore.QLocale.Country.UnitedArabEmirates
    UnitedKingdom = PySide2.QtCore.QLocale.Country.UnitedKingdom
    UnitedStates = PySide2.QtCore.QLocale.Country.UnitedStates
    UnitedStatesMinorOutlyingIslands = PySide2.QtCore.QLocale.Country.UnitedStatesMinorOutlyingIslands
    UnitedStatesVirginIslands = PySide2.QtCore.QLocale.Country.UnitedStatesVirginIslands
    UpperSorbian = PySide2.QtCore.QLocale.Language.UpperSorbian
    Urdu = PySide2.QtCore.QLocale.Language.Urdu
    Uruguay = PySide2.QtCore.QLocale.Country.Uruguay
    Uzbek = PySide2.QtCore.QLocale.Language.Uzbek
    Uzbekistan = PySide2.QtCore.QLocale.Country.Uzbekistan
    Vai = PySide2.QtCore.QLocale.Language.Vai
    VaiScript = PySide2.QtCore.QLocale.Script.VaiScript
    Vanuatu = PySide2.QtCore.QLocale.Country.Vanuatu
    VarangKshitiScript = PySide2.QtCore.QLocale.Script.VarangKshitiScript
    VaticanCityState = PySide2.QtCore.QLocale.Country.VaticanCityState
    Venda = PySide2.QtCore.QLocale.Language.Venda
    Venezuela = PySide2.QtCore.QLocale.Country.Venezuela
    Vietnam = PySide2.QtCore.QLocale.Country.Vietnam
    Vietnamese = PySide2.QtCore.QLocale.Language.Vietnamese
    Volapuk = PySide2.QtCore.QLocale.Language.Volapuk
    Vunjo = PySide2.QtCore.QLocale.Language.Vunjo
    Walamo = PySide2.QtCore.QLocale.Language.Walamo
    WallisAndFutunaIslands = PySide2.QtCore.QLocale.Country.WallisAndFutunaIslands
    Walloon = PySide2.QtCore.QLocale.Language.Walloon
    Walser = PySide2.QtCore.QLocale.Language.Walser
    Warlpiri = PySide2.QtCore.QLocale.Language.Warlpiri
    Welsh = PySide2.QtCore.QLocale.Language.Welsh
    WesternBalochi = PySide2.QtCore.QLocale.Language.WesternBalochi
    WesternFrisian = PySide2.QtCore.QLocale.Language.WesternFrisian
    WesternSahara = PySide2.QtCore.QLocale.Country.WesternSahara
    Wolof = PySide2.QtCore.QLocale.Language.Wolof
    World = PySide2.QtCore.QLocale.Country.World
    Xhosa = PySide2.QtCore.QLocale.Language.Xhosa
    Yangben = PySide2.QtCore.QLocale.Language.Yangben
    Yemen = PySide2.QtCore.QLocale.Country.Yemen
    Yiddish = PySide2.QtCore.QLocale.Language.Yiddish
    YiScript = PySide2.QtCore.QLocale.Script.YiScript
    Yoruba = PySide2.QtCore.QLocale.Language.Yoruba
    Zambia = PySide2.QtCore.QLocale.Country.Zambia
    Zarma = PySide2.QtCore.QLocale.Language.Zarma
    Zhuang = PySide2.QtCore.QLocale.Language.Zhuang
    Zimbabwe = PySide2.QtCore.QLocale.Country.Zimbabwe
    Zulu = PySide2.QtCore.QLocale.Language.Zulu
    __hash__ = None


