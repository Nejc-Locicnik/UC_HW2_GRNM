import numpy as np


def solve_model(T, state):
    X1, X2, S0, MUX = state
    dX1 = -X1 * 0
    dX2 = -X2 * 0
    dS0 = -S0 * 0
    dMUX = (
        -MUX * 0.1
        + 10
        * (((X1 / 5) ** 2))
        / (1 + ((X1 / 5) ** 2) + ((S0 / 5) ** 3) + ((X1 / 5) ** 2) * ((S0 / 5) ** 3))
        + 10
        * (((X2 / 5) ** 2) * ((S0 / 5) ** 3))
        / (1 + ((X2 / 5) ** 2) + ((S0 / 5) ** 3) + ((X2 / 5) ** 2) * ((S0 / 5) ** 3))
    )
    return np.array([dX1, dX2, dS0, dMUX])


def solve_model_steady(state):
    return solve_model(0, state)
