
from ui.ui import Ui
from repository.Repo import Repository
from repository.TextFileRepo import TextFileRepo
from repository.BinaryFileRepo import BinaryRepo
from services.service import Services
import os
print(os.getcwd())
def get_repo():
    with open("setting.properties", "r") as settings_file:
        for line in settings_file:
            line = line.strip()
            if line.startswith("REPOSITORY="):
                repository_type = line[len("REPOSITORY="):]
                if repository_type == "memory":
                    return Repository()
                elif repository_type == "text":
                    return TextFileRepo("students.txt")
                elif repository_type == "binary":
                    return BinaryRepo("students.bin")
                else:
                    raise ValueError("Invalid repository type!")
            else:
                raise ValueError("Invalid settings file!")

if __name__ == "__main__":
    repository = get_repo()
    services = Services(repository)
    ui = Ui(services)
    ui.start()
