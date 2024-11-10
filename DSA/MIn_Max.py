class Solution:
    def findMinMax(self, arr, low, high):
        if low == high:
            return arr[low], arr[high]

        if high == low + 1:
            if arr[low] < arr[high]:
                return arr[low], arr[high]
            else:
                return arr[high], arr[low]

        mid = (low + high) // 2

        left_min, left_max = self.findMinMax(arr, low, mid)
        right_min, right_max = self.findMinMax(arr, mid + 1, high)

        return min(left_min, right_min), max(left_max, right_max)

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    solution = Solution()
    
    if arr:
        min_val, max_val = solution.findMinMax(arr, 0, len(arr) - 1)
        print(f"Minimum value: {min_val}")
        print(f"Maximum value: {max_val}")
    else:
        print("The list is empty.")
