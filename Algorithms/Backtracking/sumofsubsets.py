def subset_sum_backtracking(arr, target_sum):
    def backtrack(start, current_sum, current_subset):
        # If current_sum is equal to target_sum, we found a valid subset
        if current_sum == target_sum:
            results.append(list(current_subset))
            return
        
        # If current_sum exceeds the target_sum, stop exploring further
        if current_sum > target_sum:
            return

        for i in range(start, len(arr)):
            # Include the current element in the subset
            current_subset.append(arr[i])
            # Recursively call to explore further with the updated sum
            backtrack(i + 1, current_sum + arr[i], current_subset)
            # Backtrack: remove the last element to explore other possibilities
            current_subset.pop()

    results = []
    arr.sort()  # Optional: sorting can help optimize by early termination
    backtrack(0, 0, [])
    return results

# Driver code
if __name__ == "__main__":
    # Test case 1
    set_1 = [1, 2, 1]
    sum_1 = 3
    print("Output 1:")
    result_1 = subset_sum_backtracking(set_1, sum_1)
    if result_1:
        for subset in result_1:
            print(subset)
    else:
        print("There is no such subset")

    # Test case 2
    set_2 = [3, 34, 4, 12, 5, 2]
    sum_2 = 9
    print("Output 2:")
    result_2 = subset_sum_backtracking(set_2, sum_2)
    if result_2:
        for subset in result_2:
            print(subset)
    else:
        print("There is no such subset")
