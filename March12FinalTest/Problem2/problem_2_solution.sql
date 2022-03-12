select d.name,
		e.name,
		e.salary
from department d left join employee e
on e.departmentId = d.id
where e.salary in
	((select distinct salary
	from employee
	where departmentid = 1
	order by salary desc limit 3)
	union all
	(select distinct salary from employee
	where departmentid = 2
	order by salary desc limit 3))
order by d.name;