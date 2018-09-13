X = int(input("\n\nPlease enter your age: "))

if X <= 1:
    print("You are still an infant. How are you operating this?")
else:
    if 2 <= X <= 12:
        print("You are a child. Stage 1 completed.")
    else:
        if 13 <= X <= 19:
            print("You are a teen. Stages 1 and 2 completed.")
        else:
            if X >= 20:
                print("You are a adult and passed the tutorial to life. Best of luck!")
