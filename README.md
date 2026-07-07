# clifft-qiskit

A [Qiskit](https://www.ibm.com/quantum/qiskit) `BackendV2` provider for the
[Clifft](https://github.com/unitaryfoundation/clifft) near-Clifford simulator.
Run Qiskit circuits on Clifft without hand-writing Stim.

See Clifft's [front-end integrations guide](https://unitaryfoundation.github.io/clifft/getting-started/integrations/)
for how this adapter fits with other Clifft front ends.

## Install
```bash
pip install clifft-qiskit
```

## Quickstart
```python
from qiskit import QuantumCircuit
from clifft_qiskit import ClifftProvider

qc = QuantumCircuit(2, 2)
qc.h(0); qc.cx(0, 1); qc.measure([0, 1], [0, 1])

backend = ClifftProvider().get_backend("clifft")
counts = backend.run(qc, shots=1000).result().get_counts()
print(counts)
```

## Supported basis
Clifford+T plus single-qubit rotations: `h s sdg x y z cx cy cz t tdg rx ry rz`
(+ `measure`). Higher-level gates (`ccx`, `u`, controlled rotations, …) are
decomposed into this basis by `qiskit.transpile` inside `run()`.

## Limitations
- Terminal measurement + counts only (no mid-circuit measurement / feedforward).
- `reset` and other non-unitary ops raise `QiskitError`.
- Single synchronous backend, all-to-all connectivity.

## License
Apache-2.0.
