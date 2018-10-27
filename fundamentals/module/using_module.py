#!/usr/local/bin/python3
# The shebang above identifies which python executable should be used when running this file as an executable file
# E.g. ./using_module.py, instead of python3 ./using_module.py

# different style of importing modules
from fundamentals.module.my_functions import launch_missile
# the __name__ attribute of my_functions module is set to "my_functions" (unchanged)
import my_functions
# the __name__ attribute of math module is set to "m" (changed)
import math as m

print("launch_missile():", launch_missile())

print("even_or_odd(3):", my_functions.even_or_odd(3))
