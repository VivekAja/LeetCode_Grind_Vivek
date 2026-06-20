# Write your MySQL query statement below
WITH clean_trips AS (
    SELECT t.request_at, t.status
    FROM Trips t
    JOIN Users c ON c.users_id = t.client_id -- join client
    JOIN Users d ON d.users_id = t.driver_id -- join driver
    WHERE c.banned = 'No'
      AND d.banned = 'No'
      AND t.request_at BETWEEN "2013-10-01" AND "2013-10-03"
)
SELECT 
    request_at AS Day,
    ROUND(
        SUM(IF(status LIKE 'cancelled%', 1, 0)) / COUNT(*),
        2
    ) AS `Cancellation Rate`
FROM clean_trips
GROUP BY request_at;