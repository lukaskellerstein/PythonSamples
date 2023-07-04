

# Concurrency (multitasking)

Doing a lot of things at once. Ex. One secretary is responsible (doing) multiple things: Answering on mails, Receiving the phone calls, doing a report for management. Secretary can do a multiple things, but only ONE AT THE TIME. => I/O bound problem

> Solving problems: IO-bound problems
- HTTP calls
- File IO operations


## Pre-emptive concurrency (multitasking) = THREADING

Python threading - The operating system decides when to switch tasks external to Python.

Every new thread created will have a PID (process ID)

## Cooperative concurrency (multitasking) = COROUTINES + ASYNCIO

Asyncio - The tasks decide when to give up control.


# Pararellism  = MULTIPROCESSING

Doing a lot of things simultaneously (like — doing numerical computations). Ex. Five accountants are calculating yearly summary for five companies. => CPU bound problem 

> Solving problems: CPU-bound problems

Each `process` is starting their own Python interpreter -> consuming more resources than Concurrency
