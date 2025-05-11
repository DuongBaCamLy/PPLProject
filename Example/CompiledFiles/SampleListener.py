# Generated from Sample.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SampleParser import SampleParser
else:
    from SampleParser import SampleParser

# This class defines a complete listener for a parse tree produced by SampleParser.
class SampleListener(ParseTreeListener):

    # Enter a parse tree produced by SampleParser#query.
    def enterQuery(self, ctx:SampleParser.QueryContext):
        pass

    # Exit a parse tree produced by SampleParser#query.
    def exitQuery(self, ctx:SampleParser.QueryContext):
        pass


    # Enter a parse tree produced by SampleParser#fields.
    def enterFields(self, ctx:SampleParser.FieldsContext):
        pass

    # Exit a parse tree produced by SampleParser#fields.
    def exitFields(self, ctx:SampleParser.FieldsContext):
        pass


    # Enter a parse tree produced by SampleParser#field.
    def enterField(self, ctx:SampleParser.FieldContext):
        pass

    # Exit a parse tree produced by SampleParser#field.
    def exitField(self, ctx:SampleParser.FieldContext):
        pass



del SampleParser