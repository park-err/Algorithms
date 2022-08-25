#include <stddef.h>
#include <math.h>
int square_sum(const int *values, size_t count) {
  int result = 0;
  for(int i= 0;i< count;i++) {
    result += pow(*(values+i),2);
  }
  return result;
}