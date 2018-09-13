A = float(39.99)
B = float(59.99)
C = float(69.99)
e = int(900)
f = int(450)

pGet = input("What plan is the user on? (Please enter A B or C): ")
pGet = pGet.upper()
if pGet == "A":
    print("User is on a plan that requires them to pay", '$' + str(A))
    print("They get a total of", f, "minutes each month.\n")
    G = int(input("Please enter the amount of minutes the user has used out of the plan: "))
    if G > f:
        j = G - f
        k = 0.45 * j
        print("The user has gone over", j, "minutes. They are required to pay a additional charge of: ")
        print('$' + str(float("{0:.2f}".format(k))))
    else:
        if G <= f:
            print("The user has not gone over their limit and only pays the regular charge.")
if pGet == "B":
    print("User is on a plan that requires them to pay", '$' + str(B))
    print("They get a total of", e, "minutes each month.\n")
    G = int(input("Please enter the amount of minutes the user has used out of the plan: "))
    if G > e:
        j = G - e
        k = 0.4 * j
        print("The user has gone over", j, "minutes. They are required to pay a additional charge of: ")
        print('$' + str(float("{0:.2f}".format(k))))
    else:
        if G <= e:
            print("The user has not gone over their limit and only pays the regular charge.")
if pGet == "C":
    print("This user pays", '$' + str(C), "a month for unlimited minutes.")
if pGet != "A" and pGet != "B" and pGet != "C":
    print("User failed to enter an appropriate selection.\n")
    print("The correct selections were A, B, or C. Please reboot the program and try again.")

