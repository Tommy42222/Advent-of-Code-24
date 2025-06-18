## Numbers of possiable directions to check:
- up-left
- up
- up-right
- down-left
- down
- down-right

**TOTAL == 6**

## For the first 4 rows, only check:
- down-left
- down
- down-right

## For the last 4 rows, only check:
- up-left
- up
- up-right

## If the x is at **X**_coordinate_2 or lower, only check:
- up
- up right
- down
- down right

## If the x is at **X**_coordinate_135 or higher, only check:
- up
- up left
- down
- down left
---
## ELSE, check all directions

### if cheking right ->, look for "M,A,S"

### if cheking left <-, look for "S,A,M"
---
### if checking up /\\, look for {from X going up}:
- S
- A
- M
---
### if checking down \\/, look for: {from X going down}
- M
- A
- S

---

## Function Inputs
- row/x-coord
- position/y-coord
- data4.txt as newFile
