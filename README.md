# OpenSudokuSolver
 Solve sudoku using Python
## Usage
```python
import src.OpenSudokuSolver as oss
from pprint import pprint

solved, time = oss.solve(oss.create_board("collection/AI_Escargot.osud"))
print(f"Solved in {time} ms")
pprint(solved)
```
or
```python
import src.OpenSudokuSolver as oss
from pprint import pprint

board = [
    [1, None, None, None, None, 7, None, 9, None],
    [None, 3, None, None, 2, None, None, None, 8],
    [None, None, 9, 6, None, None, 5, None, None],
    [None, None, 5, 3, None, None, 9, None, None],
    [None, 1, None, None, 8, None, None, None, 2],
    [6, None, None, None, None, 4, None, None, None],
    [3, None, None, None, None, None, None, 1, None],
    [None, 4, None, None, None, None, None, None, 7],
    [None, None, 7, None, None, None, 3, None, None],
]
solved, time = oss.solve(board)
print(f"Solved in {time} ms")
pprint(solved)
```
## .OSUD files
 **O**pen **Sud**oku file. CSV format.  
 ```
 OSUD    Name           In code
 0 ..... Blank cell ... None
 1-9 ... Number ....... Int (1-9)
 , ..... Separator .... ,
 ```
 Example:
 ```
 0,8,7,0,1,5,9,0,0
 0,0,2,7,6,3,1,0,0
 5,0,0,9,0,0,0,4,0
 9,4,0,0,0,0,5,0,3
 0,7,5,0,0,0,6,9,0
 0,3,0,5,0,9,8,7,2
 0,0,0,1,0,0,0,6,9
 0,0,0,3,0,6,2,0,0
 0,6,0,0,8,4,7,3,0
 ```
 In code: 
 ```python
 [[None, 8, 7, None, 1, 5, 9, None, None],
  [None, None, 2, 7, 6, 3, 1, None, None],
  [5, None, None, 9, None, None, None, 4, None],
  [9, 4, None, None, None, None, 5, None, 3],
  [None, 7, 5, None, None, None, 6, 9, None],
  [None, 3, None, 5, None, 9, 8, 7, 2],
  [None, None, None, 1, None, None, None, 6, 9],
  [None, None, None, 3, None, 6, 2, None, None],
  [None, 6, None, None, 8, 4, 7, 3, None]]
 ```
 Solved:
 ```python
 [[3, 8, 7, 4, 1, 5, 9, 2, 6],
  [4, 9, 2, 7, 6, 3, 1, 5, 8],
  [5, 1, 6, 9, 2, 8, 3, 4, 7],
  [9, 4, 8, 6, 7, 2, 5, 1, 3],
  [2, 7, 5, 8, 3, 1, 6, 9, 4],
  [6, 3, 1, 5, 4, 9, 8, 7, 2],
  [8, 2, 3, 1, 5, 7, 4, 6, 9],
  [7, 5, 4, 3, 9, 6, 2, 8, 1],
  [1, 6, 9, 2, 8, 4, 7, 3, 5]]
 ```