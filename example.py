import src.OpenSudokuSolver as oss
from pprint import pprint

solved, time = oss.solve(oss.create_board("collection/AI_Escargot.osud"))
print(f"Solved in {time} ms")
pprint(solved)
