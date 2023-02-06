import datetime
from typing import Any
from modules.logs import writeLog, writeUser
import mysql.connector as sql

class User:
  host = "localhost"
  connection = sql.connect()
  _database = None
  __username = None
  __password = None
  def __init__(self, username:str, password:str):
    self.__username = username
    self.__password = password

    try:
      self.connection = sql.connect(host=self.host, user=username, passwd=password)
    except sql.ProgrammingError:
      raise self.Errors.InvalidUserError("Invalid Username or Password")

  # Returns a list of databases
  def getDatabases(self):
    if (self.connection != None):
      cur = self.connection.cursor()
      cur.execute("SHOW DATABASES;")
      data: Any = cur.fetchall()
      return [database for [( database )] in data]
    
  def switchHost(self, hostname):
    self.host = hostname
    self.connection = sql.connect(
      host=self.host,
      user=self.__username,
      passwd=self.__password
      )
    pass

  # Inputs a valid database and creates a new connection with that database
  # If database is invalid, throws "InvalidDatabaseError"
  def setDatabase(self, database:str) -> None:
    self._database = database
    try:
      self.connection = sql.connect(host=self.host, user=self.__username, passwd=self.__password, database=self._database)
    except sql.ProgrammingError:
      raise self.Errors.InvalidDataBaseError("Invalid Database")

  # Inputs ID to be searched and the name of the table to be searched in
  def searchUserByID(self, id:str, table:str):
    cur = self.connection.cursor()
    cur.execute("SELECT * FROM {} WHERE no = {}".format(table, id))
    return cur.fetchall()

  def fetchAllData(self, table:str):
    cur = self.connection.cursor()
    cur.execute("SELECT * FROM " + table)
    return cur.fetchall() if cur.fetchall() else []
  
  def updateUser(self, table:str, id:str, data:dict):
    cur = self.connection.cursor()
    cur.execute("UPDATE {} SET name = '{}', zone = '{}' grade = '{}' WHERE eno = {}".format(table, data["name"], data["zone"], data["grade"], id))
    self.connection.commit()
    pass
  
  # Takes a mySQL query in the string format as Input
  # Returns a valid output from my mysql (mostly lists)
  def query(self, query:str):
    try:
      if (self.connection):
        cur = self.connection.cursor()
        cur.execute(query)
        writeUser(str(self.__username), datetime.datetime.now().strftime("%H:%M:%S"), "Query : " + query)
        return cur.fetchall() # if cur.fetchall() else []
    except sql.ProgrammingError:
        raise self.Errors.InvalidDataBaseError("No database selected") if (self._database == None) else self.Errors.InvalidSQLQueryError("Invalid Query")

  # Errors
  class Errors:
    class InvalidUserError(Exception):
      def __init__(self, *args: object) -> None:
        super().__init__(*args)
        # print(Exception)
        writeLog("Invalid User Error faced\n")
    class InvalidDataBaseError(Exception):
      def __init__(self, *args: object) -> None:
        super().__init__(*args)
        # print(Exception)
        writeLog("Invalid Database Error faced\n")
    class UnknownError(Exception):
      def __init__(self, *args: object) -> None:
        super().__init__(*args)
        # print(Exception)
        writeLog("An Unknown Error occured\n")
    class InvalidSQLQueryError(Exception):
      def __init__(self, *args: object) -> None:
        super().__init__(*args)
        # print(Exception)
        writeLog("An Invalid SQL query executed")