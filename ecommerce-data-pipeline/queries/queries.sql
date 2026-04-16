SELECT COUNT(*) FROM raw_events;

SELECT event_type, COUNT(*) 
FROM raw_events
GROUP BY event_type;

SELECT brand, SUM(price)
FROM raw_events
WHERE event_type='purchase'
GROUP BY brand
ORDER BY SUM(price) DESC
LIMIT 10;