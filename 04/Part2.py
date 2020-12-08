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
