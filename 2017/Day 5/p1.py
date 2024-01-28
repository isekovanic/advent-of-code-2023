import sys

sys.path.append('../../')

from Core import SolverCore

class Solver(SolverCore):
    def _solve(self, problem_input):
        jumps = [int(line.strip()) for line in problem_input]
        result = 0
        
        i = 0
        while 0 <= i < len(jumps):
            jump = jumps[i]
            jumps[i] += 1
            i += jump
            result += 1
            
        return result


solver = Solver(5)
solver.solve()