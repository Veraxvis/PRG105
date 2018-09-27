def main():
    x = int(input("Please enter the amount of grams of fat: "))
    fat_calories = fat(x)
    z = int(input("Please enter the amount of grams of carbohydrates: "))
    carbohydrates_calories = carbohydrates(z)
    y = int(input("Please enter the amount of grams of protein: "))
    protein_calories = protein(y)

    total_calories = fat_calories + carbohydrates_calories + protein_calories
    print("You have consumed a total of", total_calories, "calories today.")


def fat(x):
    calories_fat = x * 9
    print("You have consumed a total of", calories_fat, "calories in fat.")
    return calories_fat


def carbohydrates(z):
    calories_carbohydrates = z * 4
    print("You have consumed a total of", calories_carbohydrates, "calories in carbohydrates.")
    return calories_carbohydrates


def protein(y):
    calories_protein = y * 4
    print("You have consumed a total of", calories_protein, "calories in carbohydrates.")
    return calories_protein


main()
