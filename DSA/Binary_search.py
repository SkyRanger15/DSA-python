def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))

    arr.sort()
    
    target = int(input("Enter the number to search for: "))
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Number {target} found.")
    else:
        print(f"Number {target} not found in the list.")
