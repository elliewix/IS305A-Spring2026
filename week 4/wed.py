import pathlib
print(pathlib.Path())

# import pathlib as pl
# print(pl.Path())
#

p = pathlib.Path('cats.ihatezoom')
print(p.is_dir()) #  a method
print(p.name) # an attribute

# Path is a function but from the module
print(pathlib.Path()) # function

##


# for num in range(10):
#     print("file", num)

import this

words = this.s.split()
# print(words)
target = pathlib.Path('thiswords')
target.mkdir(exist_ok=True)
for i, w in enumerate(words):
    # print(w + "_" + str(i).zfill(4) + ".txt")
    fname = w + "_" + str(i).zfill(4) + ".txt"
    fullpath = target / pathlib.Path(fname)
    # print(fullpath)
    fullpath.write_text(w)