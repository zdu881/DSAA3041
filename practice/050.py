"""\
Problem: 50. Pow(x, n)
Source: https://leetcode.com/problems/powx-n/
Difficulty: Medium
Tags: Math, Recursion, Binary Exponentiation

Description:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Approach:
Binary exponentiation (fast power).
- If n < 0: compute (1/x)^(-n)
- Repeatedly square the base and multiply into result when the current bit of n is 1.

Time Complexity: O(log |n|)
Space Complexity: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        # Handle negative exponent by inverting the base.
        if n < 0:
            x = 1.0 / x
            n = -n

        result = 1.0
        base = x
        exp = n

        while exp > 0:
            if exp & 1:
                result *= base
            base *= base
            exp >>= 1

        return result


def main() -> None:
    sol = Solution()

    # Basic checks (match examples)
    print(sol.myPow(2.0, 10))   # 1024.0
    print(sol.myPow(2.1, 3))    # 9.261...
    print(sol.myPow(2.0, -2))   # 0.25


if __name__ == "__main__":
    main()
