#!/usr/bin/python3

import re

fh = open("input.txt", mode='r')
intxt = fh.read()
fh.close()

intxt = intxt.strip()
intxt = intxt.split("\n\n")

gpp = []

for l in intxt:
    j = l.replace(" ", "\n")
    p = j.split("\n")

    pp = { 
        "byr": "", 
        "iyr": "", 
        "eyr": "", 
        "hgt": "", 
        "hcl": "", 
        "ecl": "",
        "pid": "",
    }
    
    for f in p:
        [ fk, fv ] = f.split(":")

        if fk == "byr" and 1920 <= int(fv) <= 2002: pp[fk] = int(fv)
        if fk == "iyr" and 2010 <= int(fv) <= 2020: pp[fk] = int(fv)
        if fk == "eyr" and 2020 <= int(fv) <= 2030: pp[fk] = int(fv)
        if fk == "pid" and re.fullmatch('([0-9]){9}', fv): pp[fk] = fv
        if fk == "hcl" and re.fullmatch('#(([0-9])*([a-f])*){6}', fv): pp[fk] = fv
        if fk == "ecl" and fv in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: pp[fk] = fv
        if fk == "hgt" and fv.endswith('cm') and 150 <= int(fv[:-2]) <= 193: pp[fk] = fv
        if fk == "hgt" and fv.endswith('in') and 59 <= int(fv[:-2]) <= 76: pp[fk] = fv

    if '' not in pp.values(): gpp.append(pp)

print(len(gpp))