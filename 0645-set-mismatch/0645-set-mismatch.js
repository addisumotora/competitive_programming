/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    n = nums.length;
    actual_sum = n * (n + 1) / 2;
    dup_sum = 0;
    unique_sum = 0
    const s = new Set()

    for(const a of nums){
        dup_sum += a
    }

    for(const a of nums){
        s.add(a)
    }

    for(const a of s){
        unique_sum += a
    }
    dup = dup_sum - unique_sum
    missing = actual_sum - unique_sum

    return [dup, missing]    
};