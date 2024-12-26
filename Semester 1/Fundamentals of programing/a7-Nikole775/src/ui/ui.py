from src.error.MyException import Empty_history_exception, RepositoryException, InputError,NotFound
from src.services.service import Services
class Ui:
    def __init__(self, services: Services):
        self.__services = services
    def menu(self):
        print("_______________________________________________________________________________________________________")
        print("1.Add a student")
        print("2.Display the students")
        print("3.Filter the list so that students in a given group (read from the console) are deleted from the list.")
        print("4.Undo")
        print("_______________________________________________________________________________________________________")

    def get_input (self, txt="->"):
        return input(txt)

    def chose_option(self, option):
        if option == "1":
            self.add_student_ui()
        elif option == "2":
            self.display_students()
        elif option == "3":
            self.filter_students()
        elif option == "4":
            self.undo()
        else:
            print("bad command!")

    def add_student_ui(self):
        try:
            id_ = self.get_input("Id: ")
            self.__services.verify_data(id_)
            name = self.get_input("Name: ")
            group = self.get_input("Group: ")
            self.__services.verify_data(group)
            try:
                self.__services.add_student_services(id_, name, group)
            except RepositoryException as ve:
                print(ve)
        except InputError as ve:
            print(ve)


    def display_students(self):
        print(self.__services.display_students())

    def filter_students(self):
        try:
            group = self.get_input("group:")
            self.__services.verify_data(group)
            print(self.__services.filter_students_by_group(group))
        except InputError as ve:
            print(ve)

    def undo(self):
        try:
            self.__services.undo_services()
        except Empty_history_exception as ve:
            print(ve)
    def start(self):
        while True:
            self.menu()
            user_input = self.get_input()
            self.chose_option(user_input)


