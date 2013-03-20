### Nginx Configuration Parser

An nginx configuration parser that uses Pyparsing.

Parsing:

    >>> load(open("/etc/nginx/sites-enabled/foo.conf"))

     [['server'], [
        ['listen', '80'],
        ['server_name', 'foo.com'],
        ['root', '/home/ubuntu/sites/foo/']]]]


Dumping:

    >>> dumps([['server'], [
                ['listen', '80'],
                ['server_name', 'foo.com'],
                ['root', '/home/ubuntu/sites/foo/']]])

    'server {
        listen   80;
        server_name foo.com;
        root /home/ubuntu/sites/foo/;
     }'
