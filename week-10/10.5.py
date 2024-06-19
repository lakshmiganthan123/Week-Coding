Write a Python program to sort a list of elements using the merge sort algorithm.

def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        
        # Dividing the elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        
        # Sorting the first half
        merge_sort(L)
        
        # Sorting the second half
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr)
    print(" ".join(map(str, arr)))
if __name__ == "__main__":
    main()
