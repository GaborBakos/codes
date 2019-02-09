/*
The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.
*/

Select
    dd.Name AS Department,
    ee.Name AS Employee,
    ee.Salary
from
	Employee ee,
	Department dd
Where ee.DepartmentId = dd.id
And (DepartmentId, Salary) in
  (Select e2.DepartmentId, max(e2.Salary) as max From Employee e2 Group by e2.DepartmentId)


