# Generated from Sample.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SampleParser import SampleParser
else:
    from SampleParser import SampleParser

# This class defines a complete generic visitor for a parse tree produced by SampleParser.

class SampleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SampleParser#query.
    def visitQuery(self, ctx:SampleParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#fields.
    def visitFields(self, ctx:SampleParser.FieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampleParser#field.
    def visitField(self, ctx:SampleParser.FieldContext):
        return self.visitChildren(ctx)



del SampleParser