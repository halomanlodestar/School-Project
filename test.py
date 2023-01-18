import mysql.connector as sql
import shutil
import os

def cloneDatabase(initial:str, final:str = ""):
  cn = sql.connect(host="localhost", user="root", passwd="admin", database=initial)
  cur = cn.cursor()
  cur.execute("show tables")
  [tables] = cur.fetchall()
  for table in tables:
    cur.execute("select * from " + table)
    data = cur.fetchall()[0]
    print(data)
    inTypes = [type(data[0]), type(data[1]), type(data[2])]
    outTypes = []

    for typ in inTypes:
      if typ == int:
        outTypes.append("int")
      if typ == str:
        outTypes.append("varchar")
      if typ == float:
        outTypes.append("double")

def copyDatabase(initial:str, final:str):
  cn = sql.connect(host="localhost", user="root", passwd="admin")
  cur = cn.cursor()
  cur.execute(r"SHOW VARIABLES WHERE Variable_Name LIKE '%dir'")
  for vars in cur.fetchall():
    if vars[0] == "datadir":
      # print(os.listdir(vars[1] + initial))
      # shutil.copyfile(vars[1] + initial)
      #os.mkdir(vars[1] + final)
      for table in os.listdir(vars[1] + initial):
        shutil.copyfile(vars[1] + initial + "/" + table, vars[1] + final + "/" + table)

copyDatabase("kunal", "garv")