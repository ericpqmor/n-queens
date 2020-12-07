import abc
import utils

class Solver(abc.ABC):

    def __init__(self, n_queens):
        self.n_queens = n_queens
        self.iterations = None
        self.solution_fitness = None
        self.solution = None

    def solve(self):
        pass

    def get_solution(self):
        return self.solution, utils.fitness(self.solution), self.iterations
