class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int: 
        dic=Counter(arr) 
        dic1=sorted(dic.items(),key= lambda x:x[1]) 
        c=0
        for i in dic1:  
            if k<=0:  
                c+=1
                continue    
            k=k-i[1]
            if k<0:  
                c+=1
        return c
