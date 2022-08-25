fn square_sum(vec: Vec<i32>) -> i32 {
    let mut squared_sum: i32 = 0;
    for num in vec {
        squared_sum += num*num;
    }
    squared_sum
}