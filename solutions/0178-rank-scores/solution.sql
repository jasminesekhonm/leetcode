/* Write your T-SQL query statement below */
select score, dense_Rank() over(order by score desc) as rank
from scores
