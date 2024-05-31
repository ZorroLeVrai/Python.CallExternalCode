import ctypes
from time import process_time

NB_TERM = 100_000_000

library_path = "../C_prgm/mylib.dll"
mylib = ctypes.CDLL(library_path)

mylib.sum_inverse.argtypes = [ctypes.c_long]
mylib.sum_inverse.restype = ctypes.c_double

def sum_inverse(nb: int) -> float:
    result: float = 0
    for val in range(1,nb+1):
        result += 1 / val
    return result

def sum_inv_from_c(nb: int) -> float:
    return mylib.sum_inverse(nb)

timing_before = process_time()
result_from_python = sum_inverse(NB_TERM)
timing_after = process_time()
python_exec_time = timing_after - timing_before

print(f"Python result: {result_from_python}")
print(f"Python time spent: {python_exec_time}")

timing_before = process_time()
result_from_c = sum_inv_from_c(NB_TERM)
timing_after = process_time()
c_exec_time = timing_after - timing_before

print(f"C result: {result_from_c}")
print(f"C time spent: {c_exec_time}")
print(f"Execution speed ratio: {python_exec_time / c_exec_time}")
