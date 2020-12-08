with open('in.txt') as f:
    group, data = '', []
    for line in f.readlines():
        if line.strip() != '':
            group += line.strip()
        else:
            data.append(''.join(sorted(group)))
            group = ''
    data.append(group)

total = 0
for i in data:
    unique = ''.join(set(i))
    total += len(unique)
print(total)
