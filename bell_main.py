import modules.gd_tools as gd
import modules.ckt_tools as ct
import numpy as np

# gradient descent to find Bell state

bckt_program = ct.bell_ckt_gd()
qc, executable = ct.init_qc_exec(bckt_program)
boptimal_theta, biters = gd.bell_find_optimal_theta(qc, executable)
print("The optimal value of theta:", boptimal_theta, "pi")
print("Number of iterations:", biters)
