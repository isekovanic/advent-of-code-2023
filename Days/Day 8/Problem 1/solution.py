import sys

sys.path.append('../../../Core')

from SolverCore import SolverCore

class Solver(SolverCore):
	def _solve(self, problem_input):
		instructions = list(problem_input[0].strip())

		desert_map = {}

		for line in problem_input[2:]:
			f, t = line.strip().split(' = ')
			left, right = t.split(', ')

			desert_map[f] = (left[1:], right[:-1])

		current = 'AAA'
		end = 'ZZZ'

		result = 0

		while True:
			instruction = instructions.pop(0)
			current = desert_map[current]['LR'.index(instruction)]

			result += 1
			instructions += [instruction]

			if current == 'ZZZ':
				break
		
		return result

solver = Solver()
solver.solve()