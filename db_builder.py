'''
Alessandro Cartegni
SoftDev1 pd7
HW09 -- No Treble
2017-10-16
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id, INTEGER)")

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO courses VALUES("' + row["code"] + '"," + row["mark"] + "," + row["id"] + ")")



c.execute("CREATE TABLE peeps(name TEXT, age INTEGER, id, INTEGER)")

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO courses VALUES("' + row["name"] + '"," + row["age"] + "," + row["id"] + ")")
        
#==========================================================
db.commit() #save changes
db.close()  #close database


