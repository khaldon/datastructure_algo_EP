#### steps #####
# 1- create function has two pramaters (list, item)
# 1- create 2 vaiables low and high 
# 2- while loop if low <= high 
# 3- get mid (low+high)/2 
# 4- target = list[mid]
# 5- if target is item then return mid or value
# 6- if target > item then high = mid -1 
# 7- otherwise low = mid +1 
# 8- return None 
#################

def binary_search(list, item):
    low = 0 
    high = len(list)-1 
    while(low <= high):
        mid = int((low+high)/2) 
        target = list[mid]
        if target == item:
            return target 
        if target > item:
            high = mid - 1 
        else:
            low = mid + 1 
    return None 

a = binary_search([3,4,5,6,7,8,9],8)
print(a)