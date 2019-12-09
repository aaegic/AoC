#!/usr/bin/python3

min = 246515
max = 739105
found = 0

for _cur in range(min, max):
    if str(_cur)[1] < str(_cur)[0]: continue
    if str(_cur)[2] < str(_cur)[1]: continue
    if str(_cur)[3] < str(_cur)[2]: continue
    if str(_cur)[4] < str(_cur)[3]: continue
    if str(_cur)[5] < str(_cur)[4]: continue
    if str(_cur)[1] is str(_cur)[0]: print(_cur); found += 1; continue
    if str(_cur)[2] is str(_cur)[1]: print(_cur); found += 1; continue
    if str(_cur)[3] is str(_cur)[2]: print(_cur); found += 1; continue
    if str(_cur)[4] is str(_cur)[3]: print(_cur); found += 1; continue
    if str(_cur)[5] is str(_cur)[4]: print(_cur); found += 1; continue

print(found)