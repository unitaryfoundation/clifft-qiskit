"""Qiskit provider/backend for the Clifft near-Clifford simulator."""

from importlib.metadata import PackageNotFoundError, version

from clifft_qiskit.backend import ClifftBackend, ClifftJob, ClifftProvider

__all__ = ["ClifftBackend", "ClifftJob", "ClifftProvider"]

try:
    __version__ = version("clifft-qiskit")
except PackageNotFoundError:
    __version__ = "0.0.0"
