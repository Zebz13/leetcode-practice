# Write your MySQL query statement below
select sg.user_id, round(sum(case when action = 'confirmed' then 1 else 0 end)/(count(*)),2) as confirmation_rate from confirmations cf
right join signups sg on cf.user_id = sg.user_id
group by sg.user_id
