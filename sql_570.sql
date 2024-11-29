# Write your MySQL query statement below
with sql1 as (select managerId,count(managerId) as c_mid from employee where managerId is not null group by managerId)

select em.name from employee em left join sql1 sq
on sq.managerId = em.id where c_mid>=5