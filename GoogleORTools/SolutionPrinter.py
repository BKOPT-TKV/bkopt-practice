from ortools.sat.python import cp_model

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
	"""Print intermediate solutions."""

	def __init__(self, variables):
		cp_model.CpSolverSolutionCallback.__init__(self)
		self.__variables = variables
		self.__solution_count = 0

	def OnSolutionCallback(self, custom_variables = None):
		if custom_variables == None:
			self.__solution_count += 1
			custom_variables = self.__variables
		if type(custom_variables) == list:
			for v in custom_variables:
				self.OnSolutionCallback(v)
			print()
		else:
			print('%s = %i' % (custom_variables, self.Value(custom_variables)), end = ' ')

	def SolutionCount(self):
		return self.__solution_count

	def GetValue(self, v):
		return self.Value(v)
