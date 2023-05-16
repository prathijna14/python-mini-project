#NESTED IF CONDITION
import time
name= input("Enter your name: ")
print("welcome to adventure",name )
answer= input("you are in forest and the road is going to be end, so you have to turn right or left(right/left): ")
if answer=="right":
    answer=input("now you standing in front of Bear.... if you want to save? ok then climb a tree or else you will lose your life(yes/no): ")
    if answer=="yes":
        answer=input("Ok now you are safe!!! now you have to jump from the tree(yes/no): ")
        if answer=="yes":
            print("you got injured :( so you lost the game:(  Better Luck Next Time...")
        else:
            print("you stucked in the tree.. game over:(")
    else:
        print("Game Over.. Better Luck Next Time...")
elif answer=="left":
    answer=input("you are infront of bridge!!! \n  if you want cross the bridge or jump in to water(cross/jump): ")
    if answer=="cross":
        answer=input("now you crossed the bridge:) you want to take left or right(left/right): ")
        if answer=="left":
            answer=input("now you are infront of Home if you want to enter the home??? \n(yes/no): ")
            if answer=="yes":
                print("Hey you reached the destination!!!!!!! Congradulations You win:) : ")
            else:
                print("you lost the game:( Better Luck Next Time")
    if answer=="jump":
        answer=input("now you are in water,,,,, if want to move forword then you can swim,,,(swim/not swim): ")
        if answer=="swim":
            answer=input("now you reached land,,,,, now you can take rest below the tree or move forword(rest/move): ")
            if answer=="rest":
                answer=input("enter the resting time in seconds: ")
                time.sleep(int(answer))
                answer=input("you completed your resting time,now you can move left or right(left/right): ")
                if answer=="left":
                    answer=input("Now you are in front of Hut!!! do you want to enter the Hut(yes/no): ")
                    if answer=="yes":
                        print("Hey you got Gold in the Hut.... you won:)!! : ")
                    else:
                        print("you lost:( Better Luck Next Time")
else:
    print("you enter the wrong choice you lost the game")

