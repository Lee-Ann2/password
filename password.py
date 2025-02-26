'''
    At least 8 characters long

    Contains both uppercase and lowercase letters

    Has at least one digit

    Has at least one special character

'''
password = []
message = []
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '/']
lettersLower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
lettersCapital = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
passwordIsValid = True

def is_password_secure(password):
    if len(password) < 8:
        passwordIsValid = False
        message.append('Your password should at least be 8 character long.')
    elif not specialCharacters in password:
        passwordIsValid = False
        message.append('You should at least have 1 special character')
    elif not lettersCapital in password:
        passwordIsValid = False
        message.append('You should at least have 1 capital letter')
    elif not lettersLower in password:
        passwordIsValid = False
        message.append('You should have at least 1 lower character')
    else:
        print('Password is valid')
    return True
is_password_secure('khazi')