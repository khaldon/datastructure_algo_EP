#### steps #### 
# 1- create function has two pramaters (list, item)
# 2- for loop and check if the target in list
###############

def simple_search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return item
    return None 

a = simple_search([2,3,4,5,6,7,8], 1)

print(a)

