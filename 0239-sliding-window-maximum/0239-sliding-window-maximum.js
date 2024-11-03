/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    let result = [];
    let de = [];
    let l = 0;
    let r = 0;
    
    while (r < nums.length) {
        while (de.length && nums[de[de.length - 1]] < nums[r]){
            de.pop()
        }
        
        de.push(r)
        
        if(l > de[0]) {
            de.shift()
        }
        
        if((r + 1) >= k){
            result.push(nums[de[0]]);
            l++;
        }
        r++
    }
    
    return result
};