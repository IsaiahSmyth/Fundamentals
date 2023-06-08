const str5 = "what up, daddy-o?";
const expected5 = "dad";

const str6 = "uh, not much";
const expected6 = "u";

const str7 = "Yikes! my favorite racecar erupted!";
const expected7 = "e racecar e";

const str8 = "a1001x20002y5677765z";
const expected8 = "5677765";

const str9 = "a1001x20002y567765z";
const expected9 = "567765";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {
    let result = "";
    for (let i = 0; i < str.length; i++){
        for (let j = i; j < i.length; j++){
            result = i.split()
            console.log(result)
        }
    }
}
longestPalindromicSubstring(str6)
