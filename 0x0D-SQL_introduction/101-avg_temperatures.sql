-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) AS 'avg_tem' FROM temperatures GROUP BY 1 ORDER BY avg_tem DESC;
