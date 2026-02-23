import random

total = 0
run_count = 0

while total <= 100:
    total += random.randint(0,10)
    run_count += 1

print(total, run_count)
