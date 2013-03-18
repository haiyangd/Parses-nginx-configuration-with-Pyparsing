import operator
import unittest

from mockio import mockio

from nginxparser.parser import NginxParser, load


first = operator.itemgetter(0)


class TestNginxParser(unittest.TestCase):
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


class TestNginxParserWithIO(unittest.TestCase):
    files = {
        "/etc/nginx/sites-enabled/foo.conf": '''
        server {
            listen   80;
            server_name foo.com;
            root /home/ubuntu/sites/foo/;
        }'''
    }

    @mockio(files)
    def test_parse_from_file(self):
        parsed = load(open("/etc/nginx/sites-enabled/foo.conf"))
        self.assertEqual(parsed, [
            [['server'], [
                ['listen', '80'],
                ['server_name', 'foo.com'],
                ['root', '/home/ubuntu/sites/foo/']]]])


if __name__ == '__main__':
    unittest.main()
