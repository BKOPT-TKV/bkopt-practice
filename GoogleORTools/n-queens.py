from ortools.sat.python import cp_model
from SolutionPrinter import SolutionPrinter

def main(board_size):
	model = cp_model.CpModel()

	cVar = [model.NewIntVar(0, board_size - 1, 'cVar_%i' % i) for i in range(board_size)]
	model.AddAllDifferent(cVar)
	for i in range(board_size):
		diag1 = []
		diag2 = []
		for j in range(board_size):
			q1 = model.NewIntVar(0, 2 * board_size, 'diag1_%i' % i)
			diag1.append(q1)
			model.Add(q1 == cVar[j] + j)
			q2 = model.NewIntVar(-board_size, board_size, 'diag2_%i' % i)
			diag2.append(q2)
			model.Add(q2 == cVar[j] - j)
		model.AddAllDifferent(diag1)
		model.AddAllDifferent(diag2)

	solver = cp_model.CpSolver()
	solution_printer = SolutionPrinter(cVar)
	status = solver.SearchForAllSolutions(model, solution_printer)
	print()
	print('Solutions found : %i' % solution_printer.SolutionCount())

if __name__ == "__main__":
	board_size = 6
	main(board_size)