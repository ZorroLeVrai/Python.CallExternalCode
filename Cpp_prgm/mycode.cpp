#include <iostream>
#include "mycode.hpp"

extern "C"
{
  void hello_from_cpp()
  {
    std::cout << "Hello from CPP!" << std::endl;
  }
}