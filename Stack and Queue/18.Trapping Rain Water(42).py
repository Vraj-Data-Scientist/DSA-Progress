from typing import List

class Solution:
    def prefix_max_array(self, height: List[int]):
        n = len(height)
        prefix_max = [-1] * n
        prefix_max[0] = height[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])
        return prefix_max

    def suffix_max_array(self, height: List[int]):
        n = len(height)
        suffix_max = [-1] * n
        suffix_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])
        return suffix_max

    def trap_brute(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = self.prefix_max_array(height)
        suffix_max = self.suffix_max_array(height)
        water = 0
        for i in range(0, n):
            if (height[i] < prefix_max[i] and height[i] < suffix_max[i]):
                water += min(prefix_max[i], suffix_max[i]) - height[i]
        return water

    def trap_better(self, height: List[int]) -> int:
        n = len(height)
        left_max = 0
        right_max = 0
        water = 0
        l = 0
        r = n-1
        while (l < r):
            if (height[l] <= height[r]):
                if (height[l] < left_max):
                    water += (left_max - height[l])
                else:
                    left_max = height[l]
                l += 1
            else:
                if (height[r] < right_max):
                    water += (right_max - height[r])
                else:
                    right_max = height[r]
                r -= 1
        return water

    def trap_optimal(self, height: List[int]) -> int:
        n = len(height)
        st = []
        water = 0
        for i in range(0, n):
            while (st and height[st[-1]] < height[i]):
                top = st.pop()
                if not st:
                    break
                left = st[-1]
                right = i
                curr_width = right - left - 1
                curr_height = min(height[left], height[right]) - height[top]
                water += (curr_width * curr_height)
            st.append(i)
        return water


print(Solution().trap_brute([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap_brute([4,2,0,3,2,5]))
print(Solution().trap_better([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap_better([4,2,0,3,2,5]))
print(Solution().trap_optimal([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap_optimal([4,2,0,3,2,5]))
