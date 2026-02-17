from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        st = []
        for i in range(0, n):
            if (asteroids[i] > 0):
                st.append(asteroids[i])
            else:
                while (st and st[-1] > 0 and st[-1] < abs(asteroids[i])):
                    st.pop()
                if (st and st[-1] == abs(asteroids[i])):
                    st.pop()
                elif(not st or st[-1] < 0):
                    st.append(asteroids[i])
        return st

print(Solution().asteroidCollision([4,7,1,1,2,-3,-7,17,15,-16,-18]))
print(Solution().asteroidCollision([4,7,1,1,2,-3,-7,17,15,-16]))


