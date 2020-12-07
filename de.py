import solver
import utils
import random

class DE_Solver(solver.Solver):

    def __init__(self, n_queens):
        solver.Solver.__init__(self, n_queens)

        self.scale = 0.6
        self.genome_number = 50
        self.crossover = 0.5
        self.max_iterations = 1000

        self.solution = n_queens * [0]
        self.genomes = [ utils.random_genome(n_queens) for _ in range(self.genome_number) ]
        self.iterations = 0

    def solve(self):

        for _ in range(self.max_iterations):
            self.iterations = self.iterations + 1

            for gi in range(len(self.genomes)):
                gen = self.genomes[gi]
                g1, g2, g3 = self.genomes[random.randint(0, self.genome_number-1)], self.genomes[random.randint(0, self.genome_number-1)], self.genomes[random.randint(0, self.genome_number-1)]

                donor = self.generate_donor(g1, g2, g3)
                trial = self.generate_trial(gen, donor)

                if utils.fitness(gen) < utils.fitness(trial):
                    self.genomes[gi] = trial

                    if utils.fitness(self.solution) < utils.fitness(trial):
                        self.solution = trial

    def bound_value(self, value):
        if value > 8:
            value = 8

        if value < 0:
            value = 0

        return value

    def generate_donor(self, g1, g2, g3):
        donor = []
        g_l = len(g1)

        for i in range(g_l):
            nv = g1[i] + self.scale * (g2[i] - g3[i])
            nv = int(nv + 0.5)
            nv = self.bound_value(nv)
            donor.append(nv)

        return donor

    def generate_trial(self, g, donor):
        trial = []

        for i in range(len(g)):
            if random.uniform(0,1) < self.crossover:
                trial.append(donor[i])
            else:
                trial.append(g[i])

        return trial
