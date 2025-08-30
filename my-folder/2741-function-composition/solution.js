/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        if (functions.length == 0) {return x;}

        curr = x;
        // iterate backwards; compose functions right to left
        for (let i = functions.length - 1; i >= 0; i--) { 
            f = functions[i]
            curr = f(curr);
        }
        return curr;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
