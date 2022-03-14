# CODE for Binary Search using Recursion

def binary_search(list, to_find, low, high):
    
    if high >= low:
        mid = len(sample_list)//2
        guess = list[mid]
        if guess == to_find:
            return "Item found at index number: " + str(mid)
        
        if guess < to_find:
            binary_search(list, to_find, mid+1, high)
        
        if guess > to_find:
            binary_search(list,to_find,low, mid-1)
        
        else:
            return "Item not found in the list"


sample_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(binary_search(sample_list, 8, 0, len(sample_list)))