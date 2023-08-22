import sys
import os
import os.path

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from src.antlrlib.StellarisLexer import StellarisLexer
from src.antlrlib.StellarisParser import StellarisParser
from src.antlrlib.StellarisParserListener import StellarisParserListener
from src.Mod import Mod

directory = sys.argv[1]
mod_source = sys.argv[2]

class StellarisListener(StellarisParserListener):
    def enterMod(self, ctx:StellarisParser.ModContext):
        self._mod_content = None

    def enterVersion_value(self, ctx:StellarisParser.Version_valueContext):
        parent = ctx.parentCtx
        kind = type(parent)
        if kind == StellarisParser.Mod_versionContext:
            pass
        elif kind == StellarisParser.Game_versionContext:
            pass
        else:
            assert(False)

    def enterTechnology(self, ctx:StellarisParser.TechnologyContext):
        self._mod_content.add_technology(ctx.name, ctx.field, ctx.cat)

    def enterTradition_category(self, ctx:StellarisParser.Tradition_categoryContext):
        name = ctx.name.text
        self._mod_content.add_tradition_categories(name, ctx.tree.text)
        sub = ctx.n1
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.set_tradition_for_categories(name, sub.text, 1)
        sub = ctx.n2
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.set_tradition_for_categories(name, sub.text, 2)
        sub = ctx.n3
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.set_tradition_for_categories(name, sub.text, 3)
        sub = ctx.n4
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.set_tradition_for_categories(name, sub.text, 4)
        sub = ctx.n5
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.set_tradition_for_categories(name, sub.text, 5)
        sub = ctx.adopt_id
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.set_tradition_for_categories(name, sub.text, 0)
        sub = ctx.finish_id
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.set_tradition_for_categories(name, sub.text, -1)

        

    def enterTradition_item(self, ctx:StellarisParser.Tradition_itemContext):
        parent = ctx.parentCtx
        kind = type(ctx.parentCtx)
        name = ctx.name.text
        selectable = None
        of = None
        if kind == StellarisParser.Tradition_categoryContext:
            pp: StellarisParser.Tradition_categoryContext = parent
            pname = pp.name.text
            name = f"{pname}_{name}"
            if pp.t1 == ctx:
                self._mod_content.set_tradition_for_categories(pname, name, 1)
            elif pp.t2 == ctx:   
                self._mod_content.set_tradition_for_categories(pname, name, 2)
            elif pp.t3 == ctx:
                self._mod_content.set_tradition_for_categories(pname, name, 3)
            elif pp.t4 == ctx:
                self._mod_content.set_tradition_for_categories(pname, name, 4)  
            elif pp.t5 == ctx:
                self._mod_content.set_tradition_for_categories(pname, name, 5)
            elif pp.ta == ctx:
                selectable = "adopt"
                self._mod_content.set_tradition_for_categories(pname, name, 0)  
            elif pp.tf == ctx:
                selectable = "finish"
                self._mod_content.set_tradition_for_categories(pname, name, -1)     
            else:
                assert(False)
            of = self._mod_content.tradition_categories[pname]
        elif kind == StellarisParser.ContentContext:
            pass
        else:
            assert(False)
        self._mod_content.add_tradition(name, selectable, of)



    def enterDescription(self, ctx: StellarisParser.DescriptionContext):
        parent = ctx.parentCtx
        kind = type(ctx.parentCtx)
        #print(ctx.getText()[5:], "is in", str(kind)[8:-2])
        if kind == StellarisParser.Tradition_categoryContext:
            pass
        elif kind == StellarisParser.OriginContext:
            pass
        elif kind == StellarisParser.CivicContext:
            pass
        elif kind == StellarisParser.TechnologyContext:
            pass
        elif kind == StellarisParser.AperkContext:
            pass
        elif kind == StellarisParser.Tradition_itemContext:
            pass
        else:
            assert(False)

    def enterDescriptor(self, ctx:StellarisParser.DescriptorContext):
        name = ctx.mod_name.text
        self._mod_content = Mod(name)

    def enterTag(self, ctx:StellarisParser.TagContext):
        self._mod_content.add_tags(ctx.getText())
        
if __name__ == "__main__":
    input_data = FileStream(mod_source)
    lexer = StellarisLexer(input_data)
    stream = CommonTokenStream(lexer)
    parser = StellarisParser(stream)
    tree = parser.mod()

    listener = StellarisListener()

    walker = ParseTreeWalker()

    walker.walk(listener, tree)

    data = listener._mod_content.generate_all_the_data()

    for current_file in data:
        final_path = os.path.join(directory, current_file)
        os.makedirs(os.path.dirname(final_path), exist_ok=True)
        with open(final_path, "wb") as f:
            if current_file.split(os.path.sep, 1)[0] in [
                "descriptor.mod", "common"
            ]:
                f.write(data[current_file].encode('utf-8-sig'))
            else:
                print("cannot generate :", repr(current_file))

    