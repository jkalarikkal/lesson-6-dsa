array = [12,5,6,9,1,10]
print("Original Array: ",array)

def mergesort (array):
    if len(array) > 1:
        mid = len(array) // 2
        l = array[ :mid]
        r = array[mid: ]
        mergesort(l)
        mergesort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i = i + 1
            else:
                array[k] = r[j]
                j = j + 1
            k = k + 1
        
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1

def listy (array):
    for i in range (len(array)):
        print(array[i], end = " ")

print("sorted array: ")
mergesort(array)
listy(array)