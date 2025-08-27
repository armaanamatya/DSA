def lS(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

def bS(arr,val):
    left_index = 0
    right_index = len(arr) - 1
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = arr[mid_index]
        
        if mid_number == val:
            return mid_index
        
        if val < mid_number:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

    return -1

def bS_recursive(arr,val,left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(arr) or mid_index < 0:
        return -1

    mid_number = arr[mid_index]
    
    if mid_number == val:
        return mid_index
    
    if val < mid_number:
        right_index = mid_index - 1
    else:
        left_index = mid_index + 1
    
    return bS_recursive(arr,val,left_index,right_index)

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    index = bS(numbers_list,number_to_find)  
    index = bS_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search")