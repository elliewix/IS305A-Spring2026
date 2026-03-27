import pathlib

p = pathlib.Path('./..')
print(p.absolute())
# print(list(p.glob('*'))) # only works at one level
print(list(p.rglob('*.py')))

###

import json
with open('data.json', 'rt', encoding='utf-8') as infile:
    data = json.load(infile)
print(data)

flattened = []
def flatten_these(l):
    for item in l:
        if isinstance(item, list):
            # keep going
            flatten_these(item)
        else:
            flattened.append(item)

flatten_these(data)
print(flattened)

#####

# replacement rules

rules = {'a': 'x',
         'b': 'y',
         'e': 'a+b',
         'f': 'a-b',
         'g': 'e+f',
         'h': 'e-f',
         'i': '-e',
         'j':'+f'}

def apply_rules(start):
    new = ""
    base_chars = "xy+-"
    for char in start:
        new += rules.get(char, char )
    # print([(c in base_chars) for c in new])
    if all([(c in base_chars) for c in new]):
        return new
    else:
        return apply_rules(new)

print(apply_rules("abej-eeghggge+-j"))