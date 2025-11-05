'''
- if a function is run through pdb.runcall(), then when an exception occurs, using pdb.pm() afterwards can indeed provide richer debugging context — because the function was already being executed under debugger supervision.
- Instead of calling a function directly you could call it by passing to runcall runcall starts debugging from the starting phase
- And with it additionaly you could use pdb.pm() in the exception handling to provide you bettter assisstance for debugging  
'''

import random
import pdb

def risky_division(a, b):
    """Function that may randomly raise an exception."""
    if b == 0:
        raise ValueError("Division by zero detected!")
    return a / b


def run_many_divisions():
    """Simulate multiple random divisions."""
    for i in range(5):
        a = random.randint(1, 10)
        b = random.choice([0, 0, 0, 0, 1, 2, 3])  # sometimes 0 — causes crash
        print(f"\nAttempt {i+1}: dividing {a} by {b}")
        result = pdb.runcall(risky_division, a, b)  # runs under debugger
        print("Result:", result)


try:
    run_many_divisions()
except Exception:
    print("\n💥 Oops! An error occurred — entering post-mortem mode:")
    pdb.pm()  # opens debugger *at the exact crash point*
