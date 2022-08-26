CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
    select distinct salary from     
    (select salary,dense_rank() over(order by salary desc) as drank
    from employee e)a where drank=@N
        
    );
END
