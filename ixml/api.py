"""
See README.rst for further information

"""
try:
    # Use LXML: the Pythonic binding for the C libraries libxml2 and libxslt.
    # Known as the fastest XML library in python
    import ixml.backends.lxmliterparse as _backend
except ImportError:
    # Awaiting a real fallback backend, this makes pip installing works.
    class FakeFallbackBackend(object):
        @staticmethod
        def parse(*args, **kwargs):
            raise Exception(
                'There is currently only a lxml backend so you must install lxml to use it.')
        @staticmethod
        def items(*args, **kwargs):
            raise Exception(
                'There is currently only a lxml backend so you must install lxml to use it.')

    _backend = FakeFallbackBackend

    # TODO: direct binding to the C libraries to avoid unused intermediate Element objects?
    # TODO: Fallback to some other backends: standard library ElementTree,
    # etc.?

parse = _backend.parse
items = _backend.items
