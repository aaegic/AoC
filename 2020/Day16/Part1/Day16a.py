#!/usr/bin/python3

fh = open("input.txt")
intxt = fh.read()
fh.close()

sects = intxt.split("\n\n")
srule = sects[0].split("\n")
sytkt = sects[1].split("\n")[1:]
sntkt = sects[2].replace("\n", ",").split(",")[1:]
sntkt = list(map(int, sntkt))

rules = dict()
erate = 0

for i, r in zip(range(0, len(srule) + 2, 2), srule):
    f1, f2 = r.split(':')
    f2 = f2.strip()
    r2, r3, r4 = f2.split(' ')
    r2min, r2max = r2.split('-')
    r4min, r4max = r4.split('-')
    rules.update({i: {'r1min': int(r2min), 'r1max': int(r2max), \
        'r2min': int(r4min), 'r2max': int(r4max)}})
    
for tf in sntkt:
    flag = False
    
    for rule in rules.values():
        if rule['r1min'] <= tf <= rule['r1max'] \
            or rule['r2min'] <= tf <= rule['r2max']:
            flag = True
    
    if not flag:
        erate += tf    

print(erate)