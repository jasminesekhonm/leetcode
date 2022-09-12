/* Write your T-SQL query statement below */

with cte1 as
(select s.id as id1 ,s1.id as id2, s3.id as id3,
 s.visit_date as vd1, s1.visit_date as vd2, s3.visit_Date as vd3, s.people as p1, s1.people as p2, 
 s3.people as p3
from stadium s  join stadium s1 
on s.id=s1.id-1  
--and s.people>100 and s1.people>100
 join stadium s3 
on s.id=s3.id-2 
where (s.people>=100 and s1.people>=100 and s3.people>=100)
) 

--  select * from cte1 where p1>100 and p2>100 and p3=100


-- --and s.people>100 and s3.people>100) 
select id1 as id,vd1 as visit_date, p1 as people from cte1
union select id2 as id,vd2 as visit_date,p2 as people from cte1
union select id3 as id,vd3 as visit_date,p3 as people from cte1
--where p1>100 and p2>100 and p2>100 
