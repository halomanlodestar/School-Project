import os
import csv
from modules.logs import writeLog, readLog
from modules.login import writeUser
from modules.login import User

Errors = User.Errors

class Admin:
  _user = None

  def __init__(self, id:int, passwd:str, user:User) -> None:
    self._user = user
    writeLog("Someone logged in as Admin")
    pass

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
            db = str(input(str([self._user.getDatabases()]) + "\nPlease choose a database : "))
            self._user.setDatabase(db)
            break
          while True:
            try:
              query = str(input("Enter a query : "))
              print(self._user.query(query))
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
            for [row] in file:
              print(row)
          except FileNotFoundError:
            print("There is no such file")
 
def matchData():
  
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
      return Admin(adminID, adminPasswd, ur)
  return False