import pyodbc


def SQLconnection(mySQLServer, myDatabase):
    try:
        return pyodbc.connect(
            "Driver={SQL Server};"
            "Server=" + mySQLServer + ";"
            "Database=" + myDatabase + ";"
            "Trusted_Connection=yes;"
        )
    except Exception as e:
        print("Connection error:", e)
