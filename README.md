# bqresearcher_task_2
bqResearcher-Task 2: circuit for producing |00> and |11> with equal probabilities. Parameters are found using gradient descent. Circuit is modified for producing any of the 4 Bell states.

Run code as follows:
1. Open two terminals and run ```qvm -S``` and ```quilc -S``` in each of the terminals
2. Open another terminal and run main.py as ```python main.py```

main.py: (all qubits are initially at state |0>)
  1. Circuit for producing |00> and |11> with equal probabilties:
     - A parametric circuit is called that uses only native gates ( http://docs.rigetti.com/en/stable/apidocs/gates.html?highlight=native#native-gates-for-rigetti-qpus). 
     - A superposition of |0> and |1> on qubit-1 is produced as follows:
       - Apply RX gate on qubit-1 with angle pi/2
       - Apply RZ gate on qubit-1 with angle theta
       - Apply RX gate on qubit-1 with angle -pi/2
     - qubit-0 is changed to |1> state by applying RX and RZ gates on qubit-0 with angle pi
     - A superposition of |0> and |1> on qubit-0 is produced as follows:
       - Apply RX gate on qubit-0 with angle pi/2
       - Apply RZ gate on qubit-0 with angle theta
       - Apply RX gate on qubit-0 with angle -pi/2
     - The code uses an instance of a QuantumComputer which then compiles the parametric program to produce an executable that is scanned over for theta using gradient descent.
    
  2. Modification for producing any of the 4 Bell states:
     - An equal superposition of |0> and |1> on qubit-1 is produced as follws:
       - Apply RX gate on qubit-1 with angle pi/2
       - Apply RZ gate on qubit-1 with angle pi/2
       - Apply RX gate on qubit-1 with angle -pi/2
     - qubit-0 is changed to |1> state by applying RX and RZ gates on qubit-0 with angle pi
     - CNOT gate is implemented with qubit-1 as control and qubit-0 as target as follows:
          - Apply RX gate on qubit-0 with angle pi/2
          - Apply RZ gate on qubit-0 with angle pi/2
          - Apply RX gate on qubit-0 with angle -pi/2
          - Apply CZ gate with qubit-1 as control and qubit-0 as target
          - Apply RX gate on qubit-0 with angle pi/2
          - Apply RZ gate on qubit-0 with angle -pi/2
          - Apply RX gate on qubit-0 with angle -pi/2
    - Note: The above steps are illustrated for producing the Bell state (|01> - |10>)/sqrt(2). The code produces all of the 4 Bell states by changing thetas and rotating qubit-0 by pi to produce |1> as appropriate. 
    
bell_main.py: An attempt to find a Bell state using Gradient Descent.    
    
modules/ckt_tools.py:
  1. gen_ckt() : function that returns a program for producing |00> and |11> with equal probabilties.
  2. bell_ckt() : function that returns a program for producing any of the 4 Bell states
  3. init_qc_exec(ckt_program): function that returns an instance of a QuantumComputer and an executable after compiling ckt_program 
  4. bell_ckt_gd(): function that returns a program for producing any of the 4 Bell states using Gradient Descent
  
modules/gd_tools.py:
  1. cost_func(x) : a cost function that returns the value of a gradient at x
  2. find_optimal_theta(qc, executable): function that returns an optimal value of theta for the input executable using an intance of the QuantumComputer qc using gradient descent
  3. bell_cost_func(x): a cost function that returns the value of a gradient at x for finding Bell state
  4. bell_find_optimal_theta(qc, executable): function that returns an optimal value of theta for the input executable using an intance of the QuantumComputer qc using gradient descent for finding Bell State
