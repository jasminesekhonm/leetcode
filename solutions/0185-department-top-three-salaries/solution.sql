/* Write your T-SQL query statement below */

select department, employee, salary from 
(select d.name as department, e.name as Employee, e.salary, dense_rank() over (partition by d.name order by salary desc) as rank
from Employee e join Department d
on e.departmentid=d.id)a 
where a.rank<=3
