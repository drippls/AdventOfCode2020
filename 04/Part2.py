with open('in.txt') as f:
    data, collect = [], []
    for line in f.readlines():
        item = line.strip()
        if item != '':
            collect += item + ' '
        else:
            data.append(''.join(collect[:-1]))
            collect = []
    data.append(''.join(collect[:-1]))

fields = sorted('byr iyr eyr hgt hcl ecl pid'.split(' '))

for passport in data:
    passport = passport.split()
    # Dealing with 'cid' values
    for key in passport:
        if key[:3] == 'cid':
            passport.pop(passport.index(key))
        if len(passport) == len(fields):
            if key[:3] == 'byr' and (int(key[4:]) >= 1920 and int(key[4:]) <= 2002):
                print(key)
