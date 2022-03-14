# CODE for Binary Search

def Binary_search(list, to_find):
    low = 0
    high = len(list)
    
    
    while high >= low:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == to_find:
            return "Item Found at Index " + str(mid)
        if guess > to_find:
            high = mid-1
        else:
            low = mid + 1
    return None


sample_list = [1,2,3,4,5,6,7,8,9,10]

print(Binary_search(sample_list, 6))