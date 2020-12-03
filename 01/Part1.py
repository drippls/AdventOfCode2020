with open('in.txt') as f:
   nums = [int(i.strip()) for i in f.readlines()]

for i in nums:
    for j in nums:
        if i + j == 2020:
            print(i * j)
