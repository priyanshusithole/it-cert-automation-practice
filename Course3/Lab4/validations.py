

#!/usr/bin/env python3



import re



def validate_user(username, minlen):

    """Checks if the received username matches the required conditions."""



    if type(username) != str:

        raise TypeError("username must be a string")



    if minlen < 1:

        raise ValueError("minlen must be at least 1")



    # Username must meet the minimum length

    if len(username) < minlen:

        return False



    # Username must start with a letter and contain only letters,

    # numbers, dots, and underscores

    if not re.fullmatch(r'[a-zA-Z][a-zA-Z0-9._]*', username):

        return False



    # Username cannot end with a dot or underscore

    if username[-1] in '._':

        return False



    return True





print(validate_user("blue.kale", 3))    # True

print(validate_user(".blue.kale", 3))   # False

print(validate_user("red_quin oa", 4))  # False

print(validate_user("_red_quinoa", 4))  # False

print(validate_user("9blue", 3))        # False


