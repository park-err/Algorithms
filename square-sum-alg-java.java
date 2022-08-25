public class SquareSum {
  public static int squareSum(int[] n) { 
   // TODO: find the sum of the squares of each number in the array
    int squareSum = 0;
    for (int i = 0; i < n.length; i++) {
      squareSum += Math.pow(n[i], 2);
    }
    
    return squareSum;
  }
 }