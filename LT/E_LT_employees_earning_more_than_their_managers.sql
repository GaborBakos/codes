/*
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.
*/

Select 
    ee.name as Employee
From Employee ee
Join Employee mm
on ee.ManagerId = mm.Id
Where ee.Salary > mm.Salary
