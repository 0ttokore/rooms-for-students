import json
from connection_with_the_database import SQLconnection


def query_JSON(mySQLServer, myDatabase, save_as, query):
    try:
        connection = SQLconnection(mySQLServer, myDatabase)

        with connection:
            with connection.cursor() as curs:
                curs.execute(query)
                rows = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]

                dct = [dict(zip(column_names, row)) for row in rows]

                with open(save_as, "w") as json_file:
                    json.dump(dct, json_file, ensure_ascii=False, indent=4)
                print(f"File saved as {save_as}.")

    except Exception as e:
        print("Exception:", e)
    finally:
        connection.close()
