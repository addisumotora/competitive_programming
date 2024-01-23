/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  return nums.length === 0 ? init : nums.reduce((sum, num) => fn(sum, num), init);
};