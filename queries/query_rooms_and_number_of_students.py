import json
import xml.etree.ElementTree as ET
from connection_with_the_database import SQLconnection


# Список комнат и количество студентов в каждой из них
def Query_Rooms_Students(mySQLServer, myDatabase, save_as, doc_type):
    try:
        connection = SQLconnection(mySQLServer, myDatabase)

        query = """
        SELECT room_student as number_of_room, COUNT(*) AS student_count
        FROM Students
        GROUP BY room_student;
        """

        with connection:
            with connection.cursor() as curs:
                curs.execute(query)
                rows = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]

                if doc_type == "json":
                    dct = [dict(zip(column_names, row)) for row in rows]

                    with open(save_as, "w") as json_file:
                        json.dump(dct, json_file, ensure_ascii=False, indent=4)
                    print(f"File saved as {save_as}.")

                if doc_type == "xml":
                    root = ET.Element("Query_Rooms_Students")

                    for row in rows:
                        row_element = ET.Element("row")
                        for col_name, col_value in zip(column_names, row):
                            col_element = ET.Element(col_name)
                            col_element.text = str(col_value)
                            row_element.append(col_element)
                        root.append(row_element)

                    with open(save_as, "w", encoding="utf-8") as xml_file:
                        tree = ET.ElementTree(root)
                        ET.indent(root, space="     ", level=0)
                        tree.write(save_as, encoding="utf-8", xml_declaration=True)
                    print(f"File saved as {save_as}.")

    except Exception as e:
        print("Connection error in Query_1:", e)
    finally:
        connection.close()
