from ortools.sat.python import cp_model
from SolutionPrinter import SolutionPrinter

# a[0] == a[1] return a bounded linear expression, not a boolean value
def myConstraint(a):
	# if (a[0] == a[1]):
	# 	return True
	# return False
	return a[0] == a[1]

def main(p, l):
	model = cp_model.CpModel()

	x = model.NewIntVar(0, p, 'x')
	y = model.NewIntVar(0, p, 'y')
	model.Add(x * y <= l)

	solver = cp_model.CpSolver()
	solution_printer = SolutionPrinter([x, y])
	status = solver.SearchForAllSolutions(model, solution_printer)
	print()
	print('Solutions found : %i' % solution_printer.SolutionCount())

if __name__ == "__main__":
	p = 5
	l = 13
	main(p, l)