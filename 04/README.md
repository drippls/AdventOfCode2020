<h1 align="center">Day 4: Passport Processing</h1>

## Part 1
### Breakdown:
- It's beneficial hacking time!
- Passport data is separated by spaces and newlines
- Blank lines are used to separate passports
- There are 8 fields needed to make a passport valid
- The cid field is optional
- Count the number of valid passports
- I think the hardest part will be cleaning up the data

## Part 2
### Breakdown:
New Rules
- byr (Birth Year) - four digits; at least 1920 and at most 2002.
- iyr (Issue Year) - four digits; at least 2010 and at most 2020.
- eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
- hgt (Height) - a number followed by either cm or in:
	- If cm, the number must be at least 150 and at most 193.
	- If in, the number must be at least 59 and at most 76.
- hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
- ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
- pid (Passport ID) - a nine-digit number, including leading zeroes.

