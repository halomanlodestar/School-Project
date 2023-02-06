import datetime
import csv
import os

logs = open("logs.txt", "w")
logs.write("session started at - " + datetime.datetime
           .now()
           .strftime("%H:%M:%S"))
logs = open("logs.txt", "a")

A_logs = open("./.admin/" + datetime.datetime
              .now()
              .strftime("%d-%m-%y") + ".csv", "a")
adminLogs = csv.writer(A_logs)
# adminLogs.writerow(["NAME", "TIME", "ACTIVITY"])

def writeLog(output:str):
  try:
    logs.write(output)
  except FileNotFoundError:
    print("file not found")

def writeUser(name:str, time:str, activity:str):
  try:
    adminLogs.writerow([name, time, activity])
  except FileNotFoundError:
    print("file not found")

def readLog(name:str) -> list[list[str]]:
  try:
    print(os.getcwd() + "/.admin/" + name + ".csv", "r")
    file = open(os.getcwd() + "/.admin/" + name + ".csv", "r")
    rows = csv.reader(file)
    out = [row for row in rows]
    return out
  except FileNotFoundError:
    print("file not found")
    return []
