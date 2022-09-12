/* Write your T-SQL query statement below */


select id, case when id% 2!=0 then lead(student,1,student) over (order by id asc)
else lag(student,1, student) over (order by id asc) end as student
from seat
