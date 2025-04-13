# Built-in Module Example
import math
print("Square root using math module:", math.sqrt(16))

# User-defined Module
import my_module
my_module.hello()

# Replacing 'requests' with another built-in module (no error)
import datetime
current_time = datetime.datetime.now()
print("Current date and time:", current_time)

# Math module examples
import math  # Basic Import
import math as m  # Import with alias
from math import pi, sqrt  # Specific imports
from math import *  # Import everything
