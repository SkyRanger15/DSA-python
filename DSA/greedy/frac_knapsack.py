# class Item:
#     def __init__(self,value,weight) -> None:
#         self.value = value
#         self.weight = weight



class Item:
    def __init__(self,value,weight) -> None:
        self.value = value
        self.weight = weight


    def __repr__(self):
            return f"Item(value={self.value}, weight={self.weight})"



# def knapsack(arr,W):
#     arr.sort(key = lambda x: x.value/x.weight,reverse =True)
#     total_val = 0.0
#     curr_wgt = 0
#     for i in range(len(arr)):
#         if W >= (curr_wgt +arr[i].weight):
#             curr_wgt += arr[i].weight
#             total_val += arr[i].value
#         else:
#             remain = W - curr_wgt
#             total_val += (arr[i].value/arr[i].weight)*remain
#             break

#     return total_val







# W = int(input("Enter Weight: "))
# n= int(input("Enter Number of Items: "))
# arr =[]
# for i in range(n):
#     value = int(input(f"Enter the value of items {i+1}: "))
#     weight = int(input(f"Enter the weight of items {i+1}: "))
#     arr.append(Item(value,weight))
# ans = knapsack(arr,W)
# print(ans)

def knapsack(arr, W):
    arr.sort(key = lambda x: x.value/x.weight,reverse = True)
    total_val = 0.0
    curr_wgt = 0
    for i in range(len(arr)):
        if W >= (curr_wgt+arr[i].weight):
            curr_wgt += arr[i].weight
            total_val += arr[i].value
        else:
            remain = W - curr_wgt
            total_val += (arr[i].value/arr[i].weight)*remain
            break


    return total_val

W = int(input("Enter Total Weight: "))
n = int(input("Enter total no of items: "))
arr = []
for i in range(n):
    value = int(input(f"Enter value of items {i+1}: "))
    weight = int(input(f"Enter weight of items {i+1}: "))
    arr.append(Item(value,weight))
print(arr)
ans = knapsack(arr,W)
print(ans)