select dept.name as Department, a.name as Employee, a.salary as Salary from 
(select name, salary, departmentId, dense_rank() over (partition by departmentid order by salary desc) as rn_no from Employee)a
left join
department dept 
on  dept.id = a.departmentId
where a.rn_no<=3;