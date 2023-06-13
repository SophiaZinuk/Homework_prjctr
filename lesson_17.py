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
# print(cur.fetchall())

import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student' # звязати з таблиці

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return f'This is a student {self.name}. Age: {self.age}'
    
    def __repr__(self):
        return f'This is a student {self.name}. Age: {self.age}'
    

class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Student_Subject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("student.id"))
    subject_id = Column(Integer, ForeignKey("subject.id"))


DATABASE_URL= 'postgresql://postgres:postgresNik@localhost:5432/TestDB'

engine = create_engine(
    DATABASE_URL.format(
        host='localhost',
        database='TestDB',
        user="postgres",
        password='postgresNik',
        port = 5432
    )
)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

session.close()


# second = session.query(Student, Subject, Student_Subject).\
#     select_from(Student).join(Subject).join(Student_Subject).all()
# for student, subject, student_subject in second:
#     print(Student.name)

results = session.query(Student.name).join(Student_Subject).join(Subject).\
    filter(Subject.name == 'English')
for result in results:
    print(result)

# first_student = session.query(Student_Subject)

# Find all students` name that visited 'English' classes


