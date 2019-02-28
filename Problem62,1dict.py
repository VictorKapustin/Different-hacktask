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
        if isinstance(dict[strcube], list):
            dict[strcube][1] += 1
            if dict[strcube][1] == 5:
                print(dict[strcube][0])
                break
        else:
            dict[strcube] = [dict[strcube]]
            dict[strcube].append(2)
    else:
        dict[strcube] = cube

print(time.time() - starttime)
# 0.01785
