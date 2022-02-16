import random
print("WELCOME TO GUESS GAME!!")
print("\n1.Guessing a character ","\n2.Guessing a number")
#Getting choice
try:
    choice = int(input("Enter your choice"))
    if choice>2:
        print("Wrong choice!")
except:
    print("Wrong choice!")
result=''
if choice==1:
    guesses = 10
    print("You have to guess a character in lower case-->")
    data= "abcdefghijklmnopqrstuvwxyz"
    n= random.choice(data)
    while(guesses!=0):
        char= input("Enter a character-->")   
        try:
            x=int(char)
            print("You have entered a numeric value")
        except:
            if char not in data:
                print("Not an lowercase alphabet")
            else:
                guesses-=1
                if char==n:
                    print("You WIN! in ", 10-guesses," guesses")
                    result='WIN'
                    break
                else:
                    print(f"Try Again!\nYou have {guesses} guesses left.")
                    result='LOST'
    if result!='WIN':
        print("You LOST!")
elif choice==2:
    x=random.randint(6,995)
    l,u= x-5,x+5
    guesses=5
    anum=random.randint(l,u)
    print(f"You have to guess a number between {l} & {u}!")
    while(guesses!=0):
        try:
            num= int(input("Enter a number-->"))
            guesses-=1
            if num==anum:
                print(f"You have guessed {num}\nYOU WIN in {5-guesses} chance")
                break
            else:
                print(f"Wrong Guess!\nYou have {guesses} chance left")
                if num>anum:
                    if num-anum <5:
                        print("You are going closer!")
                    else:
                        print("You are going farther!")
                else:
                    if anum-num <5:
                        print("You are going closer!")
                    else:
                        print("You are going farther!")
        except:
            print("Not a numeric Value!")
