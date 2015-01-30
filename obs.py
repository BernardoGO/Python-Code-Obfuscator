__author__ = 'bernardo'

import ast
import codegen

expr="""
def foo():
   print("hello world")
"""
p=ast.parse(expr)

p.body[0].body = [ ast.parse("return 42").body[0] ] # Replace function body with "return 42"

print(codegen.to_source(p))