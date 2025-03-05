from data_extraction import data_extraction_from_git_hub
from data_load_from_JSON import data_load
from data_upload_to_the_database import data_upload
from queries.query_rooms_and_number_of_students import Query_Rooms_Students
from queries.query_5_rooms_with_min_age import Query_5_Rooms_min_age
from queries.query_5_rooms_with_max_age import Query_5_Rooms_max_age
from queries.query_rooms_with_2_genders import Query_rooms_with_genders


def main():
    # data extraction
    url_1 = "https://raw.githubusercontent.com/0ttokore/rooms-for-students/refs/heads/main/rooms.json"
    url_2 = "https://raw.githubusercontent.com/0ttokore/rooms-for-students/refs/heads/main/students.json"

    dir_name = "C:/python_projects/work/rooms_for_students/data/"

    data_extraction_from_git_hub(url_1, dir_name + "rooms.json")
    data_extraction_from_git_hub(url_2, dir_name + "students.json")

    # data load from JSON
    rooms_data = data_load(dir_name + "rooms.json")
    students_data = data_load(dir_name + "students.json")

    # establishing connection to the database
    mySQLServer = "DESKTOP-4AC274M\\SQLEXPRESS"
    myDatabase = "rooms_for_students"

    # data upload to the database
    data_upload(mySQLServer, myDatabase, rooms_data, students_data)

    # queries
    doc_type = "json"

    Query_Rooms_Students(
        mySQLServer, myDatabase, dir_name + f"result_of_query_1.{doc_type}", doc_type
    )
    Query_5_Rooms_min_age(
        mySQLServer, myDatabase, dir_name + f"result_of_query_2.{doc_type}", doc_type
    )
    Query_5_Rooms_max_age(
        mySQLServer, myDatabase, dir_name + f"result_of_query_3.{doc_type}", doc_type
    )
    Query_rooms_with_genders(
        mySQLServer, myDatabase, dir_name + f"result_of_query_4.{doc_type}", doc_type
    )


if __name__ == "__main__":
    main()
