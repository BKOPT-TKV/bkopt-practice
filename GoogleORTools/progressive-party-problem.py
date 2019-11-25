from ortools.sat.python import cp_model
from SolutionPrinter import SolutionPrinter

def eq_scalar(a, x):
	return a == 0

def eq(a, b):
	return a == b

def count_eq(cVar, i, j, B):
	count = 0
	for b in range(B):
		if (eq_scalar(cVar[i][b], 0) and (eq(cVar[i][b], cVar[j][b]))):
			count += 1
	return count

def count_people(cVar, b, p, S, G):
	count = 0
	for i in range(G):
		if (eq_scalar(cVar[i][b], p)):
			count += S[i]
	return count

def customAllDifferent(c):
	for i in range(len(c)):
		for j in range(i):
			if (not eq_scalar(c[i], 0)) and eq(c[i], c[j]):
				return False
	return True

def main(G, P, B, S, C):
	model = cp_model.CpModel()
	
	cVar = []
	for g in range(G):
		cVar.append([])
		for b in range(B):
			cVar[g].append(model.NewIntVar(0, P, 'cVar_%i_%i' % (g, b)))
			for ib in range(b):
				model.Add((cVar[g][b] != cVar[g][ib]) or (cVar[g][b] == 0))
		model.Add(sum(cVar[g]) > 0)
		model.Add(customAllDifferent(cVar[g]) == True)
	# for i in range(G):
	# 	for j in range(i):
	# 		model.Add(count_eq(cVar, i, j, B) <= 1)
	for b in range(B):
		for p in range(P):
			model.Add(count_people(cVar, b, p, S, G) <= C[b])

	solver = cp_model.CpSolver()
	solution_printer = SolutionPrinter(cVar)
	status = solver.SearchForAllSolutions(model, solution_printer)
	print()
	print('Solutions found : %i' % solution_printer.SolutionCount())

if __name__ == "__main__":
	G = 2
	P = 2
	B = 2
	S = [1, 1, 1, 1, 1]
	C = [2, 2, 2, 2, 2]
	main(G, P, B, S, C)