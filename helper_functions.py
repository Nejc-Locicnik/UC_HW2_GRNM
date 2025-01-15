import itertools
import pygad
import numpy as np
import matplotlib.pyplot as plt
from grenmlin import simulator, grn


def get_input_signals(n=3, amp=100):
    return [sig[::-1] for sig in itertools.product([0, amp], repeat=n)]


def visualize(T, Y, grn=None, names=None):
    fig, ax = plt.subplots(len(Y[0]), 1, figsize=(10, 5))
    for i in range(len(ax)):
        ax[i].plot(T, Y[:, i])
        if grn:
            ax[i].set_ylabel(grn.species_names[i])
        elif names:
            ax[i].set_ylabel(names[i])
        else:
            ax[i].set_ylabel(f"X{i+1}")
    ax[-1].set_xlabel("time [a.u.]")
    fig.show()


def test_inputs(inputs, x=250):
    T = np.arange(2 ** len(inputs[0]) * x)

    Y = []
    for sig in inputs:
        for i in range(x):
            Y.append(sig)

    Y = np.array(Y)
    visualize(T, Y)


def fitness_func_2_1(ga_instance, solution, solution_idx):
    my_grn = grn.grn()
    # input species
    my_grn.add_input_species("X1")
    my_grn.add_input_species("X2")
    my_grn.add_input_species("S0")
    # other species
    my_grn.add_species("MUX", 0.1)
    # X1 AND NOT S0
    regulators = [
        {"name": "X1", "type": 1, "Kd": solution[0], "n": solution[1]},
        {"name": "S0", "type": -1, "Kd": solution[2], "n": solution[3]},
    ]
    products = [{"name": "MUX"}]
    # adding a gene to the network - the first parameter specifies the rate of gene expression
    my_grn.add_gene(10, regulators, products)
    # X2 AND S0
    regulators = [
        {"name": "X2", "type": 1, "Kd": solution[4], "n": solution[5]},
        {"name": "S0", "type": 1, "Kd": solution[6], "n": solution[7]},
    ]
    products = [{"name": "MUX"}]
    # adding a gene to the network - the first parameter specifies the rate of gene expression
    my_grn.add_gene(10, regulators, products)
    inputs = get_input_signals(3, 100)
    T, Y = simulator.simulate_sequence(
        my_grn, inputs, t_single=250, plot_on=False, model="models/2_1_mux_model"
    )

    target = (map_to_bool(Y[:, 0]) and map_to_bool(Y[:, 2], True)) or (
        map_to_bool(Y[:, 1]) and map_to_bool(Y[:, 2])
    )
    output = np.sum(Y[:, -1] - target)
    fitness = 1 / (np.abs(output) + 1e-6)
    return fitness


def map_to_bool(arr, negate=False):
    if negate:
        return [not bool(x) for x in arr]
    return [bool(x) for x in arr]


def run_genetic_optim():
    ga_instance = pygad.GA(
        num_generations=10,
        sol_per_pop=10,
        num_parents_mating=5,
        num_genes=8,
        fitness_func=fitness_func_2_1,
        gene_type=float,
        init_range_low=2,
        init_range_high=5,
    )

    ga_instance.run()

    solution, solution_fitness, _ = ga_instance.best_solution(
        ga_instance.last_generation_fitness
    )
    print(f"Parameters of the best solution: {solution}")
    print(f"Fitness value of the best solution = {solution_fitness}")
