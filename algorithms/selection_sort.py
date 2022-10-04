"""
Key: select, select smallest 

This algorithm works by finding the smallest unsorted element and placing it at the end of the sorted list. 

Time Complexity: Worst => O(n^2)  Best => 0(n^2) Average => 0(n^2)

Space Complexity: O(1)
"""
def selectionsort(array):
    # index varibale is to keep track how many numbers we've sorted so far
    array_length = len(array)
    index = 0
    while(index < array_length):
        smallest = array[index]
        smallest_index = index
        #find the smallst from the unsoted art of the array from index to array_length-1
        for i in range(index, array_length):
            if (array[i] < smallest):
                smallest = array[i]
                smallest_index = i
        #swap the smallest number found at smallest_index with the number at indx, which makes everything up to i sorted.
        temp = array[index]
        array[index] = smallest
        array[smallest_index] = temp
        index += 1
    return array

