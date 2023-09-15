import string
import random

#Getting passward length

length=int(input("Enter password length: "))
print('''Choice character set for password from these
                1. Letters
                2. Digits
                3. Special characters
                4. Exit''')
characterList=""

#Getting character set for password
while True:
    choice=int(input("Choose a number :"))
    if choice==1:
        characterList=characterList+string.ascii_letters
    elif choice==2:
        characterList=characterList+string.digits
    elif choice==3:
        characterList=characterList+string.punctuation
    elif choice==4:
        break
    else:
        print("Please pick a correct option")
random_password=[]
for i in range(length):
    randomcharacter=random.choice(characterList)
    random_password.append(randomcharacter)
print("The random password is "+"".join(random_password))
         