from typing import List
import heapq

def counting_gas_station(arr, max_dist):
    n = len(arr)
    cnt = 0
    for i in range(0, n-1):
        number_inbet = int((arr[i+1] - arr[i]) / max_dist)
        if ((arr[i+1] - arr[i]) == (number_inbet * max_dist)):
            number_inbet -= 1
        cnt += number_inbet
    return cnt

class GasStationSolver:
    def minimise_max_distance_brute(self, arr, k):
        n = len(arr)
        how_many = [0]*(n-1)
        for _ in range(1, k+1):
            max_section = -1
            max_index = -1
            for i in range(0, n-1):
                diff = arr[i+1] - arr[i]
                section_length = diff / (1 + how_many[i])
                if (section_length > max_section):
                    max_section = section_length
                    max_index = i
            how_many[max_index] += 1

        max_ans = -1
        for i in range(0, n-1):
            diff = arr[i+1] - arr[i]
            section_length = diff / (1 + how_many[i])
            max_ans = max(max_ans, section_length)

        return max_ans

    def minimise_max_distance_better(self, arr, k):
        n = len(arr)
        how_many = [0]*(n-1)
        pq = []

        for i in range(0, n-1):
            diff = arr[i+1] - arr[i]
            heapq.heappush(pq, (-diff, i))

        for _ in range(1, k+1):
            diff, i = heapq.heappop(pq)
            how_many[i] += 1
            diff = arr[i+1] - arr[i]
            section_length = diff / (how_many[i] + 1)
            heapq.heappush(pq, (-section_length, i))

        return -pq[0][0]

    def minimise_max_distance_optimal(self, arr, k):
        n = len(arr)
        diff = 1e-6
        low = 0
        high = max(arr[i+1] - arr[i] for i in range(0, n-1))
        while(high - low > diff):
            mid = (low + high) / 2.0
            if (counting_gas_station(arr, mid) > k):
                low = mid
            else:
                ans = high
                high = mid
        return high


print(GasStationSolver().minimise_max_distance_brute([1,2,3,4,5], 4))
print(GasStationSolver().minimise_max_distance_brute([1,2,3,4,5,6,7,8,9,10], 1))
print(GasStationSolver().minimise_max_distance_better([1,2,3,4,5], 4))
print(GasStationSolver().minimise_max_distance_better([1,2,3,4,5,6,7,8,9,10], 1))
print(GasStationSolver().minimise_max_distance_optimal([1,2,3,4,5], 4))
print(GasStationSolver().minimise_max_distance_optimal([1,2,3,4,5,6,7,8,9,10], 1))
