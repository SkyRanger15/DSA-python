class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            par_idx = self.partition(arr, low, high)
            self.quickSort(arr, low, par_idx - 1)
            self.quickSort(arr, par_idx + 1, high)
        return arr
    
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high
        
        while i < j:
            while arr[i] <= pivot and i < high:
                i += 1
            while arr[j] >= pivot and j > low:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        
        return j

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    solution = Solution()
    
    solution.quickSort(arr, 0, len(arr) - 1)
    
    print("Sorted list:", arr)
