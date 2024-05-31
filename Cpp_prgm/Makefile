mycode_output: mycode.o
	g++ -shared -fPIC mycode.o -o mycode.dll

call_cpp: calling_cpp_code.o
	gcc -shared -fPIC calling_cpp_code.o -o calling_cpp_code.dll

call_exe: calling_cpp_code.o
	gcc -fPIC calling_cpp_code.o -o calling_cpp_code.exe

mycode.o: mycode.cpp mycode.hpp
	g++ -c main.cpp

calling_cpp_code.o: calling_cpp_code.c
	gcc -c calling_cpp_code.c

clean:
	del *.o mycode.dll calling_cpp_code.dll