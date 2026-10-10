# Write your MySQL query statement below

SELECT
    visited_on,
    amount,
    average_amount
FROM (
    SELECT
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(
            AVG(daily_amount) OVER (
                ORDER BY visited_on
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ),
            2
        ) AS average_amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
    FROM (
        SELECT
            visited_on,
            SUM(amount) AS daily_amount
        FROM Customer
        GROUP BY visited_on
    ) AS daily
) AS result
WHERE rn >= 7
ORDER BY visited_on;
