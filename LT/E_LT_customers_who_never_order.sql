/*
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.
*/


Select 
    cc.Name as Customers
From Customers cc
Where cc.Id not in (Select CustomerId
                    From Orders)



--or
Select
    cc.Name as Customers
From Customers cc
Left Join Orders oo
On cc.Id = oo.CustomerId
Where oo.CustomerId is Null                
