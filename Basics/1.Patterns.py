class Solution:
    def pattern1(self, N):
        for i in range(N):
            for j in range(N):
                print("*", end=" ")
            print()

    def pattern2(self, N):
        for i in range(N):
            for j in range(i+1):
                print("*", end=" ")
            print()

    def pattern3(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j, end=" ")
            print()

    def pattern4(self, N):
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(i, end=" ")
            print()

    def pattern5(self, N):
        for i in range(N):
            for j in range(N, 0, -1):
                print("*", end=" ")
            print()

    def pattern6(self, N):
        for i in range(N):
            for j in range(N, i, -1):
                print("*", end=" ")
            print()

    def pattern7(self, N):
        for i in range(N):
            for j in range(N, i, -1):
                print(N-j+1, end=" ")
            print()

    def pattern8(self, N):
        for i in range(N):
            for j in range(0, N-i-1):
                print(" ", end=" ")
            for k in range(0, 2*i+1):
                print("*", end=" ")
            for l in range(0, N-i-1):
                print(" ", end=" ")
            print()

    def pattern9(self, N):
        for i in range(N):
            for j in range(0, i):
                print(" ", end=" ")
            for k in range(2*N - (2*i+1)):
                print("*", end=" ")
            for j in range(0, i):
                print(" ", end=" ")
            print()

    def pattern10(self, N):
        for i in range(N):
            for j in range(0, N-i-1):
                print(" ", end=" ")
            for k in range(0, 2*i+1):
                print("*", end=" ")
            for l in range(0, N-i-1):
                print(" ", end=" ")
            print()
        for i in range(N):
            for j in range(0, i):
                print(" ", end=" ")
            for k in range(2*N - (2*i+1)):
                print("*", end=" ")
            for j in range(0, i):
                print(" ", end=" ")
            print()

    def pattern11(self, N):
        for i in range(1, 2*N):
            stars = i
            if (i > N):
                stars = 2*N-i
            for j in range(1, stars+1):
                print("*", end=" ")
            print()

    def pattern12(self, n):
        for i in range(0, n):
            if (i % 2 == 0):
                start = 1
            else:
                start = 0
            for j in range(0, i+1):
                print(start, end=" ")
                start = 1 - start
            print()

    def pattern13(self, n):
        space = 2 * (n - 1)
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=" ")
            for j in range(1, space+1):
                print(" ", end=" ")
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()
            space -= 2

    def pattern14(self, n):
        num = 1
        for i in range(0, n):
            for j in range(0, i+1):
                print(num, end=" ")
                num += 1
            print()

    def pattern15(self, n):
        for i in range(0, n):
            for j in range(0, i+1):
                print(chr(65+j), end=" ")
            print()

    def pattern16(self, n):
        for i in range(0, n):
            for j in range(0, n-i):
                print(chr(65+j), end=" ")
            print()

    def pattern17(self, n):
        for i in range(0, n):
            for j in range(0, i+1):
                print(chr(65+i), end=" ")
            print()

    def pattern18(self, n):
        for i in range(0, n):
            for j in range(0, n-i-1):
                print(" ", end=" ")
            breakpoint = (2*i+1) // 2
            ch = ord('A')
            for j in range(0, 2*i+1):
                print(chr(ch), end=" ")
                if (j < breakpoint):
                    ch += 1
                else:
                    ch -= 1
            for j in range(0, n-i-1):
                print(" ", end=" ")
            print()

    def pattern19(self, n):
        for i in range(0, n):
            ch = ord('A')
            for j in range(ch+n-1-i, ch+n):
                print(chr(j), end=" ")
            print()



Solution().pattern1(3)
Solution().pattern2(5)
Solution().pattern3(5)
Solution().pattern4(5)
Solution().pattern5(3)
Solution().pattern6(5)
Solution().pattern7(5)
Solution().pattern8(5)
Solution().pattern9(5)
Solution().pattern10(3)
Solution().pattern11(5)
Solution().pattern12(5)
Solution().pattern13(4)
Solution().pattern14(5)
Solution().pattern15(5)
Solution().pattern16(5)
Solution().pattern17(5)
Solution().pattern18(5)
Solution().pattern19(5)
