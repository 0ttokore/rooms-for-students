from datetime import datetime
from connection_with_the_database import SQLconnection


def data_upload(mySQLServer, myDatabase, rooms_data, students_data):
    try:
        connection = SQLconnection(mySQLServer, myDatabase)

        with connection:
            with connection.cursor() as curs:
                for room in rooms_data:
                    curs.execute(
                        "IF NOT EXISTS (SELECT * FROM dbo.Rooms WHERE Id_room = ?) "
                        "INSERT INTO dbo.Rooms (Id_room, name_room) VALUES (?, ?)",
                        room["id"],
                        room["id"],
                        room["name"],
                    )

        with connection:
            with connection.cursor() as curs:
                for student in students_data:
                    curs.execute(
                        "IF NOT EXISTS (SELECT * FROM dbo.Students WHERE Id_student = ?) "
                        "INSERT INTO dbo.Students (birthday_student, Id_student, name_student, room_student, sex) VALUES (?, ?, ?, ?, ?)",
                        student["id"],
                        datetime.fromisoformat(student["birthday"]),
                        student["id"],
                        student["name"],
                        student["room"],
                        student["sex"],
                    )

    except Exception as e:
        print("Connection error in data upload:", e)
    finally:
        connection.commit()
        connection.close()
