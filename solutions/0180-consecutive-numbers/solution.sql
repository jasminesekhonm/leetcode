/* Write your T-SQL query statement below */
 
  select distinct a.num as ConsecutiveNums from 
  (
 select  case when (l.num=l1.num and l1.num=l2.num) then 1 else 0  end as ind,l.num
 from logs l 
 left join logs l1
 on l.id=l1.id-1
 left join logs l2
 on l.id=l2.id-2
  ) a 
  where ind=1
 
 
 


