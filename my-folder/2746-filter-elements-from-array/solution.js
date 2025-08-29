/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    newarr = [];
    for (let i = 0; i < arr.length; i++) {
        if (Boolean(fn(arr[i], i)) == true) {
            newarr.push(arr[i]);
        }
    }
    return newarr;
};
