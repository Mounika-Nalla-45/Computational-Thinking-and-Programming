## 1. Merge Sort Using Divide and Conquer

### Aim

To implement the Merge Sort algorithm using the Divide and Conquer
technique and analyze its time complexity.

### Algorithm

1.  If the array contains zero or one element, return it.
2.  Divide the array into two halves.
3.  Recursively sort the left half.
4.  Recursively sort the right half.
5.  Merge the two sorted halves.
6.  Return the sorted array.

### Python Program

``` python
def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Conquer
    left = merge_sort(left)
    right = merge_sort(right)

    # Combine
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Main program
arr = [38, 12, 27, 43, 9, 31]

print("Original array:", arr)

sorted_arr = merge_sort(arr)

print("Sorted array:", sorted_arr)
```

### Data (Input)

``` text
Array: [38, 12, 27, 43, 9, 31]
```

### Result (Output)

``` text
Original array: [38, 12, 27, 43, 9, 31]
Sorted array: [9, 12, 27, 31, 38, 43]
```

### Inference

Merge Sort successfully sorts the array using the Divide and Conquer
technique.

### Analysis

-   Best-case time complexity: `O(n log n)`
-   Average-case time complexity: `O(n log n)`
-   Worst-case time complexity: `O(n log n)`
-   Space complexity: `O(n)` for this implementation.
