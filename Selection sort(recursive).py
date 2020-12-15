Sri karthikeya
121910313042
Selection sort(recursive)"""
def selection(ar):
    if len(ar)>1:
        mid = len(ar)//2
        left = ar[:mid]
        right = ar[mid:]
        selection(left)
        selection(right)
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                ar[k] = left[i]
                i+=1
            else:
                ar[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            ar[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            ar[k] = right[j]
            j+=1
            k+=1
#array input
l = list(map(int,input("Enter elements to sort: ").split()))
selection(l)
print("Selection sort :", l)
