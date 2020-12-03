# Input
with open('in.txt') as f:
   data = [i.strip().split(': ') for i in f.readlines()]

final = 0
for i in data:
    nums, letter = i[0][:-2].split('-'), i[0][-1]
    password = i[1]
    # Easiest way is to just pass the two letters through XOR logic
    a, b = password[int(nums[0]) - 1] == letter, password[int(nums[1]) - 1] == letter
    if (a and not b) or (not a and b):
        final += 1
print(final)

