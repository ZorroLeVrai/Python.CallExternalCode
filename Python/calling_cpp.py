import ctypes
import os

library_path = "../Cpp_prgm/mylib_c.dll"

full_path = os.path.abspath(library_path)
print(full_path)

# Load the shared library into ctypes
mylib = ctypes.CDLL(full_path)

# Call the hello_from_c function
mylib.call_func()
