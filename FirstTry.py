#Importing the 'Qiskit' Module
from qiskit import * 

from qiskit import IBMQ
#paste the api code in 'apostrophes' 
# you only need to save the account once. 
IBMQ.save_account('API_TOKENHERE') 
IBMQ.load_account()

#Creating a circuit
circuit = QuantumCircuit(2,2)

#to view use 'draw'
circuit.draw()
