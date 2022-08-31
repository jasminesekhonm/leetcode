/* Write your T-SQL query statement below */

select e1.name
from employee e join employee e1
on e.managerId=e1.id
group by e1.name
having count(*)>4;

