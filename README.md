# bqresearcher_task_2
bqResearcher-Task 2: circuit for producing |00> and |11> with equal probabilities. Parameters are found using gradient descent. Circuit is modified for producing any of the 4 Bell states.

Run code as follows:
1. Open two terminals and run ```qvm -S``` and ```quilc -S``` in each of the terminals
2. Open another terminal and run main.py as ```python main.py```

main.py: (all qubits are initially at state |0>)
  1. Circuit for producing |00> and |11> with equal probabilties:
     - A parametric circuit is called that uses only native gates ( http://docs.rigetti.com/en/stable/apidocs/gates.html?highlight=native#native-gates-for-rigetti-qpus). 
     - A superposition of |0> and |1> is produced by applying RY gate on qubit-1 with angle theta
     - RY gate is applied on qubit-0 with angle pi to produce |1>
     - RY gate is applied on qubit-0 with angle theta (same angle as step (ii))
     - The code uses an instance of a QuantumComputer which then compiles the parametric program to produce an executable that is scanned over for theta using gradient descent.
    
  2. Modification for producing any of the 4 Bell states:
     - An equal superposition of |0> and |1> is produced by applying RY gate on qubit-1 with angle theta = pi/2 
     - RY gate is applied on qubit-0 with angle pi to produce |1>
     - CNOT gate is implemented with qubit-1 as control and qubit-0 as target as follows:
          - Apply RY gate on qubit-0 with angle theta = pi/2
          - Apply CZ gate with qubit-1 as control and qubit-0 as target
          - Apply RY gate in qubit-0 with angle theta = -pi/2
    - Note: The above steps are illustrated for producing the Bell state (|01> + |10>)/sqrt(2). The code produces all of the 4 Bell states by changing thetas and rotating qubit-0 by pi to produce |1> as appropriate. 
    
    
modules/ckt_tools.py:
  1. gen_ckt() : function that returns a program for producing |00> and |11> with equal probabilties.
  2. bell_ckt() : function that returns a program for producing any of the 4 Bell states
  3. init_qc_exec(ckt_program): function that returns an instance of a QuantumComputer and an executable after compiling ckt_program 
  
modules/gd_tools.py:
  1. cost_func(x) : a cost function that returns the value of a gradient at x
  2. find_optimal_theta(qc, executable): function that returns an optimal value of theta for the input executable using an intance of the QuantumComputer qc using gradient descent
