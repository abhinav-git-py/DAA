def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[5,2,9,1,6]
target=9

result=linear_search(arr,target)

if result!=-1:
    print("Found at index",result)
else:
    print("Not Found")