-- displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending).
SELECT city, AVG(value) AS average_temp FROM temperature
GROUP BY city
ORDER BY temperature DESC;
