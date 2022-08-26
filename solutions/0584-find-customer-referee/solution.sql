/* Write your T-SQL query statement below */
select name
from Customer c 
where coalesce(referee_id,99) <> 2;
