# Generated from Sample.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\35\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\5\2\f\n\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\2\2\5\2\4\6\2\2\2\33\2\b\3\2\2\2\4\20\3")
        buf.write("\2\2\2\6\30\3\2\2\2\b\t\7\3\2\2\t\13\7\4\2\2\n\f\5\4\3")
        buf.write("\2\13\n\3\2\2\2\13\f\3\2\2\2\f\r\3\2\2\2\r\16\7\5\2\2")
        buf.write("\16\17\7\2\2\3\17\3\3\2\2\2\20\25\5\6\4\2\21\22\7\6\2")
        buf.write("\2\22\24\5\6\4\2\23\21\3\2\2\2\24\27\3\2\2\2\25\23\3\2")
        buf.write("\2\2\25\26\3\2\2\2\26\5\3\2\2\2\27\25\3\2\2\2\30\31\7")
        buf.write("\b\2\2\31\32\7\7\2\2\32\33\7\b\2\2\33\7\3\2\2\2\4\13\25")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'outfit'", "'('", "')'", "','", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_query = 0
    RULE_fields = 1
    RULE_field = 2

    ruleNames =  [ "query", "fields", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ID=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SampleParser.EOF, 0)

        def fields(self):
            return self.getTypedRuleContext(SampleParser.FieldsContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = SampleParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(SampleParser.T__0)
            self.state = 7
            self.match(SampleParser.T__1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SampleParser.ID:
                self.state = 8
                self.fields()


            self.state = 11
            self.match(SampleParser.T__2)
            self.state = 12
            self.match(SampleParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SampleParser.FieldContext)
            else:
                return self.getTypedRuleContext(SampleParser.FieldContext,i)


        def getRuleIndex(self):
            return SampleParser.RULE_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFields" ):
                listener.enterFields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFields" ):
                listener.exitFields(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFields" ):
                return visitor.visitFields(self)
            else:
                return visitor.visitChildren(self)




    def fields(self):

        localctx = SampleParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.field()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SampleParser.T__3:
                self.state = 15
                self.match(SampleParser.T__3)
                self.state = 16
                self.field()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SampleParser.ID)
            else:
                return self.getToken(SampleParser.ID, i)

        def getRuleIndex(self):
            return SampleParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = SampleParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(SampleParser.ID)
            self.state = 23
            self.match(SampleParser.T__4)
            self.state = 24
            self.match(SampleParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





