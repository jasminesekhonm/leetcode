/* Write your T-SQL query statement below */

select department, employee, salary from 
(select e.name as employee,e.salary,d.name as department,  dense_Rank() over(partition by d.name order by salary desc) as rank
from employee e join department d 
on e.departmentId=d.id)a
where rank<4

