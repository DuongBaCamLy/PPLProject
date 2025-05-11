from CompiledFiles.SampleVisitor import SampleVisitor
from Logic.rules import match_rule

class FashionBot(SampleVisitor):
    def visitQuery(self, ctx):
        if ctx.fields():
            data = self.visit(ctx.fields())
        else:
            data = {}
        return self.generate_response(data)

    def visitFields(self, ctx):
        return dict(self.visit(field) for field in ctx.field())

    def visitField(self, ctx):
        key = ctx.getChild(0).getText()
        value = ctx.getChild(2).getText()
        return (key, value)

    def generate_response(self, data):
        return match_rule(data)
