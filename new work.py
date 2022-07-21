import csv
from cs50 import SQL 
open ('new.db','w').close()
database = SQL("sqlite:///new.db")

database.execute("CREATE TABLE students(student_id INTEGER PRIMARY KEY, student_name TEXT, adress TEXT, room_number INTEGER)")

database.execute("CREATE TABLE course(course_id INTEGER PRIMARY KEY, cgpa TEXT, INTEGER, marks INTEGER, course_name TEXT)")

database.execute("CREATE TABLE date(date_id INTEGER PRIMARY KEY, starting_date INTEGER, ending_date TEXT)")

database.execute("CREATE TABLE relations(student_id INTEGER, course_id INTEGER, date_id INTEGER, FOREIGN KEY(student_id) REFERENCES students(student_id), FOREIGN KEY(course_id) REFERENCES course(course_id), FOREIGN KEY(date_id) REFERENCES date(date_id))")

with open ('Book1.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      student_name = row['student_name']
      adress = row['Adress']
      room_number = row['Room number']
      cgpa= row['CGPA']
      marks = row['Marks']
      course_names= row['course']
      starting_date = row['starting_date']
      ending_date = row['ending date']
        
      database.execute("INSERT INTO students(student_name,adress,room_number) VALUES(?,?,?)",student_name,adress,room_number,)
      database.execute("INSERT INTO course(cgpa,marks,course_name) VALUES(?,?,?)", cgpa,marks,course_names)
      database.execute("INSERT INTO date(starting_date,ending_date) VALUES(?,?)", starting_date,ending_date)
      database.execute("INSERT INTO relations(student_id,course_id,date_id) VALUES((SELECT student_id FROM students WHERE student_name=?),(SELECT course_id FROM course WHERE marks=?),(SELECT date_id FROM date WHERE starting_date=?))",student_name, marks, starting_date)