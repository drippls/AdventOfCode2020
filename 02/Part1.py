# Input
with open('in.txt') as f:
   data = [i.strip().split(': ') for i in f.readlines()]

final = 0
for i in data:
    nums = i[0][:-2].split('-')
    count = 0
    for j in i[1]:
        if j == i[0][-1]:
            count += 1
    if count >= int(nums[0]) and count <= int(nums[1]):
        final += 1
print(final)
