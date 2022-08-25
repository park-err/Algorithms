function square_sum(array $numbers) : int {
  $sum = 0;
  foreach($numbers as $number) {
    $sum += $number * $number;
  }
  
  return $sum;
}