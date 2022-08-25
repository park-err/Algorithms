function SquareSum([int] $n) {
	$squareSum = 0
	for($i = 0; $i -lt $n.length; $i++){ 
		$squareSum += ($n[$i] * $n[$i] 
	}
	
	return $squareSum
}