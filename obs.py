import ast
import unparse
import astor
from ast import *
import random

def random_string(minlength= 8, maxlength = 10):
    return ''.join(chr(random.randint(0x61, 0x7a))
                   for x in xrange(random.randint(minlength, maxlength)))

def random_spaces(minlength= 0, maxlength = 6):
    return ''.join(' '
                   for x in xrange(random.randint(minlength, maxlength)))

def random_slice(inp, minlength= 0, maxlength = 6):
    start = random.randint(minlength, maxlength/2)
    end = random.randint(start, maxlength)
    return inp[start:end]

def chunk(in_string,num_chunks):
    chunk_size = len(in_string)//num_chunks
    if len(in_string) % num_chunks: chunk_size += 1
    iterator = iter(in_string)
    for _ in range(num_chunks):
        accumulator = list()
        for _ in range(chunk_size):
            try: accumulator.append(next(iterator))
            except StopIteration: break
        yield ''.join(accumulator)

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

filename = "run.py"
with open(filename,'r') as f:
    content = f.read()
f.close()
p = ast.parse(content,filename,mode='exec')

obf = Obfuscator()
#p = obf.visit(p)

#print 'output source code'
codesr =  astor.to_source(p)
print codesr


codesr = codesr.replace("   ", "$").replace("\n", "$.$")
for hufd in reversed(range(10, 140)):
    codesr = codesr.replace(chr(hufd), chr(hufd+2))
cd = codesr.split("\"")

temp = ""
for ty in cd:
    xy = ""
    for c in ty:
        xy += str(c ) + random_spaces()
    temp += random_spaces() + xy  + "\"\n"

codesr = temp[ 0: len(temp)-2]

codes = list(chunk(codesr,2))

final = """
_ = \"\"\"%%code%%\"\"\"
t=range;import string;r = string.replace;__=globals;x_=10;_x=140;c=chr;_ += \"\"\"%%code1%%\"\"\"
_=r(_,"\\n", "");_=r(_," ", "");
def u(_): exec(
_,__());
for (_h__) in (((t(x_,_x)))): _=r(_,c(_h__+2),c(_h__))
_=r(_,"$.$", '\\n');_=r(_,"$", "    ");u(_)
"""

text_file = open("output.py", "w")
text_file.write(final.replace("%%code%%", codes[0]).replace("%%code1%%", codes[1]).replace("%%code1%%", random_slice(codesr, 10, len(codesr)-2)))
text_file.close()



