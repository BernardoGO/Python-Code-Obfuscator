import ast
import unparse
import codegen
from ast import *
import random

def random_string(minlength= 4, maxlength = 6):
    return ''.join(chr(random.randint(0x61, 0x7a))
                   for x in xrange(random.randint(minlength, maxlength)))



class Obfuscator(ast.NodeTransformer):
    def __init__(self):
        ast.NodeTransformer.__init__(self)

        # imported modules
        self.imports = {}

        # global values (can be renamed)
        self.globs = {}

        # local values
        self.locs = {}

        # inside a function
        self.indef = False

    def obfuscate_global(self, name):
        newname = random_string(3, 10)
        self.globs[name] = newname
        return newname

    def visit_Name(self, node):
        if isinstance(node.ctx, Store):
            if node.id not in self.globs:
                node.id = self.obfuscate_global(node.id)
        #elif self.indef:
            #if isinstance(node.ctx, Store):
                #node.id = self.obfuscate_local(node.id)
            #node.id = self.locs.get(node.id, node.id)
        node.id = self.globs.get(node.id, node.id)
        return node

filename = "target.py"
with open(filename,'r') as f:
    content = f.read()
f.close()
p = ast.parse(content,filename,mode='exec')

obf = Obfuscator()
p = obf.visit(p)

print 'output source code'
print codegen.to_source(p)