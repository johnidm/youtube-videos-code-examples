import ctypes
import os

# Load the shared library
libhello = ctypes.CDLL(os.path.abspath("libhello.so"))

# Call the hello_world function
libhello.hello_world()

# Define the argument and return types of the C function
libhello.add.argtypes = (ctypes.c_int, ctypes.c_int)  # Input arguments are two integers
libhello.add.restype = ctypes.c_int  # Return type is an

# Call the add function
result = libhello.add(5, 7)
print(f"The sum is: {result}")
