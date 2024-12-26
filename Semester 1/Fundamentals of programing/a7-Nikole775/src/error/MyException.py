class RepositoryException(Exception):
    """
    This class implements the exceptions for the repository.
    """
    def __str__(self):
        return "There already exists a student with this id"

class Empty_history_exception(Exception):
    def __str__(self):
        return "the history is empty"

class InputError(Exception):
    def __str__(self):
        return "that was not an integer :("

class NotFound(Exception):
    pass