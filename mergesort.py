count = 0
def swap(arr, i, j,c):
    #print(i,arr[i],'<->',j,arr[j])
    print(" "+"   "*i+c+"  "+(j-i-1)*"   "+c)
    print(arr)
    arr[i],arr[j] = arr[j],arr[i]
    global count
    count +=1
    

def mergesort(arr, left, right):
    print(" "+"   "*left+"|"+"  "+(right-left-1)*"   "+"|")
    if left == right:
        return
    elif left+1 ==right:
        if arr[right]<arr[left]:
            swap(arr,left,right,"V")
            #print("t",end='')
        return

    else:
        length = right - left
        
        center = left+(length//2)
        #print(left,center,right)
        mergesort(arr, left, center)
        if center+1<right:
            mergesort(arr, center+1, right)
        
        R_head = center+1

        pstart = left
        plast = -2
        while pstart<R_head:
            if arr[pstart]>arr[R_head]:
                swap(arr,pstart,R_head,"V")
                #print("x",end='')
                pa = R_head
                while pa!=right and (pa<(plast) or arr[pa]>arr[pa+1]):
                    swap(arr,pa,pa+1,"V")
                    pa += 1
                    
                plast = pa
            
            pstart += 1


                
        return

ulist = [2,6,8,3,4,5,6,8,3, 1,4, 1,8, 2,3]
mergesort(ulist,0,len(ulist)-1)
print(ulist)
print(count)
