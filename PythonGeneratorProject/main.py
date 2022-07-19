import string 
import random
# define list of letters , digits and chars
letters = list(string.ascii_letters)
digits = list(string.digits)
chars = list(string.punctuation)

print(" Welcome .. let's have func : ") 

def generatePassword():
    passwordLength = input('Enter password length: ')
    # check if the password length is int and >= 8
    while True:
        try:
            passwordLength = int(passwordLength)
            if passwordLength < 8 :
                print("Sorry password must be at least 8 chars")
                passwordLength = int(input('Enter password length : '))
            break
        except:
            print('Please enter numbers only ...')
            passwordLength = int(input('Enter password length: '))
            

        # define list of password 
    password = []
    random.shuffle(letters) # 60%
    random.shuffle(digits)  # 30%
    random.shuffle(chars)   # 10%

    # append letters into password
    for i in range(round(passwordLength * .6)):
        password.append(letters[i])
    # append digits into password
    for i in range(round(passwordLength * .3)):
        password.append(digits[i])
    # append punctuatuions into password
    for i in range(round(passwordLength * .1)):
        password.append(chars[i])

    password = "".join(password[0:])

    print(f"Your password is : \n  {password}")

generatePassword()