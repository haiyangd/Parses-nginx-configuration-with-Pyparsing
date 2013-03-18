from pyparsing import *


class NginxParser(object):
    """
    Parses nginx configuration from string
    """
    # constants
    left_bracket = Literal("{").suppress()
    right_bracket = Literal("}").suppress()
    semicolon = Literal(";").suppress()
    space = White().suppress()
    key = Word(alphanums + "_")
    value = CharsNotIn("{};,")

    # rules
    assignment = (key
                  + space
                  + value
                  + semicolon)

    block = Forward()

    block << Group(
        Group(key + Optional(space + value))
        + left_bracket
        + Group(ZeroOrMore(Group(assignment) | block))
        + right_bracket)

    script = OneOrMore(block)

    def __init__(self, source):
        self.source = source

    def parse(self):
        return self.script.parseString(self.source)

    def as_list(self):
        return self.parse().asList()


def parse(source):
    return NginxParser(source).as_list()