with open('in.txt') as f:
    data = [i.strip() for i in f.readlines()]

ids = []
for ticket in data:
    row, column = list(range(0, 128)), list(range(0, 8))
    for letter in ticket:
        if letter == 'F':
            row = row[0:len(row)//2]
        if letter == 'B':
            row = row[len(row)//2:]
        if letter == 'L':
            column = column[0:len(column)//2]
        if letter == 'R':
            column = column[len(column)//2:]
    ids.append((row[0] * 8) + column[0])
print(max(ids))

# Part 2

for i in sorted(ids):
    if i - 1 not in ids:
        print(i)
    if i + 1 not in ids:
        print(i)
