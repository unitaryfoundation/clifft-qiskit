# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-06-22

This is the first public release of `clifft-qiskit`, a Qiskit `BackendV2`
provider for the Clifft near-Clifford simulator. It runs Qiskit
`QuantumCircuit` instances on Clifft without hand-writing Stim, exposing
`ClifftProvider`, `ClifftBackend`, and `ClifftJob`.

The backend supports a Clifford+T basis plus single-qubit rotations
(`h s sdg x y z cx cy cz t tdg rx ry rz` and `measure`); higher-level gates
are decomposed into this basis via `qiskit.transpile` inside `run()`.
Unsupported semantics such as mid-circuit measurement, feedforward, `reset`,
and other non-unitary operations are rejected explicitly.

### Features

- scaffold Qiskit-to-Clifft backend, provider, and job APIs by @ashmitjsg
- add package release process, changelog tooling, and TestPyPI/PyPI publishing workflow by @ashmitjsg

### Testing

- add provider equivalence coverage against Qiskit Aer by @ashmitjsg
- add installed-wheel package checks to CI and release builds by @ashmitjsg
