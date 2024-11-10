class Solution:
    def merge(self, arr, l, m, r):
        lst = []
        left = l
        right = m + 1
        
        while left <= m and right <= r:
            if arr[left] <= arr[right]:
                lst.append(arr[left])
                left += 1
            else:
                lst.append(arr[right])
                right += 1
        
        while left <= m:
            lst.append(arr[left])
            left += 1
        
        while right <= r:
            lst.append(arr[right])
            right += 1
        
        for i in range(l, r + 1):
            arr[i] = lst[i - l]

    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    solution = Solution()
    
    solution.mergeSort(arr, 0, len(arr) - 1)
    
    print("Sorted list:", arr)
