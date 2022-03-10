SELECT request_at AS "Day",
	  ROUND((SUM(CASE WHEN status = 'completed' THEN 0 ELSE 1 END )/CAST(COUNT(*) AS NUMERIC)),2) AS "Cancellation_rate"
FROM 
			(SELECT STATUS, request_at, u.banned AS "client_banned", uu.banned AS "driver_banned" FROM trips t
			LEFT JOIN users u
			ON t.client_id = u.users_id
			LEFT JOIN users uu
			ON t.driver_id = uu.users_id) AS new_table
			
WHERE new_table.client_banned = 'No' AND new_table.driver_banned = 'No'
GROUP BY request_at;