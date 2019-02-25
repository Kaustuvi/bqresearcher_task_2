import numpy as np

# a cost function that returns the value of a gradient at x


def cost_func(x):
    return 2*(x-0.5)


def bell_cost_func(x):
    return (x-5)

# function that returns an optimal value of theta
# for the input executable using an intance of the QuantumComputer qc using gradient descent


def find_optimal_theta(qc, executable):
    theta_0 = np.pi
    theta_1 = 2*np.pi
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

# function that returns an optimal value of theta
# for the input executable using an intance of the QuantumComputer qc using gradient descent for finding Bell State


def bell_find_optimal_theta(qc, executable):
    theta_0 = 0  # pi
    theta_1 = 0  # pi
    x_theta = np.pi/2
    lr = 0.05
    precision = 1e-5
    prev_step_size = 1
    max_iters = 1000
    iters = 0
    print("Iterations for Gradient Descent-->\n")
    while iters < max_iters and prev_step_size > precision:
        prev_theta_1 = theta_1
        # bckt_program = ct.bell_ckt_gd(theta_0, theta_1, x_theta)
        bitstrings = qc.run(
            executable, {'theta_0': [theta_0], 'theta_1': [theta_1], 'x_theta': [x_theta]})
        y = bitstrings.sum()/100
        # y = wf.wavefunction(bckt_program).probabilities()
        theta_1 = theta_1-lr*bell_cost_func(y)
        prev_step_size = abs(theta_1-prev_theta_1)
        iters = iters+1
        if iters % 20 == 0:
            print("Iteration", iters, "\nY:", y, "\nTheta1:",
                  theta_1/np.pi, "pi")

    return np.round(theta_1/np.pi, 1), iters
