#!/usr/bin/env python
"""
Parallel Hello World
Requires mpi4py library (surprise)
"""

from mpi4py import MPI
import sys

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

def square(x):
    return x ** 2


sys.stdout.write(str(square(rank)) + "\n")
