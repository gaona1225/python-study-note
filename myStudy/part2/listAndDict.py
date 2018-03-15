#!/usr/bin/env python
#coding=utf-8

table = {"python":"Fuido van Rossum",
         "Perl":"Larry Wall",
         "Tcl":"John Ousterhout"
         }

language = "python"
creator = table[language]
print creator #output Fuido van Rossum

for lang in table.keys():
    print lang,"\t",table[lang]

""" output
    Perl      Larry Wall
    python    Fuido van Rossum
    Tcl       John Ousterhout
"""


rec = {}
rec["name"] = "mel"
rec["age"] = 30
rec["job"] = "trainer/writer"

print rec #output {'job': 'trainer/writer', 'age': 30, 'name': 'mel'}
