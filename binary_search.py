# binarySearch_rec
# Time Complexity: O(log n)
# Auxiliary Space: O(log n)

def binarySearch_rec(arr, x, low, high):
    if low > high:
        return False #If it does not exists in any segment

    else: 
        mid = int ((low + high) / 2)
        if x == arr[mid]: #base case
            return mid
        elif x > arr[mid]:
            return binarySearch_rec(arr, x, mid + 1, high)
        else:
            return binarySearch_rec(arr, x, low, mid - 1)
     

# binarySearch_it
# Time Complexity: O(log n)
# Auxiliary Space: O(log n)
def binarySearch_it(arr, x, low, high):
    while low < high:

        mid = int((low + high) / 2)
        if x == arr[mid]: #base case
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return False


if __name__ == "__main__":

    #For binary search to work, the array passed as an argument must be sorted.
    arr = [2, 3, 4, 10, 40]
    x = 5

    result = binarySearch_it(arr, x, 0, len(arr)-1)
    print(f"{x} does not exists in array.") if not result else print(f"{x} exists at index: {result}.")
