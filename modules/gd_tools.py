import numpy as np


def cost_func(x):
    return 2*(x-0.5)


def find_optimal_theta(qc, executable):
    theta_0 = np.pi
    theta_1 = np.pi
    lr = 0.01
    precision = 1e-5
    prev_step_size = 1
    max_iters = 1000
    iters = 0
    print("Iterations for Gradient Descent-->\n")
    while prev_step_size > precision and iters < max_iters:
        prev_theta_0 = theta_0
        bitstrings = qc.run(
            executable, {'theta_0': [theta_0], 'theta_1': [theta_1]})
        y = bitstrings.sum()/100
        theta_0 = theta_0-lr*cost_func(y)
        prev_step_size = abs(theta_0-prev_theta_0)
        iters = iters+1
        if iters % 20 == 0:
            print("Iteration", iters, "\nY:", y, "\nTheta0:",
                  theta_0/np.pi, "pi") 

    return np.round(theta_0/np.pi, 3), iters
