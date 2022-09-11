/* Write your T-SQL query statement below */

with cte1 as (
select accepter_id, count(requester_id ) as requests_acc
from RequestAccepted ra
group by accepter_id 
), 
cte2 as (
select  requester_id, count(requester_id) as requests_sent
    from RequestAccepted 
    group by requester_id
)
select top 1 requester_id as id, coalesce(requests_acc,0)+coalesce(requests_sent,0) as num 
from cte1 c1 full outer join cte2 c2
on c1.accepter_id=c2.requester_id
order by num desc
