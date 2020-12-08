<h1 align="center">Day 5: Binary Boarding</h1>

## Part 1
### Breakdown:
- Plane uses binary space partitioning
	- L: Left
	- R: Right
	- F: Front
	- B: Back
- First 7 characters can only be F/B
	- Explains one of the 128 rows
	- F means take the lower half (0-63)
- Last 3 characters can only be R/L
	- Explains one of the 8 columns
	- L takes the lower half (0-3)
- You need to calculate the SeatID
- The SeatID is calculated by:
	- Row * 8 + Column = SeatID
- Look for the highest value SeatID

## Part 2
### Breakdown:
- All the seats are full except yours
- Find the SeatID of your seat
- The seats -1 & +1 from your ID are full and exist
