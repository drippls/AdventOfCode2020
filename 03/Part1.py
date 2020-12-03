with open('in.txt') as f:
    land = [i.strip() for i in f.readlines()]

item = 0
dItem = 3
final = 0
for i in range(len(land)):
    position = land[i][item]
    if item + dItem >= len(land[i]):
        item = (item + dItem) - len(land[i])
    else:
        item += dItem
    if position == '#':
        final += 1
print(final)
