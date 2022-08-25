using System.Linq;
public static class SquareSum
{
  public static int squareSum(int[] n) => n.Sum(i => i * i);
}