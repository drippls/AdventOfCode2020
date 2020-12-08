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

fields = sorted('byr iyr eyr hgt hcl ecl pid cid'.split(' '))
count = 0
for passport in data:
    person = sorted([i[0:3] for i in passport.split(' ')])
    if 'cid' not in person:
        person.append('cid')
    if sorted(person) == fields:
        count += 1
print(count)

