'''
    At least 8 characters long

    Contains both uppercase and lowercase letters

    Has at least one digit

    Has at least one special character



def is_password_secure():
    password = input('Enter password: ')
    message = ''
    specialCharacters = str(['!', '@', '#', '$', '%', '^', '&', '*', '+', '/'])
    lettersLower = str([chr(i) for i in range(ord('a'), ord('z') + 1)])
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
'''

def is_password_secure():
    password = input('Enter password: ')
    message = ''
    special_characters = '!@#$%^&*+/'
    letters_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    letters_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    numbers = [str(i) for i in range(10)]
    has_number = any(char in numbers for char in password)
    has_special_char = any(char in special_characters for char in password)
    has_lower_letter = any(char in letters_lower for char in password)
    has_upper_letter = any(char in letters_upper for char in password)
    #Add the boolean
    if len(password) < 8:
        message += 'Your password should be at least 8 characters long. '
    if not has_special_char:
        message += 'Your password should have at least one special character. '
    if not has_lower_letter:
        message += 'Your password should have at least one lowercase letter. '
    if not has_upper_letter:
        message += 'Your password should have at least one uppercase letter. '
    if not has_number:
        message += 'You should have at least 1 number.'
    if message:
        print(message)
    else:
        print('Password is valid.')

is_password_secure()