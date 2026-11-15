# custom exception used when a requested cargo item cannot be found in the station
class CargoNotFoundError(Exception):
    pass

# custom exception used when trying to add a cargo item that already exists
class DuplicateCargoError(Exception):
    pass

# raise the given exception type with the given message when condition is True, otherwise just return the text
def checkForRaise(text, condition, error, exception_type=ValueError):
    if condition:
        raise exception_type(error)
    return text
