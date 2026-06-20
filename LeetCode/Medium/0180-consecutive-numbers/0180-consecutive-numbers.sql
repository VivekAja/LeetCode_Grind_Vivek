# Write your MySQL query statement below
with cte as(
    select num,
    lead(num, 1) over (order by id) as nextnum,
    lead(num, 2) over (order by id) as nextnextnum
    from Logs
)
select distinct num as ConsecutiveNums
from cte
where num = nextnum and num = nextnextnum;
