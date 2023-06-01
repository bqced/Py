def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    # print('Pivot is', pivotvalue, 'first is', alist[leftmark],  last is', alist[rightmark])
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
            # print('moving to right', alist[leftmark])
        # print(alist[leftmark], '>', pivotvalue)
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        # print('moving to left', alist[rightmark])
        # print(alist[rightmark], '<', pivotvalue)
        if rightmark < leftmark:
            # print('No need to swap')
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            # print('Swapping left', alist[leftmark], 'and right', alist[rightmark])
            # print(alist, '\n')

    # print(alist)
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    # print('split point =', rightmark, 'split value is', alist[rightmark],'\n')
    return rightmark

def quickSort(alist, first, last):
    if first < last:
        # print('\nWorking out splitpoint')
        splitpoint = partition(alist, first, last)
        # print('\nSort left of split')
        quickSort(alist, first, splitpoint-1)
        # print('\nSort right of split')
        quickSort(alist, splitpoint+1, last)

alist = [17, 8, -28, 80, 26, 44, 28, 71, -8, 35]
print(alist)
quickSort(alist, 0, len(alist) - 1)
print(alist)