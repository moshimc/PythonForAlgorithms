def quick_sort(arr):
    
    quick_sort_help(arr,0,len(arr)-1)
    
    
    
def quick_sort_help(arr,first,last):
    
    if first < last:
        
        # Initial splitpoint and sorting
        splitpoint = partition(arr,first,last)
    
        # recurse!
        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)
        
    
def partition(arr,first,last):

    # Designate first item as pivot value
    pivotvalue = arr[first]
 
    leftmark = first+1
    rightmark = last

    done = False
    
    while not done:
        
        # is our array item less than the PIVOT & right marker?
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            
            # Yes, keep going
            leftmark += 1
           
        # is our array item more than the PIVOT & left marker?
        while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
            
            # Yes, keep going
            rightmark -= 1
            
        # If our markers crossed, we've reached a split point
        if rightmark < leftmark:
            
            done = True
        
        else:

            # Otherwise we swap our left value (> PIVOT) and our right value (< PIVOT)
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    # 3 Options:
    # 1 - every value is greater than our pivot [rightmark = 0; no swap occurs]
    # 2 - every value is lesser than our pivot [rightmark = last index; pivot swapped]
    # 3 - we know everything to the left of our split point is less and vice versa [pivot placed at stopping point]
    # 3 (ex): {6} 3, 1, 2, 4, |3|, 9, 8, 10, 15 => |3|, 3, 1, 2, 4, {6}, 9, 8, 10, 15
    temp = pivotvalue
    arr[first] = arr[rightmark]
    arr[rightmark] = temp
 
    # return our new split point
    return rightmark
