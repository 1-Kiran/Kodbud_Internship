import random
random_number=random.randint(1,100)
count=0
while True:
    try:
        user_number=int(input("Guess a number between 1 and 100: : "))
    except ValueError:
        print("Enter a valid number")
    if user_number<0 or user_number>=100:
        print("Please enter an number between 100")
    else:
        if user_number<random_number:
            print("Too low")
        elif user_number>random_number:
            print("Too high")
        elif user_number==random_number:
            print("Congratulations! You guessed the number.")
            break
    count+=1
print("Number of attempt is : ",count)