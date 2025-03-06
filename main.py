from data_extraction import data_extraction_from_git_hub
from data_load_from_JSON import data_load
from data_upload_to_the_database import data_upload
import queries_text
from queries_JSON import query_JSON
from queries_XML import query_XML


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

    valid_doc_types = {"json", "xml"}
    valid_queries = {"query_1", "query_2", "query_3", "query_4"}

    while (doc_type := input("Enter doc_type ('json' or 'xml') or 'exit': ")) != "exit":
        if doc_type in valid_doc_types:
            while (query := input("Enter query_N (1-4) or 'exit': ")) != "exit":
                if query in valid_queries:
                    if doc_type == "json":
                        query_JSON(
                            mySQLServer,
                            myDatabase,
                            dir_name + "result_of_query.json",
                            queries_text.queries[query],
                        )
                    elif doc_type == "xml":
                        query_XML(
                            mySQLServer,
                            myDatabase,
                            dir_name + "result_of_query.xml",
                            queries_text.queries[query],
                        )
                else:
                    print("No such query.")
        else:
            print("No such doc type.")


if __name__ == "__main__":
    main()
