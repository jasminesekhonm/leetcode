class Solution(object):
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        min_lst=[]
        for x in timePoints:
            h=x[:2]
            m=x[3:]
            time=int(h)*60+int(m)
            min_lst.append(time)
            
        min_lst.sort()    
        minn=(23*60+60)-(min_lst[-1]-min_lst[0])
        
        for i in range(len(min_lst)-1):
            dif=abs(min_lst[i]-min_lst[i+1])
            if dif<minn:
                minn=dif
        return minn


            
        
        
        
        
