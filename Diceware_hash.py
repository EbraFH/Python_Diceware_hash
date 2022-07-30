from random import randint


def randomNum():
    """
    function that returns a random number in range 1 to 5
    return: an integer number between min range to max range
    """
    min_range = 1
    max_range = 5
    return randint(min_range, max_range)


def buildNum():
    """
    function that builds a number from 5 digits
    return: an integer number from 5 digits
    """
    number_to_return = 1
    number_of_random_numbers = 4
    number_multiplier = 10
    for i in range(number_of_random_numbers):
        number_to_return = number_to_return * number_multiplier + randomNum()
    return number_to_return


def executeSTR(path):
    """
    function that opens the file in the given path and returns the string in a random line
    if it equals the given random number
    """
    try:
        randomNumber = str(buildNum())
        with open(path, 'r') as f:
            for line in f:
                split_line = line.rstrip().split("\t")
                if (randomNumber == split_line[0]):
                    return split_line[1]
    except FileNotFoundError:
        raise("The specified file doesn't exist")
    except PermissionError:
        raise("You don't have permission to read from the file")


def buildPassword(path):
    """
    function that creates a random password by combining 6 strings
    return: a random password
    """
    password = ""
    max_range = 6
    for i in range(max_range):
        password = password + str(executeSTR(path))
    return password
