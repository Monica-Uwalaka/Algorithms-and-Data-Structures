"""
key: bubble, swap elements in a bubble of two

This algorithms works my sending the largest element of an unsorted 
array to the end of the array one at a time by swaping the larger two elements to the right.

Time Complexity: Worst => O(n^2)  Best => 0(n) Average => 0(n^2)

Space Complexity: O(1)
"""

def bubblesort(array):
    unsorted_array_length = len(array) 
    for i in range(unsorted_array_length):
        swaps = False
        for j in range(unsorted_array_length-1):
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swaps = True
        if swaps:
            unsorted_array_length -= 1
        else:
            return array
    return array

print(bubblesort([2,3,4,5,6,1]))
