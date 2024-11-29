# Write your MySQL query statement below
select round((sum(case when order_date = c_date then 1 else 0 end)/count(*))*100,2) as immediate_percentage from 
(select delivery_id,customer_id,order_date,customer_pref_delivery_date as c_date, 
rank() over (partition by customer_id order by order_date) as rn
from delivery) t where rn=1 ;