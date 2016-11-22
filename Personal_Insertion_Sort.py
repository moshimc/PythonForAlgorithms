def insertion_sort(arr):

    # 1, 2, 3, 4... n-1
    for index in range(1,len(arr)):

        # 1-0, 2-0, 3-0, n-1-0
        for i in range(index,0,-1):    

            if arr[index] < arr[i-1]:
                temp = arr[i-1]
                arr[i-1] = arr[index]
                arr[index] = temp
                index -= 1
