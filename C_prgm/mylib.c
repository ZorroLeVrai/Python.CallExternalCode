#include <stdio.h>
#include <time.h>

void hello_from_c()
{
  printf("Hello from C!\n");
}

int add(int a, int b)
{
  return a + b;
}

double sum_inverse(long nb)
{
  double result = 0;
  for (long i = 1; i <= nb; ++i)
  {
    result += 1.0 / i;
  }
  return result;
}

void exec_sum()
{
  clock_t begin = clock();
  double result = sum_inverse(100000000);
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

  printf("Result from C: %lf\n", result);
  printf("Time spent from C: %lf\n", time_spent);
}