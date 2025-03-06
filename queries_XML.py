import xml.etree.ElementTree as ET
from connection_with_the_database import SQLconnection


def query_XML(mySQLServer, myDatabase, save_as, query):
    try:
        connection = SQLconnection(mySQLServer, myDatabase)

        with connection:
            with connection.cursor() as curs:
                curs.execute(query)
                rows = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]

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
        print("Exception:", e)
    finally:
        connection.close()
