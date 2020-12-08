with open('in.txt') as f:
    group, data = '', []
    count = 0
    for line in f.readlines():
        if line.strip() != '':
            group += line.strip()
            count += 1
        else:
            group = ''.join(sorted(group))
            data.append((group, count))
            group = ''
            count = 0
    data.append((group, count))

# Main
final = 0
for group in data:
    counter = {}
    # Adding letters to counter dictionary
    for letter in group[0]:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1

    for l in counter:
        if counter[l] == group[1]:
            final += 1

print(final)
