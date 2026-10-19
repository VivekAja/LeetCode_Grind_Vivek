# Write your MySQL query statement below
select c.name as Customers
    from Orders o
    right join Customers c on o.customerId = c.id
    where o.customerId is NULL;