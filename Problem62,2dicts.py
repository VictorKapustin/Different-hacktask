import time
import itertools

dict = {}
changes = {}
count = 0
starttime = time.time()
for i in itertools.count(start=1):
    cube = i ** 3
    strcube = ''.join(sorted(str(cube)))
    if strcube in dict:
        if dict[strcube] in changes:
            changes[dict[strcube]] += 1
            if changes[dict[strcube]] == 5:
                print(dict[strcube])
                break
        else:
            changes[dict[strcube]] = 2
    else:
        dict[strcube] = cube

print(time.time() - starttime)
# 0.01735 sec
