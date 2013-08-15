"""
Define the reusable sets of data to use for testing.
"""

XML_HEADER = """<?xml version="1.0" encoding="utf-8"?>"""

# Sets of data test
# Tuples (name, xml, events_expected, path, objects_expected)

XML_TEST_DATA_SETS = [
    (
        'simple',
        XML_HEADER +
        '''<rss version="2.0">
                <channel>
                    <item>
                        <title>Title item 1</title>
                        <description>Description item 1</description>
                    </item>
                    <item>
                        <title>Title item 2</title>
                        <description>Description item 2</description>
                    </item>
                </channel>
            </rss>''',
        (
            ('rss', 'start', None),
            ('rss.@version', 'data', '2.0'),
            ('rss.channel', 'start', None),

            ('rss.channel.item', 'start', None),
            ('rss.channel.item.title', 'data', 'Title item 1'),
            ('rss.channel.item.description', 'data', 'Description item 1'),
            ('rss.channel.item', 'end', None),

            ('rss.channel.item', 'start', None),
            ('rss.channel.item.title', 'data', 'Title item 2'),
            ('rss.channel.item.description', 'data', 'Description item 2'),
            ('rss.channel.item', 'end', None),

            ('rss.channel', 'end', None),
            ('rss', 'end', None)
        ),
        'rss.channel.item',
        (
            {'description': 'Description item 1', 'title': 'Title item 1'},
            {'description': 'Description item 2', 'title': 'Title item 2'},
        )
    ),
    (
        'medium',
        XML_HEADER +
        '''<rss version="2.0">
                <channel>
                    <item name="i1" xmlns="http://www.defaultns.com">
                        <title>Title item 1</title>
                        <description>Description item 1</description>
                        <category code="1">Category item 1</category>  <!-- A COMMENT -->
                    </item>
                    <item name="i2" xmlns:ns2="http://www.ns2.com">
                        <ns2:title>Title item 2</ns2:title>
                        <ns2:description>Description item 2</ns2:description>
                        <ns2:category code="2">Category item 2</ns2:category>
                    </item>
                </channel>
            </rss>''',
        (
            ('rss', 'start', None),
            ('rss.@version', 'data', '2.0'),
            ('rss.channel', 'start', None),

            ('rss.channel.item', 'start', None),
            ('rss.channel.item.@name', 'data', 'i1'),
            ('rss.channel.item.title', 'data', 'Title item 1'),
            ('rss.channel.item.description', 'data', 'Description item 1'),
            ('rss.channel.item.category', 'data', 'Category item 1'),
            ('rss.channel.item.category.@code', 'data', '1'),
            ('rss.channel.item', 'end', None),

            ('rss.channel.item', 'start', None),
            ('rss.channel.item.@name', 'data', 'i2'),
            ('rss.channel.item.ns2:title', 'data', 'Title item 2'),
            ('rss.channel.item.ns2:description', 'data', 'Description item 2'),
            ('rss.channel.item.ns2:category', 'data', 'Category item 2'),
            ('rss.channel.item.ns2:category.@code', 'data', '2'),
            ('rss.channel.item', 'end', None),

            ('rss.channel', 'end', None),
            ('rss', 'end', None)
        ),
        'rss.channel.item',
        (
            {
                '@name': 'i1',
                'category': 'Category item 1',
                'category.@code': '1',
                'description': 'Description item 1',
                'title': 'Title item 1'
            },
            {
                '@name': 'i2',
                'ns2:category': 'Category item 2',
                'ns2:category.@code': '2',
                'ns2:description': 'Description item 2',
                'ns2:title': 'Title item 2'
            }
        )
    ),
    (
        'complex',
        XML_HEADER +
        '''<rss version="2.0">
                <channel>
                    <item name="i1" xmlns="http://www.defaultns.com">
                        <title>Title item 1</title>
                        <description nb="2">      <!-- Sub Element -->
                            <short>Desc item 1 short</short>
                            <long>Desc item 1 long</long>
                        </description>
                        <category code="1">Category 1 item 1</category>
                        <category code="2">Category 2 item 1</category>
                    </item>
                    <item name="i2" xmlns:ns2="http://www.ns2.com">
                        <ns2:title>Title item 2</ns2:title>
                        <ns2:description nb="2">
                            <short>Desc item 2 short</short>
                            <long>Desc item 2 long</long>
                        </ns2:description>
                        <ns2:category code="1">Category 1 item 2</ns2:category>
                        <ns2:category code="2">Category 2 item 2</ns2:category>
                        <ns2:category code="3">Category 3 item 2</ns2:category>
                    </item>
                </channel>
            </rss>''',
        (
            ('rss', 'start', None),
            ('rss.@version', 'data', '2.0'),
            ('rss.channel', 'start', None),

            ('rss.channel.item', 'start', None),
            ('rss.channel.item.@name', 'data', 'i1'),
            ('rss.channel.item.title', 'data', 'Title item 1'),
            ('rss.channel.item.description', 'start', None),
            ('rss.channel.item.description.@nb', 'data', '2'),
            ('rss.channel.item.description.short',
             'data', 'Desc item 1 short'),
            ('rss.channel.item.description.long', 'data', 'Desc item 1 long'),
            ('rss.channel.item.description', 'end', None),
            ('rss.channel.item.category', 'data', 'Category 1 item 1'),
            ('rss.channel.item.category.@code', 'data', '1'),
            ('rss.channel.item.category', 'data', 'Category 2 item 1'),
            ('rss.channel.item.category.@code', 'data', '2'),
            ('rss.channel.item', 'end', None),

            ('rss.channel.item', 'start', None),
            ('rss.channel.item.@name', 'data', 'i2'),
            ('rss.channel.item.ns2:title', 'data', 'Title item 2'),
            ('rss.channel.item.ns2:description', 'start', None),
            ('rss.channel.item.ns2:description.@nb', 'data', '2'),
            ('rss.channel.item.ns2:description.short',
             'data', 'Desc item 2 short'),
            ('rss.channel.item.ns2:description.long',
             'data', 'Desc item 2 long'),
            ('rss.channel.item.ns2:description', 'end', None),
            ('rss.channel.item.ns2:category', 'data', 'Category 1 item 2'),
            ('rss.channel.item.ns2:category.@code', 'data', '1'),
            ('rss.channel.item.ns2:category', 'data', 'Category 2 item 2'),
            ('rss.channel.item.ns2:category.@code', 'data', '2'),
            ('rss.channel.item.ns2:category', 'data', 'Category 3 item 2'),
            ('rss.channel.item.ns2:category.@code', 'data', '3'),
            ('rss.channel.item', 'end', None),

            ('rss.channel', 'end', None),
            ('rss', 'end', None)
        ),
        'rss.channel.item',
        (
            {
                '@name': 'i1',
                'category': [
                    'Category 1 item 1',
                    'Category 2 item 1'
                ],
                'category.@code': [
                    '1',
                    '2'
                ],
                'description': {
                    '@nb': '2',
                    'long': 'Desc item 1 long',
                    'short': 'Desc item 1 short'
                },
                'title': 'Title item 1'
            },
            {
                '@name': 'i2',
                'ns2:category': [
                    'Category 1 item 2',
                    'Category 2 item 2',
                    'Category 3 item 2'
                ],
                'ns2:category.@code': [
                    '1',
                    '2',
                    '3'
                ],
                'ns2:description': {
                    '@nb': '2',
                    'long': 'Desc item 2 long',
                    'short': 'Desc item 2 short'
                },
                'ns2:title': 'Title item 2'
            }
        )
    ),
]


import pkgutil


def iter_import_modules(package):
    prefix = package.__name__ + "."
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
        module = __import__(modname, fromlist='dummy')
        yield module

import ixml.backends
package = ixml.backends
all_backends = list(iter_import_modules(package))


def load_backend_tests(backend):
    nb_datasets = len(XML_TEST_DATA_SETS)
    return [
        (
            '{}_{}'.format(
                backend.__name__.replace('.', '_'),
                XML_TEST_DATA_SETS[i][0]  # name
            ),
            backend,
            i
        )
        for i in xrange(nb_datasets)
    ]


def load_all_backends_tests():
    tests = []
    for t in map(load_backend_tests, all_backends):
        tests.extend(t)
    return tests
