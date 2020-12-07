import solver
import utils
import itertools
import random

from discrete_dimension import Position, Velocity

class Particle:

    def __init__(self, num):
        self.num = num

        self.position = Position()
        self.position.values = utils.random_position(num)

        self.velocity = Velocity()
        self.velocity.values = utils.random_swap(num)

        self.best = (self.position, utils.fitness(self.position.values))

        self.alpha = 1.2
        self.beta = 2.3
        self.omega = 0.7

    def update(self, cbest):
        self.r1 = random.uniform(0,1)
        self.r2 = random.uniform(0,1)

        # print("cbest = ", cbest.values)
        # print("position = ", self.position.values)
        # print("Diff = ", cbest - self.position)

        inertiaFactor = self.omega*self.velocity
        cognitiveFactor = self.alpha*self.r1*(self.best[0] - self.position)
        socialFactor = self.beta*self.r2*(cbest - self.position)

        # print("Cognitive = ", cognitiveFactor)
        # print("Social = ", socialFactor)
        # print("Inercy = ", inertiaFactor)

        # print("Velocity = ", self.velocity, " and Position = ", self.position)
        self.velocity = inertiaFactor + cognitiveFactor + socialFactor
        # print("Updated velocity")
        # print("Velocity = ", self.velocity, " and Position = ", self.position)
        self.position = self.position + self.velocity

        # self.velocity = cognitive + social + inercy
        # print("Velocity = ", self.velocity, " and Position = ", self.position)
        # self.position = self.position + self.velocity

        # print("Velocity = ", self.velocity, " and Position = ", self.position)

        if utils.fitness(self.position.values) > self.best[1]:
            self.best = (self.position, utils.fitness(self.position.values))


class PSO_Solver(solver.Solver):

    def __init__(self, n_queens):
        solver.Solver.__init__(self, n_queens)

        self.n_queens = n_queens
        self.solution = None

        self.particle_number = 20
        self.swarm = [Particle(n_queens) for _ in range(self.particle_number)]

        self.iterations = 0
        self.solution_fitness = len(list(itertools.combinations(self.n_queens * [0], 2)))

    def solve(self):
        best_position = Position()
        best_position.values = self.swarm[0].position.values

        best = (best_position, self.swarm[0].best[1])
        best = self.update_best(best)

        i = 0
        self.iterations = 0

        while not self.convergence_criteria(best):
            self.iterations = self.iterations + 1
            i = i + 1

            for part in self.swarm:
                part.update(best[0])

            best = self.update_best(best)

        self.solution = best[0].values

    def update_best(self, best_value):
        best = best_value

        for part in self.swarm:
            if part.best[1] > best[1]:
                best = (part.best[0], part.best[1])

        return best

    def convergence_criteria(self, best):
        majority = self.particle_number
        count = 0

        for part in self.swarm:
            if part.best[1] == best[1]:
                count = count + 1

        return (best[1] == self.solution_fitness and count >= majority)
