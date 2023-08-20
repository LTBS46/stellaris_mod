import sys
import os
import os.path

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from target_antlr.StellarisLexer import StellarisLexer
from target_antlr.StellarisParser import StellarisParser
from target_antlr.StellarisParserListener import StellarisParserListener
from maker.Mod import Mod

directory = sys.argv[1]
mod_source = sys.argv[2]

class StellarisListener(StellarisParserListener):
    def enterMod(self, ctx:StellarisParser.ModContext):
        self._mod_content = None

    def enterTradition_category(self, ctx:StellarisParser.Tradition_categoryContext):
        name = ctx.name.text
        self._mod_content.add_tradition_cateogries(name, ctx.tree.text)
        sub = ctx.n1
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.tradition_categories[name].tradition_1 = sub.text        
        sub = ctx.n2
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.tradition_categories[name].tradition_2 = sub.text
        sub = ctx.n3
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.tradition_categories[name].tradition_3 = sub.text
        sub = ctx.n4
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.tradition_categories[name].tradition_4 = sub.text
        sub = ctx.n5
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.tradition_categories[name].tradition_5 = sub.text

        sub = ctx.adopt_id
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.tradition_categories[name].tradition_adopt = sub.text

        sub = ctx.finish_id
        if sub is not None: # else enterTradition_item will be called by the walker
            self._mod_content.tradition_categories[name].tradition_finish = sub.text

        

    def enterTradition_item(self, ctx:StellarisParser.Tradition_itemContext):
        print(ctx.parentCtx)

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
            f.write(data[current_file].encode('utf-8-sig'))

    