day = int(input("Please enter a number between 1 and 7: "))

if day == 1:
    print("Monday")
else:
    if day == 2:
        print("Tuesday")
    else:
        if day == 3:
            print("Wednesday")
        else:
            if day == 4:
                print("Thursday")
            else:
                if day == 5:
                    print("Friday")
                else:
                    if day == 6:
                        print("Saturday")
                    else:
                        if day == 7:
                            print("Sunday")
                        else:
                            if day >= 8:
                                print("That is not within the days of the week.")
                            else:
                                if day < 1:
                                    print("That is not within the days of the week.")
