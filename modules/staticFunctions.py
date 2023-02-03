def printDatabase(databases):
    for database in databases:
        print(database, end = " | ")
    pass

def printTables(tables):
    for [row] in tables:
        print(row, end=" | ")
    pass

def printRows(rows):
    for row in rows:
        print(row)
    pass