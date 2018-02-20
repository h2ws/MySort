def shellsort(arr):
    Sedgewick = [1, 5, 19, 109, 209, 505, 929, 2161]#打表出奇迹
    Islen = len(arr)
    stage = 0 #增量序列下标

    while Islen > Sedgewick[stage+1]:
        stage +=1
    for gap in Sedgewick[:stage+1][::-1]:
        for i in range(gap,Islen):
            temp = arr[i]
            j = i
            while j-gap>=0 and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp

def foo(arr):
    Islen = len(arr)
    ret = []
    for i in range(Islen):
        for j in range(Islen):
            print(i,j,arr[i]*arr[j])
            ret.append(arr[i]*arr[j])
    return ret

if __name__ == "__main__":
    arr = [8,3,2,7,6,8,9,1,7,4,5,9,1,0,3]
    arr = foo(arr)
    shellsort(arr)
    print(arr)

