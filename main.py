#! /usr/bin/env python3

from useful_package.module_a import polynom_3
from useful_package.module_b import hyperbola
import sys

x = int(sys.argv[1])
print(x)
print(polynom_3(x))
print(hyperbola(x))
