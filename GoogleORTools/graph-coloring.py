from ortools.sat.python import cp_model
from SolutionPrinter import SolutionPrinter

def main(n, k, E):
	model = cp_model.CpModel()

	cVar = [model.NewIntVar(0, k-1, 'cVar_%i' % i) for i in range(n)]
	for p in E:
		model.Add(cVar[p[0]] != cVar[p[1]])
		
	solver = cp_model.CpSolver()
	solution_printer = SolutionPrinter(cVar)
	status = solver.SearchForAllSolutions(model, solution_printer)
	print()
	print('Solutions found : %i' % solution_printer.SolutionCount())

if __name__ == "__main__":
	numV = 4
	k = 4
	listE = [(0, 1), (1, 2), (2, 3), (3, 0), (1, 3), (0, 2)]
	main(numV, k, listE)