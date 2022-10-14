def binarySearchIterative(array, target):
    if not array:
        return False
    
    start = 0
    end = len(array)-1

    while(start <= end):
        middle = (start+end)//2
        if (array[middle] > target):
            end = middle - 1
        elif (array[middle] < target):
            start = middle + 1
        else:
            return middle 

    return False        
