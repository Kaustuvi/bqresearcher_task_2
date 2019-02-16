from pyquil import Program, get_qc
from pyquil.gates import RX, RZ, RY, CZ, MEASURE


def init_qc_exec(ckt_program):
    qc = get_qc("9q-square-qvm", as_qvm=True, noisy=False)
    executable = qc.compile(ckt_program)
    return qc, executable


def gen_ckt():
    ckt = Program()
    theta_0_ref = ckt.declare('theta_0', memory_type='REAL')
    theta_1_ref = ckt.declare("theta_1", memory_type='REAL')
    ro = ckt.declare('ro', memory_type='BIT', memory_size=2)
    ckt += RY(theta_0_ref, 1)
    ckt += RY(theta_1_ref, 0)
    ckt += RY(theta_0_ref, 0)
    ckt += MEASURE(1, ro[0])
    ckt.wrap_in_numshots_loop(1000)
    return ckt


def bell_ckt(theta_0, theta_1, theta_2):
    ckt = Program()
    ckt += RY(theta_0, 1)
    ckt += RY(theta_1, 0)
    ckt += RY(theta_2, 0)
    ckt += CZ(1, 0),
    ckt += RY(-1*theta_2, 0)
    return ckt
