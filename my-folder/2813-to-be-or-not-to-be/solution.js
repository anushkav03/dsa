/**
 * @param {string} val
 * @return {Object}
 */

//  JS has == for equal value and === for equal value and type
// 7=='7' would be true; 7==='7' would be false
var expect = function(val) {
    return {
        toBe : function(newval) {
            if (newval === val) {return true;}
            else {throw "Not Equal";}
        },

        notToBe : function(newval) {
            if (newval !== val) {return true;}
            else {throw "Equal";}
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
