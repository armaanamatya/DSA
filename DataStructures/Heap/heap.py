# import heapq

# def swap(arr, i, j):
#     """
#     Swaps the elements at indices i and j in the given array.

#     Parameters:
#     arr (list): The array in which the elements are to be swapped.
#     i (int): The index of the first element.
#     j (int): The index of the second element.

#     Returns:
#     None
#     """
#     # Store the value of arr[i] in a temporary variable.
#     temp = arr[i]

#     # Assign the value of arr[j] to arr[i].
#     arr[i] = arr[j]

#     # Assign the value of the temporary variable to arr[j].
#     arr[j] = temp
    
# def heapify(arr, n, i):
#     """
#     This function takes an array, its size, and the index of the root node
#     as input and rearranges the array to maintain the heap property.
    
#     Parameters:
#     arr (list): The array to be heapified.
#     n (int): The size of the array.
#     i (int): The index of the root node.
#     """
    
#     # Find the left and right child indices of the root node.
#     largest = i
#     l = 2 * i
#     r = 2 * i + 1

#     # Find the index of the largest element among the root, left child, and right child.
#     # Initialize it to the root index.
#     largest = i

#     # If the left child exists and is greater than the root, update the largest index.
#     if l < n and arr[i] < arr[l]:
#         largest = l

#     # If the right child exists and is greater than the largest so far, update the largest index.
#     if r < n and arr[largest] < arr[r]:
#         largest = r

#     # If the largest index is not the root index, swap the root with the largest element and recursively heapify.
#     if largest != i:
#         swap(arr, i, largest)
#         heapify(arr, n, largest)

# def build_heap(arr, n):
#     """
#     Builds a heap from a given array. A heap is a complete binary tree where the
#     parent node is greater than or equal to its children.

#     Parameters:
#     arr (list): The array to be converted into a heap.
#     n (int): The size of the array.

#     Returns:
#     None
#     """
#     # Start from the last non-leaf node and move backwards.
#     # This is because all leaf nodes are already heaps.
#     for i in range(n // 2 - 1, -1, -1):
#         # Heapify the node at index i. This process ensures that the parent
#         # node is greater than or equal to its children.
#         heapify(arr, n, i)

# def heap_pop(arr, n):
#     """
#     This function removes and returns the maximum element from a heap.

#     Parameters:
#     arr (list): The heap from which to remove the maximum element.
#     n (int): The size of the heap.

#     Returns:
#     int: The maximum element from the heap.
#     """

#     # Store the maximum value in a variable.
#     # The maximum value is the root node of the heap, which is the element with the highest priority.
#     max_val = arr[0]

#     # # Replace the maximum value with the last element of the heap.
#     # # This is done by assigning the last element of the heap to the root node.
#     # # The root node is the element with the highest priority in a heap.
#     arr[0] = arr[n - 1]

#     # # Decrement the size of the heap by 1.
#     # # This is done to reflect the removal of the maximum element from the heap.
#     n -= 1

#     # # Heapify the root node of the heap to maintain the heap property.
#     # # This process ensures that the parent node is greater than or equal
#     # # to its children. This is done by comparing the root node with its children
#     # # and swapping them if necessary. This process is repeated until the root
#     # # node is greater than or equal to its children.
#     heapify(arr, n, 0)

#     # # Return the maximum value.
#     # # This is the maximum element that was removed from the heap.
#     return max_val
    
# def percolate_up(arr, n, i):
#     # This function is used to restore the heap property from the bottom up.
#     # It is used when a new element is added to the heap, or when the key of
#     # an element is increased.
    
#     # The loop continues as long as the current element is not at the root of
#     # the heap, and its parent is smaller than it.
#     # The parent of an element is the element at the index (i // 2).
#     # The loop works by swapping the parent and the current element if the
#     # parent is smaller than the current element.
#     # This process is repeated until the heap property is restored.
    
#     # The loop starts from the current element and checks if it is not at the
#     # root of the heap. The root of the heap is the element at index 1. If the
#     # current element is smaller than its parent, the loop continues.
#     while i > 1 and arr[i // 2] < arr[i]:
#         # Swap the current element with its parent.
#         swap(arr, i, i // 2)
#         # Update the index of the current element to its parent.
#         # This is done by dividing the current index by 2 and rounding down.
#         i //= 2
        
# def heap_push(arr, n, val):
#     """
#     This function adds a new element to a heap.

#     Parameters:
#     arr (list): The heap to which the new element is to be added.
#     n (int): The index of the last element in the heap.
#     val (int): The value of the new element to be added.

#     Returns:
#     None

#     This function performs the following steps:
#     1. Append the new element to the end of the heap.
#     2. Move the new element up the heap until it is greater than or equal to its parent.
#     3. Move the new element up the heap again, if necessary, to ensure that the heap property is restored.
#     """
#     # Add the new element to the end of the heap
#     arr.append(val)
    
#     # Move the new element up the heap until it is greater than or equal to its parent
#     percolate_up(arr, len(arr), n)
    
#     # Move the new element up the heap again, if necessary, to ensure that the heap property is restored
#     percolate_up(arr, len(arr), n)

# def increase_key(arr, n, i, diff):
#     """
#     Increases the key of an element in a heap.

#     Parameters:
#     arr (list): The heap.
#     n (int): The number of elements in the heap.
#     i (int): The index of the element whose key is to be increased.
#     diff (int): The amount by which the key of the element is to be increased.

#     Returns:
#     None

#     This function performs the following steps:
#     1. Checks if the amount by which the key is to be increased is negative.
#        If it is, the function simply returns without doing anything.
#     2. Increases the key of the element at index i by the specified amount.
#     3. Moves the element up the heap until it is greater than or equal to its parent.
#        This ensures that the heap property is restored.
#     """
#     # Check if the amount by which the key is to be increased is negative.
#     # If it is, the function simply returns without doing anything.
#     if diff < 0:
#         return
    
#     # Increase the key of the element at index i by the specified amount.
#     arr[i] += diff
    
#     # Move the element up the heap until it is greater than or equal to its parent.
#     # This ensures that the heap property is restored.
#     percolate_up(arr, n, i)
#     if diff < 0:
#         return
#     arr[i] += diff
#     percolate_up(arr, n, i)


# def decrease_key(arr, n, i, diff):
#     """
#     Decreases the key of an element in a heap.

#     Parameters:
#     arr (list): The heap.
#     n (int): The number of elements in the heap.
#     i (int): The index of the element whose key is to be decreased.
#     diff (int): The amount by which the key of the element is to be decreased.

#     Returns:
#     None

#     This function performs the following steps:
#     1. Checks if the amount by which the key is to be decreased is non-negative.
#        If it is, the function simply returns without doing anything.
#     2. Decreases the key of the element at index i by the specified amount.
#     3. Restores the heap property by moving the element down the heap until it is smaller than its children.
#     """
#     # Check if the amount by which the key is to be decreased is non-negative.
#     # If it is, the function simply returns without doing anything.
#     if diff >= 0:
#         return
    
#     # Decrease the key of the element at index i by the specified amount.
#     arr[i] += diff
    
#     # Restore the heap property by moving the element down the heap until it is smaller than its children.
#     # This ensures that the heap property is restored.
#     heapify(arr, n, i)
    
# def heap_sort(arr, n):
#     """
#     Sorts an array using the heap sort algorithm.

#     Args:
#         arr (list): The array to be sorted.
#         n (int): The length of the array.

#     Returns:
#         list: The sorted array.
#     """
#     # Build the initial heap using the input array.
#     build_heap(arr, n)

#     # Initialize an empty list to store the sorted elements.
#     sorted_arr = []

#     # Repeat n-1 times, where n is the length of the array.
#     for _ in range(1, n):
#         # Pop the maximum element from the heap and append it to the sorted list.
#         sorted_arr.append(heap_pop(arr, n))

#         # Decrement the length of the heap by 1.
#         n -= 1

#     # Return the sorted array.
#     return sorted_arr
#     return sorted_arr

class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_min(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        minval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return minval

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new < old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)

class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] < self.heap[left]) or (right < len(self.heap) and self.heap[i] < self.heap[right]):
            biggest = left if (right >= len(self.heap) or self.heap[left] > self.heap[right]) else right
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]
            i = biggest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_max(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        maxval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return maxval

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new > old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)


def heapsort(arr):
    heap = MinHeap(arr)
    return [heap.extract_min() for i in range(len(heap.heap))]


class PriorityQueue:
    def __init__(self):
        self.queue = MaxHeap()

    def enqueue(self, element):
        self.queue.insert(element)

    def peek(self):
        return self.queue.get_max()

    def dequeue(self, element):
        return self.queue.extract_max()

    def is_empty(self):
        return len(self.queue.heap) == 0

    def change_priority_by_index(self, i, new):
        self.queue.update_by_index(i, new)

    def change_priority(self, old, new):
        self.queue.update(old, new)

if __name__ == "__main__":
    arr = [0, 8, 6, 7, 2, 10, 5]
    n = len(arr)
    arr = MaxHeap(arr)
    print(arr.get_max())
    print(arr.heap)
