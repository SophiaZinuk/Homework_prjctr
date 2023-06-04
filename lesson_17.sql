CREATE TABLE  student (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE subject (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE student_subject (
    id serial PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES student (id),
    FOREIGN KEY (subject_id)
        REFERENCES subject (id)
)

 INSERT INTO student VALUES (1, 'Bae', 18), (2, 'Eddy', 21), (3, 'Lily', 22), (4, 'Jenny', 19);
 
--  INSERT INTO student (name, age) VALUES ('Bae', 18), ('Eddy', 21), ('Lily', 22), ('Jenny', 19);

INSERT INTO subject (name) VALUES ('English'), ('Math'), ('Spanish'), ('Ukrainian');

INSERT INTO student_subject (student_id, subject_id) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (1, 3);

-- SELECT student.name, subject.name
-- FROM student
-- INNER JOIN student_subject ON student_subject.student_id = student.id
-- INNER JOIN subject ON subject.id = student_subject.subject_id
-- WHERE subject.name = 'English'





















