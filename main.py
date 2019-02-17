import modules.gd_tools as gd
import modules.ckt_tools as ct
from pyquil.api import WavefunctionSimulator
import numpy as np

# gradient descent to find parameters for ckt producing |00> and |11> with equal probabilities
ckt_program = ct.gen_ckt()
print("Program -->", ckt_program)

qc, executable = ct.init_qc_exec(ckt_program)
print("Executable Program -->", executable.program)

optimal_theta, iters = gd.find_optimal_theta(qc, executable)
print("The optimal value of theta:", optimal_theta, "pi")
print("Number of iterations:", iters)

# modification for bell ckt
print("\nModification for Bell State--->")
iter = 1
rz_theta = np.pi/2
wf = WavefunctionSimulator()
while iter <= 4:
    theta_0 = (2*np.ceil(iter/2)-1)*np.pi/2
    theta_1 = (np.ceil(iter/2)-1)*np.pi
    theta_2 = (2*iter-1)*np.pi/2
    bckt_program = ct.bell_ckt(rz_theta, theta_0, theta_1, theta_2)
    bell_state = wf.wavefunction(bckt_program)
    print("Bell State", iter, ":", bell_state)
    iter = iter+1
