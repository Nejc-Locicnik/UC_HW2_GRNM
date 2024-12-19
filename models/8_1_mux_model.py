import numpy as np 

def solve_model(T,state):
    X1, X2, X3, X4, X5, X6, X7, X8, S1, S2, S3, MUX = state
    dX1 = -X1*0
    dX2 = -X2*0
    dX3 = -X3*0
    dX4 = -X4*0
    dX5 = -X5*0
    dX6 = -X6*0
    dX7 = -X7*0
    dX8 = -X8*0
    dS1 = -S1*0
    dS2 = -S2*0
    dS3 = -S3*0
    dMUX = -MUX*0.1+10*(((X1/5)**2))/(1+((X1/5)**2)+((S1/5)**3)+((S2/5)**3)+((S3/5)**3)+((X1/5)**2)*((S1/5)**3)+((X1/5)**2)*((S2/5)**3)+((X1/5)**2)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)+((S1/5)**3)*((S3/5)**3)+((S2/5)**3)*((S3/5)**3)+((X1/5)**2)*((S1/5)**3)*((S2/5)**3)+((X1/5)**2)*((S1/5)**3)*((S3/5)**3)+((X1/5)**2)*((S2/5)**3)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)*((S3/5)**3)+((X1/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))+10*(((X2/5)**2)*((S1/5)**3))/(1+((X2/5)**2)+((S1/5)**3)+((S2/5)**3)+((S3/5)**3)+((X2/5)**2)*((S1/5)**3)+((X2/5)**2)*((S2/5)**3)+((X2/5)**2)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)+((S1/5)**3)*((S3/5)**3)+((S2/5)**3)*((S3/5)**3)+((X2/5)**2)*((S1/5)**3)*((S2/5)**3)+((X2/5)**2)*((S1/5)**3)*((S3/5)**3)+((X2/5)**2)*((S2/5)**3)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)*((S3/5)**3)+((X2/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))+10*(((X3/5)**2)*((S2/5)**3))/(1+((X3/5)**2)+((S1/5)**3)+((S2/5)**3)+((S3/5)**3)+((X3/5)**2)*((S1/5)**3)+((X3/5)**2)*((S2/5)**3)+((X3/5)**2)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)+((S1/5)**3)*((S3/5)**3)+((S2/5)**3)*((S3/5)**3)+((X3/5)**2)*((S1/5)**3)*((S2/5)**3)+((X3/5)**2)*((S1/5)**3)*((S3/5)**3)+((X3/5)**2)*((S2/5)**3)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)*((S3/5)**3)+((X3/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))+10*(((X4/5)**2)*((S1/5)**3)*((S2/5)**3))/(1+((X4/5)**2)+((S1/5)**3)+((S2/5)**3)+((S3/5)**3)+((X4/5)**2)*((S1/5)**3)+((X4/5)**2)*((S2/5)**3)+((X4/5)**2)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)+((S1/5)**3)*((S3/5)**3)+((S2/5)**3)*((S3/5)**3)+((X4/5)**2)*((S1/5)**3)*((S2/5)**3)+((X4/5)**2)*((S1/5)**3)*((S3/5)**3)+((X4/5)**2)*((S2/5)**3)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)*((S3/5)**3)+((X4/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))+10*(((X5/5)**2)*((S3/5)**3))/(1+((X5/5)**2)+((S1/5)**3)+((S2/5)**3)+((S3/5)**3)+((X5/5)**2)*((S1/5)**3)+((X5/5)**2)*((S2/5)**3)+((X5/5)**2)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)+((S1/5)**3)*((S3/5)**3)+((S2/5)**3)*((S3/5)**3)+((X5/5)**2)*((S1/5)**3)*((S2/5)**3)+((X5/5)**2)*((S1/5)**3)*((S3/5)**3)+((X5/5)**2)*((S2/5)**3)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)*((S3/5)**3)+((X5/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))+10*(((X6/5)**2)*((S1/5)**3)*((S3/5)**3))/(1+((X6/5)**2)+((S1/5)**3)+((S2/5)**3)+((S3/5)**3)+((X6/5)**2)*((S1/5)**3)+((X6/5)**2)*((S2/5)**3)+((X6/5)**2)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)+((S1/5)**3)*((S3/5)**3)+((S2/5)**3)*((S3/5)**3)+((X6/5)**2)*((S1/5)**3)*((S2/5)**3)+((X6/5)**2)*((S1/5)**3)*((S3/5)**3)+((X6/5)**2)*((S2/5)**3)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)*((S3/5)**3)+((X6/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))+10*(((X7/5)**2)*((S2/5)**3)*((S3/5)**3))/(1+((X7/5)**2)+((S1/5)**3)+((S2/5)**3)+((S3/5)**3)+((X7/5)**2)*((S1/5)**3)+((X7/5)**2)*((S2/5)**3)+((X7/5)**2)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)+((S1/5)**3)*((S3/5)**3)+((S2/5)**3)*((S3/5)**3)+((X7/5)**2)*((S1/5)**3)*((S2/5)**3)+((X7/5)**2)*((S1/5)**3)*((S3/5)**3)+((X7/5)**2)*((S2/5)**3)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)*((S3/5)**3)+((X7/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))+10*(((X8/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))/(1+((X8/5)**2)+((S1/5)**3)+((S2/5)**3)+((S3/5)**3)+((X8/5)**2)*((S1/5)**3)+((X8/5)**2)*((S2/5)**3)+((X8/5)**2)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)+((S1/5)**3)*((S3/5)**3)+((S2/5)**3)*((S3/5)**3)+((X8/5)**2)*((S1/5)**3)*((S2/5)**3)+((X8/5)**2)*((S1/5)**3)*((S3/5)**3)+((X8/5)**2)*((S2/5)**3)*((S3/5)**3)+((S1/5)**3)*((S2/5)**3)*((S3/5)**3)+((X8/5)**2)*((S1/5)**3)*((S2/5)**3)*((S3/5)**3))
    return np.array([dX1, dX2, dX3, dX4, dX5, dX6, dX7, dX8, dS1, dS2, dS3, dMUX])

def solve_model_steady(state):
    return solve_model(0, state)
