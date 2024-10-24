# modified from IBM Qiskit tutorial: https://github.com/Qiskit/qiskit
import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives.sampler import Sampler

# create a single qubit circuit 
# - Qubit is initially |0>
# Apply a Hadamard gate, 
# Followed by the T gate 
# and then a measurement

qc0 = QuantumCircuit(1)# A quantum circuit with a single qubit. Qubits are indexed starting from 0
qc0.h(0)          # apply hadamard on qubit # 0
qc0.p(np.pi/4,0)  # a T gate is a phase gate with phase pi/4: apply it to qubit 0
qc0.h(0)# apply a hadamard to qubit 0
# 2. Measure all the qubits in this case the single qubit
qc_measured = qc0.measure_all(inplace=False)

# 3. Execute the circuit using sampler.

sampler = Sampler()
job = sampler.run(qc_measured, shots=10000)# simulate the measurement circuit 10,000 times
result = job.result() # get the result from the simulations
print(f" > Probability distribution: Probability of |0> : {result.quasi_dists[0][0]} Probability of |1> : {result.quasi_dists[0][1]} ")
qc_measured.draw('mpl')