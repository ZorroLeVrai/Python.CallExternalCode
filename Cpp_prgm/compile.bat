#compile the CPP code
g++ -shared -fPIC -c mycode.cpp -o mylib_cpp.dll

#compile the C code
gcc -shared -fPIC -c load_cpp.c -o mylib_c.dll