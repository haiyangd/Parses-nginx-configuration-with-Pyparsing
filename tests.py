import unittest
import operator

from nginxparser.parser import NginxParser


first = operator.itemgetter(0)


class TestNginxParser(unittest.TestCase):
    def setUp(self):
        pass

    def test_assignments(self):
        parsed = NginxParser.assignment.parseString('root /test;').asList()
        self.assertEqual(parsed, ['root', '/test'])
        parsed = NginxParser.assignment.parseString('root /test;'
                                                    'foo bar;').asList()
        self.assertEqual(parsed, ['root', '/test'], ['foo', 'bar'])

    def test_blocks(self):
        parsed = NginxParser.block.parseString('foo {}').asList()
        self.assertEqual(parsed, [[['foo'], []]])
        parsed = NginxParser.block.parseString('location /foo{}').asList()
        self.assertEqual(parsed, [[['location', '/foo'], []]])
        parsed = NginxParser.block.parseString('foo { bar foo; }').asList()
        self.assertEqual(parsed, [[['foo'], [['bar', 'foo']]]])

    def test_nested_blocks(self):
        parsed = NginxParser.block.parseString('foo { bar {} }').asList()
        block, content = first(parsed)
        self.assertEqual(first(content), [['bar'], []])


if __name__ == '__main__':
    unittest.main()
