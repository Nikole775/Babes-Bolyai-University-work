"""aici is functiile basic"""
import random
from random import randint,choice
from src.domain.students import Student
from src.repository import Repo
from src.error.MyException import InputError


class Services:

    def __init__(self, repository: Repo):
        self.__repository = repository
        #self.generate_n_students()

    def add_student_services(self, id_, name, group):
        self.__repository.add_student(Student(id_, name, group))

    def verify_data(self, user_input):
        if not user_input.isdigit():
            raise InputError()
        return int(user_input)

    def display_students(self):
        return self.__repository.get_all_students()

    def filter_students_by_group(self, group):
        return self.__repository.delete_students_from_group(group)

    def undo_services(self):
        self.__repository.undo_command()

