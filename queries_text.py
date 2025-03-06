queries = {
    "query_1": """
                SELECT TOP(5) room_student as number_of_room, MAX(DATEDIFF(year, birthday_student, GETDATE())) - MIN(DATEDIFF(year, birthday_student, GETDATE())) AS age_range
                FROM Students
                GROUP BY room_student
                ORDER BY age_range DESC;
                """,
    "query_2": """
                SELECT TOP (5) room_student as number_of_room, AVG(DATEDIFF(year, birthday_student, GETDATE())) AS avg_age
                FROM Students
                GROUP BY room_student
                ORDER BY avg_age ASC;
                """,
    "query_3": """
                SELECT room_student as number_of_room, COUNT(*) AS student_count
                FROM Students
                GROUP BY room_student;
                """,
    "query_4": """
                SELECT room_student as number_of_room
                FROM Students
                GROUP BY room_student
                HAVING COUNT(DISTINCT sex) > 1;
                """,
}
