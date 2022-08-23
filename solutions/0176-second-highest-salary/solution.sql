/* Write your T-SQL query statement below */


select isnull(max(Salary),null) as SecondHighestSalary from employee 
where salary <> (select max(salary) from employee)
