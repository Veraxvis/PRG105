def main():
    score1 = int(input("Please enter your test score: "))
    score2 = int(input("Please enter your test score: "))
    score3 = int(input("Please enter your test score: "))
    score4 = int(input("Please enter your test score: "))
    score5 = int(input("Please enter your test score: "))
    stuff = (score1, score2, score3, score4, score5)
    average = calc_average(stuff)
    print("The average for all the grades added up is:", '%' + "{:,.2f}".format(average))
    letter = letter_grade(average)
    print("Your letter grade is a", letter)


def calc_average(stuff):
    score_total = 0
    for x in stuff:
        score_total = score_total + x
    score_average = score_total / 5
    return score_average


def letter_grade(average):
    if average >= 90 or average == 100:
        grade = "A"
        return grade
    else:
        if 90 > average >= 80:
            grade2 = "B"
            return grade2
        else:
            if 80 > average >= 70:
                grade3 = "C"
                return grade3
            else:
                if 70 > average >= 60:
                    grade4 = "D"
                    return grade4
                else:
                    if average <= 50:
                        grade5 = "F"
                        return grade5


main()
