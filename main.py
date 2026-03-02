count = 1
for _ in range(27):
    if count == 3:
        print(count, "collect")
        count = 0
    else:
        print(count, "no")
    count += 1
all_groups = []
scratch = []
count = 1
for i in range(27):
    scratch.append(i)
    if count == 3:
        all_groups.append(scratch)
        scratch = []
        count = 0
    count += 1

print(all_groups)

all_groups = []
scratch = []
for i in range(27):
    scratch.append(i)
    if (i + 1) % 3 == 0:
        all_groups.append(scratch)
        scratch = []
print(all_groups)