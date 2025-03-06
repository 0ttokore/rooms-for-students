SELECT room_student as number_of_room, COUNT(*) AS student_count
    FROM Students
    GROUP BY room_student;

SELECT TOP (5) room_student as number_of_room, AVG(DATEDIFF(year, birthday_student, GETDATE())) AS avg_age
FROM Students
GROUP BY room_student
ORDER BY avg_age ASC;

SELECT TOP(5) room_student as number_of_room, MAX(DATEDIFF(year, birthday_student, GETDATE())) - MIN(DATEDIFF(year, birthday_student, GETDATE())) AS age_range
FROM Students
GROUP BY room_student
ORDER BY age_range DESC;

SELECT room_student as number_of_room
FROM Students
GROUP BY room_student
HAVING COUNT(DISTINCT sex) > 1;

