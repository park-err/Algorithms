int summation(int num){
 // finds the sum of all numbers 1 to n
  int sum = num;
  for (int i = 1; i < num; i++) {
    sum += i;
  }
  return sum;
}