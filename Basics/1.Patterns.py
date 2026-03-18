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
