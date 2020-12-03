<h1 align="center">Day 3: Toboggan Trajectory</h1>

## Part 1
### Breakdown:
- You're given a 2 dimensional array to traverse
- You can only traverse like a knight, right down (¬)
	- 3 across and 1 down
- If you encounter a `#` that add that to the total
- The array infinitely loops to the right
	- Get around this by just "pacmaning" the grid

## Part 2
### Breakdown:
- You now need to check a number of different slopes
	- 1, 1
	- 3, 1 (Just did this one)
	- 5, 1
	- 7, 1
	- 1, 2
- Take all these answers and multiply for final solution
