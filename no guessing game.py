import random
ch=int(input("\n\nEnter choice:\n1.EASY LEVEL:10 to 20\n2.MIDEUM LEVEL:100 to 200\n3.HARD LEVEL:1000 to 2000\n"))
if ch==1:
    generated_num=random.randint(10,20)
    print("\n\nEasy Level:10 to 20")
elif ch==2:
    generated_num=random.randint(100,200)
    print("\n\nMedium Level:100 to 200")
elif ch==3:
    generated_num=random.randint(1000,2000)
    print("\n\nHard Level:1000 to 2000")
else:
    print("Invalid Level! , Starting Easy Level")
    generated_num=random.randint(10,20)
    print("\n\nEasy Level:10to 20")
ch1=int(input("how many attempt you want:"))

for i in range(ch1):
   
    guessed_num=int(input("Guess a num , 0 to exit:"))
    if guessed_num==0:
        print("Exiting...")
        break
    elif guessed_num<generated_num:
        print("Too small num, try again..")
    elif guessed_num>generated_num:
        print("Too large num, try again..")
    elif guessed_num==generated_num:
        print("Congrulations You Won The Game!")
        break

        
