/* Write your T-SQL query statement below */


select 
Department,Employee,Salary
from
(select salary, e.name as Employee, dense_Rank() over(partition by departmentID order by salary desc ) as drank, d.name as Department
from department d  join employee e 
on d.id=e.departmentId )a
where drank=1

