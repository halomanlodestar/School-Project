import os
import csv
from modules.logs import writeLog, readLog
from modules.user import writeUser
from modules.user import User
from modules.staticFunctions import printDatabase, printRows

Errors = User.Errors

class __Admin:
  _user = None

  def __init__(self, id:int, passwd:str, user:User) -> None:
    self._user = user
    writeLog("Someone logged in as Admin")

  def proceed(self) -> None:
    while True:
      menuChoice = int(input('''
            *** Admin Menu ***
      1. Query data from SQL server
      2. Get Login history
      3. User Black List
      4. Switch host
      5. Exit Admin Dashboard
      '''))
      
      if menuChoice == 1 and self._user:
        try:
          db = None
          while True:
            printDatabase(self._user.getDatabases())
            db = str(input("\nPlease choose a database : "))
            self._user.setDatabase(db)
            break
          while True:
            try:
              query = str(input("Enter a query : "))
              if (query.lower() == "exit"): break
              printRows(self._user.query(query))
              
            except Errors.InvalidSQLQueryError:
              print("Invalid Query")

        except Errors.InvalidSQLQueryError:
              print("Invalid Database")

      if menuChoice == 2:
        dirList = os.listdir("./.admin")
        fileName = str(input(dirList.__str__() + "\nSelect a file : "))

        while True:
          try:
            open("./.admin/" + fileName + ".csv", "r")
            file = readLog(fileName)
            
            for row in file:
              if row:
                [user, time, status] = row
                print(user + " | " + time + " | " + status)
            input("Enter to continue...")
            break

          except FileNotFoundError:
            print("There is no such file")

      if menuChoice == 4 and self._user:
        while True:
          host = str(input("Enter new hostname : "))
          self._user.switchHost("")
          if self._user.connection:
            print("Connection established Successfully")
            pass
          else: print("Invalid Host")

      if menuChoice == 5: break
 
def matchData():
  
  try:
    adminID = int(input("Enter Admin ID : "))
    adminPasswd = str(input("Enter Password : "))
    adminData = open("./.admin/adminUsers.csv", "r")
    reader = csv.reader(adminData)


    for row in reader:
      if (int(adminID) == int(row[0]) and str(adminPasswd) == str(row[1])):
        while True:
            try:
              user = str(input("Enter Username : "))
              passwd = str(input("Enter Password : "))
              ur = User(username=user, password=passwd)
              break
            except Errors.InvalidUserError:
              print("Invalid Username or Password")
        return __Admin(adminID, adminPasswd, ur)

  except ValueError:
    print("Admin ID must be a password")

  return False
  