#!/usr/bin/env python
from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def square(x):
    return x ** 2

value = square(rank)
sum_ = comm.reduce(value, op=MPI.SUM, root=0)

if rank == 0:
    sys.stdout.write(str(sum_) + "\n")
