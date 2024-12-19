import numpy as np 

def solve_model(T,state):
    X1, S1, DEMUX1, DEMUX2 = state
    dX1 = -X1*0
    dS1 = -S1*0
    dDEMUX1 = -DEMUX1*0.1+10*(((X1/5)**2))/(1+((X1/5)**2)+((S1/5)**3)+((X1/5)**2)*((S1/5)**3))
    dDEMUX2 = -DEMUX2*0.1+10*(((X1/5)**2)*((S1/5)**3))/(1+((X1/5)**2)+((S1/5)**3)+((X1/5)**2)*((S1/5)**3))
    return np.array([dX1, dS1, dDEMUX1, dDEMUX2])

def solve_model_steady(state):
    return solve_model(0, state)
