import datetime
from modules.logs import writeLog, writeUser
from modules.user import User
from modules.admin import matchData
from modules.staticFunctions import printDatabase, printRows, printTables

Errors = User.Errors

class Console:
  def __init__(self) -> None:
    ur = None
    name = ""
    while True:
      mainMenuChoice = int(input('''
              *** Main Menu ***
      1. Login as Guest
      2. Login as Employee
      3. Login as Admin
      4. Exit
      '''))

      if (mainMenuChoice == 1):
        while True:
          try:
            user = str(input("Enter Username : "))
            self.name = user
            passwd = str(input("Enter Password : "))
            self.ur = User(username=user, password=passwd)
            if (self.ur.connection):
              while True:
                try:
                    printDatabase(self.ur.getDatabases())
                    
                    db = str(input("\nSelect a database : "))
                    self.ur.setDatabase(db)
                    writeUser(self.name ,datetime.datetime.now().strftime("%H:%M:%S"), "logged in")
                    print("Successfully Logged in as Guest")
                    break
                
                except Errors.InvalidDataBaseError:
                  print("Invalid Database")
            break
          except Errors.InvalidUserError:
            print("Invalid Username or Password")

        while True:
          menuChoice = int(input('''
                *** Guest Menu ***
          1 - Fetch All Data
          2 - Search User by ID
          4 - Choose new database
          5 - Back
          '''))

          if menuChoice == 1:
            while True:
              try:
                tables = self.ur.query("SHOW TABLES")
                if tables:
                  printTables(tables)
                  pass
                else: print("No table found")
                table = str(input("\nChoose a table : ")) if tables else "exit"
                if table.lower() == "exit": break
                printRows(self.ur.query("SELECT * FROM " + table))
              except Errors.InvalidSQLQueryError:
                  print("Please choose a valid table")
            continue

          if menuChoice == 2:
            choice = "Y"
            while choice.upper() == "Y":
              id = str(input("Enter ID to be seached : "))
              table = str(input("Enter the name of the Table : "))
              print(self.ur.searchUserByID(id, table))
              choice = str(input("Do you want to search another record? (Y/N) : "))[0]
            pass
            continue

          if menuChoice == 4:
            while True:
              try:
                printDatabase(self.ur.getDatabases()) 
                db = str(input(str("\nSelect a database : ")))
                self.ur.setDatabase(db)
                print("Successfully selected new Database")
                break
              except Errors.InvalidDataBaseError:
                print("Invalid Database")

          else: break
      
      if mainMenuChoice == 2:
        while True:
          try:
            user = str(input("Enter Username : "))
            self.name = user
            passwd = str(input("Enter Password : "))
            self.ur = User(username=user, password=passwd)
            while True and self.ur.connection:
              try:
                printDatabase(self.ur.getDatabases())
                db = str(input("\nSelect a database : "))
                self.ur.setDatabase(db)
                writeUser(self.name ,datetime.datetime.now().strftime("%H:%M:%S"), "logged in")
                print("Successfully Logged in as Guest")
                break

              except Errors.InvalidDataBaseError:
                print("Invalid Database")
            break
          except Errors.InvalidUserError:
            print("Invalid Username or Password")

        while True:
          menuChoice = int(input('''
                *** Employee Menu ***
          1 - Fetch  all Data
          2 - Search User by ID
          4 - Insert Data
          5 - Update a user
          6 - Choose new database
          7 - Back
          '''))

          if menuChoice == 1:
            while True:
              try:
                table = str(input("Enter the name of the table : "))
                if (table.lower() == "exit"): break
                print(self.ur.fetchAllData(table))
              except Errors.InvalidSQLQueryError or TypeError:
                  print("Invalid Syntax, please execute a valid mySQL query")

          if menuChoice == 2:
            while True:
              pass

          if menuChoice == 6:
            while True:
              try:
                printDatabase(self.ur.getDatabases())
                db = str(input("\nSelect a database : "))
                self.ur.setDatabase(db)
                print("Successfully selected new Database")
                break
              except Errors.InvalidDataBaseError or TypeError:
                print("Invalid Database")

          else:
            break

      if mainMenuChoice == 3:
        admin = matchData()
        if (admin):
          admin.proceed()

      if mainMenuChoice == 4:
        exit()

class Gui:
  def __init__(self) -> None:
    pass

Console()
