# with key/notation

# write text out
with open('mynewfile.txt', 'wt', encoding='utf-8') as outfile:
    # will create the outfile variable for you
    # set to the fileIO object that open creates
    # do what you need to do to outfile
    outfile.write("hello there from monday.py")

print("all done with outfile")

# outfile.write("can't write more")

# let's open a file

with open('cats.ihatezoom', 'rt', encoding='utf-8') as infile:
    text = infile.read()

print(text)

### let's talk about pathlib

import pathlib

# making a path object
p = pathlib.Path('makethisfile.txt')
print(p, type(p))
print(p.exists())
print(p.is_dir())
print(p.absolute())

print(p.name)
print(p.stem)
print(p.parent)
print(p.suffix)

p.write_text("hello here's a file from pathlib")

# let's look at it when working with folders

target = pathlib.Path('textfiles')
# print(target.exists())
target.mkdir(exist_ok=True)
print(target.exists(), target.is_dir())

# so we have a folder now
# now we want some files for it
animals = ['horse', 'rabbit', 'snake', 'cat']
for one_animal in animals:
    p = pathlib.Path(one_animal + ".txt")
    # print(p)
    # print(p.absolute())
    fileout = target / p
    print(fileout.absolute())
    fileout.write_text("this is an animalfile" + one_animal)

# you can use the with notation with this
print(" hey I made it line 58")
p = pathlib.Path('cats.ihatezoom')
with open(p, 'rt', encoding='utf-8') as infile:
    text = infile.read()
print(text)

# deleting files
print(list(target.glob('*.txt')))
deletethese = target.glob('*.txt')
for deleteme in deletethese:
    # print(deleteme)
    deleteme.unlink() # be really careful
