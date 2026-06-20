# Write your MySQL query statement below
WITH filtered AS (
    -- Step 1 & 2: filter people >= 100, assign row number
    SELECT id, visit_date, people,
           ROW_NUMBER() OVER (ORDER BY id) AS rn
    FROM Stadium
    WHERE people >= 100
),
grouped AS (
    -- Step 3: compute the island group key
    SELECT id, visit_date, people,
           id - rn AS grp
    FROM filtered
),
valid_groups AS (
    -- Step 4: keep only groups with 3 or more rows
    SELECT grp
    FROM grouped
    GROUP BY grp
    HAVING count(*) >= 3
)
-- Step 5: return matching rows
SELECT g.id, g.visit_date, g.people
FROM grouped g
JOIN valid_groups vg ON vg.grp = g.grp
ORDER BY g.id;