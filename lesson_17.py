import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="TestDB",
    user="postgres",
    password="postgresNik")

cur = conn.cursor() 
cur.execute('SELECT * FROM apartment')
# north_region = cur.fetchall()
# print(north_region)
# print(cur.fetchmany(3))

cur.execute("SELECT student.name FROM student INNER JOIN student_subject ON student_subject.student_id = student.id INNER JOIN subject ON subject.id = student_subject.subject_id WHERE subject.name = 'English'")
print(cur.fetchall())