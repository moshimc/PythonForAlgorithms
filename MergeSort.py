def merge_sort(arr):

    # Do we still have elements to split?
    if len(arr) > 1:

        # Yes! Split the array in half
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        # Recursively merge each half
        merge_sort(leftHalf)
        merge_sort(rightHalf)
        
        leftIndex = 0
        rightIndex = 0
        arrayIndex = 0

        # Sort until we've reached the end of one array half...
        while leftIndex < len(leftHalf) and j < len(rightHalf):
            
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                
                arr[arrayIndex] = leftHalf[leftIndex]              
                leftIndex += 1
                
            else:
                
                arr[arrayIndex] = rightHalf[rightIndex]              
                rightIndex += 1
                
            arrayIndex += 1

        # Append the unfinished and sorted other half w/ A or B loop

        # A
        while leftIndex < len(leftHalf):
            
            arr[arrayIndex] = leftHalf[leftIndex]
            leftIndex += 1
            arrayIndex += 1
            
        # B
        while rightIndex < len(rightHalf):
            
            arr[arrayIndex] = rightHalf[rightIndex]
            rightIndex += 1
            arrayIndex += 1
