def mergesort(arr, begin, end):
    if begin>=end:
        return

    mid = (end-begin) // 2 + begin
    mergesort(arr, begin, mid)
    mergesort(arr, mid+1, end)
    merge(arr, begin, mid, end)


def merge(arr, begin, mid, end):
    print(begin,mid,end)

    temp = []
    p1 = begin
    p2 = mid+1
    while (p1 <= mid and p2 <= end):
        #print(p1,p2,"len",len(arr))
        #print(arr[p1],arr[p2],'x')
        if (arr[p1] < arr[p2]):
            temp.append(arr[p1])
            p1 += 1
        else:
            temp.append(arr[p2])
            p2 += 1

    if p1 <= mid:
        temp += arr[p1:mid+1]
    elif p2 <= end:
        temp += arr[p2:end+1]
    arr[begin:end+1] = temp
    print("---")
            

if __name__ == "__main__":
    arr = [1,6,9,2,5,3,8,1,5,9,8,3]
    arr *= 3
    arr = [35,12,31,23] + arr
    mergesort(arr,0,len(arr)-1)
    print(arr)
