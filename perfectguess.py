import random
number = random.randint(1,100)
print("number generated, make a guess:",end="")
guess = int(input(""))
attemp = 0
while(guess != number):
    if(number<guess):
        print("enter a lower no.")
    elif(number>guess):
        print("enter a higher no.")
    guess = int(input("enter the next guess"))
    attemp += 1
print(f"Congraulation you have gussed the right no.{guess}, in total of {attemp} attemps")
