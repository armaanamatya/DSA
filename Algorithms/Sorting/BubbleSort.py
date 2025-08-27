def bubble_sort(arr):
    size = len(arr)
    
    for i in range(size-1):
        swapped = False
        
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
                break
    
    # for i in range(size-1):
    #     swapped = False
    #     for j in range(size-1-i):
    #         if elements[j] > elements[j+1]:
    #             tmp = elements[j]
    #             elements[j] = elements[j+1]
    #             elements[j+1] = tmp
    #             swapped = True
    #     if not swapped:
    #          break
    
if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
#    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)