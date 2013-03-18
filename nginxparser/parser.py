from pyparsing import *


def parse(source):
    left_bracket = Literal("{").suppress()
    right_bracket = Literal("}").suppress()
    semicolon = Literal(";").suppress()
    space = White().suppress()

    key = Word(alphanums + "_")
    value = CharsNotIn("{};,")

    assignment = Group(key + space + value + semicolon)

    block = Forward()

    block << key + Optional(value) + left_bracket + ZeroOrMore(
        assignment | block) + right_bracket

    return OneOrMore(Group(block)).parseString(source)