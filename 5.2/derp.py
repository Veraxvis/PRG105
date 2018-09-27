def main():
    costs = monthly()
    print("You spend", '$' + "{:,.2f}".format(costs) + " on your car per month.")
    per_year = yearly(costs)
    print("In total you spend", '$' + "{:,.2f}".format(per_year) + " on your car per year.")


def monthly():
    car_payment = float(input("Please enter your monthly car payment: "))
    insurance = float(input("Please enter your monthly insurance bill: "))
    gas = float(input("Please enter how much you spend on gas each month: "))
    repairs = float(input("Please enter how much you spend on repairs: "))
    monthly_total = car_payment + insurance + gas + repairs
    return monthly_total


def yearly(monthly_total):
    year = monthly_total * 12
    return year


main()
