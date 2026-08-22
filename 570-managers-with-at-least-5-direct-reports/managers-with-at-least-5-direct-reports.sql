-- Write your PostgreSQL query statement below
SELECT e.name 
FROM Employee e
JOIN 
    (SELECT 
        managerId
    FROM Employee
        GROUP BY managerId
        HAVING count(*) >= 5) AS m
ON e.id = m.managerId