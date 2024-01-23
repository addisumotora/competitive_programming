/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    counter = init;
    
    nums.forEach((num) => counter = fn(counter, num))
    
    return counter
};