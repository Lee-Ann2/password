'''
    At least 8 characters long

    Contains both uppercase and lowercase letters

    Has at least one digit

    Has at least one special character

'''
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '/']
lettersLower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
lettersCapital = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
password = []


