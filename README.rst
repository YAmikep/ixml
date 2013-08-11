=================================================
iXML - A simple iterative event-driven XML parser
=================================================

iXML is an iterative event-driven XML parser with a standard Python iterator interface.



Docs
----

.. http://ixml.readthedocs.org/en/latest/



Install
-------

From PyPI (stable)::

    pip install ixml

From Bitbucket (unstable)::

    pip install git+git://git@bitbucket.org/YAmikep/ixml.git#egg=iXML



Main API:
---------

- ``ixml.parse(data)``: iterator returning parsing events.

- ``ixml.items(data, path, builder_klass=DictObjectBuilder)``: iterator returning Python objects found under a specified path.
    
The objects are constructed from the events thanks to an ObjectBuilder (DictObjectBuilder by default).
Please make your own if you wish as long as it implements the ObjectBuilder interface (ixml.builders.interface).

Top-level ``ixml`` module tries to automatically find and import a suitable
parsing backend. You can also explicitly import a required backend from
``ixml.backends``.



Usage and examples
------------------

All usage example will be using this XML document.

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <cities>
        <city name="Paris">
            <country>France</country>
            <language>French</language>
            <attractions>
                <monument>Tour Eiffel</monument>
                <monument>Arc de triomphe</monument>
                <museum>Musee du Louvre</museum>
                <museum>Musee du Quai Branly</museum>*
            </attractions>          
        </city>
        <city name="Dallas">
            <country>USA</country>
            <language>English</language>
            <attractions>
                <monument>Bank America Plaza</monument>
                <monument>Dallas Theatre Center</monument>
                <museum>Dallas Museum of Art</museum>
                <museum>Old Red Museum</museum>
            </attractions>          
        </city> 
    </cities>


1. Using the ``parse`` function, you can react on individual events::

    import ixml
    from StringIO import StringIO

    data = StringIO(XML)

    # Extract only the languages and the countries
    languages, countries = set(), set()
    for path, event, value in ixml.parse(data):
        if path == 'cities.city.language':
            languages.add(value)
        elif path == 'cities.city.country':
            countries.add(value)

    The full output of ``parse`` would be::

        ('cities', u'start', None)
        ('cities.city', u'start', None)
        ('cities.city.@name', 'data', 'Paris')
        ('cities.city.country', 'data', 'France')
        ('cities.city.language', 'data', 'French')
        ('cities.city.attractions', u'start', None)
        ('cities.city.attractions.monument', 'data', 'Tour Eiffel')
        ('cities.city.attractions.monument', 'data', 'Arc de triomphe')
        ('cities.city.attractions.museum', 'data', 'Musee du Louvre')
        ('cities.city.attractions.museum', 'data', 'Musee du Quai Branly')
        ('cities.city.attractions', u'end', None)
        ('cities.city', u'end', None)
        ('cities.city', u'start', None)
        ('cities.city.@name', 'data', 'Dallas')
        ('cities.city.country', 'data', 'USA')
        ('cities.city.language', 'data', 'English')
        ('cities.city.attractions', u'start', None)
        ('cities.city.attractions.monument', 'data', 'Bank America Plaza')
        ('cities.city.attractions.monument', 'data', 'Dallas Theatre Center')
        ('cities.city.attractions.museum', 'data', 'Dallas Museum of Art')
        ('cities.city.attractions.museum', 'data', 'Old Red Museum')
        ('cities.city.attractions', u'end', None)
        ('cities.city', u'end', None)
        ('cities', u'end', None)


2. Another usage is having ixml yield native Python objects for a specific path with ``items``::

    import ixml
    from StringIO import StringIO

    data = StringIO(XML)

    for city in ixml.items(data, 'cities.city'):
        do_something_with(city)

    Below are the two 'city' Python objects yield by ``items``. They are constructed as a dict by default. 
    You can change this behavior by providing another builder class to the ``items`` function::

    {   
        'country': 'France', 
        '@name': 'Paris', 
        'language': 'French', 
        'attractions': {
            'museum': ['Musee du Louvre', 'Musee du Quai Branly'],
            'monument': ['Tour Eiffel', 'Arc de triomphe']
        }
    }

    {
        'country': 'USA',
        '@name': 'Dallas',
        'language': 'English',
        'attractions': {
            'museum': ['Dallas Museum of Art', 'Old Red Museum'], 
            'monument': ['Bank America Plaza', 'Dallas Theatre Center']
        }
    }



Parsing events
--------------

Parsing events contain the XML tree context (path), an event and a value: ``(path, event, value)``.

The tree context is a simplified path format that:

- uses dots to define different levels
- uses namespace prefixes in the tag name instead of the URI
- ignores default namespaces (handled automatically behind the scene)
- uses @ for attributes


Example of paths:

- rss.channel.item
- rss.channel.item.@myAttr
- rss.channel.ns1:item.title


The events are:

- 'start' and 'end' for containers::

    <rss>   # => ('rss', 'start', None)
        <...>
    </rss>  # => ('rss', 'end', None)


- 'data' for leaves and attributes::

    <rss>   
        <title myAttr="Test">Some text</title>  # => ('rss.title', 'data', 'Some text'), ('rss.title.@myAttr', 'data', 'Test')
    </rss>

If there is a value, it will always be a string, None otherwise.
There is no automatic conversion feature (to int, etc) for now.


Backends
--------

iXML can provide several implementation of the parsing by using backends located in ixml/backends::

- ``lxmliterparse``: wrapper around the well known iterparse LXML function.

More backends, especially a fallback backend using the standard library will follow.
You can import a specific backend and use it in the same way as the top level library::

    import ixml.backends.lxmliterparse as ixml

    for path, event, value in ixml.parse(...):
        # ...

Importing the top level library as ``import ixml`` tries to import all backends
in order, so it either finds an appropriate version of LXML or falls back to the
Python backend if none is found.
For now, it will just raise an exception if LXML cannot be found.


ObjecBuilder
------------
