from typing import List

class Solution:
    def solve(self, num, target, start, current_value, last_operand, ds, result):
        if (start == len(num)):
            if (current_value == target):
                result.append(ds)
            return

        for end in range(start, len(num)+1):
            if end > start and num[start] == "0":
                return
            curr_num = num[start:end+1]
            curr_num_val = int(curr_num)
            if start == 0:
                self.solve(num, target, end+1, curr_num_val, curr_num_val, curr_num, result)
            else:
                self.solve(num, target, end+1, current_value + curr_num_val, curr_num_val, ds + "+" + curr_num, result)
                self.solve(num, target, end+1, current_value - curr_num_val, -curr_num_val, ds + "-" + curr_num, result)
                self.solve(num, target, end+1, current_value - last_operand + last_operand * curr_num_val , last_operand * curr_num_val, ds + "*" + curr_num, result)

    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        ds = ""
        self.solve(num, target, 0, 0, 0, ds, result)
        return result


# Testing the implementation
if __name__ == "__main__":
    num = "123"
    target = 6
    sol = Solution()

    result = sol.addOperators(num, target)

    for expr in result:
        print(expr, end=" ")  # Output each valid expression