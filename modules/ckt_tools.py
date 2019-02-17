from pyquil import Program, get_qc
from pyquil.gates import RX, RZ, RY, CZ, MEASURE
import numpy as np  # remove

# function that returns a program for producing |00> and |11> with equal probabilties.


def init_qc_exec(ckt_program):
    qc = get_qc("9q-square-qvm", as_qvm=True, noisy=False)
    executable = qc.compile(ckt_program)
    return qc, executable

# function that returns a program for producing any of the 4 Bell states


def gen_ckt():
    ckt = Program()
    theta_0_ref = ckt.declare('theta_0', memory_type='REAL')
    theta_1_ref = ckt.declare("theta_1", memory_type='REAL')
    rx_theta_ref = ckt.declare("rx_theta", memory_type='REAL')
    ro = ckt.declare('ro', memory_type='BIT', memory_size=2)
    ckt += RX(rx_theta_ref, 1)
    ckt += RZ(theta_0_ref, 1)
    ckt += RX(-1*rx_theta_ref, 1)

    ckt += RX(rx_theta_ref, 0)
    ckt += RZ(theta_1_ref, 0)
    ckt += RZ(theta_0_ref, 0)
    ckt += RX(-1*rx_theta_ref, 0)
    
    ckt += MEASURE(1, ro[0])
    ckt.wrap_in_numshots_loop(1000)
    return ckt


def bell_ckt(rz_theta, theta_0, theta_1, theta_2):
    ckt = Program()
    ckt += RZ(-1*rz_theta, 1),
    ckt += RX(theta_0, 1),
    ckt += RZ(rz_theta, 1),

    ckt += RZ(theta_1, 0),
    ckt += RX(theta_1, 0),

    ckt += RZ(-1*rz_theta, 0),
    ckt += RX(theta_2, 0),
    ckt += RZ(rz_theta, 0),

    ckt += CZ(1, 0),

    ckt += RZ(-1*rz_theta, 0),
    ckt += RX(-1*theta_2, 0),
    ckt += RZ(rz_theta, 0),
    return ckt
