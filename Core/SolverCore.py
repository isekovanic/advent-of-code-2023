from time import gmtime, strftime, time
from abc import ABC, abstractmethod 

input_types = {
	'test': 'input_test.txt',
	'real': 'input.txt'
}

class SolverCore(ABC):
	@abstractmethod
	def _solve(self, input):
		pass

	def solve(self):
		print('CUSTOM TEST CASE: \n')
		print('=============================')
		self.solve_for_type('test')
		print('=============================\n')

		print('ACTUAL TEST CASE: \n')
		print('=============================')
		self.solve_for_type('real')
		print('=============================')

	def solve_for_type(self, input_type):
		input_file = input_types[input_type]

		problem_input = self.read_input(input_file)

		start = time()

		solution = str(self._solve(problem_input))

		print('The solution is: {}'.format(solution))

		if input_type == 'test':
			read_expected = open('input_test_expected.txt')
			expected = read_expected.readline()

			if solution == expected:
				print('The solution to the test case is correct !')
			else:
				print('The solution to the test case is WRONG. \n Expected: {} \n Received: {}'.format(expected, solution))

		end = time()

		took = end - start

		print('The program execution time was: {}'.format('{}.{}'.format(strftime('%H:%M:%S', gmtime(end - start)), int(took * 1000) % 1000)))

		return solution

	def read_input(self, file):
		read_input = open(file, 'r')
		input_list = []

		for line in read_input:
			input_list += [line]

		return input_list
