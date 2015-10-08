
from lxml import etree
from lxml.cssselect import CSSSelector

from xcrawler.utils.converters.string_converter import StringConverter
from xcrawler.collections.fallback_list import FallbackList


class SelectorCss:
    """Gets a list of Elements that match a CSS selector from an instance of an Element object.

    Attributes:
        element (Element): an instance of an Element object that contains nested Elements
        string_converter(StringConverter): the StringConverter that converts a string to an unicode string
    """

    def __init__(self,
                 element=None,
                 string_converter=StringConverter()):
        self.element = element
        self.string_converter = string_converter

