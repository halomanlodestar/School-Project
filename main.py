import datetime
from modules.logs import writeLog
from modules.logs import writeUser
from modules.login import User
from modules.admin import Admin
from modules.admin import matchData
 
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
                  db = str(input(str(self.ur.getDatabases()) + "\nSelect a database : "))
                  self.ur.setDatabase(db)
                  writeUser(self.name ,datetime.datetime.now().strftime("%H:%M:%S"), "logged in")
                  print("Successfully Logged in as Guest")
                  break
                
                except Errors.InvalidDataBaseError:
                  print("Invalid Database")
            
          except Errors.InvalidUserError:
            print("Invalid Username or Password")

          while True:
            menuChoice = int(input('''
                  *** Guest Menu ***
            1. Fetch Data
            2. Choose new database
            3. Back
            '''))

            if menuChoice == 1:
              while True:
                try:
                  print(self.ur.query("SHOW TABLES"))
                  table = str(input("Choose a table : "))
                  if table.lower() == "exit": break
                  print(self.ur.query("SELECT * FROM " + table))
                except Errors.InvalidSQLQueryError:
                    print("Please choose a valid table")

            if menuChoice == 2:
              while True:
                try:
                  db = str(input(str(self.ur.getDatabases()) + "\nSelect a database : "))
                  self.ur.setDatabase(db)
                  print("Successfully selected new Database")
                  break
                except Errors.InvalidDataBaseError:
                  print("Invalid Database")

            if menuChoice == 3:
              break
          break
      
      if mainMenuChoice == 2:
        while True:
          try:
            user = str(input("Enter Username : "))
            self.name = user
            passwd = str(input("Enter Password : "))
            self.ur = User(username=user, password=passwd)
            while True:
              try:
                db = str(input(str(self.ur.getDatabases()) + "\nSelect a database : "))
                self.ur.setDatabase(db)
                writeUser(self.name ,datetime.datetime.now().strftime("%H:%M:%S"), "logged in")
                print("Successfully Logged in as Guest")
                break

              except Errors.InvalidDataBaseError:
                print("Invalid Database")
        
          except Errors.InvalidUserError:
            print("Invalid Username or Password")

          while True:
            menuChoice = int(input('''
                  *** Employee Menu ***
            1. Query mySQL
            2. Choose new database
            3. Back
            '''))

            if menuChoice == 1:
              while True:
                try:
                  query = str(input("Enter a valid mySQL query : "))
                  if (query.lower() == "exit"): break
                  print(self.ur.query(query))
                except Errors.InvalidSQLQueryError:
                    print("Invalid Syntax, please execute a valid mySQL query")

            if menuChoice == 2:
              while True:
                try:
                  db = str(input(str(self.ur.getDatabases()) + "\nSelect a database : "))
                  self.ur.setDatabase(db)
                  print("Successfully selected new Database")
                  break
                except Errors.InvalidDataBaseError:
                  print("Invalid Database")

            if menuChoice == 3:
              break

      if mainMenuChoice == 3:
        admin = matchData()
        if (admin):
          admin.proceed()

class Gui:
  def __init__(self) -> None:
    pass

Console()
