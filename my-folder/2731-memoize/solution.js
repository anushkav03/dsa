/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    // sum = new Map([])
    // fac = new Map([])
    
    return function(...args) {
        if (cache.has(JSON.stringify(args)) === false) {
            cache.set(JSON.stringify(args), fn(...args));
        }
        return cache.get(JSON.stringify(args));
    }  
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
