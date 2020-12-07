from pso import PSO_Solver
from de import DE_Solver
from utils import fitness

N = [4, 5, 6, 7, 8]

for n in N:
    algorithm = PSO_Solver(n)
    algorithm.solve()
    pso_solution = algorithm.get_solution()

    print("Solving for " + str(n) + " queens")
    print("### Particle Swarm Optimization (PSO) Solution ###")
    print(pso_solution)
    print("##################################################")

    algorithm = DE_Solver(n)
    algorithm.solve()
    de_solution = algorithm.get_solution()

    print("###### Differential Evolution (DE) Solution ######")
    print(de_solution)
    print("##################################################\n\n\n")
