'''
    At least 8 characters long

    Contains both uppercase and lowercase letters

    Has at least one digit

    Has at least one special character

'''



def is_password_secure():
    password = input('Enter password: ')
    message = ''
    specialCharacters = str(['!', '@', '#', '$', '%', '^', '&', '*', '+', '/'])
    lettersLower = s
    tr([chr(i) for i in range(ord('a'), ord('z') + 1)])
    lettersCapital = str([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    passwordIsValid = True
    if len(password) < 8:
        print('Your password should at least be 8 characters long.')
    if specialCharacters in password:
        print('You should at least have 1 special character')
    if lettersCapital in password:
        print('You should at least have 1 capital letter')
    if lettersLower in password:

        print('You should have at least 1 lower character')
    else:
        print('Password is valid')
is_password_secure()