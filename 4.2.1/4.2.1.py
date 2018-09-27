money = 0
gift = float(0.01)
day = int(input("Please enter the number of days you worked: "))

for x in range(0, day):
    print("On day", x + 1, "you made a total of", '$' + str(gift))
    money += gift
    gift *= 2

print("For", day, "days you made a total of", '$' + "{:.2f}".format(money))
