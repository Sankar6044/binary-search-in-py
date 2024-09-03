def binarysearch(s,e,li,k):
      if k in li:
          mid = (s+e)//2
          if k == li[mid]:
              return mid
          elif k < li[mid]:
              return binarysearch(s,e,li,k)
          else:
              return binarysearch(mid+1,e,li,k)
     else:
         return -1

li = []
n = int(input('count the values in list'))
for i in range(n):
    li.append(int(input()))
li.sort()
k = int(input('enter the key value  :'))
print(binarysearch(0,len(li)-1,li,k))
    

            
                                  
