from pyparsing import *


def parse(source):
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
    assignment = Group(key
                       + space
                       + value
                       + semicolon)

    block = Forward()

    block << Group(
        Group(key + Optional(space + value))
        + left_bracket
        + Group(ZeroOrMore(assignment | block))
        + right_bracket)

    script = OneOrMore(block)

    return script.parseString(source).asList()