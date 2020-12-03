<h1 align="center">Day 2: Password Philosophy</h1>

## Part 1
### Breakdown:
- Password Database is corrupted
- Left side is the rule
- Right side is the password
- The answer is how many passwords are still valid

#### Rule Format
Example Rule: [1-3 a]
The password must contain between 1 and 3 `a`, anything else is still valid

## Part 2
### Breakdown:
- The rules have changed a little bit

#### Rule Format
Example Rule: [1-3 a]
The password must contain an `a` in the 1st or 3rd position
Can't be both, can't be none either. Essentially XOR
The rules ignore computer indexing so everything needs to be minus 1
