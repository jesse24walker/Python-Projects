def isSorted(lyst):
    for i in range(len(lyst)-1):
        if(lyst[i+1] < lyst[i]):
            return False
    return True

print(isSorted([5,8,6,3]))
print(isSorted([5,6,7,8]))
print(isSorted([1,3,4,2]))
