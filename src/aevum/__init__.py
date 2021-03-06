from ._version import __version__
from .api import get, now, utc
from .aevum import Format
from .factory import AevumFactory
from .formatter import (
    FORMAT_ATOM,
    FORMAT_COOKIE,
    FORMAT_RFC822,
    FORMAT_RFC850,
    FORMAT_RFC1036,
    FORMAT_RFC1123,
    FORMAT_RFC2822,
    FORMAT_RFC3339,
    FORMAT_RSS,
    FORMAT_W3C,
)
from .parser import ParserError

# https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-no-implicit-reexport
# Mypy with --strict or --no-implicit-reexport requires an explicit reexport.
__all__ = [
    "__version__",
    "get",
    "now",
    "utc",
    "Format",
    "AevumFactory",
    "FORMAT_ATOM",
    "FORMAT_COOKIE",
    "FORMAT_RFC822",
    "FORMAT_RFC850",
    "FORMAT_RFC1036",
    "FORMAT_RFC1123",
    "FORMAT_RFC2822",
    "FORMAT_RFC3339",
    "FORMAT_RSS",
    "FORMAT_W3C",
    "ParserError",
]



__version__ = "2021.1"
