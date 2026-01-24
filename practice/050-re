class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n == 0):
            return 1.0
        elif (n<0):
            return 1.0 / self.myPow(x, -n)
        else:
            result = 1.0
            base = x
            exp = n
            while (exp > 0):
                if (exp & 1):
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
