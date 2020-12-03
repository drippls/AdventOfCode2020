with open('in.txt') as f:
    land = [i.strip() for i in f.readlines()]

def solve(dItem, dRow):
    row, item = 0, 0
    final = 0
    for i in range(len(land)):
        position = land[row][item]
        if item + dItem >= len(land[row]):
            item = (item + dItem) - len(land[row])
        else:
            item += dItem
        if row + dRow > len(land):
            break
        row += dRow
        if position == '#':
            final += 1
    return final

slopes = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]
answer = 1
for i in slopes:
    answer *= solve(i[0], i[1])
print(answer)
