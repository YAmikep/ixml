"""
See README.rst for further information

"""
try:
    # Use LXML: the Pythonic binding for the C libraries libxml2 and libxslt.
    # Known as the fastest XML library in python
    import ixml.backends.lxmliterparse as _backend
except ImportError:
    def _backend(Object):
        def parse(self, *args, **kwargs):
            raise Exception(
                'There is currently only a lxml backend so you must install lxml to use it.')
        def items(self, *args, **kwargs):
            raise Exception(
                'There is currently only a lxml backend so you must install lxml to use it.')

    # TODO: direct binding to the C libraries to avoid unused intermediate Element objects?
    # TODO: Fallback to some other backends: standard library ElementTree,
    # etc.?

parse = _backend.parse
items = _backend.items
