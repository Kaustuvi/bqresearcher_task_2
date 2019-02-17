import numpy as np

# a cost function that returns the value of a gradient at x


def cost_func(x):
    return 2*(x-0.5)

# function that returns an optimal value of theta
# for the input executable using an intance of the QuantumComputer qc using gradient descent


def find_optimal_theta(qc, executable):
    theta_0 = np.pi
    theta_1 = np.pi
    rx_theta = np.pi/2
    lr = 0.01
    precision = 1e-5
    prev_step_size = 1
    max_iters = 1000
    iters = 0
    print("Iterations for Gradient Descent-->\n")
    while prev_step_size > precision and iters < max_iters:
        prev_theta_0 = theta_0
        bitstrings = qc.run(
            executable, {'theta_0': [theta_0], 'theta_1': [theta_1], 'rx_theta': [rx_theta]})
        y = bitstrings.sum()/100
        theta_0 = theta_0-lr*cost_func(y)
        prev_step_size = abs(theta_0-prev_theta_0)
        iters = iters+1
        if iters % 20 == 0:
            print("Iteration", iters, "\nY:", y, "\nTheta0:",
                  theta_0/np.pi, "pi")

    return np.round(theta_0/np.pi, 3), iters
