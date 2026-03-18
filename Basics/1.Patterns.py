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


Solution().pattern1(3)
Solution().pattern2(5)
Solution().pattern3(5)
Solution().pattern4(5)
Solution().pattern5(3)
Solution().pattern6(5)
Solution().pattern7(5)
