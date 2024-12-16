import itertools
import numpy as np
import matplotlib.pyplot as plt

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
    T = np.arange(2**len(inputs[0]) * x)

    Y = []
    for sig in inputs:
        for i in range(x):
            Y.append(sig)

    Y = np.array(Y)
    visualize(T, Y)