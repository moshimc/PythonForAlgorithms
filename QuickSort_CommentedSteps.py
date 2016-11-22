def quick_sort(arr):
    
    quick_sort_help(arr,0,len(arr)-1)
    
    
    
def quick_sort_help(arr,first,last):
    
    if first < last:
        
        splitpoint = partition(arr,first,last)
    
        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)
        
    
def partition(arr,first,last):
    print("----------")
    print("Partition Called")
    print(arr)
    
    pivotvalue = arr[first]
    print("PivotValue: " + str(arr[first]))
    
    leftmark = first+1
    rightmark = last
    print("LeftMark: " + str(leftmark))
    print("RightMark: " + str(rightmark))
    print("----------")
    done = False
    
    while not done:
        
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            print("arr[" + str(leftmark) + "]:" + str(arr[leftmark]) + " <= " + str(pivotvalue))
            leftmark += 1
            
        while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
            print("arr[" + str(rightmark) + "]:" + str(arr[rightmark]) + " >= " + str(pivotvalue))
            rightmark -= 1
            
        if rightmark < leftmark:
            
            done = True
        
        else:
            
            print("                ",end="")
            print(arr)
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
            print("Values Swapped: ", end="")
            print(arr)
      
    print("final swap")
    print("rightmark: " + str(rightmark))
    temp = pivotvalue
    arr[first] = arr[rightmark]
    arr[rightmark] = temp
    
    print("Returning array: ",end="")
    print(arr)
    print("RightMark: " + str(rightmark))
    return rightmark
