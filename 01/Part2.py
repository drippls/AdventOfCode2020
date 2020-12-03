with open('in.txt') as f:
   nums = [int(i.strip()) for i in f.readlines()]

# This is a really crappy solution, never do this ever
# Like ever, please don't do this
for x in nums:
    for y in nums:
        for z in nums:
            if x + y + z == 2020:
                print(x * y * z)
