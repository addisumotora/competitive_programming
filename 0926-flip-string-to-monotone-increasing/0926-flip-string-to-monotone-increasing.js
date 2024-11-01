/**
 * @param {string} s
 * @return {number}
 */
var minFlipsMonoIncr = function(s) {
    let res = 0
    let cntOne = 0
    
    for( const element of s ){
        if (element === '1'){
            cntOne++
        }else {
            res = Math.min(res + 1, cntOne)
        }
    }
    
    return res
};