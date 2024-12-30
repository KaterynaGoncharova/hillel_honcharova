from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import random

Base = declarative_base()

enrollment_table = Table(
    'enrollment', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary=enrollment_table, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship('Student', secondary=enrollment_table, back_populates='courses')

engine = create_engine('sqlite:///students.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def initialize_data():
    courses = [Course(title=f"Course {i+1}") for i in range(5)]
    students = [Student(name=f"Student {i+1}") for i in range(20)]
    session.add_all(courses)
    session.commit()

    for student in students:
        student.courses = random.sample(courses, random.randint(1, 3))
    session.add_all(students)
    session.commit()

def add_student(name, course_titles):
    student = Student(name=name)
    student.courses = session.query(Course).filter(Course.title.in_(course_titles)).all()
    session.add(student)
    session.commit()

def get_students_on_course(course_title):
    return [s.name for s in session.query(Student).join(enrollment_table).join(Course).filter(Course.title == course_title).all()]

def get_courses_for_student(student_name):
    return [c.title for c in session.query(Course).join(enrollment_table).join(Student).filter(Student.name == student_name).all()]

def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()

def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()

def main():
    initialize_data()
    add_student("New Student", ["Course 1", "Course 2"])
    print("Студенти на Course 1:", get_students_on_course("Course 1"))
    print("Курси для Student 5:", get_courses_for_student("Student 5"))
    update_student_name("Student 1", "Updated Student 1")
    delete_student("Student 2")

if __name__ == "__main__":
    main()