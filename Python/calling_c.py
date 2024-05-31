import ctypes
import os

library_path = "C_prgm/mylib.dll"

# Load the shared library into ctypes
if os.name == 'nt':
    mylib = ctypes.CDLL(library_path)
else:
    mylib = ctypes.CDLL(library_path)

# Call the hello_from_c function
mylib.hello_from_c()

# Call the add function
mylib.add.argtypes = (ctypes.c_int, ctypes.c_int)  # Specify argument types
mylib.add.restype = ctypes.c_int  # Specify the return type
result = mylib.add(5, 3)
print(f"5 + 3 = {result}")
