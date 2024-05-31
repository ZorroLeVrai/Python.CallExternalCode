#include <stdio.h>
#include <windows.h>

typedef void (*HelloFunc)();

void call_func()
{
  // Load the DLL
  HINSTANCE hinstLib = LoadLibrary(TEXT("mylib_cpp.dll"));
  if (hinstLib == NULL)
  {
    printf("Could not load the DLL. Error code: %lu\n", GetLastError());
    return;
  }

  // Get pointers to the functions
  HelloFunc hello_from_cpp = (HelloFunc)GetProcAddress(hinstLib, "hello_from_cpp");

  if (hello_from_cpp == NULL)
  {
    printf("Could not locate the function\n");
    FreeLibrary(hinstLib);
    return;
  }

  // Call the functions
  hello_from_cpp();

  // Free the DLL
  FreeLibrary(hinstLib);
}

int main()
{
  call_func();

  return 0;
}