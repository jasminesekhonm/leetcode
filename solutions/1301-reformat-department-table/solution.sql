/* Write your T-SQL query statement below */


select id, 
jan as Jan_Revenue,
feb as Feb_revenue,
mar as Mar_Revenue,
apr as Apr_revenue,
may as May_Revenue,
jun as Jun_Revenue,
jul as Jul_Revenue,
aug as Aug_revenue,
sep as Sep_Revenue,
oct as Oct_revenue,
nov as Nov_Revenue,
dec as Dec_Revenue
from ( select * from department
)a 
pivot(sum(revenue) for month in (jan, feb,mar,apr, may, jun, jul, aug, sep, oct, nov, dec ))p
