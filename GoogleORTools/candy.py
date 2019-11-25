from ortools.sat.python import cp_model
from SolutionPrinter import SolutionPrinter

def main(num_candy, num_people, min_candy, max_candy):
	model = cp_model.CpModel()

	cVar = [model.NewIntVar(0, num_candy, 'cVar_%i' % i) for i in range(1, num_people + 1)]
	model.Add(sum(cVar) == num_candy)
	for i in range(num_people):
		model.Add(cVar[i] >= min_candy)
		model.Add(cVar[i] <= max_candy)

	solver = cp_model.CpSolver()
	solution_printer = SolutionPrinter(cVar)
	status = solver.SearchForAllSolutions(model, solution_printer)
	print()
	print('Solutions found : %i' % solution_printer.SolutionCount())

if __name__ == "__main__":
	num_candy = 10
	num_people = 3
	min_candy = 2
	max_candy = 5
	main(num_candy, num_people, min_candy, max_candy)